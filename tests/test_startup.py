# tests/test_startup.py
"""Tests for startup validation module."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from telegras.startup import validate_telegram_config, validate_webhook_config, run_startup_validation_sync


@pytest.mark.asyncio
async def test_validate_telegram_config_success() -> None:
    """Test Telegram configuration validation with successful response."""
    # Mock get_me response matching GetMeResponse structure
    from telegras.api.methods import GetMeResponse, TelegramUser

    async def mock_get_me():
        return GetMeResponse(
            ok=True,
            result=TelegramUser(
                id=123,
                is_bot=True,
                first_name="Test",
                username="test_bot"
            )
        )

    with patch("telegras.startup.get_me", mock_get_me):
        result = await validate_telegram_config()

    assert result["bot_token"]["status"] == "ok"
    assert "test_bot" in result["bot_token"]["message"]
    assert result["bot_token"]["bot_id"] == 123
    assert result["bot_token"]["username"] == "test_bot"


@pytest.mark.asyncio
async def test_validate_telegram_config_error() -> None:
    """Test Telegram configuration validation with error."""
    # Mock get_me to raise an exception
    async def mock_get_me():
        raise Exception("Invalid bot token")

    with patch("telegras.startup.get_me", mock_get_me):
        result = await validate_telegram_config()

    assert result["bot_token"]["status"] == "error"
    assert "Invalid bot token" in result["bot_token"]["message"]


@pytest.mark.asyncio
async def test_validate_webhook_config_configured() -> None:
    """Test webhook validation when webhook is configured."""
    # Mock get_webhook_info response matching WebhookInfo structure
    from telegras.api.getting_updates import WebhookInfo

    async def mock_get_webhook_info():
        return WebhookInfo(
            url="https://example.com/webhook",
            pending_update_count=5
        )

    with patch("telegras.startup.get_webhook_info", mock_get_webhook_info):
        result = await validate_webhook_config()

    assert result["webhook"]["status"] == "configured"
    assert "https://example.com/webhook" in result["webhook"]["message"]
    assert result["webhook"]["url"] == "https://example.com/webhook"
    assert result["webhook"]["pending_updates"] == 5


@pytest.mark.asyncio
async def test_validate_webhook_config_not_configured() -> None:
    """Test webhook validation when webhook is not configured."""
    # Mock get_webhook_info response with empty URL (default value)
    from telegras.api.getting_updates import WebhookInfo

    async def mock_get_webhook_info():
        return WebhookInfo()  # url defaults to ""

    with patch("telegras.startup.get_webhook_info", mock_get_webhook_info):
        result = await validate_webhook_config()

    assert result["webhook"]["status"] == "not_configured"
    assert result["webhook"]["message"] == "No webhook configured"


@pytest.mark.asyncio
async def test_validate_webhook_config_error() -> None:
    """Test webhook validation with error."""
    # Mock get_webhook_info to raise an exception
    async def mock_get_webhook_info():
        raise Exception("Network error")

    with patch("telegras.startup.get_webhook_info", mock_get_webhook_info):
        result = await validate_webhook_config()

    assert result["webhook"]["status"] == "error"
    assert "Network error" in result["webhook"]["message"]


def test_run_startup_validation_sync_success() -> None:
    """Test complete startup validation run with all checks passing."""
    # Mock the async functions matching actual API structures
    from telegras.api.methods import GetMeResponse, TelegramUser
    from telegras.api.getting_updates import WebhookInfo

    async def mock_get_me():
        return GetMeResponse(
            ok=True,
            result=TelegramUser(
                id=123,
                is_bot=True,
                first_name="Test",
                username="test_bot"
            )
        )

    async def mock_get_webhook_info():
        return WebhookInfo(
            url="https://example.com/webhook",
            pending_update_count=0
        )

    with patch("telegras.startup.get_me", mock_get_me):
        with patch("telegras.startup.get_webhook_info", mock_get_webhook_info):
            result = run_startup_validation_sync()

    assert result["overall"]["status"] == "ok"
    assert result["overall"]["errors"] == []
    assert result["telegram"]["bot_token"]["status"] == "ok"
    assert result["webhook"]["webhook"]["status"] == "configured"


def test_run_startup_validation_sync_with_display() -> None:
    """Test startup validation with custom DisplayManager."""
    # Mock the async functions matching actual API structures
    from telegras.api.methods import GetMeResponse, TelegramUser
    from telegras.api.getting_updates import WebhookInfo

    async def mock_get_me():
        return GetMeResponse(
            ok=True,
            result=TelegramUser(
                id=456,
                is_bot=True,
                first_name="Custom",
                username="custom_bot"
            )
        )

    async def mock_get_webhook_info():
        return WebhookInfo(
            url="https://custom.example.com/webhook",
            pending_update_count=2
        )

    from telegras.display import DisplayManager
    display = DisplayManager(force_plain=True)

    with patch("telegras.startup.get_me", mock_get_me):
        with patch("telegras.startup.get_webhook_info", mock_get_webhook_info):
            result = run_startup_validation_sync(display=display)

    assert result["overall"]["status"] == "ok"
    assert result["telegram"]["bot_token"]["username"] == "custom_bot"
    assert result["webhook"]["webhook"]["pending_updates"] == 2


def test_run_startup_validation_sync_failure() -> None:
    """Test startup validation with failures."""
    # Mock the async functions to fail
    from telegras.api.getting_updates import WebhookInfo

    async def mock_get_me():
        raise Exception("Token invalid")

    async def mock_get_webhook_info():
        return WebhookInfo()  # url defaults to ""

    with patch("telegras.startup.get_me", mock_get_me):
        with patch("telegras.startup.get_webhook_info", mock_get_webhook_info):
            result = run_startup_validation_sync()

    assert result["overall"]["status"] == "failed"
    assert "bot_token" in result["overall"]["errors"]
    assert "webhook_not_set" in result["overall"]["errors"]
