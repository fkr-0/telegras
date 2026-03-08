"""create telegras schema

Revision ID: 0001_create_telegras_schema
Revises: None
Create Date: 2026-03-08 00:00:00
"""
from __future__ import annotations

from alembic import op

from telegras.persistence.models import Base

revision = "0001_create_telegras_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    Base.metadata.create_all(bind)


def downgrade() -> None:
    bind = op.get_bind()
    Base.metadata.drop_all(bind)
