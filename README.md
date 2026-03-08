# telegras

Standalone Telegram ingestion core extracted from `tg-wp-bridge`.
## telegras architecture

`telegras` is a focused Telegram + FastAPI ingestion core offering:

- Async ingestion service and backend abstraction (`PublishBackend`)
- Async SQLAlchemy persistence (default `sqlite+aiosqlite:///./data/telegras.db`)
- OpenAPI endpoints for persisted interactions/publications
- Alembic migrations (`telegras db-init`, `telegras backends`)
- Media download utilities for Telegram Bot API files
- Message parsing for extracting media and text from updates
- Logging utilities with rotation and error artifact recording
- DisplayManager for rich CLI output with plain text fallback
- Startup validation and diagnostics
- Enhanced CLI with Telegram operations

The plugin-capable handler registry lets downstream packages (like `tg-wp-bridge`) register WordPress publishing via `telegras.default_handlers.handler_plugin`.

## Concept

```ascii
[Telegram Channel]
        |
        | (forwarded via bot)
        v
[Telegram Bot Webhook (our service, in Docker)]
        |
        | 1. Parse message (text + media URLs)
        | 2. Optionally download media
        | 3. POST to WordPress REST API
        v
[WordPress REST API]
        |
        v
[New Post in Category X]
```

Each channel message becomes a WordPress post:

- **Text** → post title & content
- **Media** (photos, videos, documents) → uploaded to WordPress and embedded

No WordPress plugin required; uses built-in REST API + Application Passwords.

# Parsed Telegram API

The generated Telegram Bot API models live in `tg_api_parsed`. They are copied from the reviewed `telegram-api-extract` artifacts and expose only the types used by `telegras`:

- `tg_api_parsed.Update`
- `tg_api_parsed.WebhookInfo`
- `tg_api_parsed.SetWebhookRequest`
- `tg_api_parsed.SendMessageRequest`
- `tg_api_parsed.GetMeResponse`

# CI & Releases

- **CI**: `ci.yml` runs `uv run pytest -q` and `uv run --extra docs mkdocs build --strict` on pushes/PRs against `main`.
- **Releases**: `publish.yml` triggers on `push` tags `v*`, builds the package, checks artifacts, and publishes to PyPI. Configure a PyPI trusted publisher (OIDC) so `secrets.PYPI_TOKEN` can stay empty while GitHub forwards identity securely. If you prefer the classic API token, create a repository secret named `PYPI_TOKEN`.

## Local development

- Install: `uv pip install -e .[dev]`
- Run API: `uv run uvicorn telegras.app:app --reload`
- Run tests: `uv run pytest`

## Media Download

Telegras provides utilities for downloading files from Telegram Bot API:

```python
from telegras import get_file_direct_url, download_file

# Get direct download URL for a file
url = await get_file_direct_url(file_id)

# Download file to bytes
content = await download_file(file_id)

# Download file to path
await download_file(file_id, destination_path="/path/to/file")
```

## Message Parsing

The message parser extracts media and text from Telegram updates:

```python
from telegras.message_parser import (
    TelegramMedia,
    collect_supported_media,
    extract_message_entity,
    extract_message_text,
)

# Extract media from a message
media_items = collect_supported_media(message)
for item in media_items:
    print(f"{item.media_type}: {item.file_id}")

# Extract text from update
text = extract_message_text(update)

# Get the message entity from an update
msg = extract_message_entity(update)
```

Supported media types:
- Photos (largest variant selected)
- Videos
- Animations (GIFs)
- Documents

## Logging Utilities

Telegras includes structured logging utilities with rotation:

```python
from telegras.logging_utils import (
    resolve_writable_dir,
    rotate_logs,
    record_update_log,
    record_error_artifact,
)

# Resolve a writable directory with fallback
log_dir = resolve_writable_dir(
    Path("./logs"),
    fallback_env_var="STORAGE_FALLBACK_DIR",
    fallback_subdir="logs",
)

# Record update and result to disk
paths = await record_update_log(update, result, tg_message_id=123)

# Record error with traceback
error_path = await record_error_artifact(update, exception, tg_message_id=123)
```

Log rotation is controlled by environment variables:
- `LOG_MAX_FILES`: Maximum number of log files to keep
- `LOG_MAX_BYTES`: Maximum total bytes of logs

## DisplayManager

CLI output formatting with rich support and plain text fallback:

```python
from telegras.display import DisplayManager

display = DisplayManager(force_rich=True, force_plain=False)

# Print with formatting
display.print("[bold]Hello[/bold]")

# Print status with icons
display.print_status("ok", "Operation successful", success=True)

# Print section header
display.print_section("Configuration")
```

## Startup Validation

Validate Telegram and webhook configuration:

```python
from telegras.startup import run_startup_validation_sync

results = run_startup_validation_sync()
# Returns dict with validation results
```

## CLI Commands

Telegras provides a comprehensive CLI:

```bash
# Start the server
telegras start [--host HOST] [--port PORT] [--reload]

# Webhook operations
telegras webhook-info [--format json|table]
telegras set-webhook --url URL [--dry-run]
telegras delete-webhook [--drop-pending]

# Bot information
telegras get-me

# Startup diagnostics
telegras startup-check [--auto-fix-webhook/--no-auto-fix-webhook]

# Database operations
telegras db-init
telegras backends
```

## Mounting on Existing FastAPI Apps

You can mount telegras on an existing FastAPI application:

```python
from fastapi import FastAPI
from telegras import create_app

app = FastAPI()
telegras_app = create_app()

# Mount telegras at a specific path
app.mount("/telegram", telegras_app)
```

## Standalone Entry Point

For running telegras directly:

```python
# Via start.py
python -m telegras.start

# Or via CLI
telegras start
```

## Bot mode

Set `BOT_MODE` to control update transport:

- `webhook` (default)
- `polling`

Examples:

- `BOT_MODE=webhook uv run uvicorn telegras.app:app --reload`
- `BOT_MODE=polling uv run uvicorn telegras.app:app --reload`

## API submodule

`telegras` now includes a curated Telegram API runtime subset in `telegras.api`:

- `telegras.api.client.TelegramBotAPI`
- `telegras.api.getting_updates` (`Update`, `WebhookInfo`, `SetWebhookRequest`)
- `telegras.api.methods` (`SendMessageRequest`, `GetMeResponse`)

This subset is extracted from reviewed generated specs in `docs/telegram_api/` and used by `telegras.telegram_api`.

## Webhook Attachments

Webhook attachments are composable match rules bound to handler identifiers.

### Attachment schema

```json
{
  "name": "blog-channel",
  "handler": "handlers.python:eval",
  "handler_args": ["result = '{{ message.title }}'"],
  "enabled": true,
  "priority": 10,
  "stop_on_match": false,
  "when": {
    "op": "all",
    "children": [
      {
        "op": "leaf",
        "leaf": {
          "field": "chat.type",
          "match": "eq",
          "value": "channel"
        }
      },
      {
        "op": "leaf",
        "leaf": {
          "field": "message.text",
          "match": "regex",
          "value": "#blog\\b"
        }
      }
    ]
  }
}
```

### API endpoints

- `GET /v1/webhook-attachments`
- `POST /v1/webhook-attachments`
- `DELETE /v1/webhook-attachments/{name}`
- `POST /v1/webhook-attachments/match`
- `POST /v1/webhook-attachments/execute`

### Protected introspection API

Set `INTROSPECTION_TOKEN` and call with `Authorization: Bearer <token>`.

- `GET /internal/introspection/config`
- `GET /internal/introspection/attachments`
- `POST /internal/introspection/attachments`
- `PUT /internal/introspection/attachments/{name}`
- `DELETE /internal/introspection/attachments/{name}`
- `GET /internal/introspection/webhook-executions`
- `GET /internal/introspection/handlers`
- `GET /internal/introspection/match-criteria`

### Exact examples

Register a shell listing handler:

```json
{
  "name": "list-temp",
  "handler": "handlers.shell:ls",
  "handler_args": ["/home", "/tmp"],
  "when": {
    "op": "leaf",
    "leaf": {
      "field": "chat.type",
      "match": "eq",
      "value": "group"
    }
  }
}
```

Register a Python eval handler with parse-result templates:

```json
{
  "name": "mail-on-title",
  "handler": "handlers.python:eval",
  "handler_args": [
    "import mails",
    "mails.send_mail('{{ message.title }}')",
    "log.info(f\"full message: {{ message.full }}\")"
  ],
  "when": {
    "op": "all",
    "children": [
      {
        "op": "leaf",
        "leaf": {
          "field": "chat.type",
          "match": "eq",
          "value": "group"
        }
      },
      {
        "op": "leaf",
        "leaf": {
          "field": "message.text",
          "match": "contains",
          "value": "urgent"
        }
      }
    ]
  }
}
```

Register a grouped handler chain with parser extraction:

```json
{
  "name": "grouped-mail",
  "handler_chain": [
    {
      "handler": "handlers.python:eval",
      "handler_args": ["title = '{{ match.title }}'"]
    },
    {
      "handler": "handlers.python:eval",
      "handler_args": ["log.info('full=' + '{{ message.full }}')"]
    }
  ],
  "execution_mode": "sequential",
  "stop_on_error": true,
  "parse": {
    "regex": {
      "title": "^(?P<title>[^\\n]+)"
    },
    "parser_ref": null,
    "allow_partial": true
  },
  "parse_mode": "warn",
  "when": {
    "op": "leaf",
    "leaf": {
      "field": "chat.type",
      "match": "eq",
      "value": "group"
    }
  }
}
```

Execute matching attachments for an incoming update:

```json
{
  "update": {
    "update_id": 10001,
    "message": {
      "message_id": 33,
      "date": 1700000000,
      "chat": {
        "id": 444,
        "type": "group",
        "title": "Ops"
      },
      "text": "Status report\nEverything looks green."
    }
  }
}
```

### Built-in handlers

- `handlers.shell:ls`
  - Args: path strings
  - Result: map of path to directory entries (or error)
- `handlers.shell:sh`
  - Args: shell command fragments, joined with `&&`
  - Result: `returncode`, `stdout`, `stderr`, `command`
- `handlers.python:eval`
  - Args: Python snippets executed in order
  - Available variables: `message`, `chat`, `update`, `log`
  - Result: serializable `locals` snapshot

For the complete user guide to matcher expressions and handler execution, see:

- `docs/webhook-attachments.md`

### Template fields for `handler_args`

`{{ ... }}` placeholders are supported:

- `{{ message.title }}` first line of text/caption
- `{{ message.full }}` full text/caption
- `{{ message.text }}` full text/caption
- `{{ message.has_media }}` boolean
- `{{ message.media_type }}` detected media kind
- `{{ chat.id }}` chat id
- `{{ chat.type }}` chat type
- `{{ chat.title }}` chat title
- `{{ update.update_id }}` Telegram update id
- `{{ update.kind }}` detected update kind
- `{{ match.<key> }}` parser output values

## Telegram API extraction tooling

Extraction and generation scripts that parse Telegram HTML API docs were moved to:

- `docs/telegram_api_extraction/`

Purpose and script-level documentation:

- `docs/telegram_api_extraction/README.md`

Backward-compatible wrappers remain in `docs/*.py`.
