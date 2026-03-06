from __future__ import annotations

import asyncio

import click

from telegras.backends.factory import parse_backend_names
from telegras.persistence.db import init_db


@click.group()
def cli() -> None:
    """telegras operational CLI."""


@cli.command(name="db-init")
def db_init_cmd() -> None:
    """Initialize telegras persistence tables."""

    asyncio.run(init_db())
    click.echo("telegras database initialized")


@cli.command(name="backends")
def backends_cmd() -> None:
    """List configured telegras publication backends."""

    for name in parse_backend_names(None):
        click.echo(name)


if __name__ == "__main__":
    cli()
