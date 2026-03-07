# telegras

Standalone Telegram ingestion core extracted from `tg-wp-bridge`.

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
