"""init telegras schema

Revision ID: 20260303_000001
Revises:
Create Date: 2026-03-03
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "20260303_000001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "telegram_interactions",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("update_id", sa.Integer(), nullable=False),
        sa.Column("kind", sa.String(length=64), nullable=True),
        sa.Column("chat_id", sa.Integer(), nullable=True),
        sa.Column("chat_type", sa.String(length=32), nullable=True),
        sa.Column("message_id", sa.Integer(), nullable=True),
        sa.Column("text", sa.Text(), nullable=True),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("error", sa.Text(), nullable=True),
        sa.Column("raw_update", sa.JSON(), nullable=False),
        sa.Column("received_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("processed_at", sa.DateTime(timezone=True), nullable=True),
        sa.UniqueConstraint("update_id"),
    )
    op.create_index("ix_telegram_interactions_update_id", "telegram_interactions", ["update_id"])
    op.create_index("ix_telegram_interactions_status", "telegram_interactions", ["status"])

    op.create_table(
        "publications",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("interaction_id", sa.Integer(), sa.ForeignKey("telegram_interactions.id"), nullable=False),
        sa.Column("backend", sa.String(length=64), nullable=False),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("external_id", sa.String(length=128), nullable=True),
        sa.Column("url", sa.String(length=1024), nullable=True),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_publications_interaction_id", "publications", ["interaction_id"])
    op.create_index("ix_publications_backend", "publications", ["backend"])
    op.create_index("ix_publications_status", "publications", ["status"])

    op.create_table(
        "attachment_definitions",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("handler", sa.String(length=256), nullable=True),
        sa.Column("handler_args", sa.JSON(), nullable=False),
        sa.Column("handler_chain", sa.JSON(), nullable=False),
        sa.Column("execution_mode", sa.String(length=32), nullable=False),
        sa.Column("stop_on_error", sa.Boolean(), nullable=False),
        sa.Column("enabled", sa.Boolean(), nullable=False),
        sa.Column("priority", sa.Integer(), nullable=False),
        sa.Column("stop_on_match", sa.Boolean(), nullable=False),
        sa.Column("when_json", sa.JSON(), nullable=False),
        sa.Column("parse_json", sa.JSON(), nullable=True),
        sa.Column("parse_mode", sa.String(length=16), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.UniqueConstraint("name"),
    )
    op.create_index("ix_attachment_definitions_name", "attachment_definitions", ["name"])

    op.create_table(
        "webhook_executions",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("update_id", sa.Integer(), nullable=True),
        sa.Column("chat_id", sa.Integer(), nullable=True),
        sa.Column("chat_type", sa.String(length=32), nullable=True),
        sa.Column("raw_update", sa.JSON(), nullable=False),
        sa.Column("matched_attachments", sa.JSON(), nullable=False),
        sa.Column("overall_status", sa.String(length=32), nullable=False),
        sa.Column("error", sa.Text(), nullable=True),
        sa.Column("received_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_webhook_executions_update_id", "webhook_executions", ["update_id"])
    op.create_index("ix_webhook_executions_chat_id", "webhook_executions", ["chat_id"])
    op.create_index("ix_webhook_executions_received_at", "webhook_executions", ["received_at"])

    op.create_table(
        "handler_executions",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("webhook_execution_id", sa.Integer(), sa.ForeignKey("webhook_executions.id"), nullable=False),
        sa.Column("attachment_name", sa.String(length=128), nullable=False),
        sa.Column("handler", sa.String(length=256), nullable=False),
        sa.Column("rendered_args", sa.JSON(), nullable=False),
        sa.Column("ok", sa.Boolean(), nullable=False),
        sa.Column("result", sa.JSON(), nullable=True),
        sa.Column("error", sa.Text(), nullable=True),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("finished_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("duration_ms", sa.Integer(), nullable=True),
    )
    op.create_index("ix_handler_executions_webhook_execution_id", "handler_executions", ["webhook_execution_id"])
    op.create_index("ix_handler_executions_attachment_name", "handler_executions", ["attachment_name"])
    op.create_index("ix_handler_executions_handler", "handler_executions", ["handler"])
    op.create_index("ix_handler_executions_ok", "handler_executions", ["ok"])


def downgrade() -> None:
    op.drop_index("ix_handler_executions_ok", table_name="handler_executions")
    op.drop_index("ix_handler_executions_handler", table_name="handler_executions")
    op.drop_index("ix_handler_executions_attachment_name", table_name="handler_executions")
    op.drop_index("ix_handler_executions_webhook_execution_id", table_name="handler_executions")
    op.drop_table("handler_executions")

    op.drop_index("ix_webhook_executions_received_at", table_name="webhook_executions")
    op.drop_index("ix_webhook_executions_chat_id", table_name="webhook_executions")
    op.drop_index("ix_webhook_executions_update_id", table_name="webhook_executions")
    op.drop_table("webhook_executions")

    op.drop_index("ix_attachment_definitions_name", table_name="attachment_definitions")
    op.drop_table("attachment_definitions")

    op.drop_index("ix_publications_status", table_name="publications")
    op.drop_index("ix_publications_backend", table_name="publications")
    op.drop_index("ix_publications_interaction_id", table_name="publications")
    op.drop_table("publications")

    op.drop_index("ix_telegram_interactions_status", table_name="telegram_interactions")
    op.drop_index("ix_telegram_interactions_update_id", table_name="telegram_interactions")
    op.drop_table("telegram_interactions")
