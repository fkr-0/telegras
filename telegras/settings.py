from __future__ import annotations

import os
from dataclasses import dataclass
from enum import Enum


class BotMode(str, Enum):
    """How telegras receives Telegram updates."""

    WEBHOOK = "webhook"
    POLLING = "polling"


@dataclass(frozen=True)
class AppSettings:
    """Runtime settings sourced from environment variables."""

    bot_mode: BotMode = BotMode.WEBHOOK
    polling_timeout_seconds: int = 30
    polling_error_backoff_seconds: float = 2.0
    polling_idle_sleep_seconds: float = 0.25

    @classmethod
    def from_env(cls) -> "AppSettings":
        mode_raw = os.getenv("BOT_MODE", BotMode.WEBHOOK.value).strip().lower()
        bot_mode = BotMode(mode_raw) if mode_raw in {m.value for m in BotMode} else BotMode.WEBHOOK

        def _int(name: str, default: int) -> int:
            raw = os.getenv(name)
            if raw is None:
                return default
            try:
                value = int(raw)
            except ValueError:
                return default
            return value if value >= 0 else default

        def _float(name: str, default: float) -> float:
            raw = os.getenv(name)
            if raw is None:
                return default
            try:
                value = float(raw)
            except ValueError:
                return default
            return value if value >= 0 else default

        return cls(
            bot_mode=bot_mode,
            polling_timeout_seconds=_int("BOT_POLLING_TIMEOUT_SECONDS", 30),
            polling_error_backoff_seconds=_float("BOT_POLLING_ERROR_BACKOFF_SECONDS", 2.0),
            polling_idle_sleep_seconds=_float("BOT_POLLING_IDLE_SLEEP_SECONDS", 0.25),
        )
