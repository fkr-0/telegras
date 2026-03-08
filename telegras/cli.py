# telegras/cli.py
"""Telegras CLI powered by pydantic-settings subcommand parsing."""

from __future__ import annotations

import asyncio
import json
import logging
import sys
from contextlib import redirect_stderr, redirect_stdout
from io import TextIOBase
from typing import Literal, Sequence

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, CliSubCommand, SettingsConfigDict

from .telegram_api import (
    delete_webhook,
    get_me,
    get_webhook_info,
    set_webhook,
)
from .startup import run_startup_validation_sync
from .display import DisplayManager
from .persistence.db import init_db
from .backends.factory import parse_backend_names

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
log = logging.getLogger("telegras.cli")


class StartCommand(BaseModel):
    """Start the telegras server."""

    host: str = Field(default="0.0.0.0", description="Host to bind to")
    port: int = Field(default=8000, description="Port to bind to")
    reload: bool = Field(default=False, description="Enable auto-reload")


class WebhookInfoCommand(BaseModel):
    """Display current Telegram webhook information."""

    output_format: Literal["json", "table"] = Field(default="table")


class SetWebhookCommand(BaseModel):
    """Configure Telegram webhook."""

    url: str = Field(description="Webhook URL")
    dry_run: bool = Field(default=False, description="Show what would be set")


class DeleteWebhookCommand(BaseModel):
    """Delete Telegram webhook."""

    drop_pending: bool = Field(default=False, description="Drop pending updates")


class GetMeCommand(BaseModel):
    """Get bot information."""


class StartupCheckCommand(BaseModel):
    """Run comprehensive startup diagnostics."""

    auto_fix_webhook: bool = Field(default=True)


class DbInitCommand(BaseModel):
    """Initialize telegras database."""


class BackendsCommand(BaseModel):
    """List configured telegras publication backends."""


class TelegrasCliSettings(BaseSettings):
    model_config = SettingsConfigDict(
        cli_prog_name="telegras",
        cli_kebab_case=True,
        cli_implicit_flags=True,
        cli_enforce_required=True,
        cli_use_class_docs_for_groups=True,
        extra="ignore",
    )

    debug: bool = Field(default=False, description="Enable debug logging")
    plain: bool = Field(default=False, description="Force plain text output")
    start: CliSubCommand[StartCommand]
    webhook_info: CliSubCommand[WebhookInfoCommand]
    set_webhook: CliSubCommand[SetWebhookCommand]
    delete_webhook: CliSubCommand[DeleteWebhookCommand]
    get_me: CliSubCommand[GetMeCommand]
    startup_check: CliSubCommand[StartupCheckCommand]
    db_init: CliSubCommand[DbInitCommand]
    backends: CliSubCommand[BackendsCommand]


class CliError(RuntimeError):
    pass


async def _run_webhook_info(display: DisplayManager, command: WebhookInfoCommand) -> None:
    info = await get_webhook_info()
    if command.output_format == "json":
        print(json.dumps(info.model_dump(), indent=2))
        return

    display.print_section("Webhook Information")
    display.print(f"  URL: {info.url or 'Not set'}")
    display.print(f"  Pending updates: {info.pending_update_count}")
    display.print(f"  Custom certificate: {info.has_custom_certificate}")
    if info.last_error_message:
        display.print_status("", f"Last error: {info.last_error_message}", success=False)


async def _run_set_webhook(display: DisplayManager, command: SetWebhookCommand) -> None:
    if command.dry_run:
        display.print(f"Would set webhook to: {command.url}")
        return

    result = await set_webhook(url=command.url)
    if result.get("ok"):
        display.print_status("", "Webhook configured successfully", success=True)
        return
    display.print_status("", result.get("description", "Unknown error"), success=False)
    raise CliError(result.get("description", "Webhook configuration failed"))


async def _run_delete_webhook(display: DisplayManager, command: DeleteWebhookCommand) -> None:
    result = await delete_webhook(drop_pending_updates=command.drop_pending)
    if result.get("ok"):
        display.print_status("", "Webhook deleted successfully", success=True)
        return
    display.print_status("", result.get("description", "Unknown error"), success=False)
    raise CliError(result.get("description", "Webhook deletion failed"))


async def _run_get_me(display: DisplayManager) -> None:
    info = await get_me()
    display.print_section("Bot Information")
    display.print(f"  ID: {info.id}")
    display.print(f"  Username: @{info.username}")
    display.print(f"  First name: {info.first_name}")
    if info.last_name:
        display.print(f"  Last name: {info.last_name}")


def _dispatch(settings: TelegrasCliSettings, display: DisplayManager) -> int:
    if settings.start is not None:
        import uvicorn
        from .app import create_app

        display.print_section("Starting telegras")
        display.print_status("", f"Listening on {settings.start.host}:{settings.start.port}", success=True)
        app = create_app()
        uvicorn.run(app, host=settings.start.host, port=settings.start.port, reload=settings.start.reload)
        return 0

    if settings.webhook_info is not None:
        asyncio.run(_run_webhook_info(display, settings.webhook_info))
        return 0

    if settings.set_webhook is not None:
        asyncio.run(_run_set_webhook(display, settings.set_webhook))
        return 0

    if settings.delete_webhook is not None:
        asyncio.run(_run_delete_webhook(display, settings.delete_webhook))
        return 0

    if settings.get_me is not None:
        asyncio.run(_run_get_me(display))
        return 0

    if settings.startup_check is not None:
        results = run_startup_validation_sync(display=display)
        overall = results["overall"]["status"] if isinstance(results, dict) else results.overall_status
        if overall == "failed":
            raise CliError("Startup check failed")
        return 0

    if settings.db_init is not None:
        asyncio.run(init_db())
        print("Database initialized")
        return 0

    if settings.backends is not None:
        for name in parse_backend_names(None):
            print(name)
        return 0

    return 0


def cli(
    args: Sequence[str] | None = None,
    *,
    stdout: TextIOBase | None = None,
    stderr: TextIOBase | None = None,
) -> int:
    stdout = stdout or sys.stdout
    stderr = stderr or sys.stderr
    cli_args = list(args) if args is not None else sys.argv[1:]

    try:
        with redirect_stdout(stdout), redirect_stderr(stderr):
            settings = TelegrasCliSettings(_cli_parse_args=cli_args)
            if settings.debug:
                logging.getLogger().setLevel(logging.DEBUG)
                log.debug("Debug mode enabled")
            display = DisplayManager(force_rich=True, force_plain=settings.plain)
            return _dispatch(settings, display)
    except SystemExit as exc:
        code = exc.code if isinstance(exc.code, int) else 0
        return code
    except CliError as exc:
        print(str(exc), file=stderr)
        return 1


main = cli


if __name__ == "__main__":
    raise SystemExit(cli())
