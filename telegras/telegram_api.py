from __future__ import annotations

import httpx
import logging

from telegras.api.client import TelegramBotAPI
from telegras.api.getting_updates import (
    GetUpdatesRequest,
    SetWebhookRequest,
    Update,
    WebhookInfo,
)
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


async def get_updates(
    *,
    offset: int | None = None,
    limit: int | None = None,
    timeout: int | None = None,
    allowed_updates: list[str] | None = None,
) -> list[Update]:
    request = GetUpdatesRequest(
        offset=offset,
        limit=limit,
        timeout=timeout,
        allowed_updates=allowed_updates,
    )
    return await _client().get_updates(request)


async def get_file_direct_url(file_id: str) -> str | None:
    """
    Given a Telegram file_id, return a direct HTTPS URL for that file.

    Note: This URL is temporary and should be used only to download once.
    """
    client = _client()
    bot_url = f"{client.base_url}/getFile"

    async with httpx.AsyncClient() as http_client:
        resp = await http_client.get(
            bot_url,
            params={"file_id": file_id},
            timeout=10.0
        )
        resp.raise_for_status()
        data = await resp.json()
        if not data.get("ok"):
            log = logging.getLogger("telegras.telegram_api")
            log.warning("getFile failed: %s", data)
            return None

        file_path = data["result"]["file_path"]
        token = client.bot_token
        return f"https://api.telegram.org/file/bot{token}/{file_path}"


async def download_file(file_url: str) -> bytes:
    """Download a Telegram file via HTTPS."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(file_url, timeout=30.0)
        resp.raise_for_status()
        return resp.content
