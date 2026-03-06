from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from telegras.api.getting_updates import Update as TelegramUpdate


@dataclass(slots=True)
class PublishResult:
    backend: str
    status: str
    external_id: str | None = None
    url: str | None = None
    payload: dict[str, Any] = field(default_factory=dict)


class PublishBackend:
    """Minimal async publisher contract for Telegram updates."""

    name: str = "unknown"

    async def publish(self, update: TelegramUpdate) -> PublishResult:
        raise NotImplementedError
