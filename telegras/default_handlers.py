from __future__ import annotations

import logging
import subprocess
from pathlib import Path
from typing import Any

log = logging.getLogger("telegras.default_handlers")


def shell_ls(context: dict[str, Any], *paths: str) -> dict[str, Any]:
    targets = list(paths) or ["."]
    output: dict[str, Any] = {}
    for raw in targets:
        path = Path(raw)
        try:
            output[str(path)] = sorted(entry.name for entry in path.iterdir())
        except Exception as exc:
            output[str(path)] = {"error": str(exc)}
    return output


def python_eval(context: dict[str, Any], *snippets: str) -> dict[str, Any]:
    local_vars: dict[str, Any] = {
        "message": context.get("message", {}),
        "chat": context.get("chat", {}),
        "update": context.get("update", {}),
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


def shell_sh(context: dict[str, Any], *commands: str) -> dict[str, Any]:
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


def get_default_handlers() -> dict[str, Any]:
    return {
        "handlers.shell:ls": shell_ls,
        "handlers.shell:sh": shell_sh,
        "handlers.python:eval": python_eval,
    }
