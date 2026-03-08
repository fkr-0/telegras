# telegras/display.py
"""CLI display manager with rich formatting and plain text fallback."""

from __future__ import annotations

import re


class DisplayManager:
    """Manage CLI output with rich formatting and plain text fallback."""

    def __init__(
        self,
        *,
        force_rich: bool = False,
        force_plain: bool = False,
    ) -> None:
        self.force_rich = force_rich
        self.force_plain = force_plain

    def is_rich(self) -> bool:
        """Return True if rich output is enabled."""
        if self.force_plain:
            return False
        if self.force_rich:
            return True
        # Auto-detect based on terminal support
        try:
            import sys

            return sys.stdout.isatty()
        except Exception:
            return False

    def print(self, message: str, **kwargs: object) -> None:
        """Print a message with appropriate formatting."""
        if self.is_rich():
            from rich.console import Console

            console = Console()
            console.print(message, **kwargs)
        else:
            # Strip rich markup for plain output
            clean = re.sub(r"\[.*?\]", "", message)
            # Filter kwargs to valid print() parameters
            valid_kwargs = {
                k: v for k, v in kwargs.items()
                if k in {"sep", "end", "file", "flush"}
            }
            print(clean, **valid_kwargs)

    def print_status(self, status: str, message: str, success: bool = True) -> None:
        """Print a status message with icon."""
        if self.is_rich():
            icon = "[green]✓[/green]" if success else "[red]✗[/red]"
            self.print(f"{icon} {message}")
        else:
            icon = "OK" if success else "FAIL"
            self.print(f"{icon}: {message}")

    def print_section(self, title: str) -> None:
        """Print a section header."""
        if self.is_rich():
            from rich.console import Console

            console = Console()
            console.print(f"\n[bold cyan]{title}[/bold cyan]")
        else:
            print(f"\n{title}")
