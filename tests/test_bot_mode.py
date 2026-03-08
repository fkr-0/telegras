from __future__ import annotations

import importlib
import sqlite3
import time
from pathlib import Path

from fastapi.testclient import TestClient
from telegras.api.getting_updates import Update


def _build_app(monkeypatch, tmp_path: Path, *, bot_mode: str | None = None):
    db_path = tmp_path / "telegras_bot_mode.db"
    monkeypatch.setenv("TELEGRAS_DATABASE_URL", f"sqlite+aiosqlite:///{db_path}")
    if bot_mode is None:
        monkeypatch.delenv("BOT_MODE", raising=False)
    else:
        monkeypatch.setenv("BOT_MODE", bot_mode)

    db_module = importlib.import_module("telegras.persistence.db")
    app_module = importlib.import_module("telegras.app")
    importlib.reload(db_module)
    app_module = importlib.reload(app_module)
    app_module._db_initialized = False
    app = app_module.create_app()
    return app_module, app, db_path


def test_default_bot_mode_is_webhook(monkeypatch, tmp_path: Path) -> None:
    settings_module = importlib.import_module("telegras.settings")
    monkeypatch.delenv("BOT_MODE", raising=False)
    settings_module = importlib.reload(settings_module)

    settings = settings_module.AppSettings()
    assert settings.bot_mode == "webhook"


def test_polling_mode_starts_background_ingestion(monkeypatch, tmp_path: Path) -> None:
    app_module, app, db_path = _build_app(monkeypatch, tmp_path, bot_mode="polling")

    calls = {"get_updates": 0}

    async def _mock_get_updates(*, offset=None, limit=None, timeout=None, allowed_updates=None):
        calls["get_updates"] += 1
        if calls["get_updates"] == 1:
            return [
                Update.model_validate(
                    {
                        "update_id": 700001,
                        "message": {
                            "message_id": 1,
                            "date": 1700000000,
                            "chat": {"id": 123, "type": "group"},
                            "text": "polling hello",
                        },
                    }
                )
            ]
        return []

    async def _mock_delete_webhook(*, drop_pending_updates=None):
        return {"ok": True, "result": True}

    monkeypatch.setattr(app_module.telegram_api, "get_updates", _mock_get_updates)
    monkeypatch.setattr(app_module.telegram_api, "delete_webhook", _mock_delete_webhook)

    with TestClient(app) as client:
        health = client.get("/healthz")
        assert health.status_code == 200
        time.sleep(0.2)

    assert calls["get_updates"] >= 1

    conn = sqlite3.connect(db_path)
    try:
        row = conn.execute("SELECT COUNT(*) FROM telegram_interactions").fetchone()
    finally:
        conn.close()

    assert row is not None
    assert row[0] >= 1
