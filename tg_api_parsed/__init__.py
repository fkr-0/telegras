"""Curated Telegram Bot API exports."""

from __future__ import annotations

from .getting_updates import Update, WebhookInfo, SetWebhookRequest
from .methods import SendMessageRequest, GetMeResponse

__all__ = [
    "Update",
    "WebhookInfo",
    "SetWebhookRequest",
    "SendMessageRequest",
    "GetMeResponse",
]
