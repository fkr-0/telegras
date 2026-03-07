# Telegram API Review (Docs -> telegras.api)

Date: 2026-03-06

## Source reviewed

Generated package under `docs/telegram_api/`:
- `getting_updates.py`
- `methods.py`
- `types.py`
- feature modules (`games.py`, `inline_mode.py`, `payments.py`, `passport.py`, `stickers.py`, `updating_messages.py`)

## Findings

- The generated package is broad and not fully integration-ready for runtime use in `telegras` without additional stabilization:
  - very large surface area
  - many forward references and cross-type dependencies
  - naming conventions mixed between type and method representations
- `telegras` currently needs a narrow, high-confidence subset for runtime operations.

## Implemented extraction

Created curated runtime submodule:

- `telegras/api/__init__.py`
- `telegras/api/getting_updates.py`
  - `Update` (alias to telegras runtime update model)
  - `WebhookInfo`
  - `SetWebhookRequest`
- `telegras/api/methods.py`
  - `SendMessageRequest`
  - `TelegramUser`
  - `GetMeResponse`
- `telegras/api/client.py`
  - `TelegramBotAPI` client wrapper for:
    - `send_message`
    - `get_webhook_info`
    - `set_webhook`
    - `get_me`

## Usage migration completed

- `telegras/telegram_api.py` now wraps `telegras.api.TelegramBotAPI`.
- Runtime modules now import update type from `telegras.api.getting_updates` (alias `Update as TelegramUpdate`) where feasible.

## Deferred scope

The full generated Telegram API corpus remains in `docs/telegram_api/` for future staged integration.
Recommended next stage is to add additional strongly-needed method/type slices as requirements emerge, instead of bulk import.
