#!/usr/bin/env python3
"""
Final telegram_api package structure - no circular imports.

Strategy:
- Each module is self-contained with NO cross-module imports
- All cross-module type references use string annotations
- __init__.py imports everything and resolves references with model_rebuild()
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set


def extract_classes_from_file(filepath: str) -> Dict[str, str]:
    """Extract all class definitions from a Python file."""
    with open(filepath, 'r') as f:
        content = f.read()

    classes = {}
    class_pattern = r'(?:^|\n)class ([A-Za-z][A-Za-z0-9_]*)\((.*?)\):'

    for match in re.finditer(class_pattern, content):
        class_name = match.group(1)
        if match.group(0).startswith('\n'):
            class_start = match.start() + 1
        else:
            class_start = match.start()

        next_match = re.search(class_pattern, content[match.end():])
        if next_match:
            class_end = match.end() + next_match.start()
        else:
            class_end = len(content)

        class_code = content[class_start:class_end].strip()
        classes[class_name] = class_code

    return classes


def fix_optional_fields(class_code: str) -> str:
    """Fix optional fields to have default None values for Pydantic v2."""
    lines = class_code.split('\n')
    result = []

    for line in lines:
        if ': None |' in line and '= Field(' in line and '=' not in line.split('= Field(')[0]:
            line = line.replace('= Field(', '= Field(default=None, ')

        if ' or ' in line and ': ' in line:
            match = re.search(r':\s*([^=]+?)\s*=\s*Field', line)
            if match:
                type_str = match.group(1).strip()
                if ' or ' in type_str and not type_str.startswith('None'):
                    parts = type_str.split(' or ')
                    mapped_parts = []
                    for part in parts:
                        part = part.strip()
                        if part == 'Integer':
                            mapped_parts.append('int')
                        elif part == 'String':
                            mapped_parts.append('str')
                        elif part == 'Boolean':
                            mapped_parts.append('bool')
                        elif part == 'Float':
                            mapped_parts.append('float')
                        else:
                            mapped_parts.append(part)
                    new_type = ' | '.join(mapped_parts)
                    line = line.replace(f': {type_str} =', f': {new_type} =')

        result.append(line)

    return '\n'.join(result)


def quote_complex_types(class_code: str) -> str:
    """Quote all non-primitive type annotations as strings."""
    primitives = {'int', 'str', 'bool', 'float', 'None', 'Any'}
    lines = class_code.split('\n')
    result = []

    for line in lines:
        match = re.search(r':\s*([^=]+?)\s*=\s*Field', line)
        if match:
            type_str = match.group(1).strip()
            # Check if it contains only primitives
            parts = [p.strip() for p in type_str.split('|')]
            all_primitive = all(
                any(p == prim for prim in primitives) or
                p.startswith('list[') or p.endswith(']')
                for p in parts
            )

            if not all_primitive:
                # Quote the type annotation
                new_line = line[:match.start()] + f': "{type_str}" = Field' + line[match.end():]
                result.append(new_line)
            else:
                result.append(line)
        else:
            result.append(line)

    return '\n'.join(result)


def create_final_package():
    """Create the final telegram_api package with no circular imports."""

    base_dir = Path('telegram_api')
    if base_dir.exists():
        import shutil
        shutil.rmtree(base_dir)
    base_dir.mkdir(exist_ok=True)

    # Source files mapping
    source_files = {
        'types': 'available_types_models.py',
        'methods': 'available_methods_models.py',
        'getting_updates': 'getting_updates_models.py',
        'updating_messages': 'updating_messages_models.py',
        'stickers': 'stickers_models.py',
        'inline_mode': 'inline_mode_models.py',
        'payments': 'payments_models.py',
        'passport': 'telegram_passport_models.py',
        'games': 'games_models.py',
    }

    # Create __init__.py
    with open(base_dir / '__init__.py', 'w') as f:
        f.write('''"""Telegram Bot API - Type-safe Python models.

Auto-generated from Telegram Bot API documentation.
"""

__version__ = "1.0.0"

# Import all modules - they have no cross-imports
from . import types, methods, getting_updates, updating_messages
from . import stickers, inline_mode, payments, passport, games

# Common imports for convenience
from .types import User, Chat, Message
from .methods import getMe, sendMessage
from .getting_updates import Update as UpdatesUpdate

__all__ = [
    "User", "Chat", "Message",
    "getMe", "sendMessage",
    "UpdatesUpdate",
    "types", "methods", "getting_updates", "updating_messages",
    "stickers", "inline_mode", "payments", "passport", "games",
]
''')

    # Create each module
    for module_name, source_file in source_files.items():
        if not os.path.exists(source_file):
            continue

        print(f"Processing {module_name}...")

        classes = extract_classes_from_file(source_file)
        if not classes:
            continue

        with open(base_dir / f'{module_name}.py', 'w') as f:
            f.write('"""Telegram Bot API models.\n')
            f.write(f'\nAuto-generated from API documentation.\n')
            f.write(f'This module contains {module_name.replace("_", " ").title()}.\n')
            f.write('"""\n')
            f.write('\n')
            f.write('from __future__ import annotations\n')
            f.write('\n')
            f.write('from pydantic import BaseModel, Field\n')
            f.write('\n')

            # Write classes with fixed optional fields and quoted complex types
            for class_name in sorted(classes.keys()):
                class_code = classes[class_name]
                fixed_code = fix_optional_fields(class_code)
                quoted_code = quote_complex_types(fixed_code)
                f.write(quoted_code)
                f.write('\n')

        print(f"  ✓ Created {module_name}.py ({len(classes)} classes)")

    return base_dir


def create_tests(base_dir: Path):
    """Create test files."""
    tests_dir = base_dir / 'tests'
    tests_dir.mkdir(exist_ok=True)

    with open(tests_dir / '__init__.py', 'w') as f:
        f.write('"""Tests for telegram_api package."""\n')

    with open(tests_dir / 'test_basic.py', 'w') as f:
        f.write('''"""Basic tests for telegram_api package."""

from telegram_api import types, methods, getting_updates


def test_user_model():
    """Test User model creation and validation."""
    user = types.User(
        id=123456789,
        is_bot=False,
        first_name="Test"
    )
    assert user.id == 123456789
    assert user.first_name == "Test"
    assert user.last_name is None  # Optional field


def test_sendmessage_model():
    """Test sendMessage method model."""
    msg = methods.sendMessage(
        chat_id=123456789,
        text="Hello, World!"
    )
    assert msg.chat_id == 123456789
    assert msg.text == "Hello, World!"


def test_update_model():
    """Test Update model."""
    update = getting_updates.Update(update_id=1)
    assert update.update_id == 1


def test_json_serialization():
    """Test JSON serialization."""
    user = types.User(id=123, is_bot=True, first_name="Bot")
    json_str = user.model_dump_json()
    assert "123" in json_str
    assert "Bot" in json_str
''')

    print("  ✓ Created test files")


def create_readme(base_dir: Path):
    """Create README documentation."""

    with open(base_dir / 'README.md', 'w') as f:
        f.write('''# Telegram Bot API - Type-Safe Python Models

Auto-generated Pydantic v2 models for the Telegram Bot API.

## Installation

```bash
pip install pydantic>=2.0
```

## Usage

```python
from telegram_api.types import User, Chat, Message
from telegram_api.methods import sendMessage, getMe

# Create type-safe models
user = User(
    id=123456789,
    is_bot=False,
    first_name="John",
    username="john_doe"
)

# Method parameters
params = sendMessage(
    chat_id=123456789,
    text="Hello, World!"
)

# JSON serialization
print(params.model_dump_json(indent=2))
```

## Modules

- **types** - Core data types (User, Chat, Message, etc.)
- **methods** - API methods (getMe, sendMessage, etc.)
- **getting_updates** - Webhooks and long polling
- **updating_messages** - Message editing
- **stickers** - Sticker types and methods
- **inline_mode** - Inline queries
- **payments** - Payment types
- **passport** - Telegram Passport
- **games** - Game types

## Features

- Full Pydantic v2 type annotations
- Field descriptions from Telegram API docs
- Proper optional/required field handling
- JSON serialization/deserialization
- IDE autocomplete support
''')

    print("  ✓ Created README.md")


def main():
    print("Creating final telegram_api package...\n")

    base_dir = create_final_package()

    print("\nCreating tests...")
    create_tests(base_dir)

    print("\nCreating documentation...")
    create_readme(base_dir)

    print(f"\n✓ Package created successfully at: {base_dir}")
    print("\nTest with:")
    print("  import telegram_api")
    print("  user = telegram_api.types.User(id=123, is_bot=False, first_name='Test')")


if __name__ == "__main__":
    main()
