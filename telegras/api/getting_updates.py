from __future__ import annotations

from pydantic import BaseModel, Field

from telegras.update_model import TelegramUpdate


class Update(TelegramUpdate):
    """Runtime update model used by telegras ingestion/webhook paths."""


class WebhookInfo(BaseModel):
    url: str = ""
    has_custom_certificate: bool = False
    pending_update_count: int = 0
    ip_address: str | None = None
    last_error_date: int | None = None
    last_error_message: str | None = None
    last_synchronization_error_date: int | None = None
    max_connections: int | None = None
    allowed_updates: list[str] | None = None


class SetWebhookRequest(BaseModel):
    url: str
    ip_address: str | None = None
    max_connections: int | None = None
    allowed_updates: list[str] | None = None
    drop_pending_updates: bool | None = None
    secret_token: str | None = Field(default=None, min_length=1, max_length=256)


class GetUpdatesRequest(BaseModel):
    offset: int | None = None
    limit: int | None = Field(default=None, ge=1, le=100)
    timeout: int | None = Field(default=None, ge=0)
    allowed_updates: list[str] | None = None
