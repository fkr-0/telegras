from __future__ import annotations

import os
from pathlib import Path
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from telegras.persistence.models import Base

DEFAULT_DATABASE_URL = "sqlite+aiosqlite:///./data/telegras.db"


def _current_database_url() -> str:
    return os.getenv("TELEGRAS_DATABASE_URL", DEFAULT_DATABASE_URL)


def _new_engine(database_url: str):
    if database_url.startswith("sqlite+aiosqlite:///"):
        db_path = database_url.replace("sqlite+aiosqlite:///", "", 1)
        parent = Path(db_path).expanduser().resolve().parent
        parent.mkdir(parents=True, exist_ok=True)
    return create_async_engine(database_url, future=True, pool_pre_ping=True)


engine = _new_engine(_current_database_url())
SessionLocal = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
_engine_url = str(engine.url)


def _ensure_engine_matches_env() -> None:
    global engine, SessionLocal, _engine_url
    target_url = _current_database_url()
    if target_url == _engine_url:
        return
    engine = _new_engine(target_url)
    SessionLocal = async_sessionmaker(
        bind=engine, autoflush=False, expire_on_commit=False
    )
    _engine_url = target_url


async def init_db() -> None:
    _ensure_engine_matches_env()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
