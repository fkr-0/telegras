from __future__ import annotations

from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Runtime settings sourced from environment variables."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="BOT_",
        case_sensitive=False,
        extra="ignore",
    )
    
    mode: Literal["webhook", "polling"] = Field(
        default="webhook",
        description="How telegras receives Telegram updates"
    )
    
    polling_timeout_seconds: int = Field(
        default=30,
        ge=0,
        description="Timeout for Telegram polling in seconds"
    )
    
    polling_error_backoff_seconds: float = Field(
        default=2.0,
        ge=0.0,
        description="Backoff delay when polling errors occur"
    )
    
    polling_idle_sleep_seconds: float = Field(
        default=0.25,
        ge=0.0,
        description="Sleep duration when no updates are available during polling"
    )
    
    @property
    def bot_mode(self) -> Literal["webhook", "polling"]:
        """Alias for mode to maintain backward compatibility."""
        return self.mode
    
    @field_validator("mode")
    @classmethod
    def validate_bot_mode(cls, v: str) -> str:
        """Validate bot mode is one of the allowed values."""
        if v not in ("webhook", "polling"):
            raise ValueError(f"BOT_MODE must be either 'webhook' or 'polling', got '{v}'")
        return v


# Create a singleton instance for easy access
settings = AppSettings()
