from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from telegras.backends.factory import build_backends
from telegras.contracts import PublishBackend, PublishResult
from telegras.persistence import repository
from telegras.api.getting_updates import Update as TelegramUpdate

log = logging.getLogger("telegras.ingestion")


class TelegramIngestionService:
    """Persists every Telegram interaction and dispatches to a publication backend."""

    def __init__(
        self,
        backend: PublishBackend | None = None,
        backends: list[PublishBackend] | None = None,
    ) -> None:
        if backends is not None:
            self.backends = backends
        elif backend is not None:
            self.backends = [backend]
        else:
            # Option B-ready hook: backend set is configured via env/registry.
            self.backends = build_backends()

    async def ingest(self, session: AsyncSession, update: TelegramUpdate) -> int:
        interaction = await repository.create_or_get_interaction(session, update)

        if interaction.status in {"processed", "failed", "partial_failed"}:
            return interaction.id

        results: list[PublishResult] = []
        for backend in self.backends:
            try:
                result = await backend.publish(update)
            except Exception as exc:
                log.exception(
                    "Backend %s failed for update_id=%s",
                    backend.name,
                    update.update_id,
                )
                result = PublishResult(
                    backend=backend.name,
                    status="failed",
                    payload={"error": str(exc)},
                )
            results.append(result)
            await repository.add_publication(session, interaction, result)

        failed = [r for r in results if r.status == "failed"]
        if failed and len(failed) == len(results):
            await repository.finalize_interaction(
                session,
                interaction,
                status="failed",
                error="; ".join(
                    f"{r.backend}: {r.payload.get('error', 'unknown')}" for r in failed
                ),
            )
        elif failed:
            await repository.finalize_interaction(
                session,
                interaction,
                status="partial_failed",
                error="; ".join(
                    f"{r.backend}: {r.payload.get('error', 'unknown')}" for r in failed
                ),
            )
        else:
            await repository.finalize_interaction(
                session,
                interaction,
                status="processed",
                error=None,
            )

        return interaction.id
