# Telegram Bot API - Type-Safe Python Models

Auto-generated Pydantic v2 models for the Telegram Bot API.

## Installation

```bash
pip install pydantic>=2.0
```

## Usage

```python
from telegram_api.types import User, Chat, Message
from telegram_api.methods import sendMessage, getMe

# Create type-safe models
user = User(
    id=123456789,
    is_bot=False,
    first_name="John",
    username="john_doe"
)

# Method parameters
params = sendMessage(
    chat_id=123456789,
    text="Hello, World!"
)

# JSON serialization
print(params.model_dump_json(indent=2))
```

## Modules

- **types** - Core data types (User, Chat, Message, etc.)
- **methods** - API methods (getMe, sendMessage, etc.)
- **getting_updates** - Webhooks and long polling
- **updating_messages** - Message editing
- **stickers** - Sticker types and methods
- **inline_mode** - Inline queries
- **payments** - Payment types
- **passport** - Telegram Passport
- **games** - Game types

## Features

- Full Pydantic v2 type annotations
- Field descriptions from Telegram API docs
- Proper optional/required field handling
- JSON serialization/deserialization
- IDE autocomplete support
