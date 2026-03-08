"""Standalone entry point for running telegras server."""

import uvicorn
from .app import create_app


def main():
    """Start the telegras server."""
    app = create_app()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=False,
    )


if __name__ == "__main__":
    main()
