# Telegram API Extraction Pipeline

This project includes maintainers-only tooling for parsing the Telegram Bot API HTML documentation and generating reviewable Python artifacts.

For the full script inventory and purpose, see:

- [`docs/telegram_api_extraction/README.md`](telegram_api_extraction/README.md)

The extraction pipeline is separate from runtime code:

- Runtime API surface used by the app lives in `telegras.api`.
- Extraction scripts and generated intermediate artifacts live under `docs/`.

Use this pipeline when Telegram API docs change and you want to regenerate, compare, and curate updates before promoting them into runtime modules.
