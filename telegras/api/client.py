from __future__ import annotations

import os

import httpx

from .getting_updates import GetUpdatesRequest, SetWebhookRequest, Update, WebhookInfo
from .methods import GetMeResponse, SendMessageRequest


class TelegramBotAPI:
    def __init__(
        self,
        bot_token: str | None = None,
        *,
        timeout: float = 30.0,
    ) -> None:
        self.bot_token = bot_token or os.getenv("TELEGRAM_BOT_TOKEN")
        if not self.bot_token:
            raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
        self.timeout = timeout

    async def _post(self, method: str, payload: dict) -> dict:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(f"{self.base_url}/{method}", json=payload)
            response.raise_for_status()
            return response.json()

    async def _get(self, method: str) -> dict:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(f"{self.base_url}/{method}")
            response.raise_for_status()
            return response.json()

    async def send_message(self, request: SendMessageRequest) -> dict:
        return await self._post("sendMessage", request.model_dump(mode="json", exclude_none=True))

    async def get_webhook_info(self) -> WebhookInfo:
        payload = await self._get("getWebhookInfo")
        if payload.get("ok") is False:
            raise RuntimeError(payload.get("description", "Telegram getWebhookInfo failed"))
        result = payload.get("result", {})
        return WebhookInfo.model_validate(result)

    async def set_webhook(self, request: SetWebhookRequest) -> dict:
        return await self._post("setWebhook", request.model_dump(mode="json", exclude_none=True))

    async def delete_webhook(self, *, drop_pending_updates: bool | None = None) -> dict:
        payload: dict = {}
        if drop_pending_updates is not None:
            payload["drop_pending_updates"] = drop_pending_updates
        return await self._post("deleteWebhook", payload)

    async def get_updates(self, request: GetUpdatesRequest) -> list[Update]:
        payload = await self._post(
            "getUpdates",
            request.model_dump(mode="json", exclude_none=True),
        )
        if payload.get("ok") is False:
            raise RuntimeError(payload.get("description", "Telegram getUpdates failed"))
        result = payload.get("result", [])
        return [Update.model_validate(item) for item in result]

    async def get_me(self) -> GetMeResponse:
        payload = await self._get("getMe")
        return GetMeResponse.model_validate(payload)
