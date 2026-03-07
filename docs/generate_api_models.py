#!/usr/bin/env python3
"""Compatibility wrapper for moved Telegram API extraction tooling."""

import os
from pathlib import Path
import runpy

if __name__ == "__main__":
    docs_dir = Path(__file__).resolve().parent
    os.chdir(docs_dir)
    target = docs_dir / "telegram_api_extraction" / Path(__file__).name
    runpy.run_path(str(target), run_name="__main__")
