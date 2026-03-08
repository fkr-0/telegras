# tests/test_display.py
"""Tests for DisplayManager."""

from __future__ import annotations

from telegras.display import DisplayManager


def test_display_manager_force_plain():
    """Test DisplayManager with forced plain output."""
    display = DisplayManager(force_plain=True)
    assert not display.is_rich()


def test_display_manager_force_rich():
    """Test DisplayManager with forced rich output."""
    display = DisplayManager(force_rich=True)
    assert display.is_rich()


def test_display_manager_print_status(capsys):
    """Test print_status output."""
    display = DisplayManager(force_plain=True)
    display.print_status("", "Test message", success=True)
    captured = capsys.readouterr()
    assert "OK" in captured.out
    assert "Test message" in captured.out


def test_display_manager_print_status_failure(capsys):
    """Test print_status output with failure."""
    display = DisplayManager(force_plain=True)
    display.print_status("", "Error message", success=False)
    captured = capsys.readouterr()
    assert "FAIL" in captured.out
    assert "Error message" in captured.out


def test_display_manager_print_section(capsys):
    """Test print_section output."""
    display = DisplayManager(force_plain=True)
    display.print_section("Test Section")
    captured = capsys.readouterr()
    assert "Test Section" in captured.out
    assert captured.out.startswith("\n")


def test_display_manager_print_rich_markup_stripped(capsys):
    """Test that rich markup is stripped in plain mode."""
    display = DisplayManager(force_plain=True)
    display.print("Hello [bold]world[/bold]")
    captured = capsys.readouterr()
    assert "Hello world" in captured.out
    assert "[" not in captured.out


def test_display_manager_force_rich_overrides_plain():
    """Test that force_rich overrides auto-detection."""
    # When both are set, force_plain should take precedence for safety
    display = DisplayManager(force_rich=True, force_plain=True)
    # force_plain takes precedence
    assert not display.is_rich()
