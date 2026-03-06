from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import case, desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from telegras.contracts import PublishResult
from telegras.persistence.models import (
    AttachmentDefinition,
    HandlerExecution,
    Publication,
    TelegramInteraction,
    WebhookExecution,
)
from telegras.api.getting_updates import Update as TelegramUpdate
from telegras.webhook_attachments import Attachment


def _extract_context(
    update: TelegramUpdate,
) -> tuple[int | None, str | None, int | None, str | None]:
    payload = update.get_payload()
    if payload is None:
        return None, None, None, None
    if isinstance(payload, dict):
        chat = payload.get("chat") or {}
        chat_id = chat.get("id")
        chat_type = chat.get("type")
        message_id = payload.get("message_id")
        text = payload.get("text") or payload.get("caption")
        return chat_id, chat_type, message_id, text

    chat = getattr(payload, "chat", None)
    if isinstance(chat, dict):
        chat_id = chat.get("id")
        chat_type = chat.get("type")
    else:
        chat_id = getattr(chat, "id", None) if chat is not None else None
        chat_type = getattr(chat, "type", None) if chat is not None else None
    message_id = getattr(payload, "message_id", None)
    text = getattr(payload, "text", None) or getattr(payload, "caption", None)
    return chat_id, chat_type, message_id, text


async def create_or_get_interaction(
    session: AsyncSession,
    update: TelegramUpdate,
) -> TelegramInteraction:
    existing = await session.scalar(
        select(TelegramInteraction)
        .where(TelegramInteraction.update_id == update.update_id)
        .options(selectinload(TelegramInteraction.publications))
    )
    if existing:
        return existing

    chat_id, chat_type, message_id, text = _extract_context(update)
    interaction = TelegramInteraction(
        update_id=update.update_id,
        kind=update.kind.value if update.kind else None,
        chat_id=chat_id,
        chat_type=chat_type,
        message_id=message_id,
        text=text,
        status="received",
        raw_update=update.model_dump(mode="json", exclude_none=True),
    )
    session.add(interaction)
    await session.flush()
    await session.refresh(interaction)
    return interaction


async def mark_interaction_processed(
    session: AsyncSession,
    interaction: TelegramInteraction,
    result: PublishResult,
) -> Publication:
    interaction.status = result.status
    interaction.error = None
    interaction.processed_at = datetime.now(timezone.utc)

    publication = Publication(
        interaction_id=interaction.id,
        backend=result.backend,
        status=result.status,
        external_id=result.external_id,
        url=result.url,
        payload=result.payload,
    )
    session.add(publication)
    await session.flush()
    return publication


async def mark_interaction_failed(
    session: AsyncSession,
    interaction: TelegramInteraction,
    error: str,
) -> None:
    interaction.status = "failed"
    interaction.error = error
    interaction.processed_at = datetime.now(timezone.utc)
    await session.flush()


async def add_publication(
    session: AsyncSession,
    interaction: TelegramInteraction,
    result: PublishResult,
) -> Publication:
    publication = Publication(
        interaction_id=interaction.id,
        backend=result.backend,
        status=result.status,
        external_id=result.external_id,
        url=result.url,
        payload=result.payload,
    )
    session.add(publication)
    await session.flush()
    return publication


async def finalize_interaction(
    session: AsyncSession,
    interaction: TelegramInteraction,
    *,
    status: str,
    error: str | None = None,
) -> None:
    interaction.status = status
    interaction.error = error
    interaction.processed_at = datetime.now(timezone.utc)
    await session.flush()


async def list_interactions(
    session: AsyncSession, limit: int, offset: int
) -> list[TelegramInteraction]:
    rows = await session.scalars(
        select(TelegramInteraction)
        .options(selectinload(TelegramInteraction.publications))
        .order_by(desc(TelegramInteraction.received_at))
        .offset(offset)
        .limit(limit)
    )
    return list(rows)


async def get_interaction_by_id(
    session: AsyncSession, interaction_id: int
) -> TelegramInteraction | None:
    return await session.scalar(
        select(TelegramInteraction)
        .where(TelegramInteraction.id == interaction_id)
        .options(selectinload(TelegramInteraction.publications))
    )


async def get_interaction_by_update_id(
    session: AsyncSession, update_id: int
) -> TelegramInteraction | None:
    return await session.scalar(
        select(TelegramInteraction)
        .where(TelegramInteraction.update_id == update_id)
        .options(selectinload(TelegramInteraction.publications))
    )


async def list_publications(
    session: AsyncSession, limit: int, offset: int
) -> list[Publication]:
    rows = await session.scalars(
        select(Publication)
        .order_by(desc(Publication.created_at))
        .offset(offset)
        .limit(limit)
    )
    return list(rows)


async def list_chat_ids(
    session: AsyncSession, limit: int, offset: int
) -> list[int]:
    rows = await session.scalars(
        select(TelegramInteraction.chat_id)
        .where(TelegramInteraction.chat_id.is_not(None))
        .distinct()
        .order_by(TelegramInteraction.chat_id.asc())
        .offset(offset)
        .limit(limit)
    )
    return [chat_id for chat_id in rows if chat_id is not None]


async def list_interactions_by_chat_id(
    session: AsyncSession,
    chat_id: int,
    limit: int,
    offset: int,
) -> list[TelegramInteraction]:
    rows = await session.scalars(
        select(TelegramInteraction)
        .where(TelegramInteraction.chat_id == chat_id)
        .options(selectinload(TelegramInteraction.publications))
        .order_by(desc(TelegramInteraction.received_at))
        .offset(offset)
        .limit(limit)
    )
    return list(rows)


def _attachment_to_row(attachment: Attachment) -> dict:
    return {
        "name": attachment.name,
        "handler": attachment.handler,
        "handler_args": attachment.handler_args,
        "handler_chain": [step.model_dump(mode="json") for step in attachment.handler_chain],
        "execution_mode": attachment.execution_mode,
        "stop_on_error": attachment.stop_on_error,
        "enabled": attachment.enabled,
        "priority": attachment.priority,
        "stop_on_match": attachment.stop_on_match,
        "when_json": attachment.when.model_dump(mode="json"),
        "parse_json": attachment.parse.model_dump(mode="json") if attachment.parse else None,
        "parse_mode": attachment.parse_mode,
        "updated_at": datetime.now(timezone.utc),
    }


def _row_to_attachment(row: AttachmentDefinition) -> Attachment:
    return Attachment(
        name=row.name,
        handler=row.handler,
        handler_args=list(row.handler_args or []),
        handler_chain=list(row.handler_chain or []),
        execution_mode=row.execution_mode,
        stop_on_error=row.stop_on_error,
        enabled=row.enabled,
        priority=row.priority,
        stop_on_match=row.stop_on_match,
        when=row.when_json,
        parse=row.parse_json,
        parse_mode=row.parse_mode,
    )


async def upsert_attachment_definition(
    session: AsyncSession,
    attachment: Attachment,
) -> Attachment:
    existing = await session.scalar(
        select(AttachmentDefinition).where(AttachmentDefinition.name == attachment.name)
    )
    data = _attachment_to_row(attachment)
    if existing is None:
        row = AttachmentDefinition(
            created_at=datetime.now(timezone.utc),
            **data,
        )
        session.add(row)
    else:
        for key, value in data.items():
            setattr(existing, key, value)
        row = existing

    await session.flush()
    await session.refresh(row)
    return _row_to_attachment(row)


async def delete_attachment_definition(session: AsyncSession, name: str) -> bool:
    row = await session.scalar(
        select(AttachmentDefinition).where(AttachmentDefinition.name == name)
    )
    if row is None:
        return False
    await session.delete(row)
    await session.flush()
    return True


async def list_attachment_definitions(session: AsyncSession) -> list[Attachment]:
    rows = await session.scalars(
        select(AttachmentDefinition).order_by(AttachmentDefinition.priority.asc(), AttachmentDefinition.name.asc())
    )
    return [_row_to_attachment(row) for row in rows]


async def create_webhook_execution(
    session: AsyncSession,
    *,
    update: TelegramUpdate,
    matched_attachments: list[str],
    overall_status: str = "processed",
    error: str | None = None,
) -> WebhookExecution:
    chat_id, chat_type, _, _ = _extract_context(update)
    row = WebhookExecution(
        update_id=update.update_id,
        chat_id=chat_id,
        chat_type=chat_type,
        raw_update=update.model_dump(mode="json", exclude_none=True),
        matched_attachments=matched_attachments,
        overall_status=overall_status,
        error=error,
    )
    session.add(row)
    await session.flush()
    await session.refresh(row)
    return row


async def add_handler_execution(
    session: AsyncSession,
    *,
    webhook_execution_id: int,
    attachment_name: str,
    handler: str,
    rendered_args: list[str],
    ok: bool,
    result: dict | list | str | int | float | bool | None = None,
    error: str | None = None,
    started_at: datetime | None = None,
    finished_at: datetime | None = None,
) -> HandlerExecution:
    start = started_at or datetime.now(timezone.utc)
    finish = finished_at or datetime.now(timezone.utc)
    duration_ms = int((finish - start).total_seconds() * 1000)
    row = HandlerExecution(
        webhook_execution_id=webhook_execution_id,
        attachment_name=attachment_name,
        handler=handler,
        rendered_args=rendered_args,
        ok=ok,
        result=result,
        error=error,
        started_at=start,
        finished_at=finish,
        duration_ms=duration_ms,
    )
    session.add(row)
    await session.flush()
    return row


async def list_webhook_executions(
    session: AsyncSession,
    *,
    limit: int,
    offset: int,
) -> list[WebhookExecution]:
    rows = await session.scalars(
        select(WebhookExecution)
        .options(selectinload(WebhookExecution.handler_executions))
        .order_by(desc(WebhookExecution.received_at))
        .offset(offset)
        .limit(limit)
    )
    return list(rows)


async def get_webhook_execution_by_id(
    session: AsyncSession,
    execution_id: int,
) -> WebhookExecution | None:
    return await session.scalar(
        select(WebhookExecution)
        .where(WebhookExecution.id == execution_id)
        .options(selectinload(WebhookExecution.handler_executions))
    )


async def get_last_webhook_execution(session: AsyncSession) -> WebhookExecution | None:
    return await session.scalar(
        select(WebhookExecution)
        .options(selectinload(WebhookExecution.handler_executions))
        .order_by(desc(WebhookExecution.received_at))
        .limit(1)
    )


async def list_handler_stats(session: AsyncSession) -> list[dict]:
    stmt = (
        select(
            HandlerExecution.handler.label("handler"),
            func.count(HandlerExecution.id).label("runs"),
            func.sum(case((HandlerExecution.ok.is_(True), 1), else_=0)).label("successes"),
            func.avg(HandlerExecution.duration_ms).label("avg_duration_ms"),
            func.max(HandlerExecution.finished_at).label("last_run_at"),
        )
        .group_by(HandlerExecution.handler)
        .order_by(HandlerExecution.handler.asc())
    )
    rows = await session.execute(stmt)
    result: list[dict] = []
    for row in rows:
        runs = int(row.runs or 0)
        successes = int(row.successes or 0)
        success_rate = (successes / runs) if runs else 0.0
        result.append(
            {
                "handler": row.handler,
                "runs": runs,
                "successes": successes,
                "success_rate": success_rate,
                "avg_duration_ms": float(row.avg_duration_ms or 0.0),
                "last_run_at": row.last_run_at,
            }
        )
    return result
