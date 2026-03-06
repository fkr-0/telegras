"""Typed Telegram Bot API submodule for telegras.

This is a curated, production-focused subset derived from generated specs in `docs/telegram_api`.
"""

from .client import TelegramBotAPI
from .getting_updates import Update, WebhookInfo, SetWebhookRequest
from .methods import SendMessageRequest, GetMeResponse

__all__ = [
    "TelegramBotAPI",
    "Update",
    "WebhookInfo",
    "SetWebhookRequest",
    "SendMessageRequest",
    "GetMeResponse",
]
