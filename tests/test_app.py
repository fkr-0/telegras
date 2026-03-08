import pytest
from fastapi import FastAPI
from telegras.app import create_app


def test_create_app_standalone():
    """Test creating a standalone app."""
    app = create_app()
    assert isinstance(app, FastAPI)
    assert app.title == "telegras"


def test_create_app_mount_on_existing():
    """Test mounting routes on existing app."""
    existing_app = FastAPI(title="Existing App")
    app = create_app(app=existing_app)
    # Should be the same app instance
    assert app is existing_app
    # Should have telegras routes registered
    routes = [r.path for r in app.routes]
    assert "/healthz" in routes
