from __future__ import annotations

import sqlite3
from pathlib import Path



def test_telegras_db_init_creates_tables(tmp_path: Path, monkeypatch, invoke_cli) -> None:
    db_path = tmp_path / "telegras_cli.db"
    monkeypatch.setenv("TELEGRAS_DATABASE_URL", f"sqlite+aiosqlite:///{db_path}")

    result = invoke_cli(["db-init"])

    assert result.exit_code == 0

    conn = sqlite3.connect(db_path)
    try:
        tables = {
            row[0]
            for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        }
    finally:
        conn.close()

    assert "telegram_interactions" in tables
    assert "publications" in tables


def test_telegras_backends_lists_configured(monkeypatch, invoke_cli) -> None:
    monkeypatch.setenv("TELEGRAS_BACKENDS", "wordpress")

    result = invoke_cli(["backends"])

    assert result.exit_code == 0
    assert "wordpress" in result.output
