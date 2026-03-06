from __future__ import annotations

from telegras.contracts import PublishBackend, PublishResult
from telegras.api.getting_updates import Update as TelegramUpdate


class WordPressPublishBackend(PublishBackend):
    """WordPress implementation for telegras, backed by the legacy dispatcher."""

    name = "wordpress"

    async def publish(self, update: TelegramUpdate) -> PublishResult:
        # Lazy import keeps telegras importable without tg_wp_bridge installed.
        from tg_wp_bridge import handlers as _handlers  # noqa: F401
        from tg_wp_bridge.dispatcher import dispatch_update

        await dispatch_update(update)
        return PublishResult(backend=self.name, status="processed")
