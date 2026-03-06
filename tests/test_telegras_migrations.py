from __future__ import annotations

import logging
import sqlite3
from pathlib import Path

from alembic import command
from alembic.config import Config


def test_alembic_upgrade_head_creates_telegras_tables(tmp_path: Path) -> None:
    db_path = tmp_path / "telegras.db"

    cfg = Config("alembic.ini")
    cfg.set_main_option("script_location", "alembic")
    cfg.set_main_option("sqlalchemy.url", f"sqlite:///{db_path}")

    command.upgrade(cfg, "head")

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


def test_alembic_upgrade_keeps_existing_loggers_enabled(tmp_path: Path) -> None:
    db_path = tmp_path / "telegras_logging.db"
    logger = logging.getLogger("tg-wp-bridge.app")
    logger.disabled = False

    cfg = Config("alembic.ini")
    cfg.set_main_option("script_location", "alembic")
    cfg.set_main_option("sqlalchemy.url", f"sqlite:///{db_path}")

    command.upgrade(cfg, "head")

    assert logger.disabled is False
