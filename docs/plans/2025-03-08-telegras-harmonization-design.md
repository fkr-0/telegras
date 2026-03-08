# Telegras Harmonization Design

**Date:** 2025-03-08
**Author:** Design review for harmonizing telegras extraction from tg-wp-bridge
**Status:** Approved

## Overview

Refactor telegras to be the canonical Telegram service library by moving Telegram-specific code from tg-wp-bridge, while making tg-wp-bridge a thin wrapper that uses telegras APIs.

## Goals

1. Move all Telegram tooling (media downloads, webhook management) from tg-wp-bridge to telegras
2. Port strong logging utilities from tg-wp-bridge to telegras
3. Refactor app.py to support mounting on existing FastAPI apps
4. Add comprehensive CLI with all Telegram operations
5. Strip tg-wp-bridge to strictly operate the telegras API

## Approach

**Modular Migration (Approach 1):** Incremental migration with clear separation of concerns.

---

## Section 1: Media Download Functions

**Move from:** `tg-wp-bridge/telegram_api.py`
**Move to:** `telegras/telegram_api.py`

### Functions to Add:

```python
async def get_file_direct_url(file_id: str) -> str | None:
    """Given a Telegram file_id, return a direct HTTPS URL for that file."""

async def download_file(file_url: str) -> bytes:
    """Download a Telegram file via HTTPS."""
```

### Changes:
- Add these functions to `telegras/telegram_api.py`
- Update `tg-wp-bridge/handlers.py` to import from telegras
- Optionally remove `tg-wp-bridge/telegram_api.py` entirely

---

## Section 2: Message Parser Split

**Move from:** `tg-wp-bridge/message_parser.py`
**Move to:** `telegras/message_parser.py`

### Move to telegras (Telegram-specific):

```python
class TelegramMedia:
    """Lightweight descriptor for supported Telegram media attachments."""
    file_id: str
    media_type: str
    file_name: str | None = None
    mime_type: str | None = None

def collect_supported_media(msg: TgMessage) -> list[TelegramMedia]
def extract_message_entity(update: TelegramUpdate) -> TgMessage | None
def extract_message_text(update: TelegramUpdate) -> str | None
def find_photo_with_max_size(msg: TgMessage) -> TgPhotoSize | None
```

### Keep in tg-wp-bridge (WordPress-specific):

- `build_title_from_text()`
- `build_slug_from_text()`
- `text_to_html()`
- `strip_title_line_from_text()`
- `strip_emojis()`
- `extract_hashtags()`

### Dependencies:
- Add `telegras/schemas.py` with `TgMessage`, `TgPhotoSize` models
- tg-wp-bridge imports media functions from `telegras.message_parser`

---

## Section 3: Logging System

**Move from:** `tg-wp-bridge/logging_utils.py`
**Move to:** `telegras/logging_utils.py`

### Functions:

```python
def resolve_writable_dir(preferred: Path, *, fallback_env_var: str, fallback_subdir: str) -> Path
def rotate_logs(storage_dir: Path) -> None
def record_update_log(update: Any, result: dict | None = None, *, tg_message_id: int | None = None) -> dict
def record_error_artifact(update: Any, exc: BaseException, *, tg_message_id: int | None = None, result: dict | None = None) -> str | None
```

### Changes:
- Rename `wp_result` parameter to generic `result`
- Update module docstring for telegras context
- tg-wp-bridge imports from `telegras.logging_utils`

### Configuration:
- `STORAGE_DIR` - primary log storage location
- `STORAGE_FALLBACK_DIR` - fallback if primary not writable
- `LOG_MAX_FILES` - maximum number of log files to keep
- `LOG_MAX_BYTES` - maximum total bytes of logs

---

## Section 4: App.py Refactoring with Lifespan Management

**File:** `telegras/app.py`

### Updated `create_app()` Signature:

```python
def create_app(
    app: FastAPI | None = None,
    *,
    settings: AppSettings | None = None,
    service: TelegramIngestionService | None = None,
    merge_lifespan: bool = True,
) -> FastAPI
```

### Behavior:
- If `app is None`: Creates new FastAPI app
- If `app provided`: Registers routes on existing app
- If `merge_lifespan=True`: Merges telegras lifespan with existing app's lifespan

### Lifespan Merging:

```python
def _merge_lifespans(ctx1, ctx2):
    """Merge two lifespan contexts into one."""
    @asynccontextmanager
    async def merged(app):
        async with ctx1(app):
            async with ctx2(app):
                yield
    return merged
```

### Remove from app.py:
```python
# DELETE this line:
app = create_app()
```

---

## Section 5: DisplayManager

**Move from:** `tg-wp-bridge/display.py`
**Move to:** `telegras/display.py`

### Class:

```python
class DisplayManager:
    def __init__(self, *, force_rich: bool = False, force_plain: bool = False)
    def is_rich(self) -> bool
    def print(message: str, **kwargs)
    def print_status(status: str, message: str, success: bool = True)
    def print_section(title: str)
```

### Features:
- Rich formatting with colors/icons when available
- Plain text fallback for non-interactive terminals
- Auto-detection of terminal capability

---

## Section 6: Startup Validation

**Create:** `telegras/startup.py`

### Functions:

```python
async def validate_telegram_config() -> dict[str, Any]
async def validate_webhook_config() -> dict[str, Any]
def run_startup_validation_sync(*, display: DisplayManager | None = None) -> dict[str, Any]
```

### Validations:
- Bot token validity and connectivity
- Bot information (username, ID)
- Webhook status (configured/not configured/error)

---

## Section 7: CLI Enhancement

**Update:** `telegras/cli.py`

### Commands:

| Command | Description |
|---------|-------------|
| `start` | Start the telegras server (with --host, --port, --reload) |
| `webhook-info` | Display current Telegram webhook information |
| `set-webhook` | Configure Telegram webhook |
| `delete-webhook` | Delete Telegram webhook |
| `get-me` | Get bot information |
| `startup-check` | Run comprehensive startup diagnostics |
| `db-init` | Initialize telegras database |

### CLI Options:
- `--debug` - Enable debug logging
- `--plain` - Force plain text output (no colors)

---

## Implementation Order

1. **Add to telegras:**
   - Update `telegram_api.py` with media download functions
   - Create `message_parser.py` with Telegram-specific helpers
   - Add `schemas.py` with `TgMessage`, `TgPhotoSize` models
   - Move `logging_utils.py` from tg-wp-bridge
   - Move `display.py` from tg-wp-bridge
   - Create `startup.py`

2. **Refactor telegras app.py:**
   - Update `create_app()` with app parameter and lifespan merging
   - Remove `app = create_app()` from module level
   - Update `__init__.py`

3. **Create telegras/start.py:**
   - Standalone entry point for running telegras

4. **Update telegras CLI:**
   - Add all Telegram commands

5. **Update tg-wp-bridge:**
   - Update imports to use telegras modules
   - Remove moved code from tg-wp-bridge
   - Add WordPress-specific startup checks on top of telegras checks

---

## Success Criteria

- [ ] All Telegram-related functions accessible via `telegras` package
- [ ] telegras can be used standalone OR mounted into another FastAPI app
- [ ] tg-wp-bridge imports all Telegram utilities from telegras
- [ ] CLI provides all Telegram operations
- [ ] Structured logging with rotation works in both projects
- [ ] All tests pass
