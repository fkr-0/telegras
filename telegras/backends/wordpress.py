from __future__ import annotations

from telegras.contracts import PublishBackend, PublishResult
from telegras.api.getting_updates import Update as TelegramUpdate


class WordPressPublishBackend(PublishBackend):
    """WordPress implementation for telegras, backed by the legacy dispatcher."""

    name = "wordpress"

    async def publish(self, update: TelegramUpdate) -> PublishResult:
        # Lazy import keeps telegras importable without tg_wp_bridge installed.

        raise NotImplementedError("WordPress publishing is not implemented yet.")
