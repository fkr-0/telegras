# Changelog

All notable changes to `telegras` will be documented in this file.

## [0.4.1] - 2026-03-08

### Fixed

- Test failure preventing build

## [0.4.0] - 2026-03-08

### Added
- Media download functions from Telegram Bot API:
  - `get_file_direct_url()` - Get direct download URL for Telegram files
  - `download_file()` - Download files to bytes or filesystem
- Message parser module for extracting media and text from Telegram updates:
  - `TelegramMedia` dataclass for media descriptors
  - `collect_supported_media()` - Extract all supported media from messages
  - `extract_message_entity()` - Get message from update (prefers channel_post)
  - `extract_message_text()` - Extract text or caption from updates
- Logging utilities with rotation:
  - `resolve_writable_dir()` - Resolve writable directory with fallback
  - `rotate_logs()` - Rotate logs by count or size
  - `record_update_log()` - Record updates and results to disk
  - `record_error_artifact()` - Write timestamped .error artifacts with traceback
- DisplayManager class for CLI output:
  - Rich formatting with automatic TTY detection
  - Plain text fallback for non-TTY environments
  - Status printing with icons
  - Section headers
- Startup validation utilities:
  - `validate_telegram_config()` - Validate bot token and connectivity
  - `validate_webhook_config()` - Check webhook status
  - `run_startup_validation_sync()` - Run all validations
- Enhanced CLI with Telegram operations:
  - `start` - Start the telegras server
  - `webhook-info` - Display current webhook information
  - `set-webhook` - Configure Telegram webhook
  - `delete-webhook` - Delete Telegram webhook
  - `get-me` - Get bot information
  - `startup-check` - Run comprehensive diagnostics
- Standalone entry point `start.py` for running telegras directly

### Changed
- Refactored `create_app()` to support mounting on existing FastAPI apps
- Removed module-level app instantiation for better composability
- Exported new functions in `__init__.py`: `get_file_direct_url`, `download_file`

## [0.3.2] - 2026-03-08

### Added
- Handler plugin hooks (`telegras.default_handlers.handler_plugin`
  and `register_handler_plugin`) so downstream packages can extend the handler map.

### Removed
- `telegras.backends.wordpress.WordPressPublishBackend`; WordPress publishing now sits in handler plugins outside telegras.

## [0.3.0] - 2026-03-07

### Added
- Additional assurance that CI installs `uv` so workflow runs succeed on GitHub Actions.
- Release workflow `publish.yml` now bumps via tags `v*`, builds with `uv build`, validates artifacts, and pushes to PyPI via trusted publisher/OIDC.
- `tg_api_parsed`, a copy of the curated Telegram API extraction, now distributed alongside `telegras` so dependent services can share the same reviewed models.
- `tg_api_parsed` re-exports only the types that the runtime uses (`Update`, `WebhookInfo`, `SetWebhookRequest`, `SendMessageRequest`, `GetMeResponse`).
- README notes about the centralized API package.
- CI workflow (`ci.yml`) runs tests and strict docs builds on pushes and pull requests; `publish.yml` automates PyPI uploads for `v*` tags via trusted publisher/OIDC.

### Changed
- Documentation and changelog mention the CI/release improvements, and the version metadata now reflects 0.3.0.

### Changed
- Docker assets now reference the `telegras` package and include `tg_api_parsed`, ensuring the container matches the library layout.
- `pyproject.toml` now packages `tg_api_parsed`.
- Updated docs and tooling to describe the centralized parsed API.

## [0.1.0] - 2026-03-06

### Added
- Curated runtime `telegras.api` submodule extracted from reviewed generated Telegram API docs:
  - `telegras.api.client.TelegramBotAPI`
  - `telegras.api.getting_updates` (`Update`, `WebhookInfo`, `SetWebhookRequest`)
  - `telegras.api.methods` (`SendMessageRequest`, `GetMeResponse`)
- Internal introspection webhook control endpoints:
  - `GET /internal/introspection/webhook/status`
  - `DELETE /internal/introspection/webhook`
- Internal UI controls for querying webhook status and deleting webhook.
- Review document for generated Telegram API migration strategy:
  - `docs/telegram_api_review.md`

### Changed
- `telegras.telegram_api` now delegates to `telegras.api.TelegramBotAPI`.
- Core runtime modules now reference update model through `telegras.api.getting_updates.Update`.
- Added `httpx` as a core runtime dependency for the Telegram API client layer.

## [1.2.0] - 2026-03-06

### Added
- Protected internal introspection API under `/internal/introspection/*` with Bearer token authentication via `INTROSPECTION_TOKEN`.
- Persistent introspection/audit storage for:
  - attachment definitions
  - webhook executions
  - per-handler execution records
- Webhook attachment enhancements:
  - composable matcher expressions
  - parser envelope support (`parse`, `parse_mode`)
  - `{{ match.* }}` template context values
  - grouped handler chains with sequential/parallel execution
- Internal overview UI at `/internal/introspection/ui` with inline JS for:
  - config/criteria/handlers overview
  - webhook history browsing and detail view
  - attachment CRUD helpers
  - filtering and sorting controls
- Built-in handler `handlers.shell:sh`.

### Changed
- Attachment registration/execution now uses persisted DB-backed definitions instead of in-memory-only state.
- `/v1/webhook-attachments/execute` now records execution telemetry for introspection.
- Expanded baseline Alembic schema to include introspection/audit tables.

## [1.1.0] - 2026-03-05

### Added
- `telegras` extracted as standalone package in `/home/user/work/code/telegras`.
- Dedicated packaging and test setup for `telegras`.
- Telegras API endpoints for:
  - listing chat IDs
  - chat message history by chat ID
  - sending messages to a chat
- Webhook attachment registry with composable matching and default handlers:
  - `handlers.shell:ls`
  - `handlers.python:eval`

### Changed
- `telegras.app` migrated to FastAPI lifespan startup handling (replacing deprecated `on_event`).

## [1.0.0] - 2026-03-03

### Added
- Initial `telegras` ingestion service and persistence schema.
- Multi-backend publication orchestration.
- Basic CLI (`telegras db-init`, `telegras backends`).
- Initial Alembic migration baseline.
