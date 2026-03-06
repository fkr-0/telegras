from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    pass


class TelegramInteraction(Base):
    __tablename__ = "telegram_interactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    update_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    kind: Mapped[str | None] = mapped_column(String(64), nullable=True)
    chat_id: Mapped[int | None] = mapped_column(nullable=True)
    chat_type: Mapped[str | None] = mapped_column(String(32), nullable=True)
    message_id: Mapped[int | None] = mapped_column(nullable=True)
    text: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(32), default="received", index=True)
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
    raw_update: Mapped[dict] = mapped_column(JSON)
    received_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utcnow
    )
    processed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    publications: Mapped[list[Publication]] = relationship(
        back_populates="interaction", cascade="all, delete-orphan"
    )


class Publication(Base):
    __tablename__ = "publications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    interaction_id: Mapped[int] = mapped_column(
        ForeignKey("telegram_interactions.id"), index=True
    )
    backend: Mapped[str] = mapped_column(String(64), index=True)
    status: Mapped[str] = mapped_column(String(32), index=True)
    external_id: Mapped[str | None] = mapped_column(String(128), nullable=True)
    url: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    payload: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utcnow
    )

    interaction: Mapped[TelegramInteraction] = relationship(
        back_populates="publications"
    )


class AttachmentDefinition(Base):
    __tablename__ = "attachment_definitions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    handler: Mapped[str | None] = mapped_column(String(256), nullable=True)
    handler_args: Mapped[list] = mapped_column(JSON, default=list)
    handler_chain: Mapped[list] = mapped_column(JSON, default=list)
    execution_mode: Mapped[str] = mapped_column(String(32), default="sequential")
    stop_on_error: Mapped[bool] = mapped_column(Boolean, default=True)
    enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    priority: Mapped[int] = mapped_column(Integer, default=100)
    stop_on_match: Mapped[bool] = mapped_column(Boolean, default=False)
    when_json: Mapped[dict] = mapped_column(JSON)
    parse_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    parse_mode: Mapped[str] = mapped_column(String(16), default="warn")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utcnow
    )


class WebhookExecution(Base):
    __tablename__ = "webhook_executions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    update_id: Mapped[int | None] = mapped_column(Integer, index=True, nullable=True)
    chat_id: Mapped[int | None] = mapped_column(Integer, index=True, nullable=True)
    chat_type: Mapped[str | None] = mapped_column(String(32), nullable=True)
    raw_update: Mapped[dict] = mapped_column(JSON)
    matched_attachments: Mapped[list] = mapped_column(JSON, default=list)
    overall_status: Mapped[str] = mapped_column(String(32), default="processed")
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
    received_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utcnow, index=True
    )

    handler_executions: Mapped[list[HandlerExecution]] = relationship(
        back_populates="webhook_execution", cascade="all, delete-orphan"
    )


class HandlerExecution(Base):
    __tablename__ = "handler_executions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    webhook_execution_id: Mapped[int] = mapped_column(
        ForeignKey("webhook_executions.id"), index=True
    )
    attachment_name: Mapped[str] = mapped_column(String(128), index=True)
    handler: Mapped[str] = mapped_column(String(256), index=True)
    rendered_args: Mapped[list] = mapped_column(JSON, default=list)
    ok: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    result: Mapped[dict | list | str | int | float | bool | None] = mapped_column(
        JSON, nullable=True
    )
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    finished_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    duration_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)

    webhook_execution: Mapped[WebhookExecution] = relationship(
        back_populates="handler_executions"
    )
