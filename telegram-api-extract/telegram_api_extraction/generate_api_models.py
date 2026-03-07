#!/usr/bin/env python3
"""Generate Pydantic v2 models from parsed API JSON directories."""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
from collections import defaultdict


# Python reserved keywords that cannot be used as field names
PYTHON_RESERVED_KEYWORDS = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'
}

# Type mapping for Telegram Bot API types
PRIMITIVE_TYPE_MAPPING = {
    "Integer": "int",
    "String": "str",
    "Boolean": "bool",
    "Float": "float",
    "True": "bool",
}

# Types that should be optional
OPTIONAL_KEYWORDS = ["optional", "optional."]


def is_optional(description: str) -> bool:
    """Check if a field/parameter is optional based on its description."""
    if not description:
        return False
    desc_lower = description.lower()
    return any(kw in desc_lower for kw in OPTIONAL_KEYWORDS)


def parse_required_from_value(required_str: str) -> bool:
    """Parse the 'Required' column value to determine if field is required."""
    if not required_str:
        return True
    return required_str.lower() in ("yes", "true", "required")


def pythonize_type(type_str: str, forward_refs: Set[str]) -> str:
    """Convert Telegram type string to Python type annotation."""
    type_str = type_str.strip()

    # Check if it's an array type
    if type_str.startswith("Array of"):
        inner_type = type_str.replace("Array of", "").strip()
        inner_python = pythonize_type(inner_type, forward_refs)
        if inner_python not in ['int', 'str', 'bool', 'float']:
            forward_refs.add(inner_python)
        return f"list[{inner_python}]"

    # Check direct mapping
    if type_str in PRIMITIVE_TYPE_MAPPING:
        return PRIMITIVE_TYPE_MAPPING[type_str]

    # It's a custom type - track for forward reference
    forward_refs.add(type_str)
    return type_str


def sanitize_description(description: str) -> str:
    """Clean up description text for use in Field()."""
    if not description:
        return ""

    # Remove extra whitespace
    description = re.sub(r'\s+', ' ', description)

    # Escape quotes
    description = description.replace('"', '\\"')

    return description


def generate_pydantic_model(
    name: str,
    rows: List[Dict[str, str]],
    headers: List[str],
    all_forward_refs: Set[str],
    base_class: str = "BaseModel"
) -> str:
    """Generate a modern Pydantic v2 model class from table data."""

    # Determine if this is a Method or Object based on headers
    has_required = "required" in [h.lower() for h in headers]
    is_method = "parameter" in [h.lower() for h in headers]

    lines = []
    lines.append(f'class {name}({base_class}):')
    lines.append('    """')
    lines.append(f'    {name}' + (' method' if is_method else ' type') + ' from Telegram Bot API.')
    lines.append('    """')
    lines.append('')

    # Collect forward refs for this model
    model_forward_refs: Set[str] = set()

    for row in rows:
        field_name = row.get('field') or row.get('parameter', '')
        if not field_name:
            continue

        py_field_name = field_name

        # Handle Python reserved keywords by appending underscore
        if py_field_name in PYTHON_RESERVED_KEYWORDS:
            py_field_name = py_field_name + '_'

        type_str = row.get('type', 'str')
        description = sanitize_description(row.get('description', ''))

        # Determine if optional
        if has_required:
            required = parse_required_from_value(row.get('required', ''))
        else:
            required = not is_optional(description)

        # Get Python type
        py_type = pythonize_type(type_str, model_forward_refs)

        # Add Optional wrapper if not required
        if not required:
            py_type = f'None | {py_type}'  # Pydantic v2 style union

        # Build the field line with Field()
        if description:
            field_line = f'    {py_field_name}: {py_type} = Field(description="{description}")'
        else:
            field_line = f'    {py_field_name}: {py_type}'

        lines.append(field_line)

    # Add forward refs to global set
    all_forward_refs.update(model_forward_refs)

    lines.append('')
    return '\n'.join(lines)


def generate_pydantic_module(json_dir: str, output_file: str, module_name: str):
    """Generate a complete Pydantic v2 module from all JSON files in a directory."""

    all_forward_refs: Set[str] = set()
    models = []
    dependencies = defaultdict(set)

    json_files = sorted(Path(json_dir).glob('*.json'))

    for json_file in json_files:
        with open(json_file, 'r') as f:
            data = json.load(f)

        name = data['name'].replace(' ', '')
        table = data.get('table')
        if not table:
            continue

        rows = table['rows']
        headers = table['headers']

        # Collect dependencies
        for row in rows:
            type_str = row.get('type', '')
            if type_str and type_str not in PRIMITIVE_TYPE_MAPPING:
                if type_str.startswith('Array of'):
                    inner = type_str.replace('Array of', '').strip()
                    if inner not in PRIMITIVE_TYPE_MAPPING:
                        dependencies[name].add(inner)
                else:
                    dependencies[name].add(type_str)

        # Generate model
        model_code = generate_pydantic_model(name, rows, headers, all_forward_refs)
        models.append((name, model_code))

    # Write module
    with open(output_file, 'w') as f:
        # Module docstring
        f.write(f'"""Telegram Bot API - {module_name} Pydantic Models.\n')
        f.write('\n')
        f.write('Auto-generated from API documentation.\n')
        f.write('"""\n')
        f.write('\n')

        # Imports
        f.write('from __future__ import annotations\n')
        f.write('\n')
        f.write('from pydantic import BaseModel, Field\n')
        f.write('from typing import Any\n')
        f.write('\n')

        # Forward reference declarations for external types
        external_refs = all_forward_refs - set(m[0] for m in models)
        if external_refs:
            f.write('# External type references (would need to be imported or defined elsewhere)\n')
            for ref in sorted(external_refs):
                f.write(f'# {ref}\n')
            f.write('\n')

        # Write models
        written = set()
        to_write = set(m[0] for m in models)

        # Sort by dependency order
        while to_write:
            progress = False
            for name in list(to_write):
                deps = dependencies[name] - written - external_refs
                if not deps:
                    for model_name, model_code in models:
                        if model_name == name:
                            f.write(model_code)
                            f.write('\n')
                            written.add(name)
                            to_write.remove(name)
                            progress = True
                            break

            if not progress:
                # Write remaining (circular or external deps)
                for name in list(to_write):
                    for model_name, model_code in models:
                        if model_name == name:
                            f.write(model_code)
                            f.write('\n')
                            written.add(name)
                            to_write.remove(name)
                            break
                break


def main():
    # Generate for available-types
    print("Generating for available-types...")
    generate_pydantic_module(
        json_dir='available-types',
        output_file='available_types_models.py',
        module_name='Available Types'
    )
    print(f"✓ Generated available_types_models.py")

    # Count models
    with open('available_types_models.py', 'r') as f:
        content = f.read()
        class_count = content.count('class ')
    print(f"  ({class_count} models)")

    # Generate for available-methods
    print("\nGenerating for available-methods...")
    generate_pydantic_module(
        json_dir='available-methods',
        output_file='available_methods_models.py',
        module_name='Available Methods'
    )
    print(f"✓ Generated available_methods_models.py")

    # Count models
    with open('available_methods_models.py', 'r') as f:
        content = f.read()
        class_count = content.count('class ')
    print(f"  ({class_count} models)")


if __name__ == "__main__":
    main()
