from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class PublicationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    interaction_id: int
    backend: str
    status: str
    external_id: str | None = None
    url: str | None = None
    payload: dict[str, Any]
    created_at: datetime


class TelegramInteractionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    update_id: int
    kind: str | None = None
    chat_id: int | None = None
    chat_type: str | None = None
    message_id: int | None = None
    text: str | None = None
    status: str
    error: str | None = None
    raw_update: dict[str, Any]
    received_at: datetime
    processed_at: datetime | None = None
    publications: list[PublicationRead] = []
