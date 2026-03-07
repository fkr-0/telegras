"""Telegram Bot API - Type-safe Python models.

Restructured to avoid circular imports.
"""

__version__ = "1.0.0"

# Import all modules
from . import core, types, methods
from .features import updates, stickers, inline_mode, payments, passport, games

# Convenience imports
from .core import User, Chat, Message
from .types import Update, BotCommand
from .methods import getMe, sendMessage
from .features.updates import Update as UpdatesUpdate
