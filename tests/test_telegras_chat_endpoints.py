from __future__ import annotations

import importlib
from pathlib import Path
from unittest.mock import AsyncMock

from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from telegras.persistence.models import Base
from telegras.persistence.repository import create_or_get_interaction
from telegras.update_model import TelegramUpdate


def _build_app(monkeypatch, tmp_path: Path):
    db_path = tmp_path / "telegras_chat_endpoints.db"
    monkeypatch.setenv("TELEGRAS_DATABASE_URL", f"sqlite+aiosqlite:///{db_path}")

    db_module = importlib.import_module("telegras.persistence.db")
    app_module = importlib.import_module("telegras.app")
    importlib.reload(db_module)
    app_module = importlib.reload(app_module)
    app_module._db_initialized = False

    app = app_module.create_app()
    return app_module, app


async def _seed_interactions(db_url: str) -> None:
    engine = create_async_engine(db_url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    update_a = TelegramUpdate(
        update_id=1001,
        message={
            "message_id": 10,
            "date": 1700000000,
            "chat": {"id": 12345, "type": "channel"},
            "text": "hello from 12345",
        },
    )
    update_b = TelegramUpdate(
        update_id=1002,
        message={
            "message_id": 11,
            "date": 1700000001,
            "chat": {"id": 67890, "type": "channel"},
            "text": "hello from 67890",
        },
    )

    async with session_factory() as session:
        await create_or_get_interaction(session, update_a)
        await create_or_get_interaction(session, update_b)
        await session.commit()

    await engine.dispose()


def test_list_chat_ids_returns_distinct_chat_ids(monkeypatch, tmp_path: Path) -> None:
    app_module, app = _build_app(monkeypatch, tmp_path)
    db_url = f"sqlite+aiosqlite:///{tmp_path / 'telegras_chat_endpoints.db'}"

    import asyncio

    asyncio.run(_seed_interactions(db_url))

    client = TestClient(app)
    response = client.get("/v1/chats")

    assert response.status_code == 200
    assert response.json() == {"chat_ids": [12345, 67890]}


def test_history_endpoint_returns_messages_for_specific_chat(monkeypatch, tmp_path: Path) -> None:
    app_module, app = _build_app(monkeypatch, tmp_path)
    db_url = f"sqlite+aiosqlite:///{tmp_path / 'telegras_chat_endpoints.db'}"

    import asyncio

    asyncio.run(_seed_interactions(db_url))

    client = TestClient(app)
    response = client.get("/v1/chats/12345/history")

    assert response.status_code == 200
    payload = response.json()
    assert payload["chat_id"] == 12345
    assert len(payload["messages"]) == 1
    assert payload["messages"][0]["text"] == "hello from 12345"


def test_send_message_endpoint_sends_text_to_chat(monkeypatch, tmp_path: Path) -> None:
    app_module, app = _build_app(monkeypatch, tmp_path)

    mock_send = AsyncMock(return_value={"ok": True, "result": {"message_id": 42}})
    monkeypatch.setattr(app_module.telegram_api, "send_message", mock_send)

    client = TestClient(app)
    response = client.post("/v1/chats/12345/send", json={"message_body": "ping"})

    assert response.status_code == 200
    assert response.json() == {"ok": True, "result": {"message_id": 42}}
    mock_send.assert_awaited_once_with(chat_id=12345, text="ping")
