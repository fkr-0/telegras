# Changelog

All notable changes to `telegras` will be documented in this file.

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
