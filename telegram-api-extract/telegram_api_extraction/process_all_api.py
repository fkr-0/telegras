#!/usr/bin/env python3
"""Process all remaining API HTML files to JSON and Pydantic models."""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
from collections import defaultdict
from bs4 import BeautifulSoup


# Mapping of file names to output directory names
FILE_MAPPING = {
    'api-updating-messages.html': 'updating-messages',
    'api-stickers.html': 'stickers',
    'api-inline-mode.html': 'inline-mode',
    'api-payments.html': 'payments',
    'api-telegram-passport.html': 'telegram-passport',
    'api-games.html': 'games',
}

# Python reserved keywords that cannot be used as field names
PYTHON_RESERVED_KEYWORDS = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'
}

PRIMITIVE_TYPE_MAPPING = {
    "Integer": "int",
    "String": "str",
    "Boolean": "bool",
    "Float": "float",
    "True": "bool",
}

OPTIONAL_KEYWORDS = ["optional", "optional."]


def parse_table_data(table):
    """Parse a table and return structured data."""
    thead = table.find('thead')
    tbody = table.find('tbody')
    if not thead or not tbody:
        return None
    headers = [th.get_text(strip=True) for th in thead.find_all('th')]
    rows = []
    for tr in tbody.find_all('tr', recursive=False):
        cells = tr.find_all('td', recursive=False)
        if not cells:
            continue
        row_data = {}
        for i, cell in enumerate(cells):
            if i >= len(headers):
                continue
            header = headers[i].lower()
            text = ' '.join(cell.stripped_strings)
            row_data[header] = text
        rows.append(row_data)
    return {'headers': headers, 'rows': rows}


def parse_html_file(file_path):
    """Parse an API HTML file and extract structured data."""
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    sections = []

    for h4 in soup.find_all('h4'):
        anchor = h4.find('a', class_='anchor')
        if not anchor:
            continue

        name = anchor.get('name', '')
        text = h4.get_text(strip=True)

        description = []
        next_elem = h4.find_next_sibling()
        while next_elem and next_elem.name == 'p':
            desc_text = ' '.join(next_elem.stripped_strings)
            description.append(desc_text)
            next_elem = next_elem.find_next_sibling()

        table = h4.find_next('table', class_='table')
        table_data = None
        if table:
            table_data = parse_table_data(table)

        notes = []
        if table:
            next_elem = table.find_next_sibling()
            if next_elem and next_elem.name == 'blockquote':
                notes_text = ' '.join(next_elem.stripped_strings)
                notes.append(notes_text)

        sections.append({
            'name': text,
            'anchor': name,
            'description': description,
            'table': table_data,
            'notes': notes
        })

    return sections


def is_optional(description: str) -> bool:
    if not description:
        return False
    desc_lower = description.lower()
    return any(kw in desc_lower for kw in OPTIONAL_KEYWORDS)


def parse_required_from_value(required_str: str) -> bool:
    if not required_str:
        return True
    return required_str.lower() in ("yes", "true", "required")


def pythonize_type(type_str: str, forward_refs: Set[str]) -> str:
    type_str = type_str.strip()
    if type_str.startswith("Array of"):
        inner_type = type_str.replace("Array of", "").strip()
        inner_python = pythonize_type(inner_type, forward_refs)
        if inner_python not in ['int', 'str', 'bool', 'float']:
            forward_refs.add(inner_python)
        return f"list[{inner_python}]"
    if type_str in PRIMITIVE_TYPE_MAPPING:
        return PRIMITIVE_TYPE_MAPPING[type_str]
    forward_refs.add(type_str)
    return type_str


def sanitize_description(description: str) -> str:
    if not description:
        return ""
    description = re.sub(r'\s+', ' ', description)
    description = description.replace('"', '\\"')
    return description


def generate_pydantic_model(
    name: str,
    rows: List[Dict[str, str]],
    headers: List[str],
    all_forward_refs: Set[str],
    base_class: str = "BaseModel"
) -> str:
    has_required = "required" in [h.lower() for h in headers]
    is_method = "parameter" in [h.lower() for h in headers]

    lines = []
    lines.append(f'class {name}({base_class}):')
    lines.append('    """')
    lines.append(f'    {name}' + (' method' if is_method else ' type') + ' from Telegram Bot API.')
    lines.append('    """')
    lines.append('')

    model_forward_refs: Set[str] = set()

    for row in rows:
        field_name = row.get('field') or row.get('parameter', '')
        if not field_name:
            continue

        py_field_name = field_name

        # Handle Python reserved keywords
        if py_field_name in PYTHON_RESERVED_KEYWORDS:
            py_field_name = py_field_name + '_'

        type_str = row.get('type', 'str')
        description = sanitize_description(row.get('description', ''))

        if has_required:
            required = parse_required_from_value(row.get('required', ''))
        else:
            required = not is_optional(description)

        py_type = pythonize_type(type_str, model_forward_refs)

        if not required:
            py_type = f'None | {py_type}'

        if description:
            field_line = f'    {py_field_name}: {py_type} = Field(description="{description}")'
        else:
            field_line = f'    {py_field_name}: {py_type}'

        lines.append(field_line)

    all_forward_refs.update(model_forward_refs)
    lines.append('')
    return '\n'.join(lines)


def generate_pydantic_module(json_dir: str, output_file: str, module_name: str):
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

        for row in rows:
            type_str = row.get('type', '')
            if type_str and type_str not in PRIMITIVE_TYPE_MAPPING:
                if type_str.startswith('Array of'):
                    inner = type_str.replace('Array of', '').strip()
                    if inner not in PRIMITIVE_TYPE_MAPPING:
                        dependencies[name].add(inner)
                else:
                    dependencies[name].add(type_str)

        model_code = generate_pydantic_model(name, rows, headers, all_forward_refs)
        models.append((name, model_code))

    with open(output_file, 'w') as f:
        f.write(f'"""Telegram Bot API - {module_name} Pydantic Models.\n')
        f.write('\n')
        f.write('Auto-generated from API documentation.\n')
        f.write('"""\n')
        f.write('\n')

        f.write('from __future__ import annotations\n')
        f.write('\n')
        f.write('from pydantic import BaseModel, Field\n')
        f.write('from typing import Any\n')
        f.write('\n')

        external_refs = all_forward_refs - set(m[0] for m in models)
        if external_refs:
            f.write('# External type references (would need to be imported or defined elsewhere)\n')
            for ref in sorted(external_refs):
                f.write(f'# {ref}\n')
            f.write('\n')

        written = set()
        to_write = set(m[0] for m in models)

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
    total_sections = 0

    # Step 1: Parse all HTML files to JSON
    print("Step 1: Parsing HTML files to JSON...")
    for html_file, output_dir in FILE_MAPPING.items():
        if not os.path.exists(html_file):
            print(f"  Skipping {html_file} (not found)")
            continue

        sections = parse_html_file(html_file)
        total_sections += len(sections)

        os.makedirs(output_dir, exist_ok=True)

        for section in sections:
            name = section['anchor'].replace('-', '_')
            filename = f'{name}.json'
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(section, f, indent=2, ensure_ascii=False)

        print(f"  ✓ {output_dir}: {len(sections)} sections")

    print(f"\n  Total: {total_sections} sections parsed\n")

    # Step 2: Generate Pydantic models for each directory
    print("Step 2: Generating Pydantic models...")
    total_classes = 0

    for output_dir in FILE_MAPPING.values():
        if not os.path.exists(output_dir):
            continue

        # Generate module name from directory
        module_name = output_dir.replace('-', ' ').title()
        output_file = f"{output_dir.replace('-', '_')}_models.py"

        try:
            generate_pydantic_module(output_dir, output_file, module_name)

            # Count classes
            with open(output_file, 'r') as f:
                class_count = f.read().count('class ')
            total_classes += class_count

            print(f"  ✓ {output_file} ({class_count} classes)")
        except Exception as e:
            print(f"  ✗ {output_dir}: {e}")

    print(f"\n  Total: {total_classes} Pydantic classes generated")


if __name__ == "__main__":
    main()
