from __future__ import annotations

import io
from dataclasses import dataclass
from typing import Callable, Sequence

import pytest


@dataclass
class CLIResult:
    exit_code: int
    output: str
    stdout: str
    stderr: str


@pytest.fixture
def invoke_cli() -> Callable[[Sequence[str]], CLIResult]:
    from telegras.cli import cli

    def _invoke(args: Sequence[str]) -> CLIResult:
        stdout = io.StringIO()
        stderr = io.StringIO()
        exit_code = cli(list(args), stdout=stdout, stderr=stderr)
        return CLIResult(
            exit_code=exit_code,
            output=stdout.getvalue() + stderr.getvalue(),
            stdout=stdout.getvalue(),
            stderr=stderr.getvalue(),
        )

    return _invoke
