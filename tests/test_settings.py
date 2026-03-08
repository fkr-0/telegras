"""Tests for the new pydantic-settings based configuration."""

import os
import tempfile
from pathlib import Path

import pytest

from telegras.settings import AppSettings


def test_settings_default_values() -> None:
    """Test that default values are correctly set."""
    settings = AppSettings()
    
    assert settings.mode == "webhook"
    assert settings.bot_mode == "webhook"  # Test the property
    assert settings.polling_timeout_seconds == 30
    assert settings.polling_error_backoff_seconds == 2.0
    assert settings.polling_idle_sleep_seconds == 0.25


def test_settings_from_env() -> None:
    """Test that settings are loaded from environment variables."""
    with tempfile.TemporaryDirectory() as tmpdir:
        env_file = Path(tmpdir) / ".env"
        env_file.write_text("""
BOT_MODE=polling
BOT_POLLING_TIMEOUT_SECONDS=60
BOT_POLLING_ERROR_BACKOFF_SECONDS=5.0
BOT_POLLING_IDLE_SLEEP_SECONDS=0.5
""")
        
        settings = AppSettings(_env_file=str(env_file))
        
        assert settings.mode == "polling"
        assert settings.bot_mode == "polling"  # Test the property
        assert settings.polling_timeout_seconds == 60
        assert settings.polling_error_backoff_seconds == 5.0
        assert settings.polling_idle_sleep_seconds == 0.5


def test_settings_env_override() -> None:
    """Test that environment variables override .env file values."""
    os.environ["BOT_MODE"] = "webhook"
    os.environ["BOT_POLLING_TIMEOUT_SECONDS"] = "45"
    
    try:
        settings = AppSettings()
        
        assert settings.mode == "webhook"
        assert settings.polling_timeout_seconds == 45
    finally:
        # Clean up
        del os.environ["BOT_MODE"]
        del os.environ["BOT_POLLING_TIMEOUT_SECONDS"]


def test_settings_validation() -> None:
    """Test that invalid values raise validation errors."""
    with pytest.raises(ValueError, match="Input should be 'webhook' or 'polling'"):
        AppSettings(_env_file=None, mode="invalid")
    
    with pytest.raises(ValueError, match="Input should be greater than or equal to 0"):
        AppSettings(_env_file=None, polling_timeout_seconds=-1)
    
    with pytest.raises(ValueError, match="Input should be greater than or equal to 0"):
        AppSettings(_env_file=None, polling_error_backoff_seconds=-1.0)
    
    with pytest.raises(ValueError, match="Input should be greater than or equal to 0"):
        AppSettings(_env_file=None, polling_idle_sleep_seconds=-1.0)


def test_settings_case_insensitive() -> None:
    """Test that environment variable names are case insensitive."""
    os.environ["bot_mode"] = "polling"
    
    try:
        settings = AppSettings()
        assert settings.bot_mode == "polling"
    finally:
        del os.environ["bot_mode"]


def test_settings_singleton() -> None:
    """Test that the settings singleton works as expected."""
    # Import the settings instance from the module
    from telegras.settings import settings
    
    # Should be an instance of AppSettings
    assert type(settings).__name__ == "AppSettings"
    
    # Default values should be present
    assert settings.bot_mode == "webhook"
    assert settings.polling_timeout_seconds == 30


def test_settings_bot_mode_property() -> None:
    """Test the bot_mode property provides backward compatibility."""
    settings = AppSettings(mode="polling")
    
    # Both should return the same value
    assert settings.bot_mode == settings.mode
    
    # Changing mode should change bot_mode
    settings.mode = "webhook"
    assert settings.bot_mode == "webhook"