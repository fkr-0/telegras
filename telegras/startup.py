"""telegras startup validation utilities."""

from __future__ import annotations

import asyncio
from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel, Field

from .display import DisplayManager
from .telegram_api import get_webhook_info, get_me, set_webhook


class BotTokenStatus(str, Enum):
    UNKNOWN = "unknown"
    OK = "ok"
    ERROR = "error"


class WebhookStatus(str, Enum):
    UNKNOWN = "unknown"
    CONFIGURED = "configured"
    NOT_CONFIGURED = "not_configured"
    ERROR = "error"
    SETTING = "setting"


class BotTokenValidation(BaseModel):
    status: BotTokenStatus = BotTokenStatus.UNKNOWN
    message: str = ""
    bot_id: int | None = None
    username: str | None = None


class WebhookValidation(BaseModel):
    status: WebhookStatus = WebhookStatus.UNKNOWN
    message: str = ""
    url: str | None = None
    pending_updates: int | None = None


class StartupValidation(BaseModel):
    telegram: BotTokenValidation
    webhook: WebhookValidation
    overall_status: Literal["ok", "failed"]
    errors: List[str] = Field(default_factory=list)


_latest_validation: StartupValidation | None = None


async def validate_telegram_config() -> BotTokenValidation:
    """Validate Telegram bot token connectivity and return structured result."""
    try:
        bot_info = await get_me()
        return BotTokenValidation(
            status=BotTokenStatus.OK,
            message=f"Bot: @{bot_info.result.username}",
            bot_id=bot_info.result.id,
            username=bot_info.result.username,
        )
    except Exception as exc:
        return BotTokenValidation(
            status=BotTokenStatus.ERROR,
            message=str(exc),
        )


async def validate_webhook_config() -> WebhookValidation:
    """Return structured webhook status without modifying it."""
    try:
        webhook_info = await get_webhook_info()
        if webhook_info.url:
            return WebhookValidation(
                status=WebhookStatus.CONFIGURED,
                message=f"Webhook: {webhook_info.url}",
                url=webhook_info.url,
                pending_updates=webhook_info.pending_update_count,
            )
        return WebhookValidation(
            status=WebhookStatus.NOT_CONFIGURED,
            message="No webhook configured",
        )
    except Exception as exc:
        return WebhookValidation(
            status=WebhookStatus.ERROR,
            message=str(exc),
        )


async def ensure_webhook_configured(
    expected_url: str | None,
    *,
    secret_token: str | None = None,
) -> WebhookValidation:
    """Ensure the webhook is pointing to the expected URL."""
    if not expected_url:
        return WebhookValidation(
            status=WebhookStatus.NOT_CONFIGURED,
            message="Webhook URL not provided",
        )

    try:
        info = await get_webhook_info()
    except Exception as exc:
        return WebhookValidation(
            status=WebhookStatus.ERROR,
            message=f"Failed to inspect webhook: {exc}",
        )

    if info.url == expected_url and not info.last_error_message:
        return WebhookValidation(
            status=WebhookStatus.CONFIGURED,
            message=f"Webhook already configured: {info.url}",
            url=info.url,
            pending_updates=info.pending_update_count,
        )

    try:
        result = await set_webhook(url=expected_url, secret_token=secret_token)
        if result.get("ok"):
            return WebhookValidation(
                status=WebhookStatus.CONFIGURED,
                message=f"Webhook configured: {expected_url}",
                url=expected_url,
            )
        return WebhookValidation(
            status=WebhookStatus.ERROR,
            message=f"Failed to set webhook: {result.get('description', 'unknown error')}",
        )
    except Exception as exc:
        return WebhookValidation(
            status=WebhookStatus.ERROR,
            message=f"Exception while setting webhook: {exc}",
        )


async def run_startup_validation(
    *,
    expected_webhook_url: str | None = None,
    secret_token: str | None = None,
    auto_setup_webhook: bool = False,
    display: DisplayManager | None = None,
) -> StartupValidation:
    """Run Telegram startup validation and optional webhook setup."""
    global _latest_validation
    telegram = await validate_telegram_config()
    webhook = await validate_webhook_config()

    if auto_setup_webhook and expected_webhook_url:
        webhook = await ensure_webhook_configured(
            expected_webhook_url, secret_token=secret_token
        )

    errors: List[str] = []
    if telegram.status != BotTokenStatus.OK:
        errors.append("bot_token")
    if webhook.status != WebhookStatus.CONFIGURED:
        errors.append("webhook")

    overall_status = "failed" if errors else "ok"
    result = StartupValidation(
        telegram=telegram,
        webhook=webhook,
        overall_status=overall_status,
        errors=errors,
    )

    _latest_validation = result

    return result


def get_latest_validation() -> StartupValidation | None:
    """Return the most recent validation run (if any)."""
    return _latest_validation


def run_startup_validation_sync(
    *,
    expected_webhook_url: str | None = None,
    secret_token: str | None = None,
    auto_setup_webhook: bool = False,
    display: DisplayManager | None = None,
) -> StartupValidation:
    """Run startup validation synchronously (used by CLI)."""
    if display is None:
        display = DisplayManager()
    return asyncio.run(
        run_startup_validation(
            expected_webhook_url=expected_webhook_url,
            secret_token=secret_token,
            auto_setup_webhook=auto_setup_webhook,
            display=display,
        )
    )
