#!/usr/bin/env python3
"""
Create a clean telegram_api package structure with proper forward references.

This script reorganizes all generated models into a proper package structure.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict


def extract_classes_from_file(filepath: str) -> Dict[str, str]:
    """Extract all class definitions from a Python file."""
    with open(filepath, 'r') as f:
        content = f.read()

    classes = {}

    # Match either start of file or newline before class
    class_pattern = r'(?:^|\n)class ([A-Za-z][A-Za-z0-9_]*)\((.*?)\):'

    for match in re.finditer(class_pattern, content):
        class_name = match.group(1)
        # Start after the newline (if present) or at start
        if match.group(0).startswith('\n'):
            class_start = match.start() + 1
        else:
            class_start = match.start()

        # Find where this class ends (start of next class or end of file)
        next_match = re.search(class_pattern, content[match.end():])
        if next_match:
            class_end = match.end() + next_match.start()
        else:
            class_end = len(content)

        class_code = content[class_start:class_end].strip()
        classes[class_name] = class_code

    return classes


def get_all_classes_map() -> Dict[str, Dict[str, str]]:
    """Get all classes from all source files."""
    source_files = {
        'getting_updates': 'getting_updates_models.py',
        'updating_messages': 'updating_messages_models.py',
        'stickers': 'stickers_models.py',
        'inline_mode': 'inline_mode_models.py',
        'payments': 'payments_models.py',
        'telegram_passport': 'telegram_passport_models.py',
        'games': 'games_models.py',
        'available_types': 'available_types_models.py',
        'available_methods': 'available_methods_models.py',
    }

    all_classes = {}

    for section, filename in source_files.items():
        if not os.path.exists(filename):
            continue

        classes = extract_classes_from_file(filename)
        for class_name, class_code in classes.items():
            all_classes[class_name] = {
                'code': class_code,
                'section': section
            }

    return all_classes


def find_type_references(class_code: str) -> Set[str]:
    """Find all type references in a class definition."""
    types = set()

    # Find type annotations (after the colon)
    for match in re.finditer(r':\s*([^\n=]+?)(?:\s*=\s*|\s*$)', class_code):
        type_str = match.group(1).strip()

        # Handle Union types with |
        for part in type_str.split('|'):
            part = part.strip()

            # Handle list[Type]
            if part.startswith('list[') and part.endswith(']'):
                inner = part[5:-1].strip()
                types.add(inner)
            elif part and part not in ['None', 'Any', 'int', 'str', 'bool', 'float']:
                types.add(part)

    return types


def resolve_imports_for_class(
    class_name: str,
    class_code: str,
    current_section: str,
    all_classes: Dict[str, Dict[str, str]]
) -> Set[Tuple[str, str]]:
    """Resolve which imports are needed for a class."""
    imports = set()

    # Find type references
    types = find_type_references(class_code)

    for type_name in types:
        # Skip primitives and None
        if type_name in ['None', 'Any', 'int', 'str', 'bool', 'float']:
            continue

        # Skip "Integer or String" style compound types
        if ' or ' in type_name:
            continue

        # Check if this type is one of our classes
        if type_name in all_classes:
            type_section = all_classes[type_name]['section']
            if type_section != current_section:
                module_name = type_section.replace('_', '_')  # e.g., getting_updates -> getting_updates
                # Special case: available_types -> types
                if type_section == 'available_types':
                    module_name = 'types'
                elif type_section == 'available_methods':
                    module_name = 'methods'
                elif type_section == 'telegram_passport':
                    module_name = 'passport'

                imports.add((module_name, type_name))

    return imports


def fix_optional_fields(class_code: str) -> str:
    """Fix optional fields to have default None values for Pydantic v2."""
    lines = class_code.split('\n')
    result = []

    for line in lines:
        # Check if this is a field definition with None | type but no default
        # Pattern:    field_name: None | Type = Field(description="...")
        if ': None |' in line and '= Field(' in line and '=' not in line.split('= Field(')[0]:
            # Add default None before Field()
            line = line.replace('= Field(', '= Field(default=None, ')

        # Handle compound types like "Integer or String"
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


def quote_external_type_references(class_code: str, external_types: Set[str]) -> str:
    """Quote ALL external type references to use string annotations."""
    if not external_types:
        return class_code

    lines = class_code.split('\n')
    result = []

    for line in lines:
        # Check if this line contains any external type
        has_external = any(ext_type in line for ext_type in external_types)

        if not has_external:
            result.append(line)
            continue

        # Get the type annotation part (between : and = Field)
        match = re.search(r':\s*([^=]+?)\s*=\s*Field', line)
        if not match:
            result.append(line)
            continue

        type_annotation = match.group(1).strip()
        rest_of_line = line[match.end():]

        # If the type annotation contains external types, quote the whole thing
        if any(ext_type in type_annotation for ext_type in external_types):
            # Quote the entire type annotation
            new_line = line[:match.start()] + f': "{type_annotation}" = Field' + rest_of_line
            result.append(new_line)
        else:
            result.append(line)

    return '\n'.join(result)


def create_package():
    """Create the telegram_api package."""

    base_dir = Path('telegram_api')
    base_dir.mkdir(exist_ok=True)

    # Get all classes
    all_classes = get_all_classes_map()

    # Create __init__.py with all imports and rebuild function
    with open(base_dir / '__init__.py', 'w') as f:
        f.write('"""Telegram Bot API - Type-safe Python models.\n\n')
        f.write('Auto-generated from API documentation.\n')
        f.write('"""\n')
        f.write('\n')
        f.write('__version__ = "1.0.0"\n')
        f.write('\n')
        f.write('# Import all modules first\n')
        f.write('from . import getting_updates, types, methods\n')
        f.write('from . import updating_messages, stickers, inline_mode\n')
        f.write('from . import payments, passport, games\n')
        f.write('\n')
        f.write('# Re-export common types for convenience\n')
        f.write('from .types import User, Chat, Message, Update, BotCommand\n')
        f.write('from .methods import getMe, sendMessage\n')
        f.write('from .getting_updates import Update as UpdateType, WebhookInfo\n')
        f.write('\n')
        f.write('__all__ = [\n')
        f.write('    "User", "Chat", "Message", "Update", "BotCommand",\n')
        f.write('    "getMe", "sendMessage",\n')
        f.write('    "UpdateType", "WebhookInfo",\n')
        f.write(']\n')
        f.write('\n')
        f.write('# Rebuild models to resolve forward references\n')
        f.write('def _rebuild_all_models():\n')
        f.write('    """Internal function to rebuild all models after import."""\n')
        f.write('    # Collect all model classes\n')
        f.write('    all_models = {}\n')
        f.write('    for module in [getting_updates, types, methods, updating_messages,\n')
        f.write('                   stickers, inline_mode, payments, passport, games]:\n')
        f.write('        for name in dir(module):\n')
        f.write('            if name.startswith(\'_\'):\n')
        f.write('                continue\n')
        f.write('            obj = getattr(module, name)\n')
        f.write('            try:\n')
        f.write('                if isinstance(obj, type) and issubclass(obj, type):  # BaseModel check\n')
        f.write('                    all_models[name] = obj\n')
        f.write('            except TypeError:\n')
        f.write('                pass\n')
        f.write('    \n')
        f.write('    # Inject all models into each module\'s namespace and rebuild\n')
        f.write('    for module in [getting_updates, types, methods, updating_messages,\n')
        f.write('                   stickers, inline_mode, payments, passport, games]:\n')
        f.write('        for name, cls in all_models.items():\n')
        f.write('            if not hasattr(module, name):\n')
        f.write('                setattr(module, name, cls)\n')
        f.write('        for name in dir(module):\n')
        f.write('            if name.startswith(\'_\'):\n')
        f.write('                continue\n')
        f.write('            obj = getattr(module, name)\n')
        f.write('            try:\n')
        f.write('                if isinstance(obj, type) and issubclass(obj, type):\n')
        f.write('                    if hasattr(obj, \'model_rebuild\'):\n')
        f.write('                        obj.model_rebuild()\n')
        f.write('            except TypeError:\n')
        f.write('                pass\n')
        f.write('\n')
        f.write('# Rebuild on import\n')
        f.write('_rebuild_all_models()\n')

    # Create each module
    source_files = {
        'getting_updates': ('getting_updates', 'getting_updates_models.py'),
        'updating_messages': ('updating_messages', 'updating_messages_models.py'),
        'stickers': ('stickers', 'stickers_models.py'),
        'inline_mode': ('inline_mode', 'inline_mode_models.py'),
        'payments': ('payments', 'payments_models.py'),
        'telegram_passport': ('passport', 'telegram_passport_models.py'),
        'games': ('games', 'games_models.py'),
        'available_types': ('types', 'available_types_models.py'),
        'available_methods': ('methods', 'available_methods_models.py'),
    }

    for section, (module_name, source_file) in source_files.items():
        if not os.path.exists(source_file):
            continue

        print(f"Processing {section} -> {module_name}...")

        classes = extract_classes_from_file(source_file)
        if not classes:
            continue

        with open(base_dir / f'{module_name}.py', 'w') as f:
            # __future__ import must be first
            f.write('from __future__ import annotations\n')
            f.write('\n')

            # Module docstring
            f.write(f'"""Telegram Bot API - {section.replace("_", " ").title()}.\n\n')
            f.write('Auto-generated from API documentation.\n')
            f.write('"""\n')
            f.write('\n')

            # Standard imports - we don't import from other modules to avoid circular deps
            f.write('from pydantic import BaseModel, Field\n')
            f.write('\n')

            # Collect all external types for string annotations
            all_imports = set()
            for class_name, class_code in classes.items():
                imports = resolve_imports_for_class(class_name, class_code, section, all_classes)
                all_imports.update(imports)

            # Get all external types that need string annotations
            string_annotation_types = set(cls for _, cls in all_imports)

            # Write classes with fixed optional fields and string annotations for all external types
            for class_name in sorted(classes.keys()):
                fixed_code = fix_optional_fields(classes[class_name])
                # Quote ALL external types to avoid circular imports
                quoted_code = quote_external_type_references(fixed_code, string_annotation_types)
                f.write(quoted_code)
                f.write('\n')

        print(f"  ✓ Wrote {len(classes)} classes to {module_name}.py")


def create_tests():
    """Create test files for the package."""

    tests_dir = Path('telegram_api/tests')
    tests_dir.mkdir(exist_ok=True)

    with open(tests_dir / '__init__.py', 'w') as f:
        f.write('"""Tests for telegram_api package."""\n')

    with open(tests_dir / 'test_types.py', 'w') as f:
        f.write('''"""Tests for telegram_api.types module."""

import pytest
from telegram_api.types import User, Chat, Message


def test_user_creation():
    """Test creating a User model."""
    user = User(
        id=123456789,
        is_bot=False,
        first_name="Test"
    )

    assert user.id == 123456789
    assert user.is_bot is False
    assert user.first_name == "Test"


def test_user_with_optional_fields():
    """Test creating a User with optional fields."""
    user = User(
        id=123456789,
        is_bot=True,
        first_name="Bot",
        username="test_bot"
    )

    assert user.username == "test_bot"


def test_chat_creation():
    """Test creating a Chat model."""
    chat = Chat(
        id=-100123456789,
        type="supergroup"
    )

    assert chat.id == -100123456789
    assert chat.type == "supergroup"


def test_message_creation():
    """Test creating a Message model."""
    message = Message(
        message_id=1,
        date=1234567890,
        chat=Chat(id=123, type="private")
    )

    assert message.message_id == 1
    assert message.chat.id == 123
''')

    with open(tests_dir / 'test_methods.py', 'w') as f:
        f.write('''"""Tests for telegram_api.methods module."""

import pytest
from telegram_api.methods import getMe, sendMessage


def test_sendmessage_required_fields():
    """Test sendMessage with required fields."""
    method = sendMessage(
        chat_id=123456789,
        text="Hello, World!"
    )

    assert method.chat_id == 123456789
    assert method.text == "Hello, World!"


def test_sendmessage_with_optional_fields():
    """Test sendMessage with optional fields."""
    method = sendMessage(
        chat_id=123456789,
        text="Hello!",
        parse_mode="Markdown",
        disable_notification=True
    )

    assert method.parse_mode == "Markdown"
    assert method.disable_notification is True
''')

    with open(tests_dir / 'conftest.py', 'w') as f:
        f.write('''"""Pytest configuration for telegram_api tests."""

import pytest


@pytest.fixture
def sample_user():
    """Create a sample User for testing."""
    from telegram_api.types import User
    return User(
        id=123456789,
        is_bot=False,
        first_name="Test",
        username="test_user"
    )
''')

    print("  ✓ Created test files")


def create_documentation():
    """Create documentation files."""

    base_dir = Path('telegram_api')

    with open(base_dir / 'README.md', 'w') as f:
        f.write('''# Telegram Bot API - Type-Safe Python Models

Auto-generated Pydantic v2 models for the Telegram Bot API.

## Features

- **Type Safety**: Full Pydantic v2 model definitions
- **Validation**: Automatic field validation and serialization
- **IDE Support**: Full autocomplete and type hints
- **Documentation**: Field descriptions from Telegram API docs

## Installation

```bash
pip install pydantic
```

## Usage

```python
from telegram_api.types import User, Message, Chat
from telegram_api.methods import sendMessage

# Create type-safe models
user = User(
    id=123456789,
    is_bot=False,
    first_name="John",
    username="john_doe"
)

# Method parameters with validation
params = sendMessage(
    chat_id=123456789,
    text="Hello, World!"
)

# JSON serialization
print(params.model_dump_json(indent=2))
```

## Module Structure

- `types` - All type definitions (User, Message, Chat, etc.)
- `methods` - All API methods (getMe, sendMessage, etc.)
- `getting_updates` - Webhooks and long polling
- `updating_messages` - Message editing methods
- `stickers` - Sticker-related types and methods
- `inline_mode` - Inline query types and methods
- `payments` - Payment types and methods
- `passport` - Telegram Passport types
- `games` - Game types and methods
''')

    with open(base_dir / 'pyproject.toml', 'w') as f:
        f.write('''[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "telegram-api-models"
version = "1.0.0"
description = "Type-safe Pydantic models for Telegram Bot API"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
''')

    print("  ✓ Created documentation")


def main():
    print("Creating telegram_api package...\n")

    print("Step 1: Creating modules...")
    create_package()

    print("\nStep 2: Creating tests...")
    create_tests()

    print("\nStep 3: Creating documentation...")
    create_documentation()

    print("\n✓ Package created successfully!")
    print("\nUsage:")
    print("  import telegram_api")
    print("  user = telegram_api.types.User(id=123, is_bot=False, first_name='Test')")


if __name__ == "__main__":
    main()
