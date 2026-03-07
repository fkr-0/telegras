#!/usr/bin/env python3
"""
Restructure telegram_api to avoid circular imports using dependency layers.

Layer structure:
1. core.py - Core types with no/minimal dependencies (User, Chat, etc.)
2. types.py - Complex types that depend on core
3. methods.py - API methods that depend on types
4. features/ - Feature-specific modules
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict


# Define dependency layers
CORE_TYPES = {
    # These are foundational types that others depend on
    'User', 'Chat', 'Message', 'BotCommand', 'BotCommandScope',
    'BotCommandScopeDefault', 'BotCommandScopeAllPrivateChats',
    'BotCommandScopeAllGroupChats', 'BotCommandScopeAllChatAdministrators',
    'BotCommandScopeChat', 'BotCommandScopeChatAdministrators',
    'BotCommandScopeChatMember',
}

FEATURE_TYPES = {
    # Feature-specific types
    'InlineQuery', 'ChosenInlineResult', 'ShippingQuery', 'PreCheckoutQuery',
    'LabeledPrice', 'Invoice', 'SuccessfulPayment', 'OrderInfo', 'ShippingOption',
    'PassportElementError', 'PassportData', 'EncryptedPassportElement',
    'Game', 'CallbackGame', 'GameHighScore',
}


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

    for match in re.finditer(r':\s*([^\n=]+?)(?:\s*=\s*|\s*$)', class_code):
        type_str = match.group(1).strip()

        for part in type_str.split('|'):
            part = part.strip()

            if part.startswith('list[') and part.endswith(']'):
                inner = part[5:-1].strip()
                types.add(inner)
            elif part and part not in ['None', 'Any', 'int', 'str', 'bool', 'float']:
                # Extract the actual type name
                types.add(part)

    return types


def determine_target_module(class_name: str, all_classes: Dict[str, Dict[str, str]]) -> str:
    """Determine which module a class should belong to based on dependencies."""
    if class_name in CORE_TYPES:
        return 'core'

    if class_name in FEATURE_TYPES:
        # Check which section it came from to decide the feature module
        section = all_classes.get(class_name, {}).get('section', '')
        if section == 'inline_mode':
            return 'features/inline'
        elif section == 'payments':
            return 'features/payments'
        elif section == 'telegram_passport':
            return 'features/passport'
        elif section == 'games':
            return 'features/games'
        elif section == 'stickers':
            return 'features/stickers'
        elif section == 'getting_updates':
            return 'features/updates'
        elif section == 'updating_messages':
            return 'features/updates'

    # Check if it's a method
    section = all_classes.get(class_name, {}).get('section', '')
    if section == 'available_methods':
        return 'methods'

    # Default to types
    return 'types'


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


def create_restructured_package():
    """Create the restructured telegram_api package."""

    base_dir = Path('telegram_api_restructured')
    if base_dir.exists():
        import shutil
        shutil.rmtree(base_dir)
    base_dir.mkdir(exist_ok=True)

    # Get all classes
    all_classes = get_all_classes_map()

    # Organize classes by target module
    modules = defaultdict(list)
    for class_name, class_info in all_classes.items():
        target_module = determine_target_module(class_name, all_classes)
        modules[target_module].append((class_name, class_info['code']))

    # Create features directory
    (base_dir / 'features').mkdir(exist_ok=True)

    # Create __init__.py
    with open(base_dir / '__init__.py', 'w') as f:
        f.write('"""Telegram Bot API - Type-safe Python models.\n\n')
        f.write('Restructured to avoid circular imports.\n')
        f.write('"""\n')
        f.write('\n')
        f.write('__version__ = "1.0.0"\n')
        f.write('\n')
        f.write('# Import all modules\n')
        f.write('from . import core, types, methods\n')
        f.write('from .features import updates, stickers, inline_mode, payments, passport, games\n')
        f.write('\n')
        f.write('# Convenience imports\n')
        f.write('from .core import User, Chat, Message\n')
        f.write('from .types import Update, BotCommand\n')
        f.write('from .methods import getMe, sendMessage\n')
        f.write('from .features.updates import Update as UpdatesUpdate\n')

    # Write __init__.py for features
    with open(base_dir / 'features' / '__init__.py', 'w') as f:
        f.write('"""Feature-specific Telegram API types and methods."""\n')
        f.write('from . import updates, stickers, inline_mode, payments, passport, games\n')

    # Write each module
    for module_name in ['core', 'types', 'methods']:
        module_file = base_dir / f'{module_name}.py'
        classes_list = modules.get(module_name, [])

        with open(module_file, 'w') as f:
            f.write('from __future__ import annotations\n')
            f.write('\n')
            f.write(f'"""Telegram Bot API - {module_name.title()}."""\n')
            f.write('\n')
            f.write('from pydantic import BaseModel, Field\n')
            f.write('\n')

            # Determine imports needed
            imports_needed = set()
            for class_name, class_code in classes_list:
                refs = find_type_references(class_code)
                for ref in refs:
                    if ref in all_classes:
                        ref_target = determine_target_module(ref, all_classes)
                        if ref_target != module_name and ref_target != 'features/updates':
                            # Import from other modules
                            imports_needed.add((ref_target, ref))

            # Write imports (only from core for other modules, from types for methods)
            if imports_needed:
                for target_module, cls in sorted(imports_needed):
                    if target_module == 'core':
                        f.write(f'from .core import {cls}\n')
                    elif target_module == 'types':
                        f.write(f'from .types import {cls}\n')

                f.write('\n')

            # Write classes
            for class_name, class_code in sorted(classes_list, key=lambda x: x[0]):
                fixed_code = fix_optional_fields(class_code)
                f.write(fixed_code)
                f.write('\n')

        print(f"  ✓ Created {module_name}.py ({len(classes_list)} classes)")

    # Write feature modules
    feature_mapping = {
        'features/updates': ['getting_updates', 'updating_messages'],
        'features/stickers': ['stickers'],
        'features/inline_mode': ['inline_mode'],
        'features/payments': ['payments'],
        'features/passport': ['telegram_passport'],
        'features/games': ['games'],
    }

    feature_files = {
        'getting_updates': 'getting_updates_models.py',
        'updating_messages': 'updating_messages_models.py',
        'stickers': 'stickers_models.py',
        'inline_mode': 'inline_mode_models.py',
        'payments': 'payments_models.py',
        'telegram_passport': 'telegram_passport_models.py',
        'games': 'games_models.py',
    }

    for module_path, sections in feature_mapping.items():
        module_file = base_dir / f'{module_path}.py'
        all_classes_in_module = []

        for section in sections:
            if section not in feature_files:
                continue
            classes = extract_classes_from_file(feature_files[section])
            all_classes_in_module.extend(classes.items())

        with open(module_file, 'w') as f:
            f.write('from __future__ import annotations\n')
            f.write('\n')
            feature_name = module_path.split('/')[-1].replace('_', ' ').title()
            f.write(f'"""Telegram Bot API - {feature_name}."""\n')
            f.write('\n')
            f.write('from pydantic import BaseModel, Field\n')
            f.write('from ..core import User, Chat, Message\n')
            f.write('from ..types import Update\n')
            f.write('\n')

            for class_name, class_code in sorted(all_classes_in_module, key=lambda x: x[0]):
                fixed_code = fix_optional_fields(class_code)
                f.write(fixed_code)
                f.write('\n')

        print(f"  ✓ Created {module_path}.py ({len(all_classes_in_module)} classes)")

    return base_dir


def main():
    print("Restructuring telegram_api package...\n")
    print("New structure:")
    print("- core.py: Foundational types (User, Chat, Message)")
    print("- types.py: Complex types (Update, BotCommand, etc.)")
    print("- methods.py: All API methods")
    print("- features/: Feature-specific modules")
    print("  - updates.py: Getting/updating messages")
    print("  - stickers.py: Sticker types")
    print("  - inline_mode.py: Inline mode types")
    print("  - payments.py: Payment types")
    print("  - passport.py: Telegram Passport types")
    print("  - games.py: Game types")
    print()

    base_dir = create_restructured_package()

    print(f"\n✓ Restructured package created at: {base_dir}")
    print("\nTest it with:")
    print(f"  sys.path.insert(0, '{base_dir.parent}')")
    print(f"  from telegram_api_restructured import core, types, methods")


if __name__ == "__main__":
    main()
