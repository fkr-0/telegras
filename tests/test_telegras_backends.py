from __future__ import annotations

from pathlib import Path

import pytest
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from telegras.backends.factory import build_backends
from telegras.contracts import PublishBackend, PublishResult
from telegras.persistence import repository
from telegras.persistence.models import Base
from telegras.services.ingestion import TelegramIngestionService
from telegras.update_model import TelegramUpdate


class OkBackend(PublishBackend):
    name = "ok"

    async def publish(self, update: TelegramUpdate) -> PublishResult:
        return PublishResult(backend=self.name, status="processed", external_id="1")


class FailingBackend(PublishBackend):
    name = "broken"

    async def publish(self, update: TelegramUpdate) -> PublishResult:
        raise RuntimeError("boom")


@pytest.mark.asyncio
async def test_build_backends_uses_registry(monkeypatch) -> None:
    from telegras.backends import factory

    monkeypatch.setattr(
        factory,
        "AVAILABLE_BACKENDS",
        {"ok": OkBackend, "broken": FailingBackend},
    )

    backends = build_backends("ok,broken")

    assert [b.name for b in backends] == ["ok", "broken"]


@pytest.mark.asyncio
async def test_ingestion_service_runs_multiple_backends_and_marks_partial_failed(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "telegras_multi.db"
    engine = create_async_engine(f"sqlite+aiosqlite:///{db_path}")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    Session = async_sessionmaker(engine, expire_on_commit=False)
    service = TelegramIngestionService(backends=[OkBackend(), FailingBackend()])
    update = TelegramUpdate(
        update_id=999,
        channel_post={
            "message_id": 1,
            "date": 1700000000,
            "chat": {"id": 1, "type": "channel"},
            "text": "hello",
        },
    )

    async with Session() as session:
        interaction_id = await service.ingest(session, update)
        await session.commit()

        interaction = await repository.get_interaction_by_id(session, interaction_id)
        assert interaction is not None
        assert interaction.status == "partial_failed"
        assert len(interaction.publications) == 2
        assert {p.backend for p in interaction.publications} == {"ok", "broken"}
        assert any(p.status == "processed" for p in interaction.publications)
        assert any(p.status == "failed" for p in interaction.publications)
