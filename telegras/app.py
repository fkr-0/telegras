from __future__ import annotations

import asyncio
import logging
import os
from asyncio import Lock
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager, suppress
from pathlib import Path
from typing import Any

from fastapi import Depends, FastAPI, Header, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import HTMLResponse

from telegras import telegram_api
from telegras.persistence import repository
from telegras.persistence.db import SessionLocal, get_session, init_db
from telegras.persistence.schemas import PublicationRead, TelegramInteractionRead
from telegras.settings import AppSettings, BotMode
from telegras.services.ingestion import TelegramIngestionService
from telegras.api.getting_updates import Update as TelegramUpdate
from telegras.webhook_attachments import (
    Attachment,
    ExecutionMode,
    FieldName,
    MatchOp,
    ParseMode,
    WebhookAttachmentRegistry,
)

_db_init_lock = Lock()
_db_initialized = False
log = logging.getLogger("telegras.app")


class SendMessageRequest(BaseModel):
    message_body: str


class ChatIdsResponse(BaseModel):
    chat_ids: list[int]


class ChatHistoryMessage(BaseModel):
    interaction_id: int
    update_id: int
    message_id: int | None = None
    text: str | None = None
    status: str


class ChatHistoryResponse(BaseModel):
    chat_id: int
    messages: list[ChatHistoryMessage]


class AttachmentMatchRequest(BaseModel):
    update: TelegramUpdate


class AttachmentExecutionRecord(BaseModel):
    attachment: str
    handler: str
    rendered_args: list[str]
    ok: bool
    result: dict | list | str | int | float | bool | None = None
    error: str | None = None
    parse: dict[str, Any] | None = None
    handler_executions: list[dict[str, Any]] = []


class WebhookExecutionRead(BaseModel):
    id: int
    update_id: int | None = None
    chat_id: int | None = None
    chat_type: str | None = None
    raw_update: dict
    matched_attachments: list
    overall_status: str
    error: str | None = None
    received_at: str
    handler_executions: list[dict[str, Any]]


class DeleteWebhookRequest(BaseModel):
    drop_pending_updates: bool | None = None


async def _ensure_db_ready() -> None:
    global _db_initialized
    if _db_initialized:
        return

    async with _db_init_lock:
        if _db_initialized:
            return
        await init_db()
        _db_initialized = True


def _read_bearer_token(authorization: str | None) -> str | None:
    if not authorization:
        return None
    prefix = "Bearer "
    if not authorization.startswith(prefix):
        return None
    return authorization[len(prefix) :].strip()


async def require_introspection_auth(
    authorization: str | None = Header(default=None, alias="Authorization"),
) -> None:
    expected = os.getenv("INTROSPECTION_TOKEN")
    if not expected:
        raise HTTPException(
            status_code=503, detail="Introspection token not configured"
        )

    provided = _read_bearer_token(authorization)
    if provided is None:
        raise HTTPException(status_code=401, detail="Missing bearer token")
    if provided != expected:
        raise HTTPException(status_code=403, detail="Invalid token")


async def _registry_from_db(session: AsyncSession) -> WebhookAttachmentRegistry:
    registry = WebhookAttachmentRegistry()
    for attachment in await repository.list_attachment_definitions(session):
        registry.register(attachment)
    return registry


async def _run_polling_loop(
    *,
    service: TelegramIngestionService,
    settings: AppSettings,
) -> None:
    offset: int | None = None
    log.info(
        "BOT_MODE=polling enabled (timeout=%ss)",
        settings.polling_timeout_seconds,
    )

    while True:
        try:
            updates = await telegram_api.get_updates(
                offset=offset,
                timeout=settings.polling_timeout_seconds,
            )

            if not updates:
                await asyncio.sleep(settings.polling_idle_sleep_seconds)
                continue

            for update in updates:
                async with SessionLocal() as session:
                    await service.ingest(session, update)
                    await session.commit()
                offset = update.update_id + 1
        except asyncio.CancelledError:
            raise
        except Exception:
            log.exception("Polling loop failed; retrying")
            await asyncio.sleep(settings.polling_error_backoff_seconds)


def _create_telegras_lifespan(
    settings: AppSettings,
    service: TelegramIngestionService,
):
    """Create the lifespan context manager for telegras.

    Args:
        settings: Application settings
        service: Telegram ingestion service

    Returns:
        An async context manager for startup/shutdown lifecycle
    """
    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        await _ensure_db_ready()
        polling_task: asyncio.Task[None] | None = None
        if settings.bot_mode == BotMode.POLLING:
            try:
                await telegram_api.delete_webhook(drop_pending_updates=False)
            except Exception:
                log.exception(
                    "Failed to delete webhook before starting polling; continuing",
                )
            polling_task = asyncio.create_task(
                _run_polling_loop(service=service, settings=settings),
                name="telegras-polling-loop",
            )
        try:
            yield
        finally:
            if polling_task is not None:
                polling_task.cancel()
                with suppress(asyncio.CancelledError):
                    await polling_task

    return lifespan


def _merge_lifespans(
    ctx1: Any,
    ctx2: Any,
) -> Any:
    """Merge two lifespan context managers into one.

    Args:
        ctx1: First lifespan context manager
        ctx2: Second lifespan context manager

    Returns:
        A new async context manager that runs both lifespans
    """
    @asynccontextmanager
    async def merged_lifespan(app: FastAPI) -> AsyncIterator[None]:
        async with ctx1(app):
            async with ctx2(app):
                yield

    return merged_lifespan


def create_app(
    *,
    app: FastAPI | None = None,
    settings: AppSettings | None = None,
    service: TelegramIngestionService | None = None,
    merge_lifespan: bool = True,
) -> FastAPI:
    """Create or configure the FastAPI application.

    This function can either create a new standalone FastAPI app or
    mount telegras routes onto an existing FastAPI app.

    Args:
        app: Optional existing FastAPI app to mount routes onto.
             If None, creates a new standalone app.
        settings: Optional application settings. If None, loads from environment.
        service: Optional TelegramIngestionService instance. If None, creates one.
        merge_lifespan: Whether to merge lifespans when mounting on existing app.
                       Only applicable when app is provided.

    Returns:
        The configured FastAPI application (new or provided)
    """
    if settings is None:
        settings = AppSettings.from_env()

    if service is None:
        service = TelegramIngestionService()

    if app is None:
        # Create new standalone app
        app = FastAPI(
            title="telegras",
            description=(
                "Telegram + FastAPI bridge with persistent interaction history "
                "and pluggable publication backends."
            ),
            version="0.1.0",
        )
        telegras_lifespan = _create_telegras_lifespan(settings, service)
        app.router.lifespan_context = telegras_lifespan
    elif merge_lifespan:
        # Mount on existing app and merge lifespans
        telegras_lifespan = _create_telegras_lifespan(settings, service)
        existing_lifespan = app.router.lifespan_context
        if existing_lifespan is not None:
            app.router.lifespan_context = _merge_lifespans(
                existing_lifespan,
                telegras_lifespan,
            )
        else:
            app.router.lifespan_context = telegras_lifespan

    @app.get("/healthz")
    async def healthz() -> dict[str, str]:
        return {"status": "ok", "service": "telegras"}

    @app.post("/simulate-update")
    async def simulate_update_endpoint(
        update: TelegramUpdate,
        force: bool = False,
        secret: str | None = None,
        x_webhook_secret: str | None = Header(default=None, alias="X-Webhook-Secret"),
        session: AsyncSession = Depends(get_session),
    ) -> dict[str, object]:
        await _ensure_db_ready()

        expected = os.getenv("TELEGRAM_WEBHOOK_SECRET")
        provided = secret or x_webhook_secret
        if expected and provided != expected:
            raise HTTPException(status_code=403, detail="Forbidden")

        previous_tg_skip = os.getenv("TG_SKIP")
        if force:
            os.environ["TG_SKIP"] = "false"

        try:
            interaction_id = await service.ingest(session, update)
            await session.commit()
        finally:
            if force:
                if previous_tg_skip is None:
                    os.environ.pop("TG_SKIP", None)
                else:
                    os.environ["TG_SKIP"] = previous_tg_skip

        return {"ok": True, "interaction_id": interaction_id}

    async def _telegram_webhook(
        secret: str,
        update: TelegramUpdate,
        session: AsyncSession = Depends(get_session),
    ) -> dict[str, object]:
        await _ensure_db_ready()

        expected = os.getenv("TELEGRAM_WEBHOOK_SECRET")
        if expected and secret != expected:
            raise HTTPException(status_code=403, detail="Forbidden")

        interaction_id = await service.ingest(session, update)
        await session.commit()
        return {"ok": True, "interaction_id": interaction_id}

    webhook_prefix = os.getenv("WEBHOOK_PREFIX", "webhook").strip("/")
    webhook_path_pattern = (
        f"/{webhook_prefix}/{{secret}}" if webhook_prefix else "/{secret}"
    )
    app.post(webhook_path_pattern)(_telegram_webhook)
    app.post("/v1/telegram/webhook/{secret}")(_telegram_webhook)

    @app.get("/v1/interactions", response_model=list[TelegramInteractionRead])
    async def list_interactions(
        limit: int = Query(default=50, ge=1, le=200),
        offset: int = Query(default=0, ge=0),
        session: AsyncSession = Depends(get_session),
    ) -> list[TelegramInteractionRead]:
        await _ensure_db_ready()
        rows = await repository.list_interactions(session, limit=limit, offset=offset)
        return [TelegramInteractionRead.model_validate(row) for row in rows]

    @app.get(
        "/v1/interactions/{interaction_id}", response_model=TelegramInteractionRead
    )
    async def get_interaction(
        interaction_id: int,
        session: AsyncSession = Depends(get_session),
    ) -> TelegramInteractionRead:
        await _ensure_db_ready()
        row = await repository.get_interaction_by_id(session, interaction_id)
        if row is None:
            raise HTTPException(status_code=404, detail="Interaction not found")
        return TelegramInteractionRead.model_validate(row)

    @app.get("/v1/publications", response_model=list[PublicationRead])
    async def list_publications(
        limit: int = Query(default=50, ge=1, le=200),
        offset: int = Query(default=0, ge=0),
        session: AsyncSession = Depends(get_session),
    ) -> list[PublicationRead]:
        await _ensure_db_ready()
        rows = await repository.list_publications(session, limit=limit, offset=offset)
        return [PublicationRead.model_validate(row) for row in rows]

    @app.get(
        "/v1/interactions/by-update/{update_id}",
        response_model=TelegramInteractionRead,
    )
    async def get_interaction_by_update(
        update_id: int,
        session: AsyncSession = Depends(get_session),
    ) -> TelegramInteractionRead:
        await _ensure_db_ready()
        row = await repository.get_interaction_by_update_id(session, update_id)
        if row is None:
            raise HTTPException(status_code=404, detail="Interaction not found")
        return TelegramInteractionRead.model_validate(row)

    @app.get("/v1/chats", response_model=ChatIdsResponse)
    async def list_chat_ids(
        limit: int = Query(default=200, ge=1, le=1000),
        offset: int = Query(default=0, ge=0),
        session: AsyncSession = Depends(get_session),
    ) -> ChatIdsResponse:
        await _ensure_db_ready()
        chat_ids = await repository.list_chat_ids(session, limit=limit, offset=offset)
        return ChatIdsResponse(chat_ids=chat_ids)

    @app.get("/v1/chats/{chat_id}/history", response_model=ChatHistoryResponse)
    async def get_chat_history(
        chat_id: int,
        limit: int = Query(default=100, ge=1, le=1000),
        offset: int = Query(default=0, ge=0),
        session: AsyncSession = Depends(get_session),
    ) -> ChatHistoryResponse:
        await _ensure_db_ready()
        rows = await repository.list_interactions_by_chat_id(
            session, chat_id=chat_id, limit=limit, offset=offset
        )
        messages = [
            ChatHistoryMessage(
                interaction_id=row.id,
                update_id=row.update_id,
                message_id=row.message_id,
                text=row.text,
                status=row.status,
            )
            for row in rows
        ]
        return ChatHistoryResponse(chat_id=chat_id, messages=messages)

    @app.post("/v1/chats/{chat_id}/send")
    async def send_message_to_chat(
        chat_id: int,
        body: SendMessageRequest,
    ) -> dict:
        return await telegram_api.send_message(chat_id=chat_id, text=body.message_body)

    @app.get("/v1/webhook-attachments", response_model=list[Attachment])
    async def list_webhook_attachments(
        session: AsyncSession = Depends(get_session),
    ) -> list[Attachment]:
        await _ensure_db_ready()
        return await repository.list_attachment_definitions(session)

    @app.post("/v1/webhook-attachments", response_model=Attachment)
    async def register_webhook_attachment(
        attachment: Attachment,
        session: AsyncSession = Depends(get_session),
    ) -> Attachment:
        await _ensure_db_ready()
        out = await repository.upsert_attachment_definition(session, attachment)
        await session.commit()
        return out

    @app.delete("/v1/webhook-attachments/{name}")
    async def unregister_webhook_attachment(
        name: str,
        session: AsyncSession = Depends(get_session),
    ) -> dict[str, bool]:
        await _ensure_db_ready()
        removed = await repository.delete_attachment_definition(session, name)
        await session.commit()
        return {"removed": removed}

    @app.post("/v1/webhook-attachments/match", response_model=list[str])
    async def match_webhook_attachments(
        payload: AttachmentMatchRequest,
        session: AsyncSession = Depends(get_session),
    ) -> list[str]:
        await _ensure_db_ready()
        registry = await _registry_from_db(session)
        matched = registry.match_attachments(payload.update)
        return [item.name for item in matched]

    @app.post(
        "/v1/webhook-attachments/execute",
        response_model=list[AttachmentExecutionRecord],
    )
    async def execute_webhook_attachments(
        payload: AttachmentMatchRequest,
        session: AsyncSession = Depends(get_session),
    ) -> list[AttachmentExecutionRecord]:
        await _ensure_db_ready()
        registry = await _registry_from_db(session)
        rows = await registry.execute_matching_attachments(payload.update)

        matched_names = [row.get("attachment") for row in rows]
        overall_ok = all(bool(row.get("ok")) for row in rows) if rows else True
        execution = await repository.create_webhook_execution(
            session,
            update=payload.update,
            matched_attachments=matched_names,
            overall_status="processed" if overall_ok else "failed",
            error=None if overall_ok else "One or more handlers failed",
        )

        for row in rows:
            for step in row.get("handler_executions", []):
                await repository.add_handler_execution(
                    session,
                    webhook_execution_id=execution.id,
                    attachment_name=row.get("attachment", ""),
                    handler=step.get("handler", ""),
                    rendered_args=step.get("rendered_args", []),
                    ok=bool(step.get("ok")),
                    result=step.get("result"),
                    error=step.get("error"),
                )

        await session.commit()
        return [AttachmentExecutionRecord.model_validate(row) for row in rows]

    @app.get("/internal/introspection/config")
    async def introspection_config(
        _auth: None = Depends(require_introspection_auth),
        session: AsyncSession = Depends(get_session),
    ) -> dict[str, Any]:
        await _ensure_db_ready()
        try:
            webhook_info = await telegram_api.get_webhook_info()
            bot_api = (
                webhook_info.model_dump(mode="json")
                if hasattr(webhook_info, "model_dump")
                else webhook_info
            )
        except Exception as exc:
            bot_api = {"error": str(exc)}

        attachments = await repository.list_attachment_definitions(session)
        last = await repository.get_last_webhook_execution(session)
        last_payload = None
        if last is not None:
            last_payload = {
                "id": last.id,
                "update_id": last.update_id,
                "received_at": last.received_at.isoformat(),
                "matched_attachments": last.matched_attachments,
                "overall_status": last.overall_status,
            }

        return {
            "runtime": {"bot_mode": settings.bot_mode.value},
            "bot_api": bot_api,
            "last_webhook_trigger": last_payload,
            "handler_bindings": [
                {
                    "name": att.name,
                    "handler": att.handler,
                    "handler_chain": [
                        step.model_dump(mode="json") for step in att.handler_chain
                    ],
                    "enabled": att.enabled,
                    "priority": att.priority,
                }
                for att in attachments
            ],
        }

    @app.get("/internal/introspection/webhook/status")
    async def introspection_webhook_status(
        _auth: None = Depends(require_introspection_auth),
    ) -> dict[str, Any]:
        webhook_info = await telegram_api.get_webhook_info()
        if hasattr(webhook_info, "model_dump"):
            return webhook_info.model_dump(mode="json")
        return webhook_info

    @app.delete("/internal/introspection/webhook")
    async def introspection_delete_webhook(
        payload: DeleteWebhookRequest | None = None,
        _auth: None = Depends(require_introspection_auth),
    ) -> dict[str, Any]:
        result = await telegram_api.delete_webhook(
            drop_pending_updates=(
                payload.drop_pending_updates if payload is not None else None
            )
        )
        return result

    @app.get("/internal/introspection/ui", response_class=HTMLResponse)
    async def introspection_ui(
        _auth: None = Depends(require_introspection_auth),
    ) -> HTMLResponse:
        html_path = Path(__file__).parent / "static" / "internal" / "index.html"
        if not html_path.exists():
            raise HTTPException(status_code=500, detail="UI asset missing")
        return HTMLResponse(html_path.read_text(encoding="utf-8"))

    @app.get("/internal/introspection/attachments", response_model=list[Attachment])
    async def introspection_list_attachments(
        _auth: None = Depends(require_introspection_auth),
        session: AsyncSession = Depends(get_session),
    ) -> list[Attachment]:
        await _ensure_db_ready()
        return await repository.list_attachment_definitions(session)

    @app.post("/internal/introspection/attachments", response_model=Attachment)
    async def introspection_create_attachment(
        attachment: Attachment,
        _auth: None = Depends(require_introspection_auth),
        session: AsyncSession = Depends(get_session),
    ) -> Attachment:
        await _ensure_db_ready()
        out = await repository.upsert_attachment_definition(session, attachment)
        await session.commit()
        return out

    @app.put("/internal/introspection/attachments/{name}", response_model=Attachment)
    async def introspection_update_attachment(
        name: str,
        attachment: Attachment,
        _auth: None = Depends(require_introspection_auth),
        session: AsyncSession = Depends(get_session),
    ) -> Attachment:
        await _ensure_db_ready()
        normalized = attachment.model_copy(update={"name": name})
        out = await repository.upsert_attachment_definition(session, normalized)
        await session.commit()
        return out

    @app.delete("/internal/introspection/attachments/{name}")
    async def introspection_delete_attachment(
        name: str,
        _auth: None = Depends(require_introspection_auth),
        session: AsyncSession = Depends(get_session),
    ) -> dict[str, bool]:
        await _ensure_db_ready()
        removed = await repository.delete_attachment_definition(session, name)
        await session.commit()
        return {"removed": removed}

    @app.get("/internal/introspection/webhook-executions")
    async def introspection_list_webhook_executions(
        limit: int = Query(default=50, ge=1, le=500),
        offset: int = Query(default=0, ge=0),
        _auth: None = Depends(require_introspection_auth),
        session: AsyncSession = Depends(get_session),
    ) -> list[dict[str, Any]]:
        await _ensure_db_ready()
        rows = await repository.list_webhook_executions(
            session, limit=limit, offset=offset
        )
        return [
            {
                "id": row.id,
                "update_id": row.update_id,
                "chat_id": row.chat_id,
                "chat_type": row.chat_type,
                "raw_update": row.raw_update,
                "matched_attachments": row.matched_attachments,
                "overall_status": row.overall_status,
                "error": row.error,
                "received_at": row.received_at.isoformat(),
                "handler_executions": [
                    {
                        "id": item.id,
                        "attachment_name": item.attachment_name,
                        "handler": item.handler,
                        "rendered_args": item.rendered_args,
                        "ok": item.ok,
                        "result": item.result,
                        "error": item.error,
                        "duration_ms": item.duration_ms,
                        "finished_at": item.finished_at.isoformat(),
                    }
                    for item in row.handler_executions
                ],
            }
            for row in rows
        ]

    @app.get("/internal/introspection/webhook-executions/{execution_id}")
    async def introspection_get_webhook_execution(
        execution_id: int,
        _auth: None = Depends(require_introspection_auth),
        session: AsyncSession = Depends(get_session),
    ) -> dict[str, Any]:
        await _ensure_db_ready()
        row = await repository.get_webhook_execution_by_id(session, execution_id)
        if row is None:
            raise HTTPException(status_code=404, detail="Execution not found")
        return {
            "id": row.id,
            "update_id": row.update_id,
            "chat_id": row.chat_id,
            "chat_type": row.chat_type,
            "raw_update": row.raw_update,
            "matched_attachments": row.matched_attachments,
            "overall_status": row.overall_status,
            "error": row.error,
            "received_at": row.received_at.isoformat(),
            "handler_executions": [
                {
                    "id": item.id,
                    "attachment_name": item.attachment_name,
                    "handler": item.handler,
                    "rendered_args": item.rendered_args,
                    "ok": item.ok,
                    "result": item.result,
                    "error": item.error,
                    "duration_ms": item.duration_ms,
                    "finished_at": item.finished_at.isoformat(),
                }
                for item in row.handler_executions
            ],
        }

    @app.get("/internal/introspection/handlers")
    async def introspection_handlers(
        _auth: None = Depends(require_introspection_auth),
        session: AsyncSession = Depends(get_session),
    ) -> list[dict[str, Any]]:
        await _ensure_db_ready()
        rows = await repository.list_handler_stats(session)
        return [
            {
                **row,
                "last_run_at": (
                    row["last_run_at"].isoformat() if row.get("last_run_at") else None
                ),
            }
            for row in rows
        ]

    @app.get("/internal/introspection/match-criteria")
    async def introspection_match_criteria(
        _auth: None = Depends(require_introspection_auth),
    ) -> dict[str, list[str]]:
        return {
            "fields": [item.value for item in FieldName],
            "operators": [item.value for item in MatchOp],
            "parse_modes": [item.value for item in ParseMode],
            "execution_modes": [item.value for item in ExecutionMode],
        }

    return app
