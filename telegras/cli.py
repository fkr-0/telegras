# telegras/cli.py
"""Telegras CLI - comprehensive Telegram operations."""

from __future__ import annotations

import asyncio
import logging
import click

from .telegram_api import (
    get_webhook_info,
    set_webhook,
    delete_webhook,
    get_me,
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


@click.group()
@click.option("--debug", is_flag=True, help="Enable debug logging")
@click.option("--plain", is_flag=True, help="Force plain text output")
@click.pass_context
def cli(ctx: click.Context, debug: bool, plain: bool) -> None:
    """telegras operational CLI."""
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
        log.debug("Debug mode enabled")

    display = DisplayManager(force_rich=True, force_plain=plain)
    ctx.ensure_object(dict)
    ctx.obj["debug"] = debug
    ctx.obj["plain"] = plain
    ctx.obj["display"] = display


@cli.command(name="start")
@click.option("--host", default="0.0.0.0", help="Host to bind to")
@click.option("--port", default=8000, type=int, help="Port to bind to")
@click.option("--reload", is_flag=True, help="Enable auto-reload")
@click.pass_context
def start_cmd(ctx: click.Context, host: str, port: int, reload: bool) -> None:
    """Start the telegras server."""
    import uvicorn
    from .app import create_app

    display = ctx.obj.get("display", DisplayManager())
    display.print_section("Starting telegras")
    display.print_status("", f"Listening on {host}:{port}", success=True)

    app = create_app()
    uvicorn.run(app, host=host, port=port, reload=reload)


@cli.command(name="webhook-info")
@click.option("--output-format", type=click.Choice(["json", "table"]), default="table")
@click.pass_context
def webhook_info(ctx: click.Context, output_format: str) -> None:
    """Display current Telegram webhook information."""
    display = ctx.obj.get("display", DisplayManager())

    async def _get_info():
        info = await get_webhook_info()
        if output_format == "json":
            import json
            click.echo(json.dumps(info.model_dump(), indent=2))
        else:
            display.print_section("Webhook Information")
            display.print(f"  URL: {info.url or 'Not set'}")
            display.print(f"  Pending updates: {info.pending_update_count}")
            display.print(f"  Custom certificate: {info.has_custom_certificate}")
            if info.last_error_message:
                display.print_status("", f"Last error: {info.last_error_message}", success=False)

    asyncio.run(_get_info())


@cli.command(name="set-webhook")
@click.option("--url", required=True, help="Webhook URL")
@click.option("--dry-run", is_flag=True, help="Show what would be set")
@click.pass_context
def set_webhook_cmd(ctx: click.Context, url: str, dry_run: bool) -> None:
    """Configure Telegram webhook."""
    display = ctx.obj.get("display", DisplayManager())

    if dry_run:
        display.print(f"Would set webhook to: {url}")
        return

    async def _set_webhook():
        result = await set_webhook(url=url)
        if result.get("ok"):
            display.print_status("", "Webhook configured successfully", success=True)
        else:
            display.print_status("", result.get("description", "Unknown error"), success=False)
            raise click.ClickException("Webhook configuration failed")

    asyncio.run(_set_webhook())


@cli.command(name="delete-webhook")
@click.option("--drop-pending", is_flag=True, help="Drop pending updates")
@click.pass_context
def delete_webhook_cmd(ctx: click.Context, drop_pending: bool) -> None:
    """Delete Telegram webhook."""
    display = ctx.obj.get("display", DisplayManager())

    async def _delete():
        result = await delete_webhook(drop_pending_updates=drop_pending)
        if result.get("ok"):
            display.print_status("", "Webhook deleted successfully", success=True)
        else:
            display.print_status("", result.get("description", "Unknown error"), success=False)

    asyncio.run(_delete())


@cli.command(name="get-me")
@click.pass_context
def get_me_cmd(ctx: click.Context) -> None:
    """Get bot information."""
    display = ctx.obj.get("display", DisplayManager())

    async def _get_me():
        info = await get_me()
        display.print_section("Bot Information")
        display.print(f"  ID: {info.id}")
        display.print(f"  Username: @{info.username}")
        display.print(f"  First name: {info.first_name}")
        if info.last_name:
            display.print(f"  Last name: {info.last_name}")

    asyncio.run(_get_me())


@cli.command(name="startup-check")
@click.option("--auto-fix-webhook/--no-auto-fix-webhook", default=True)
@click.pass_context
def startup_check_cmd(ctx: click.Context, auto_fix_webhook: bool) -> None:
    """Run comprehensive startup diagnostics."""
    display = ctx.obj.get("display", DisplayManager())

    results = run_startup_validation_sync(display=display)

    if results["overall"]["status"] == "failed":
        raise click.ClickException("Startup check failed")


@cli.command(name="db-init")
def db_init_cmd() -> None:
    """Initialize telegras database."""
    asyncio.run(init_db())
    click.echo("Database initialized")


@cli.command(name="backends")
def backends_cmd() -> None:
    """List configured telegras publication backends."""
    for name in parse_backend_names(None):
        click.echo(name)


if __name__ == "__main__":
    cli()
