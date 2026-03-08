# telegras/logging_utils.py
"""Structured logging utilities for telegras services."""

from __future__ import annotations

import json
import logging
import os
import tempfile
import traceback
from datetime import datetime, timezone
from pathlib import Path

log = logging.getLogger("telegras.logging_utils")


def resolve_writable_dir(
    preferred: Path,
    *,
    fallback_env_var: str,
    fallback_subdir: str,
) -> Path:
    """Return a writable directory path, falling back to /tmp when needed."""
    try:
        preferred.mkdir(parents=True, exist_ok=True)
        return preferred
    except PermissionError as exc:
        fallback_root = Path(
            os.getenv(
                fallback_env_var,
                str(Path(tempfile.gettempdir()) / "telegras" / fallback_subdir),
            )
        )
        fallback_root.mkdir(parents=True, exist_ok=True)
        log.warning(
            "Directory %s is not writable (%s); falling back to %s",
            preferred,
            exc,
            fallback_root,
        )
        return fallback_root


def rotate_logs(storage_dir: Path) -> None:
    """Rotate log files based on count or size limits."""
    try:
        files = sorted(
            (p for p in storage_dir.glob("*.json") if p.is_file()),
            key=lambda p: p.stat().st_mtime,
        )
        max_files = int(os.getenv("LOG_MAX_FILES", "0") or 0)
        if max_files > 0 and len(files) > max_files:
            to_remove = files[: len(files) - max_files]
            for f in to_remove:
                try:
                    f.unlink()
                    log.debug("Rotated log file %s (exceeded max files)", f)
                except Exception:
                    log.warning("Failed to remove old log file %s", f)
            files = files[len(files) - max_files :]

        max_bytes = int(os.getenv("LOG_MAX_BYTES", "0") or 0)
        if max_bytes > 0:
            total = sum(f.stat().st_size for f in files)
            idx = 0
            while total > max_bytes and idx < len(files):
                f = files[idx]
                try:
                    size = f.stat().st_size
                    f.unlink()
                    log.debug("Rotated log file %s (exceeded max bytes)", f)
                    total -= size
                except Exception:
                    log.warning("Failed to remove old log file %s", f)
                idx += 1
    except Exception:
        log.exception("Error while rotating log files in %s", storage_dir)


def record_update_log(
    update: object,
    result: dict | None = None,
    *,
    tg_message_id: int | None = None,
) -> dict[str, str | None]:
    """Record raw update and optional result to disk."""
    preferred_storage_dir = Path(os.getenv("STORAGE_DIR", "data/logs"))
    storage_dir = resolve_writable_dir(
        preferred_storage_dir,
        fallback_env_var="STORAGE_FALLBACK_DIR",
        fallback_subdir="logs",
    )
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    tgid = tg_message_id if tg_message_id is not None else getattr(update, 'update_id', ts)
    out: dict[str, str | None] = {"tg_path": None, "result_path": None}

    tg_filename = f"{ts}_tg_{tgid}.json"
    try:
        # Handle both Pydantic models and dict-like updates
        if hasattr(update, 'model_dump'):
            update_data = update.model_dump(mode="json", exclude_none=True)
        elif hasattr(update, 'dict'):
            update_data = update.dict(mode="json", exclude_none=True)
        else:
            update_data = update

        with (storage_dir / tg_filename).open("w", encoding="utf-8") as fh:
            json.dump(update_data, fh, indent=2)
        out["tg_path"] = str(storage_dir / tg_filename)
    except Exception:
        log.exception("Failed to write update log")

    if result is not None:
        result_id = result.get("id") if isinstance(result, dict) else None
        result_filename = f"{ts}_result_{tgid}_{result_id or 'unknown'}.json"
        try:
            with (storage_dir / result_filename).open("w", encoding="utf-8") as fh:
                json.dump(result, fh, indent=2)
            out["result_path"] = str(storage_dir / result_filename)
        except Exception:
            log.exception("Failed to write result log")

    rotate_logs(storage_dir)
    return out


def record_error_artifact(
    update: object,
    exc: BaseException,
    *,
    tg_message_id: int | None = None,
    result: dict | None = None,
) -> str | None:
    """Write a timestamped .error artifact with raw update and traceback."""
    preferred_storage_dir = Path(os.getenv("STORAGE_DIR", "data/logs"))
    storage_dir = resolve_writable_dir(
        preferred_storage_dir,
        fallback_env_var="STORAGE_FALLBACK_DIR",
        fallback_subdir="logs",
    )
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    error_path = storage_dir / f"{ts}.error"

    # Handle update serialization
    if hasattr(update, 'model_dump'):
        update_data = update.model_dump(mode="json", exclude_none=True)
    elif hasattr(update, 'dict'):
        update_data = update.dict(mode="json", exclude_none=True)
    else:
        update_data = update

    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "message_id": tg_message_id,
        "update": update_data,
        "result": result,
        "exception": f"{type(exc).__name__}: {exc}",
        "traceback": "".join(
            traceback.format_exception(type(exc), exc, exc.__traceback__)
        ),
    }
    try:
        with error_path.open("w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
        rotate_logs(storage_dir)
        return str(error_path)
    except Exception:
        log.exception(
            "Failed to write error artifact for update %s", getattr(update, 'update_id', 'unknown')
        )
        return None
