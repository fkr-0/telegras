"""Telegram Bot API - Type-safe Python models.

Auto-generated from Telegram Bot API documentation.
"""

__version__ = "1.0.0"

# Import all modules - they have no cross-imports
from . import types, methods, getting_updates, updating_messages
from . import stickers, inline_mode, payments, passport, games

# Common imports for convenience
from .types import User, Chat, Message
from .methods import getMe, sendMessage
from .getting_updates import Update as UpdatesUpdate

__all__ = [
    "User", "Chat", "Message",
    "getMe", "sendMessage",
    "UpdatesUpdate",
    "types", "methods", "getting_updates", "updating_messages",
    "stickers", "inline_mode", "payments", "passport", "games",
]
