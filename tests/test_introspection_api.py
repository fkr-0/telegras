from __future__ import annotations

import importlib
from pathlib import Path

from fastapi.testclient import TestClient


def _build_app(monkeypatch, tmp_path: Path):
    db_path = tmp_path / "telegras_introspection.db"
    monkeypatch.setenv("TELEGRAS_DATABASE_URL", f"sqlite+aiosqlite:///{db_path}")
    monkeypatch.setenv("INTROSPECTION_TOKEN", "secret-introspect")

    db_module = importlib.import_module("telegras.persistence.db")
    app_module = importlib.import_module("telegras.app")
    importlib.reload(db_module)
    app_module = importlib.reload(app_module)
    app_module._db_initialized = False

    return app_module.app


def _auth_headers() -> dict[str, str]:
    return {"Authorization": "Bearer secret-introspect"}


def test_introspection_requires_token(monkeypatch, tmp_path: Path) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    resp = client.get("/internal/introspection/config")
    assert resp.status_code == 401

    ui_resp = client.get("/internal/introspection/ui")
    assert ui_resp.status_code == 401


def test_introspection_ui_served_with_token(monkeypatch, tmp_path: Path) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    resp = client.get("/internal/introspection/ui", headers=_auth_headers())
    assert resp.status_code == 200
    assert "text/html" in resp.headers["content-type"]
    assert "<title>telegras internal overview</title>" in resp.text


def test_introspection_webhook_status_and_delete(monkeypatch, tmp_path: Path) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    app_module = importlib.import_module("telegras.app")
    async def _mock_status():
        return {"url": "https://example.com/hook", "pending_update_count": 1}
    async def _mock_delete(drop_pending_updates=None):
        return {
            "ok": True,
            "result": True,
            "drop_pending_updates": drop_pending_updates,
        }
    monkeypatch.setattr(
        app_module.telegram_api,
        "get_webhook_info",
        _mock_status,
    )
    monkeypatch.setattr(
        app_module.telegram_api,
        "delete_webhook",
        _mock_delete,
    )

    status_resp = client.get(
        "/internal/introspection/webhook/status",
        headers=_auth_headers(),
    )
    assert status_resp.status_code == 200
    assert status_resp.json()["url"] == "https://example.com/hook"

    delete_resp = client.request(
        "DELETE",
        "/internal/introspection/webhook",
        headers=_auth_headers(),
        json={"drop_pending_updates": True},
    )
    assert delete_resp.status_code == 200
    assert delete_resp.json()["ok"] is True
    assert delete_resp.json()["drop_pending_updates"] is True


def test_introspection_attachment_crud_and_match_criteria(monkeypatch, tmp_path: Path) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    create_resp = client.post(
        "/internal/introspection/attachments",
        headers=_auth_headers(),
        json={
            "name": "mail-title",
            "handler": "handlers.python:eval",
            "handler_args": ["result='{{ match.title }}'"],
            "parse": {
                "regex": {
                    "title": "^(?P<title>[^\\n]+)"
                }
            },
            "parse_mode": "warn",
            "when": {
                "op": "leaf",
                "leaf": {
                    "field": "chat.type",
                    "match": "eq",
                    "value": "group",
                },
            },
        },
    )
    assert create_resp.status_code == 200

    list_resp = client.get(
        "/internal/introspection/attachments", headers=_auth_headers()
    )
    assert list_resp.status_code == 200
    names = [row["name"] for row in list_resp.json()]
    assert "mail-title" in names

    criteria_resp = client.get(
        "/internal/introspection/match-criteria", headers=_auth_headers()
    )
    assert criteria_resp.status_code == 200
    body = criteria_resp.json()
    assert "fields" in body
    assert "operators" in body
    assert "parse_modes" in body

    del_resp = client.delete(
        "/internal/introspection/attachments/mail-title",
        headers=_auth_headers(),
    )
    assert del_resp.status_code == 200
    assert del_resp.json() == {"removed": True}


def test_execution_history_and_handler_stats(monkeypatch, tmp_path: Path) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    create_resp = client.post(
        "/internal/introspection/attachments",
        headers=_auth_headers(),
        json={
            "name": "grouped-eval",
            "handler_chain": [
                {
                    "handler": "handlers.python:eval",
                    "handler_args": ["x='{{ message.title }}'"],
                },
                {
                    "handler": "handlers.python:eval",
                    "handler_args": ["y='{{ message.full }}'"],
                }
            ],
            "execution_mode": "sequential",
            "stop_on_error": True,
            "when": {
                "op": "leaf",
                "leaf": {
                    "field": "chat.type",
                    "match": "eq",
                    "value": "group",
                },
            },
        },
    )
    assert create_resp.status_code == 200

    exec_resp = client.post(
        "/v1/webhook-attachments/execute",
        json={
            "update": {
                "update_id": 202020,
                "message": {
                    "message_id": 77,
                    "date": 1700000000,
                    "chat": {"id": 700, "type": "group", "title": "Ops"},
                    "text": "Release update\\nFull detail line",
                },
            }
        },
    )
    assert exec_resp.status_code == 200

    history_resp = client.get(
        "/internal/introspection/webhook-executions", headers=_auth_headers()
    )
    assert history_resp.status_code == 200
    rows = history_resp.json()
    assert len(rows) >= 1
    latest = rows[0]
    assert latest["update_id"] == 202020
    assert "matched_attachments" in latest
    assert "handler_executions" in latest
    assert len(latest["handler_executions"]) == 2

    detail_resp = client.get(
        f"/internal/introspection/webhook-executions/{latest['id']}",
        headers=_auth_headers(),
    )
    assert detail_resp.status_code == 200
    assert detail_resp.json()["id"] == latest["id"]
    assert detail_resp.json()["update_id"] == 202020

    handlers_resp = client.get(
        "/internal/introspection/handlers", headers=_auth_headers()
    )
    assert handlers_resp.status_code == 200
    stats = handlers_resp.json()
    by_name = {row["handler"]: row for row in stats}
    assert "handlers.python:eval" in by_name
    assert by_name["handlers.python:eval"]["runs"] >= 2

    config_resp = client.get("/internal/introspection/config", headers=_auth_headers())
    assert config_resp.status_code == 200
    cfg = config_resp.json()
    assert "bot_api" in cfg
    assert "last_webhook_trigger" in cfg
    assert "handler_bindings" in cfg
