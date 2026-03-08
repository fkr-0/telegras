# telegras/startup.py
"""Startup validation utilities for telegras services."""

from __future__ import annotations

import asyncio

from .telegram_api import get_webhook_info, get_me
from .display import DisplayManager


async def validate_telegram_config() -> dict[str, object]:
    """Validate Telegram bot token and connectivity."""
    results = {
        "bot_token": {"status": "unknown", "message": ""},
    }

    try:
        bot_info = await get_me()
        results["bot_token"] = {
            "status": "ok",
            "message": f"Bot: @{bot_info.result.username}",
            "bot_id": bot_info.result.id,
            "username": bot_info.result.username,
        }
    except Exception as e:
        results["bot_token"] = {
            "status": "error",
            "message": str(e),
        }

    return results


async def validate_webhook_config() -> dict[str, object]:
    """Validate Telegram webhook status."""
    results = {
        "webhook": {"status": "unknown", "message": ""},
    }

    try:
        webhook_info = await get_webhook_info()
        if webhook_info.url:
            results["webhook"] = {
                "status": "configured",
                "message": f"Webhook: {webhook_info.url}",
                "url": webhook_info.url,
                "pending_updates": webhook_info.pending_update_count,
            }
        else:
            results["webhook"] = {
                "status": "not_configured",
                "message": "No webhook configured",
            }
    except Exception as e:
        results["webhook"] = {
            "status": "error",
            "message": str(e),
        }

    return results


async def _run_all_validations(display: DisplayManager) -> dict[str, object]:
    """Run all startup validations and display results."""
    results = {
        "telegram": await validate_telegram_config(),
        "webhook": await validate_webhook_config(),
        "overall": {"status": "ok", "errors": []},
    }

    # Display results
    display.print_section("Telegram Configuration")
    tg_result = results["telegram"]["bot_token"]
    if tg_result["status"] == "ok":
        display.print_status("", tg_result["message"], success=True)
    else:
        display.print_status("", tg_result["message"], success=False)
        results["overall"]["errors"].append("bot_token")

    display.print_section("Webhook Status")
    webhook_result = results["webhook"]["webhook"]
    if webhook_result["status"] == "configured":
        display.print_status("", webhook_result["message"], success=True)
    elif webhook_result["status"] == "not_configured":
        display.print_status("", webhook_result["message"], success=False)
        results["overall"]["errors"].append("webhook_not_set")
    else:
        display.print_status("", webhook_result["message"], success=False)
        results["overall"]["errors"].append("webhook_error")

    if results["overall"]["errors"]:
        results["overall"]["status"] = "failed"

    return results


def run_startup_validation_sync(
    *,
    display: DisplayManager | None = None,
) -> dict[str, object]:
    """Run all startup validations synchronously."""
    if display is None:
        display = DisplayManager()

    return asyncio.run(_run_all_validations(display))
