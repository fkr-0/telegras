from __future__ import annotations

from telegras.api.client import TelegramBotAPI
from telegras.api.getting_updates import SetWebhookRequest, WebhookInfo
from telegras.api.methods import SendMessageRequest, GetMeResponse


def _client() -> TelegramBotAPI:
    return TelegramBotAPI()


async def send_message(chat_id: int | str, text: str) -> dict:
    return await _client().send_message(SendMessageRequest(chat_id=chat_id, text=text))


async def get_webhook_info() -> WebhookInfo:
    return await _client().get_webhook_info()


async def set_webhook(
    *,
    url: str,
    ip_address: str | None = None,
    max_connections: int | None = None,
    allowed_updates: list[str] | None = None,
    drop_pending_updates: bool | None = None,
    secret_token: str | None = None,
) -> dict:
    request = SetWebhookRequest(
        url=url,
        ip_address=ip_address,
        max_connections=max_connections,
        allowed_updates=allowed_updates,
        drop_pending_updates=drop_pending_updates,
        secret_token=secret_token,
    )
    return await _client().set_webhook(request)


async def get_me() -> GetMeResponse:
    return await _client().get_me()


async def delete_webhook(*, drop_pending_updates: bool | None = None) -> dict:
    return await _client().delete_webhook(
        drop_pending_updates=drop_pending_updates,
    )
