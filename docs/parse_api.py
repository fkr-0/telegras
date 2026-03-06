#!/usr/bin/env python3
"""Parse Telegram Bot API HTML documentation into structured JSON."""

from bs4 import BeautifulSoup
import json
import os
import re
from pathlib import Path


def parse_table_data(table, table_type="object"):
    """Parse a table and return structured data.

    Args:
        table: BeautifulSoup table element
        table_type: Either "object" (Field, Type, Description) or "method" (Parameter, Type, Required, Description)

    Returns:
        dict: Structured table data
    """
    thead = table.find('thead')
    tbody = table.find('tbody')

    if not thead or not tbody:
        return None

    # Get headers
    headers = [th.get_text(strip=True) for th in thead.find_all('th')]

    # Get rows
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
            # Get text content with proper spacing
            text = ' '.join(cell.stripped_strings)
            row_data[header] = text

        rows.append(row_data)

    return {
        "headers": headers,
        "rows": rows
    }


def extract_links(text):
    """Extract href links from text."""
    return re.findall(r'href="([^"]*)"', text)


def parse_html_file(file_path):
    """Parse an API HTML file and extract structured data.

    Returns:
        list: List of sections with their data
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    sections = []

    # Find all h4 tags (section headers)
    for h4 in soup.find_all('h4'):
        # Extract section name from the anchor
        anchor = h4.find('a', class_='anchor')
        if not anchor:
            continue

        name = anchor.get('name', '')
        # The text is after the anchor in the h4 tag
        text = h4.get_text(strip=True)

        # Get the description paragraph(s) after h4
        description = []
        next_elem = h4.find_next_sibling()
        while next_elem and next_elem.name == 'p':
            # Get text with better spacing handling
            desc_text = ' '.join(next_elem.stripped_strings)
            description.append(desc_text)
            next_elem = next_elem.find_next_sibling()

        # Find the next table
        table = h4.find_next('table', class_='table')
        if table:
            # Determine table type by headers
            thead = table.find('thead')
            if thead:
                headers = [th.get_text(strip=True).lower() for th in thead.find_all('th')]
                table_type = "method" if "required" in headers else "object"

                table_data = parse_table_data(table, table_type)
            else:
                table_data = None
        else:
            table_data = None

        # Check for blockquote (notes) after table
        notes = []
        if table:
            next_elem = table.find_next_sibling()
            if next_elem and next_elem.name == 'blockquote':
                notes_text = ' '.join(next_elem.stripped_strings)
                notes.append(notes_text)

        section_data = {
            "name": text,
            "anchor": name,
            "description": description,
            "table": table_data,
            "notes": notes
        }

        sections.append(section_data)

    return sections


def save_sections_to_json(sections, output_dir):
    """Save each section to a separate JSON file."""
    os.makedirs(output_dir, exist_ok=True)

    for section in sections:
        # Create safe filename
        name = section['anchor'].replace('-', '_')
        filename = f"{name}.json"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(section, f, indent=2, ensure_ascii=False)

        print(f"Created: {filepath}")


def main():
    input_file = "api-getting-updates.html"
    output_dir = "getting-updates"

    sections = parse_html_file(input_file)

    print(f"Found {len(sections)} sections")

    for section in sections:
        print(f"\n{section['name']} ({section['anchor']})")
        if section['table']:
            print(f"  Rows: {len(section['table']['rows'])}")
        if section['notes']:
            print(f"  Notes: {len(section['notes'])}")

    save_sections_to_json(sections, output_dir)


if __name__ == "__main__":
    main()
