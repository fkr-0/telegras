# Telegram API Extraction Tooling

This directory contains the extraction/generation pipeline used to turn Telegram's HTML Bot API documentation into structured JSON and generated Python model modules.

## Purpose

`telegras` keeps a curated `telegras.api` runtime subset. These scripts support review and regeneration workflows by:

1. Parsing HTML API pages into structured per-method/type JSON files.
2. Generating intermediate model modules from extracted JSON.
3. Building and restructuring generated API packages.
4. Applying post-processing fixes (forward references and compound type annotations).

The tooling is intended for maintainers, not runtime execution in production.

## Main scripts

- `parse_api.py`
  - Parses `api-getting-updates.html` into `getting-updates/*.json`.
- `process_all_api.py`
  - Parses remaining Telegram HTML API pages into section JSON.
- `generate_pydantic_models.py`
  - Generates Pydantic models and JSON schemas from extracted JSON.
- `generate_api_models.py`
  - Generates multi-module Pydantic output from parsed directories.
- `create_api_package.py`
  - Creates a package layout from generated model modules.
- `restructure_api.py`
  - Reorganizes generated package modules to reduce cross-module import issues.
- `fix_forward_references.py`, `fix_forward_references_v2.py`
  - Applies forward-reference quoting fixes.
- `fix_compound_types.py`
  - Converts compound textual types (for example `Integer or String`) into Python union syntax.
- `final_api_package.py`
  - Final consolidation step for generated package outputs.

## Usage notes

- Backward-compatible wrappers remain in `docs/*.py` so existing commands still work.
- Run from repository root, for example:

```bash
python docs/parse_api.py
python docs/process_all_api.py
```

or call the moved scripts directly:

```bash
python docs/telegram_api_extraction/parse_api.py
```

## Output scope

Generated outputs include:

- JSON extraction artifacts under `docs/*` subfolders.
- Generated model modules under `docs/*_models.py`.
- Generated package variants under `docs/telegram_api/` and related review artifacts.
