# tests/test_logging_utils.py
"""Tests for logging utilities."""

from __future__ import annotations

import pytest
from pathlib import Path
from telegras.logging_utils import (
    resolve_writable_dir,
    rotate_logs,
    record_update_log,
)
import tempfile
import os


def test_resolve_writable_dir(tmp_path):
    """Test resolving writable directory."""
    result = resolve_writable_dir(
        tmp_path / "logs",
        fallback_env_var="TEST_FALLBACK",
        fallback_subdir="test_logs",
    )
    assert result.exists()
    assert (tmp_path / "logs").exists()


def test_record_update_log(tmp_path, monkeypatch):
    """Test recording update log."""
    monkeypatch.setenv("STORAGE_DIR", str(tmp_path))

    class MockUpdate:
        update_id = 123
        def model_dump(self, **kwargs):
            return {"update_id": 123, "text": "test"}

    update = MockUpdate()
    result = record_update_log(update, result={"id": 456})

    assert result["tg_path"] is not None
    assert Path(result["tg_path"]).exists()


def test_rotate_logs_by_count(tmp_path, monkeypatch):
    """Test rotating logs by file count."""
    monkeypatch.setenv("STORAGE_DIR", str(tmp_path))
    monkeypatch.setenv("LOG_MAX_FILES", "3")

    # Create 5 test log files
    for i in range(5):
        log_file = tmp_path / f"test_{i}.json"
        log_file.write_text('{"test": "data"}')

    rotate_logs(tmp_path)

    # Should only have 3 files remaining
    remaining = list(tmp_path.glob("*.json"))
    assert len(remaining) <= 3


def test_rotate_logs_by_size(tmp_path, monkeypatch):
    """Test rotating logs by total size."""
    monkeypatch.setenv("STORAGE_DIR", str(tmp_path))
    monkeypatch.setenv("LOG_MAX_BYTES", "500")

    # Create test log files with known sizes
    for i in range(3):
        log_file = tmp_path / f"test_{i}.json"
        log_file.write_text("x" * 250)  # 250 bytes each

    rotate_logs(tmp_path)

    # Total size should be <= 500 bytes
    total_size = sum(f.stat().st_size for f in tmp_path.glob("*.json"))
    assert total_size <= 500
