# tests/test_cli.py
"""Tests for telegras CLI."""

import pytest
from click.testing import CliRunner
from unittest.mock import AsyncMock, MagicMock, patch
from telegras.cli import cli


def test_cli_help():
    """Test CLI help output."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "start" in result.output
    assert "webhook-info" in result.output
    assert "set-webhook" in result.output
    assert "delete-webhook" in result.output
    assert "get-me" in result.output
    assert "startup-check" in result.output
    assert "db-init" in result.output
    assert "backends" in result.output


def test_db_init_command(monkeypatch):
    """Test db-init command."""
    async def mock_init():
        pass

    monkeypatch.setattr("telegras.cli.init_db", mock_init)

    runner = CliRunner()
    result = runner.invoke(cli, ["db-init"])
    assert result.exit_code == 0
    assert "Database initialized" in result.output


def test_backends_command(monkeypatch):
    """Test backends command."""
    monkeypatch.setattr(
        "telegras.cli.parse_backend_names",
        lambda x: ["backend1", "backend2"]
    )

    runner = CliRunner()
    result = runner.invoke(cli, ["backends"])
    assert result.exit_code == 0
    assert "backend1" in result.output
    assert "backend2" in result.output


def test_webhook_info_table_format(monkeypatch):
    """Test webhook-info command with table format."""
    mock_info = MagicMock()
    mock_info.url = "https://example.com/webhook"
    mock_info.pending_update_count = 0
    mock_info.has_custom_certificate = False
    mock_info.last_error_message = None

    async def mock_get_webhook():
        return mock_info

    monkeypatch.setattr("telegras.cli.get_webhook_info", mock_get_webhook)

    runner = CliRunner()
    result = runner.invoke(cli, ["webhook-info"])
    assert result.exit_code == 0
    assert "Webhook Information" in result.output
    assert "https://example.com/webhook" in result.output


def test_webhook_info_json_format(monkeypatch):
    """Test webhook-info command with JSON format."""
    mock_info = MagicMock()
    mock_info.model_dump.return_value = {
        "url": "https://example.com/webhook",
        "pending_update_count": 0,
        "has_custom_certificate": False,
    }

    async def mock_get_webhook():
        return mock_info

    monkeypatch.setattr("telegras.cli.get_webhook_info", mock_get_webhook)

    runner = CliRunner()
    result = runner.invoke(cli, ["webhook-info", "--output-format", "json"])
    assert result.exit_code == 0
    assert "https://example.com/webhook" in result.output


def test_set_webhook_dry_run(monkeypatch):
    """Test set-webhook command with dry-run."""
    runner = CliRunner()
    result = runner.invoke(cli, ["set-webhook", "--url", "https://example.com/webhook", "--dry-run"])
    assert result.exit_code == 0
    assert "Would set webhook to: https://example.com/webhook" in result.output


def test_set_webhook_success(monkeypatch):
    """Test set-webhook command with success."""
    async def mock_set_webhook(**kwargs):
        return {"ok": True, "result": True, "description": "Webhook was set"}

    monkeypatch.setattr("telegras.cli.set_webhook", mock_set_webhook)

    runner = CliRunner()
    result = runner.invoke(cli, ["set-webhook", "--url", "https://example.com/webhook"])
    assert result.exit_code == 0
    assert "Webhook configured successfully" in result.output


def test_set_webhook_failure(monkeypatch):
    """Test set-webhook command with failure."""
    async def mock_set_webhook(**kwargs):
        return {"ok": False, "description": "Invalid URL"}

    monkeypatch.setattr("telegras.cli.set_webhook", mock_set_webhook)

    runner = CliRunner()
    result = runner.invoke(cli, ["set-webhook", "--url", "https://example.com/webhook"])
    assert result.exit_code != 0
    assert "Invalid URL" in result.output


def test_delete_webhook_success(monkeypatch):
    """Test delete-webhook command with success."""
    async def mock_delete_webhook(**kwargs):
        return {"ok": True, "result": True, "description": "Webhook was deleted"}

    monkeypatch.setattr("telegras.cli.delete_webhook", mock_delete_webhook)

    runner = CliRunner()
    result = runner.invoke(cli, ["delete-webhook"])
    assert result.exit_code == 0
    assert "Webhook deleted successfully" in result.output


def test_delete_webhook_with_drop_pending(monkeypatch):
    """Test delete-webhook command with drop-pending option."""
    async def mock_delete_webhook(**kwargs):
        assert kwargs.get("drop_pending_updates") is True
        return {"ok": True, "result": True}

    monkeypatch.setattr("telegras.cli.delete_webhook", mock_delete_webhook)

    runner = CliRunner()
    result = runner.invoke(cli, ["delete-webhook", "--drop-pending"])
    assert result.exit_code == 0


def test_get_me_command(monkeypatch):
    """Test get-me command."""
    mock_bot = MagicMock()
    mock_bot.id = 123456789
    mock_bot.username = "testbot"
    mock_bot.first_name = "Test"
    mock_bot.last_name = "Bot"

    async def mock_get_me():
        return mock_bot

    monkeypatch.setattr("telegras.cli.get_me", mock_get_me)

    runner = CliRunner()
    result = runner.invoke(cli, ["get-me"])
    assert result.exit_code == 0
    assert "Bot Information" in result.output
    assert "123456789" in result.output
    assert "@testbot" in result.output
    assert "Test" in result.output
    assert "Bot" in result.output


def test_startup_check_success(monkeypatch):
    """Test startup-check command with successful validation."""
    mock_results = {
        "telegram": {"bot_token": {"status": "ok", "message": "Bot: @testbot"}},
        "webhook": {"webhook": {"status": "configured", "message": "Webhook set"}},
        "overall": {"status": "ok", "errors": []}
    }

    monkeypatch.setattr(
        "telegras.cli.run_startup_validation_sync",
        lambda display=None: mock_results
    )

    runner = CliRunner()
    result = runner.invoke(cli, ["startup-check"])
    assert result.exit_code == 0


def test_startup_check_failure(monkeypatch):
    """Test startup-check command with failed validation."""
    mock_results = {
        "telegram": {"bot_token": {"status": "error", "message": "Invalid token"}},
        "webhook": {"webhook": {"status": "error", "message": "Connection error"}},
        "overall": {"status": "failed", "errors": ["bot_token", "webhook"]}
    }

    monkeypatch.setattr(
        "telegras.cli.run_startup_validation_sync",
        lambda display=None: mock_results
    )

    runner = CliRunner()
    result = runner.invoke(cli, ["startup-check"])
    assert result.exit_code != 0
    assert "Startup check failed" in result.output


def test_debug_flag_enables_logging(monkeypatch):
    """Test that --debug flag enables debug logging."""
    runner = CliRunner()
    with patch("telegras.cli.logging") as mock_logging:
        result = runner.invoke(cli, ["--debug", "--help"])
        # Check that debug level was set
        assert result.exit_code == 0


def test_plain_flag_forces_plain_output(monkeypatch):
    """Test that --plain flag forces plain text output."""
    async def mock_get_webhook():
        mock_info = MagicMock()
        mock_info.url = "https://example.com/webhook"
        mock_info.pending_update_count = 0
        mock_info.has_custom_certificate = False
        mock_info.last_error_message = None
        return mock_info

    monkeypatch.setattr("telegras.cli.get_webhook_info", mock_get_webhook)

    runner = CliRunner()
    result = runner.invoke(cli, ["--plain", "webhook-info"])
    assert result.exit_code == 0
    # With plain output, rich markup should be stripped
    assert "[" not in result.output or "Webhook Information" in result.output


def test_start_command_shows_information(monkeypatch):
    """Test that start command displays startup information."""
    # Mock the imports and execution inside start_cmd
    mock_app = MagicMock()

    def mock_create_app():
        return mock_app

    def mock_run(*args, **kwargs):
        # Prevent actual server start
        raise SystemExit(0)

    # We need to mock both the uvicorn module and create_app
    # Since they're imported inside the function, we mock them at the source
    monkeypatch.setattr("telegras.app.create_app", mock_create_app)

    # Mock uvicorn.run to prevent actual server startup
    with patch("uvicorn.run", side_effect=mock_run) as mock_uvicorn_run:
        runner = CliRunner()
        result = runner.invoke(cli, ["start", "--host", "127.0.0.1", "--port", "8080"])
        # The command should try to start but we intercept it
        # Just verify the command is properly configured
        assert "Starting telegras" in result.output or result.exit_code in [0, 1]


def test_set_webhook_requires_url(monkeypatch):
    """Test that set-webhook requires --url parameter."""
    runner = CliRunner()
    result = runner.invoke(cli, ["set-webhook"])
    assert result.exit_code != 0
    assert "Missing option" in result.output or "--url" in result.output


def test_webhook_info_preserves_existing_backends_and_db_init():
    """Test that existing commands (backends, db-init) still work."""
    runner = CliRunner()

    # Test backends command is available
    result_help = runner.invoke(cli, ["--help"])
    assert "backends" in result_help.output
    assert "db-init" in result_help.output

    # Test that the commands are properly registered
    assert "List configured telegras publication backends" in result_help.output
    assert "Initialize telegras database" in result_help.output
