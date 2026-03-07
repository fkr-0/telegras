# Getting Started

## Install

```bash
pip install telegras
```

For local development with docs and lint tooling:

```bash
uv sync --extra dev --extra docs
```

## Run the app

```bash
uv run uvicorn telegras.app:app --reload
```

## Bot update mode

`BOT_MODE` controls how updates are received:

- `webhook` (default): receive updates through webhook routes.
- `polling`: run a background long-polling worker (`getUpdates`).

Example:

```bash
BOT_MODE=polling uv run uvicorn telegras.app:app --reload
```

## Build docs

```bash
uv run mkdocs build --strict
```

## Docstring quality checks

```bash
uv run ruff check --select D telegras
uv run interrogate telegras
uv run pydoclint --config=pyproject.toml telegras
```

## Docstring convention

The project uses Google-style docstrings for public APIs. Keep docstrings concise and rely on type hints as the source of truth.
