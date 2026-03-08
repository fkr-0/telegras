from __future__ import annotations

import logging
import subprocess
from pathlib import Path
from typing import Any

from telegras.handler_registry import handler_plugin, parser_plugin

log = logging.getLogger("telegras.default_handlers")


@handler_plugin("handlers.shell:ls")
def shell_ls(context: dict[str, Any], *paths: str) -> dict[str, Any]:
    """List the contents of one or more directories."""
    targets = list(paths) or ["."]
    output: dict[str, Any] = {}
    for raw in targets:
        path = Path(raw)
        try:
            output[str(path)] = sorted(entry.name for entry in path.iterdir())
        except Exception as exc:
            output[str(path)] = {"error": str(exc)}
    return output


@handler_plugin("handlers.python:eval")
def python_eval(context: dict[str, Any], *snippets: str) -> dict[str, Any]:
    """Evaluate one or more Python snippets in a shared local context."""
    local_vars: dict[str, Any] = {
        "message": context.get("message", {}),
        "chat": context.get("chat", {}),
        "update": context.get("update", {}),
        "match": context.get("match", {}),
        "log": log,
    }

    for snippet in snippets:
        exec(snippet, {"__builtins__": __builtins__}, local_vars)

    serializable_locals = {
        key: value
        for key, value in local_vars.items()
        if key not in {"log"} and not callable(value)
    }
    return {"locals": serializable_locals, "snippets": len(snippets)}


@handler_plugin("handlers.shell:sh")
def shell_sh(context: dict[str, Any], *commands: str) -> dict[str, Any]:
    """Execute one or more shell commands using /bin/sh."""
    command = " && ".join(commands).strip()
    if not command:
        raise ValueError("No shell command provided")

    completed = subprocess.run(
        ["sh", "-c", command],
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "command": command,
    }


@handler_plugin("handlers.telegram:to_markdown")
def telegram_to_markdown(context: dict[str, Any], *args: str) -> dict[str, Any]:
    """Write a Telegram message to a markdown file with frontmatter."""
    import datetime
    import re

    message = context.get("message", {})
    text = message.get("text", "")
    message_id = message.get("message_id", "unknown")
    date = message.get("date", None)
    if date is not None:
        ts = datetime.datetime.fromtimestamp(date).isoformat()
    else:
        ts = datetime.datetime.now().isoformat()

    lines = text.splitlines()
    if lines:
        headline = lines[0].strip("# ").strip()
        body = "\n".join(lines[1:]).strip()
    else:
        headline = "No headline"
        body = ""

    body = re.sub(r"\*(.*?)\*", r"**\1**", body)
    body = re.sub(r"_(.*?)_", r"*\1*", body)

    frontmatter = f"---\nts: {ts}\nid: {message_id}\n---\n"
    markdown = f"{frontmatter}\n# {headline}\n\n{body}\n"

    output_path = args[0] if args else "telegram_message.md"
    path = Path(output_path)
    path.write_text(markdown, encoding="utf-8")

    return {"path": str(path), "status": "written", "headline": headline}


@handler_plugin("handlers.telegram:to_pandoc")
def telegram_to_pandoc(context: dict[str, Any], *args: str) -> dict[str, Any]:
    """Convert a Telegram message to markdown, then to another format using pandoc."""
    import datetime
    import re
    import tempfile

    message = context.get("message", {})
    text = message.get("text", "")
    message_id = message.get("message_id", "unknown")
    date = message.get("date", None)
    if date is not None:
        ts = datetime.datetime.fromtimestamp(date).isoformat()
    else:
        ts = datetime.datetime.now().isoformat()

    lines = text.splitlines()
    filetype = "html5"
    if lines and lines[0].startswith("#pandoc:"):
        filetype = lines[0][8:].strip()
        lines = lines[1:]

    if lines:
        headline = lines[0].strip("# ").strip()
        body = "\n".join(lines[1:]).strip()
    else:
        headline = "No headline"
        body = ""

    body = re.sub(r"\*(.*?)\*", r"**\1**", body)
    body = re.sub(r"_(.*?)_", r"*\1*", body)

    frontmatter = f"---\nts: {ts}\nid: {message_id}\n---\n"
    markdown = f"{frontmatter}\n# {headline}\n\n{body}\n"

    ext = filetype if filetype != "html5" else "html"
    output_path = args[0] if args else f"telegram_message.{ext}"
    path = Path(output_path)

    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".md") as tmp_md:
        tmp_md.write(markdown)
        tmp_md.flush()
        tmp_md_path = tmp_md.name

    try:
        subprocess.run(
            ["pandoc", "-f", "markdown", "-t", filetype, "-o", str(path), tmp_md_path],
            check=True,
        )
        status = "converted"
    except Exception as exc:
        status = f"pandoc error: {exc}"

    return {
        "path": str(path),
        "status": status,
        "headline": headline,
        "filetype": filetype,
    }


@parser_plugin("parsers.message:text_parts")
def parse_message_text_parts(context: dict[str, Any], update: Any) -> dict[str, Any]:
    """Extract a title/body split from the current Telegram message text."""
    text = context.get("message", {}).get("full") or ""
    lines = text.splitlines()
    title = lines[0].strip() if lines else ""
    body = "\n".join(lines[1:]).strip() if len(lines) > 1 else ""
    return {
        "status": "ok",
        "match": {
            "title": title,
            "body": body,
        },
        "warnings": [],
        "errors": [],
    }


def get_default_handlers() -> dict[str, Any]:
    """Return the built-in handler map for documentation and compatibility."""
    return {
        "handlers.shell:ls": shell_ls,
        "handlers.shell:sh": shell_sh,
        "handlers.python:eval": python_eval,
        "handlers.telegram:to_markdown": telegram_to_markdown,
        "handlers.telegram:to_pandoc": telegram_to_pandoc,
    }
