#!/usr/bin/env python3
"""
Fix compound type annotations in telegram_api modules.

Converts types like "Integer or String" to "int | str" within quoted annotations.
"""

import re
from pathlib import Path


# Type mappings for Telegram API types to Python types
TYPE_MAPPINGS = {
    "Integer": "int",
    "String": "str",
    "Boolean": "bool",
    "Float": "float",
    "True": "bool",
    "False": "bool",
}


def convert_compound_type(type_str: str) -> str:
    """Convert a compound type string to Python type annotation."""
    original = type_str

    # Replace each type with its Python equivalent
    for telegram_type, python_type in TYPE_MAPPINGS.items():
        # Use word boundaries to avoid partial matches
        type_str = re.sub(r'\b' + telegram_type + r'\b', python_type, type_str)

    # Replace " or " with " | "
    type_str = type_str.replace(' or ', ' | ')

    return type_str


def fix_quoted_types_in_line(line: str) -> str:
    """Fix compound types within quoted annotations."""
    # Find quoted type annotations: "TYPE" = Field(...)
    pattern = r':\s*"([^"]+)"\s*=\s*Field'

    def replace_quoted_type(match):
        quote_content = match.group(1)
        converted = convert_compound_type(quote_content)
        return f': "{converted}" = Field'

    result = re.sub(pattern, replace_quoted_type, line)
    return result


def fix_module_file(file_path: Path) -> int:
    """Fix compound types in a module file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()

    fixed_lines = []
    changes = 0

    for line in lines:
        fixed_line = fix_quoted_types_in_line(line)
        if fixed_line != line:
            changes += 1
        fixed_lines.append(fixed_line)

    if changes > 0:
        with open(file_path, 'w') as f:
            f.writelines(fixed_lines)
        print(f"  ✓ Fixed {changes} compound type annotations in {file_path.name}")
    else:
        print(f"  - No changes needed in {file_path.name}")

    return changes


def main():
    """Fix compound types in all telegram_api modules."""
    print("Fixing compound type annotations in telegram_api modules...")
    print()

    base_dir = Path(__file__).resolve().parents[1] / "telegram_api"

    module_files = [
        base_dir / 'types.py',
        base_dir / 'methods.py',
        base_dir / 'getting_updates.py',
        base_dir / 'stickers.py',
        base_dir / 'inline_mode.py',
        base_dir / 'payments.py',
        base_dir / 'passport.py',
        base_dir / 'games.py',
        base_dir / 'updating_messages.py',
    ]

    total_changes = 0
    for file_path in module_files:
        if file_path.exists():
            changes = fix_module_file(file_path)
            total_changes += changes
        else:
            print(f"  ⚠ File not found: {file_path}")

    print()
    print(f"✓ Total compound type annotations fixed: {total_changes}")
    print()
    print("Now rebuild Python cache and run tests:")
    print("  find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null")
    print("  find . -name '*.pyc' -delete 2>/dev/null")
    print("  python -m pytest tests/test_basic.py -v")


if __name__ == "__main__":
    main()
