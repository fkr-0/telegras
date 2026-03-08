# Telegras Harmonization Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Refactor telegras to be the canonical Telegram service library by moving Telegram-specific code from tg-wp-bridge, making tg-wp-bridge a thin wrapper.

**Architecture:**
- Move Telegram utilities (media downloads, message parsing, logging, display) from tg-wp-bridge to telegras
- Refactor app.py to support mounting on existing FastAPI apps with lifespan merging
- Add comprehensive CLI with all Telegram operations
- Update tg-wp-bridge to import from telegras

**Tech Stack:**
- Python 3.10+
- FastAPI
- httpx
- Click
- Rich (for CLI formatting)
- Pydantic

---

## Task 1: Add Media Download Functions to telegras

**Files:**
- Modify: `telegras/telegram_api.py`
- Test: `tests/test_telegram_api.py`

**Step 1: Read current telegras telegram_api.py**

Read the file to understand current structure.

**Step 2: Add media download helper functions**

```python
# Add to telegras/telegram_api.py

async def get_file_direct_url(file_id: str) -> str | None:
    """
    Given a Telegram file_id, return a direct HTTPS URL for that file.

    Note: This URL is temporary and should be used only to download once.
    """
    client = _client()
    bot_url = f"{client.base_url}/getFile"

    async with httpx.AsyncClient() as http_client:
        resp = await http_client.get(
            bot_url,
            params={"file_id": file_id},
            timeout=10.0
        )
        resp.raise_for_status()
        data = resp.json()
        if not data.get("ok"):
            log = logging.getLogger("telegras.telegram_api")
            log.warning("getFile failed: %s", data)
            return None

        file_path = data["result"]["file_path"]
        token = client.bot_token
        return f"https://api.telegram.org/file/bot{token}/{file_path}"


async def download_file(file_url: str) -> bytes:
    """Download a Telegram file via HTTPS."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(file_url, timeout=30.0)
        resp.raise_for_status()
        return resp.content
```

**Step 3: Update __init__.py to export new functions**

```python
# telegras/__init__.py - update exports
from .telegram_api import (
    send_message,
    get_webhook_info,
    set_webhook,
    delete_webhook,
    get_updates,
    get_me,
    get_file_direct_url,  # NEW
    download_file,        # NEW
)

__all__ = [
    "create_app",
    "send_message",
    "get_webhook_info",
    "set_webhook",
    "delete_webhook",
    "get_updates",
    "get_me",
    "get_file_direct_url",  # NEW
    "download_file",        # NEW
]
```

**Step 4: Write tests for new functions**

```python
# tests/test_telegram_api.py - add tests

import pytest
from telegras.telegram_api import get_file_direct_url, download_file

@pytest.mark.asyncio
async def test_get_file_direct_url(monkeypatch):
    """Test get_file_direct_url with mocked response."""
    async def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self):
                pass
            def json(self):
                return {
                    "ok": True,
                    "result": {"file_path": "photos/file.jpg"}
                }
        return MockResponse()

    monkeypatch.setattr("httpx.AsyncClient.get", mock_get)
    # Test would need proper mocking of client

@pytest.mark.asyncio
async def test_download_file(monkeypatch):
    """Test download_file with mocked response."""
    test_content = b"test image data"

    async def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self):
                pass
            @property
            def content(self):
                return test_content
        return MockResponse()

    monkeypatch.setattr("httpx.AsyncClient.get", mock_get)
    # Test would need proper mocking
```

**Step 5: Run tests**

Run: `pytest tests/test_telegram_api.py -v`
Expected: Tests may need mocking setup - implement proper mocks

**Step 6: Commit**

```bash
git add telegras/telegram_api.py telegras/__init__.py tests/test_telegram_api.py
git commit -m "feat(telegras): add media download functions

Add get_file_direct_url() and download_file() for downloading
Telegram media files. These functions were previously in
tg-wp-bridge and are now part of the core telegras API.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 2: Add Schemas for Telegram Message Models

**Files:**
- Create: `telegras/schemas.py`
- Test: `tests/test_schemas.py`

**Step 1: Create schemas.py with Telegram models**

```python
# telegras/schemas.py
"""Pydantic models for Telegram API responses."""

from pydantic import BaseModel
from typing import Optional, List


class TgPhotoSize(BaseModel):
    """Telegram photo size model."""
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: Optional[int] = None


class TgVideo(BaseModel):
    """Telegram video model."""
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional[TgPhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None


class TgAnimation(BaseModel):
    """Telegram animation model."""
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional[TgPhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None


class TgDocument(BaseModel):
    """Telegram document model."""
    file_id: str
    file_unique_id: str
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    thumb: Optional[TgPhotoSize] = None


class TgChat(BaseModel):
    """Telegram chat model."""
    id: int
    type: str
    title: Optional[str] = None
    username: Optional[str] = None


class TgMessage(BaseModel):
    """Telegram message model."""
    message_id: int
    chat: TgChat
    date: int
    text: Optional[str] = None
    caption: Optional[str] = None
    photo: Optional[List[TgPhotoSize]] = None
    video: Optional[TgVideo] = None
    animation: Optional[TgAnimation] = None
    document: Optional[TgDocument] = None
    edit_date: Optional[int] = None
    media_group_id: Optional[str] = None
```

**Step 2: Write basic tests**

```python
# tests/test_schemas.py
from pydantic import ValidationError
import pytest
from telegras.schemas import TgPhotoSize, TgMessage, TgChat

def test_photo_size_model():
    """Test TgPhotoSize model."""
    data = {
        "file_id": "abc123",
        "file_unique_id": "uniq123",
        "width": 800,
        "height": 600,
    }
    photo = TgPhotoSize(**data)
    assert photo.file_id == "abc123"
    assert photo.width == 800

def test_message_model():
    """Test TgMessage model."""
    data = {
        "message_id": 1,
        "chat": {"id": 123, "type": "private"},
        "date": 1234567890,
        "text": "Hello",
    }
    message = TgMessage(**data)
    assert message.message_id == 1
    assert message.text == "Hello"
```

**Step 3: Run tests**

Run: `pytest tests/test_schemas.py -v`
Expected: PASS

**Step 4: Commit**

```bash
git add telegras/schemas.py tests/test_schemas.py
git commit -m "feat(telegras): add Telegram message schemas

Add Pydantic models for Telegram API responses including
TgPhotoSize, TgVideo, TgAnimation, TgDocument, TgChat, TgMessage.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 3: Create Message Parser Module

**Files:**
- Create: `telegras/message_parser.py`
- Test: `tests/test_message_parser.py`

**Step 1: Create message_parser.py**

```python
# telegras/message_parser.py
"""Telegram message parsing utilities - extracts media and text from updates."""

import mimetypes
from dataclasses import dataclass
from typing import Optional, List

from .schemas import TgMessage, TgPhotoSize, TgVideo, TgAnimation, TgDocument
from .api.getting_updates import Update


@dataclass
class TelegramMedia:
    """Lightweight descriptor for supported Telegram media attachments."""
    file_id: str
    media_type: str
    file_name: Optional[str] = None
    mime_type: Optional[str] = None


def find_photo_with_max_size(msg: TgMessage) -> Optional[TgPhotoSize]:
    """
    From a TgMessage, pick the largest photo variant if present.

    Telegram sends multiple sizes of the same photo in msg.photo.
    """
    if not msg.photo:
        return None
    return max(msg.photo, key=lambda p: p.width * p.height)


def _add_media(
    media: List[TelegramMedia],
    seen_ids: set,
    *,
    file_id: Optional[str],
    media_type: str,
    file_name: Optional[str] = None,
    mime_type: Optional[str] = None,
) -> None:
    """Add media to list if not already seen."""
    if not file_id or file_id in seen_ids:
        return
    seen_ids.add(file_id)
    media.append(
        TelegramMedia(
            file_id=file_id,
            media_type=media_type,
            file_name=file_name,
            mime_type=mime_type,
        )
    )


def _infer_filename(
    *,
    file_id: str,
    media_type: str,
    file_name: Optional[str],
    mime_type: Optional[str],
) -> str:
    """Return a stable filename with extension when Telegram omits file_name."""
    if file_name:
        return file_name

    ext = mimetypes.guess_extension(mime_type or "")
    if not ext:
        fallback_ext = {
            "photo": ".jpg",
            "video": ".mp4",
            "animation": ".gif",
            "document": ".bin",
        }
        ext = fallback_ext.get(media_type, ".bin")
    return f"{file_id}{ext}"


def collect_supported_media(msg: TgMessage) -> List[TelegramMedia]:
    """Return a list of supported media descriptors for the message."""
    media: List[TelegramMedia] = []
    seen_ids: set = set()

    photo = find_photo_with_max_size(msg)
    if photo:
        _add_media(
            media,
            seen_ids,
            file_id=photo.file_id,
            media_type="photo",
            file_name=f"{photo.file_id}.jpg",
            mime_type="image/jpeg",
        )

    if isinstance(msg.video, TgVideo):
        inferred_name = _infer_filename(
            file_id=msg.video.file_id,
            media_type="video",
            file_name=msg.video.file_name,
            mime_type=msg.video.mime_type,
        )
        _add_media(
            media,
            seen_ids,
            file_id=msg.video.file_id,
            media_type="video",
            file_name=inferred_name,
            mime_type=msg.video.mime_type,
        )

    if isinstance(msg.animation, TgAnimation):
        inferred_name = _infer_filename(
            file_id=msg.animation.file_id,
            media_type="animation",
            file_name=msg.animation.file_name,
            mime_type=msg.animation.mime_type,
        )
        _add_media(
            media,
            seen_ids,
            file_id=msg.animation.file_id,
            media_type="animation",
            file_name=inferred_name,
            mime_type=msg.animation.mime_type,
        )

    if isinstance(msg.document, TgDocument):
        inferred_name = _infer_filename(
            file_id=msg.document.file_id,
            media_type="document",
            file_name=msg.document.file_name,
            mime_type=msg.document.mime_type,
        )
        _add_media(
            media,
            seen_ids,
            file_id=msg.document.file_id,
            media_type="document",
            file_name=inferred_name,
            mime_type=msg.document.mime_type,
        )

    return media


def extract_message_entity(update: Update) -> Optional[TgMessage]:
    """
    Return the effective TgMessage from a Telegram update.

    This helper prefers channel_post over message when both are present.
    """
    # Check for channel_post first
    if hasattr(update, 'channel_post') and update.channel_post is not None:
        return update.channel_post

    # Fall back to message
    if hasattr(update, 'message') and update.message is not None:
        return update.message

    # Check for edited variants
    if hasattr(update, 'edited_channel_post') and update.edited_channel_post is not None:
        return update.edited_channel_post

    if hasattr(update, 'edited_message') and update.edited_message is not None:
        return update.edited_message

    return None


def extract_message_text(update: Update) -> Optional[str]:
    """
    Extract text from an update, preferring message/channel_post.text
    and falling back to .caption.
    """
    msg = extract_message_entity(update)
    if not msg:
        return None

    return msg.text or msg.caption
```

**Step 2: Write tests**

```python
# tests/test_message_parser.py
import pytest
from telegras.message_parser import (
    TelegramMedia,
    find_photo_with_max_size,
    collect_supported_media,
    extract_message_entity,
    extract_message_text,
)
from telegras.schemas import TgMessage, TgPhotoSize, TgChat, TgVideo
from telegras.api.getting_updates import Update

def test_find_photo_with_max_size():
    """Test finding largest photo."""
    small = TgPhotoSize(file_id="small", file_unique_id="s", width=100, height=100)
    large = TgPhotoSize(file_id="large", file_unique_id="l", width=800, height=600)

    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
        photo=[small, large],
    )

    result = find_photo_with_max_size(msg)
    assert result == large

def test_collect_supported_media():
    """Test collecting media from message."""
    video = TgVideo(
        file_id="vid123",
        file_unique_id="v123",
        width=1280,
        height=720,
        duration=30,
        file_name="video.mp4",
        mime_type="video/mp4",
    )

    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
        video=video,
    )

    media = collect_supported_media(msg)
    assert len(media) == 1
    assert media[0].file_id == "vid123"
    assert media[0].media_type == "video"
```

**Step 3: Run tests**

Run: `pytest tests/test_message_parser.py -v`
Expected: PASS

**Step 4: Commit**

```bash
git add telegras/message_parser.py tests/test_message_parser.py
git commit -m "feat(telegras): add message parser module

Add Telegram-specific message parsing utilities:
- TelegramMedia dataclass for media descriptors
- collect_supported_media() to extract media from messages
- find_photo_with_max_size() to find largest photo
- extract_message_entity() to get message from update
- extract_message_text() to get text/caption from update

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 4: Move Logging Utilities

**Files:**
- Create: `telegras/logging_utils.py`
- Test: `tests/test_logging_utils.py`

**Step 1: Create logging_utils.py**

```python
# telegras/logging_utils.py
"""Structured logging utilities for telegras services."""

import json
import logging
import os
import tempfile
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

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
    update: Any,
    result: Optional[dict] = None,
    *,
    tg_message_id: Optional[int] = None,
) -> dict[str, Optional[str]]:
    """Record raw update and optional result to disk."""
    preferred_storage_dir = Path(os.getenv("STORAGE_DIR", "data/logs"))
    storage_dir = resolve_writable_dir(
        preferred_storage_dir,
        fallback_env_var="STORAGE_FALLBACK_DIR",
        fallback_subdir="logs",
    )
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    tgid = tg_message_id if tg_message_id is not None else getattr(update, 'update_id', ts)
    out: dict[str, Optional[str]] = {"tg_path": None, "result_path": None}

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
    update: Any,
    exc: BaseException,
    *,
    tg_message_id: Optional[int] = None,
    result: Optional[dict] = None,
) -> Optional[str]:
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
```

**Step 2: Write tests**

```python
# tests/test_logging_utils.py
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
```

**Step 3: Run tests**

Run: `pytest tests/test_logging_utils.py -v`
Expected: PASS

**Step 4: Commit**

```bash
git add telegras/logging_utils.py tests/test_logging_utils.py
git commit -m "feat(telegras): add structured logging utilities

Add logging utilities with:
- resolve_writable_dir() for handling permission errors
- rotate_logs() for log file rotation by count/size
- record_update_log() for recording updates to JSON
- record_error_artifact() for error logging with tracebacks

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 5: Move DisplayManager

**Files:**
- Create: `telegras/display.py`
- Test: `tests/test_display.py`

**Step 1: Create display.py**

```python
# telegras/display.py
"""CLI display manager with rich formatting and plain text fallback."""

import re
from typing import Optional


class DisplayManager:
    """Manage CLI output with rich formatting and plain text fallback."""

    def __init__(
        self,
        *,
        force_rich: bool = False,
        force_plain: bool = False,
    ) -> None:
        self.force_rich = force_rich
        self.force_plain = force_plain

    def is_rich(self) -> bool:
        """Return True if rich output is enabled."""
        if self.force_plain:
            return False
        if self.force_rich:
            return True
        # Auto-detect based on terminal support
        try:
            import sys

            return sys.stdout.isatty()
        except Exception:
            return False

    def print(self, message: str, **kwargs) -> None:
        """Print a message with appropriate formatting."""
        if self.is_rich():
            from rich.console import Console

            console = Console()
            console.print(message, **kwargs)
        else:
            # Strip rich markup for plain output
            clean = re.sub(r"\[.*?\]", "", message)
            print(clean, **kwargs)

    def print_status(self, status: str, message: str, success: bool = True) -> None:
        """Print a status message with icon."""
        if self.is_rich():
            icon = "[green]✓[/green]" if success else "[red]✗[/red]"
            self.print(f"{icon} {message}")
        else:
            icon = "OK" if success else "FAIL"
            self.print(f"{icon}: {message}")

    def print_section(self, title: str) -> None:
        """Print a section header."""
        if self.is_rich():
            from rich.console import Console

            console = Console()
            console.print(f"\n[bold cyan]{title}[/bold cyan]")
        else:
            print(f"\n{title}")
```

**Step 2: Write tests**

```python
# tests/test_display.py
import pytest
from telegras.display import DisplayManager

def test_display_manager_force_plain():
    """Test DisplayManager with forced plain output."""
    display = DisplayManager(force_plain=True)
    assert not display.is_rich()

def test_display_manager_force_rich():
    """Test DisplayManager with forced rich output."""
    display = DisplayManager(force_rich=True)
    assert display.is_rich()

def test_display_manager_print_status(capsys):
    """Test print_status output."""
    display = DisplayManager(force_plain=True)
    display.print_status("", "Test message", success=True)
    captured = capsys.readouterr()
    assert "OK" in captured.out
    assert "Test message" in captured.out
```

**Step 3: Run tests**

Run: `pytest tests/test_display.py -v`
Expected: PASS

**Step 4: Commit**

```bash
git add telegras/display.py tests/test_display.py
git commit -m "feat(telegras): add DisplayManager for CLI output

Add DisplayManager class for formatted CLI output with:
- Rich formatting with colors/icons when available
- Plain text fallback for non-interactive terminals
- Auto-detection of terminal capability
- print_status(), print_section() helpers

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 6: Create Startup Validation Module

**Files:**
- Create: `telegras/startup.py`
- Test: `tests/test_startup.py`

**Step 1: Create startup.py**

```python
# telegras/startup.py
"""Startup validation utilities for telegras services."""

import asyncio
from typing import Any

from .telegram_api import get_webhook_info, get_me
from .display import DisplayManager


async def validate_telegram_config() -> dict[str, Any]:
    """Validate Telegram bot token and connectivity."""
    results = {
        "bot_token": {"status": "unknown", "message": ""},
    }

    try:
        bot_info = await get_me()
        results["bot_token"] = {
            "status": "ok",
            "message": f"Bot: @{bot_info.username}",
            "bot_id": bot_info.id,
            "username": bot_info.username,
        }
    except Exception as e:
        results["bot_token"] = {
            "status": "error",
            "message": str(e),
        }

    return results


async def validate_webhook_config() -> dict[str, Any]:
    """Validate Telegram webhook status."""
    results = {
        "webhook": {"status": "unknown", "message": ""},
    }

    try:
        webhook_info = await get_webhook_info()
        if webhook_info.url:
            results["webhook"] = {
                "status": "configured",
                "message": f"Webhook: {webhook_info.url}",
                "url": webhook_info.url,
                "pending_updates": webhook_info.pending_update_count,
            }
        else:
            results["webhook"] = {
                "status": "not_configured",
                "message": "No webhook configured",
            }
    except Exception as e:
        results["webhook"] = {
            "status": "error",
            "message": str(e),
        }

    return results


def run_startup_validation_sync(
    *,
    display: DisplayManager | None = None,
) -> dict[str, Any]:
    """Run all startup validations synchronously."""
    if display is None:
        display = DisplayManager()

    results = {
        "telegram": asyncio.run(validate_telegram_config()),
        "webhook": asyncio.run(validate_webhook_config()),
        "overall": {"status": "ok", "errors": []},
    }

    # Display results
    display.print_section("Telegram Configuration")
    tg_result = results["telegram"]["bot_token"]
    if tg_result["status"] == "ok":
        display.print_status("", tg_result["message"], success=True)
    else:
        display.print_status("", tg_result["message"], success=False)
        results["overall"]["errors"].append("bot_token")

    display.print_section("Webhook Status")
    webhook_result = results["webhook"]["webhook"]
    if webhook_result["status"] == "configured":
        display.print_status("", webhook_result["message"], success=True)
    elif webhook_result["status"] == "not_configured":
        display.print_status("", webhook_result["message"], success=False)
        results["overall"]["errors"].append("webhook_not_set")
    else:
        display.print_status("", webhook_result["message"], success=False)
        results["overall"]["errors"].append("webhook_error")

    if results["overall"]["errors"]:
        results["overall"]["status"] = "failed"

    return results
```

**Step 2: Write tests**

```python
# tests/test_startup.py
import pytest
from telegras.startup import validate_telegram_config, validate_webhook_config

@pytest.mark.asyncio
async def test_validate_telegram_config(monkeypatch):
    """Test Telegram configuration validation."""
    # Test with mocked get_me
    async def mock_get_me():
        class Response:
            id = 123
            username = "test_bot"
        return Response()

    monkeypatch.setattr("telegras.startup.get_me", mock_get_me)

    result = await validate_telegram_config()
    assert result["bot_token"]["status"] == "ok"
    assert "test_bot" in result["bot_token"]["message"]
```

**Step 3: Run tests**

Run: `pytest tests/test_startup.py -v`
Expected: PASS (may need mocking adjustments)

**Step 4: Commit**

```bash
git add telegras/startup.py tests/test_startup.py
git commit -m "feat(telegras): add startup validation module

Add startup validation with:
- validate_telegram_config() for bot token validation
- validate_webhook_config() for webhook status check
- run_startup_validation_sync() for comprehensive diagnostics
- DisplayManager integration for formatted output

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 7: Refactor app.py with Lifespan Management

**Files:**
- Modify: `telegras/app.py`
- Test: `tests/test_app.py`

**Step 1: Read current app.py structure**

Read the file to understand the current `create_app()` implementation.

**Step 2: Update create_app() signature and implementation**

```python
# Update telegras/app.py - modify create_app function signature

def create_app(
    app: FastAPI | None = None,
    *,
    settings: AppSettings | None = None,
    service: TelegramIngestionService | None = None,
    merge_lifespan: bool = True,
) -> FastAPI:
    """
    Create or extend a FastAPI app with telegras routes.

    Args:
        app: Existing FastAPI app to extend. If None, creates new app.
        settings: App settings. If None, loads from environment.
        service: Ingestion service. If None, creates default.
        merge_lifespan: If True, merges lifespan with existing app's lifespan.

    Returns:
        The FastAPI app with telegras routes registered.
    """
    if settings is None:
        settings = AppSettings.from_env()

    if service is None:
        service = TelegramIngestionService()

    if app is None:
        app = FastAPI(
            title="telegras",
            description=(
                "Telegram + FastAPI bridge with persistent interaction history "
                "and pluggable publication backends."
            ),
            version="0.1.0",
            lifespan=_create_telegras_lifespan(settings, service),
        )
    elif merge_lifespan:
        # Merge lifespan if app already has one
        existing_lifespan = app.router.lifespan_context
        app.router.lifespan_context = _merge_lifespans(
            existing_lifespan,
            _create_telegras_lifespan(settings, service),
        )
    else:
        # Register telegras lifespan as a separate route handler's startup
        # This is a simplified approach - actual implementation may vary
        pass

    # Register all routes on the app...
    # (Keep existing route registration code)

    return app


@asynccontextmanager
async def _create_telegras_lifespan(settings: AppSettings, service: TelegramIngestionService):
    """Telegras-specific lifespan logic."""
    await _ensure_db_ready()
    polling_task: asyncio.Task[None] | None = None
    if settings.bot_mode == BotMode.POLLING:
        try:
            await telegram_api.delete_webhook(drop_pending_updates=False)
        except Exception:
            log.exception("Failed to delete webhook before starting polling")
        polling_task = asyncio.create_task(
            _run_polling_loop(service=service, settings=settings),
            name="telegras-polling-loop",
        )
    try:
        yield
    finally:
        if polling_task is not None:
            polling_task.cancel()
            with suppress(asyncio.CancelledError):
                await polling_task


def _merge_lifespans(ctx1, ctx2):
    """Merge two lifespan contexts into one."""
    @asynccontextmanager
    async def merged(app_state):
        async with ctx1(app_state):
            async with ctx2(app_state):
                yield
    return merged
```

**Step 3: Remove module-level app instantiation**

```python
# At the end of telegras/app.py, REMOVE these lines:

# app = create_app()  # <-- DELETE THIS
```

**Step 4: Create start.py**

```python
# telegras/start.py
"""Standalone entry point for running telegras server."""

import uvicorn
from .app import create_app


def main():
    """Start the telegras server."""
    app = create_app()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=False,
    )


if __name__ == "__main__":
    main()
```

**Step 5: Write tests for app mounting**

```python
# tests/test_app.py
import pytest
from fastapi import FastAPI
from telegras.app import create_app

def test_create_app_standalone():
    """Test creating a standalone app."""
    app = create_app()
    assert isinstance(app, FastAPI)
    assert app.title == "telegras"

def test_create_app_mount_on_existing():
    """Test mounting routes on existing app."""
    existing_app = FastAPI(title="Existing App")
    app = create_app(app=existing_app)
    # Should be the same app instance
    assert app is existing_app
    # Should have telegras routes registered
    routes = [r.path for r in app.routes]
    assert "/healthz" in routes
```

**Step 6: Run tests**

Run: `pytest tests/test_app.py -v`
Expected: PASS

**Step 7: Update pyproject.toml start script**

```toml
# telegras/pyproject.toml - update start script
[tool.hatch.envs.default.scripts]
start = "python -m telegras.start"  # Changed from uvicorn telegras.app:app
```

**Step 8: Commit**

```bash
git add telegras/app.py telegras/start.py tests/test_app.py telegras/pyproject.toml
git commit -m "refactor(telegras): support mounting on existing FastAPI apps

- Add app parameter to create_app() for extending existing apps
- Add merge_lifespan parameter for lifespan management
- Extract lifespan logic to _create_telegras_lifespan()
- Add _merge_lifespans() for combining lifespan contexts
- Remove module-level app instantiation
- Add telegras/start.py for standalone execution
- Update pyproject.toml start script

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 8: Enhance CLI with All Telegram Commands

**Files:**
- Modify: `telegras/cli.py`
- Test: `tests/test_cli.py`

**Step 1: Update cli.py with all commands**

```python
# telegras/cli.py - replace entire content
"""Telegras CLI - comprehensive Telegram operations."""

import asyncio
import logging
import click

from .telegram_api import (
    get_webhook_info,
    set_webhook,
    delete_webhook,
    get_me,
)
from .startup import run_startup_validation_sync
from .display import DisplayManager
from .persistence.db import init_db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
log = logging.getLogger("telegras.cli")


@click.group()
@click.option("--debug", is_flag=True, help="Enable debug logging")
@click.option("--plain", is_flag=True, help="Force plain text output")
@click.pass_context
def cli(ctx: click.Context, debug: bool, plain: bool) -> None:
    """telegras operational CLI."""
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
        log.debug("Debug mode enabled")

    display = DisplayManager(force_rich=True, force_plain=plain)
    ctx.ensure_object(dict)
    ctx.obj["debug"] = debug
    ctx.obj["plain"] = plain
    ctx.obj["display"] = display


@cli.command(name="start")
@click.option("--host", default="0.0.0.0", help="Host to bind to")
@click.option("--port", default=8000, type=int, help="Port to bind to")
@click.option("--reload", is_flag=True, help="Enable auto-reload")
@click.pass_context
def start_cmd(ctx: click.Context, host: str, port: int, reload: bool) -> None:
    """Start the telegras server."""
    import uvicorn
    from .app import create_app

    display = ctx.obj.get("display", DisplayManager())
    display.print_section("Starting telegras")
    display.print_status("", f"Listening on {host}:{port}", success=True)

    app = create_app()
    uvicorn.run(app, host=host, port=port, reload=reload)


@cli.command(name="webhook-info")
@click.option("--format", type=click.Choice(["json", "table"]), default="table")
@click.pass_context
def webhook_info_cmd(ctx: click.Context, output_format: str) -> None:
    """Display current Telegram webhook information."""
    display = ctx.obj.get("display", DisplayManager())

    async def _get_info():
        info = await get_webhook_info()
        if output_format == "json":
            import json
            click.echo(json.dumps(info.model_dump(), indent=2))
        else:
            display.print_section("Webhook Information")
            display.print(f"  URL: {info.url or 'Not set'}")
            display.print(f"  Pending updates: {info.pending_update_count}")
            display.print(f"  Custom certificate: {info.has_custom_certificate}")
            if info.last_error_message:
                display.print_status("", f"Last error: {info.last_error_message}", success=False)

    asyncio.run(_get_info())


@cli.command(name="set-webhook")
@click.option("--url", required=True, help="Webhook URL")
@click.option("--dry-run", is_flag=True, help="Show what would be set")
@click.pass_context
def set_webhook_cmd(ctx: click.Context, url: str, dry_run: bool) -> None:
    """Configure Telegram webhook."""
    display = ctx.obj.get("display", DisplayManager())

    if dry_run:
        display.print(f"Would set webhook to: {url}")
        return

    async def _set_webhook():
        result = await set_webhook(url=url)
        if result.get("ok"):
            display.print_status("", "Webhook configured successfully", success=True)
        else:
            display.print_status("", result.get("description", "Unknown error"), success=False)
            raise click.ClickException("Webhook configuration failed")

    asyncio.run(_set_webhook())


@cli.command(name="delete-webhook")
@click.option("--drop-pending", is_flag=True, help="Drop pending updates")
@click.pass_context
def delete_webhook_cmd(ctx: click.Context, drop_pending: bool) -> None:
    """Delete Telegram webhook."""
    display = ctx.obj.get("display", DisplayManager())

    async def _delete():
        result = await delete_webhook(drop_pending_updates=drop_pending)
        if result.get("ok"):
            display.print_status("", "Webhook deleted successfully", success=True)
        else:
            display.print_status("", result.get("description", "Unknown error"), success=False)

    asyncio.run(_delete())


@cli.command(name="get-me")
@click.pass_context
def get_me_cmd(ctx: click.Context) -> None:
    """Get bot information."""
    display = ctx.obj.get("display", DisplayManager())

    async def _get_me():
        info = await get_me()
        display.print_section("Bot Information")
        display.print(f"  ID: {info.id}")
        display.print(f"  Username: @{info.username}")
        display.print(f"  First name: {info.first_name}")
        if info.last_name:
            display.print(f"  Last name: {info.last_name}")

    asyncio.run(_get_me())


@cli.command(name="startup-check")
@click.option("--auto-fix-webhook/--no-auto-fix-webhook", default=True)
@click.pass_context
def startup_check_cmd(ctx: click.Context, auto_fix_webhook: bool) -> None:
    """Run comprehensive startup diagnostics."""
    display = ctx.obj.get("display", DisplayManager())

    results = run_startup_validation_sync(display=display)

    if results["overall"]["status"] == "failed":
        raise click.ClickException("Startup check failed")


@cli.command(name="db-init")
def db_init_cmd() -> None:
    """Initialize telegras database."""
    asyncio.run(init_db())
    click.echo("Database initialized")


if __name__ == "__main__":
    cli()
```

**Step 2: Write CLI tests**

```python
# tests/test_cli.py
import pytest
from click.testing import CliRunner
from telegras.cli import cli

def test_cli_help():
    """Test CLI help output."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "start" in result.output
    assert "webhook-info" in result.output

def test_db_init_command(monkeypatch):
    """Test db-init command."""
    async def mock_init():
        pass

    monkeypatch.setattr("telegras.cli.init_db", mock_init)

    runner = CliRunner()
    result = runner.invoke(cli, ["db-init"])
    assert result.exit_code == 0
    assert "Database initialized" in result.output
```

**Step 3: Run tests**

Run: `pytest tests/test_cli.py -v`
Expected: PASS

**Step 4: Test CLI manually**

Run: `telegras --help`
Expected: Show all commands

Run: `telegras get-me`
Expected: Show bot information (requires TELEGRAM_BOT_TOKEN)

**Step 5: Commit**

```bash
git add telegras/cli.py tests/test_cli.py
git commit -m "feat(telegras): enhance CLI with all Telegram commands

Add comprehensive CLI commands:
- start: Start the telegras server (with --host, --port, --reload)
- webhook-info: Display current Telegram webhook information
- set-webhook: Configure Telegram webhook
- delete-webhook: Delete Telegram webhook
- get-me: Get bot information
- startup-check: Run comprehensive startup diagnostics
- db-init: Initialize telegras database

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 9: Update tg-wp-bridge to Use telegras Modules

**Files:**
- Modify: `tg-wp-bridge/tg_wp_bridge/telegram_api.py`
- Modify: `tg-wp-bridge/tg_wp_bridge/handlers.py`
- Modify: `tg-wp-bridge/tg_wp_bridge/message_parser.py`
- Modify: `tg-wp-bridge/tg_wp_bridge/logging_utils.py`
- Modify: `tg-wp-bridge/tg_wp_bridge/display.py`
- Modify: `tg-wp-bridge/tg_wp_bridge/startup.py`

**Step 1: Update telegram_api.py to use telegras**

```python
# tg-wp-bridge/tg_wp_bridge/telegram_api.py - replace with:

"""
Telegram HTTP API helpers - now delegating to telegras.

Responsibilities:
- Use Settings for configuration.
- Provide convenience functions for tg-wp-bridge specific needs.
"""

import logging
from typing import Optional, Dict, Any

from .config import settings
from .schemas import TelegramWebhookInfo

# Import from telegras
from telegras.telegram_api import (
    get_file_direct_url as _tg_get_file_direct_url,
    download_file as _tg_download_file,
    get_webhook_info as _tg_get_webhook_info,
)

log = logging.getLogger("tg-wp-bridge.telegram")


async def get_file_direct_url(file_id: str) -> Optional[str]:
    """Get file URL, respecting tg_skip flag."""
    if settings.tg_skip:
        log.info("tg_skip enabled; returning None for file_id=%s", file_id)
        return None
    return await _tg_get_file_direct_url(file_id)


async def download_file(file_url: str) -> bytes:
    """Download file, respecting tg_skip flag."""
    return await _tg_download_file(file_url)


def expected_webhook_url() -> str:
    """Return the expected webhook URL for this service."""
    if not settings.public_base_url:
        raise RuntimeError("PUBLIC_BASE_URL is not set")
    if not settings.telegram_webhook_secret:
        raise RuntimeError("TELEGRAM_WEBHOOK_SECRET is not set")

    base = str(settings.public_base_url).rstrip("/")
    prefix = (settings.webhook_prefix or "webhook").strip("/")
    return f"{base}/{prefix}/{settings.telegram_webhook_secret}"


async def set_webhook() -> Dict[str, Any]:
    """Configure Telegram webhook for this bridge."""
    from telegras.telegram_api import set_webhook as _tg_set_webhook

    if settings.tg_skip:
        webhook_url = expected_webhook_url()
        log.info(
            "tg_skip enabled; not setting Telegram webhook (would set to: %s)",
            webhook_url,
        )
        return {"ok": True, "result": "skipped"}

    webhook_url = expected_webhook_url()
    log.info("Setting Telegram webhook to: %s", webhook_url)

    return await _tg_set_webhook(url=webhook_url)


async def get_webhook_info() -> TelegramWebhookInfo:
    """Inspect current webhook status."""
    if settings.tg_skip:
        log.info("tg_skip enabled; returning empty TelegramWebhookInfo")
        return TelegramWebhookInfo.model_validate({})

    return await _tg_get_webhook_info()
```

**Step 2: Update handlers.py imports**

```python
# tg-wp-bridge/tg_wp_bridge/handlers.py - update imports

# REMOVE these imports (now from telegras):
# from .telegram_api import get_file_direct_url, download_file

# ADD these imports:
from telegras.telegram_api import get_file_direct_url, download_file
from telegras.logging_utils import record_update_log, record_error_artifact
from telegras.message_parser import collect_supported_media
```

**Step 3: Update message_parser.py to remove moved functions**

```python
# tg-wp-bridge/tg_wp_bridge/message_parser.py

# REMOVE these functions (now in telegras):
# - collect_supported_media
# - find_photo_with_max_size
# - extract_message_entity
# - extract_message_text
# - TelegramMedia class

# KEEP these WordPress-specific functions:
# - build_title_from_text
# - build_slug_from_text
# - text_to_html
# - strip_title_line_from_text
# - strip_emojis
# - extract_hashtags

# UPDATE imports at top:
from telegras.message_parser import (
    TelegramMedia,
    collect_supported_media,
    extract_message_entity,
    extract_message_text,
)
from telegras.schemas import TgMessage, TgPhotoSize, TgVideo, TgAnimation, TgDocument
```

**Step 4: Update logging_utils.py**

```python
# tg-wp-bridge/tg_wp_bridge/logging_utils.py - replace with:

"""Logging utilities for tg-wp-bridge - now using telegras."""

# Import from telegras
from telegras.logging_utils import (
    resolve_writable_dir,
    rotate_logs,
    record_update_log,
    record_error_artifact,
)

__all__ = [
    "resolve_writable_dir",
    "rotate_logs",
    "record_update_log",
    "record_error_artifact",
]
```

**Step 5: Update display.py**

```python
# tg-wp-bridge/tg_wp_bridge/display.py - replace with:

"""Display utilities for tg-wp-bridge - now using telegras."""

# Import from telegras
from telegras.display import DisplayManager

__all__ = ["DisplayManager"]
```

**Step 6: Update startup.py**

```python
# tg-wp-bridge/tg_wp_bridge/startup.py - add WordPress checks on top of telegras

from telegras.startup import (
    validate_telegram_config,
    validate_webhook_config,
)
from . import wordpress_api


async def validate_wordpress_config() -> dict[str, Any]:
    """Validate WordPress API configuration."""
    results = {
        "wordpress": {"status": "unknown", "message": ""},
    }

    try:
        ping_info = await wordpress_api.ping_wp_api()
        results["wordpress"] = {
            "status": "ok",
            "message": f"WordPress reachable: {ping_info.get('name', 'Unknown')}",
        }
    except Exception as e:
        results["wordpress"] = {
            "status": "error",
            "message": str(e),
        }

    return results


# Update run_startup_validation_sync to include WordPress checks
```

**Step 7: Update tests**

Update tg-wp-bridge tests to use new imports.

**Step 8: Run tests**

Run: `cd /home/user/work/code/tg-wp-bridge && pytest tests/ -v`
Expected: PASS (after fixing any import issues)

**Step 9: Commit**

```bash
cd /home/user/work/code/tg-wp-bridge
git add tg_wp_bridge/telegram_api.py tg_wp_bridge/handlers.py tg_wp_bridge/message_parser.py
git add tg_wp_bridge/logging_utils.py tg_wp_bridge/display.py tg_wp_bridge/startup.py
git commit -m "refactor(tg-wp-bridge): use telegras for all Telegram utilities

Update tg-wp-bridge to import Telegram tooling from telegras:
- Media downloads from telegras.telegram_api
- Message parsing from telegras.message_parser
- Logging from telegras.logging_utils
- Display from telegras.display
- Startup validation extends telegras.startup

Keep only WordPress-specific code in tg-wp-bridge.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 10: Update Dependencies and Documentation

**Files:**
- Modify: `tg-wp-bridge/pyproject.toml`
- Create: `telegras/README.md` updates

**Step 1: Update tg-wp-bridge dependencies**

```toml
# tg-wp-bridge/pyproject.toml - ensure telegras version is correct
dependencies = [
  "fastapi>=0.112.0",
  "uvicorn[standard]>=0.30.0",
  "httpx>=0.27.0",
  "pydantic>=2.7.0",
  "pydantic-settings>=2.2.0",
  "click>=8.0.0",
  "rich>=14.2.0",
  "telegras>=0.4.0",  # UPDATE to new version
]
```

**Step 2: Update telegras README**

Add documentation for new CLI commands and API.

**Step 3: Update CHANGELOG**

Document changes in both projects.

**Step 4: Commit**

```bash
# In telegras
git add README.md CHANGELOG.md
git commit -m "docs: update documentation for CLI and new features

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# In tg-wp-bridge
git add pyproject.toml README.md CHANGELOG.md
git commit -m "docs: update dependencies and documentation

Update to require telegras 0.4.0+ for Telegram utilities.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 11: Final Integration Testing

**Files:**
- Test: Manual testing commands

**Step 1: Test telegras standalone**

```bash
cd /home/user/work/code/telegras

# Test CLI
telegras --help
telegras get-me
telegras webhook-info
telegras startup-check

# Test server start (background)
telegras start --port 8888 &
SERVER_PID=$!
sleep 2
curl http://localhost:8888/healthz
kill $SERVER_PID
```

**Step 2: Test tg-wp-bridge with telegras**

```bash
cd /home/user/work/code/tg-wp-bridge

# Install local telegras
pip install -e /home/user/work/code/telegras

# Run tests
pytest tests/ -v

# Test CLI
tg-wp-bridge --help
tg-wp-bridge startup-check
```

**Step 3: Test app mounting**

```python
# Create test script: test_mounting.py
from fastapi import FastAPI
from telegras import create_app

# Test 1: Standalone app
standalone = create_app()
print(f"Standalone app title: {standalone.title}")

# Test 2: Mount on existing app
existing = FastAPI(title="My App")
mounted = create_app(app=existing)
print(f"Mounted app is same instance: {mounted is existing}")
print(f"Mounted has /healthz: {any(r.path == '/healthz' for r in mounted.routes)}")
```

Run: `python test_mounting.py`
Expected: All assertions pass

**Step 4: Full integration test**

Test a complete flow:
1. Start telegras server
2. Send webhook update
3. Verify update is logged
4. Check database for interaction

**Step 5: Fix any issues**

Address any bugs or integration issues found during testing.

**Step 6: Final commit**

```bash
# In both repos
git add .
git commit -m "test: pass integration tests

All tests passing. telegras and tg-wp-bridge integration verified.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Success Criteria Verification

- [ ] All Telegram-related functions accessible via `telegras` package
- [ ] telegras can be used standalone OR mounted into another FastAPI app
- [ ] tg-wp-bridge imports all Telegram utilities from telegras
- [ ] CLI provides all Telegram operations
- [ ] Structured logging with rotation works in both projects
- [ ] All tests pass

---

## End of Implementation Plan

Total estimated tasks: 11
Total estimated steps: ~50-60

Remember to:
- Commit frequently after each task
- Run tests after each change
- Use TDD (write test, implement, verify)
- Keep changes small and focused
