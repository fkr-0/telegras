"""Telegram Bot API - Games Pydantic Models.

Auto-generated from API documentation.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any

# External type references (would need to be imported or defined elsewhere)
# Animation
# InlineKeyboardMarkup
# MessageEntity
# PhotoSize
# ReplyParameters
# User

class getGameHighScores(BaseModel):
    """
    getGameHighScores method from Telegram Bot API.
    """

    user_id: int = Field(description="Target user id")
    chat_id: None | int = Field(description="Required if inline_message_id is not specified. Unique identifier for the target chat")
    message_id: None | int = Field(description="Required if inline_message_id is not specified. Identifier of the sent message")
    inline_message_id: None | str = Field(description="Required if chat_id and message_id are not specified. Identifier of the inline message")

class Game(BaseModel):
    """
    Game type from Telegram Bot API.
    """

    title: str = Field(description="Title of the game")
    description: str = Field(description="Description of the game")
    photo: list[PhotoSize] = Field(description="Photo that will be displayed in the game message in chats.")
    text: None | str = Field(description="Optional . Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore , or manually edited using editMessageText . 0-4096 characters.")
    text_entities: None | list[MessageEntity] = Field(description="Optional . Special entities that appear in text , such as usernames, URLs, bot commands, etc.")
    animation: None | Animation = Field(description="Optional . Animation that will be displayed in the game message in chats. Upload via BotFather")

class GameHighScore(BaseModel):
    """
    GameHighScore type from Telegram Bot API.
    """

    position: int = Field(description="Position in high score table for the game")
    user: User = Field(description="User")
    score: int = Field(description="Score")

class CallbackGame(BaseModel):
    """
    CallbackGame method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier")
    score: int = Field(description="New score, must be non-negative")
    force: None | bool = Field(description="Pass True if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters")
    disable_edit_message: None | bool = Field(description="Pass True if the game message should not be automatically edited to include the current scoreboard")
    chat_id: None | int = Field(description="Required if inline_message_id is not specified. Unique identifier for the target chat")
    message_id: None | int = Field(description="Required if inline_message_id is not specified. Identifier of the sent message")
    inline_message_id: None | str = Field(description="Required if chat_id and message_id are not specified. Identifier of the inline message")

class setGameScore(BaseModel):
    """
    setGameScore method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier")
    score: int = Field(description="New score, must be non-negative")
    force: None | bool = Field(description="Pass True if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters")
    disable_edit_message: None | bool = Field(description="Pass True if the game message should not be automatically edited to include the current scoreboard")
    chat_id: None | int = Field(description="Required if inline_message_id is not specified. Unique identifier for the target chat")
    message_id: None | int = Field(description="Required if inline_message_id is not specified. Identifier of the sent message")
    inline_message_id: None | str = Field(description="Required if chat_id and message_id are not specified. Identifier of the inline message")

class sendGame(BaseModel):
    """
    sendGame method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int = Field(description="Unique identifier for the target chat. Games can't be sent to channel direct messages chats and channel chats.")
    message_thread_id: None | int = Field(description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    game_short_name: str = Field(description="Short name of the game, serves as the unique identifier for the game. Set up your games via @BotFather .")
    disable_notification: None | bool = Field(description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(description="Unique identifier of the message effect to be added to the message; for private chats only")
    reply_parameters: None | ReplyParameters = Field(description="Description of the message to reply to")
    reply_markup: None | InlineKeyboardMarkup = Field(description="A JSON-serialized object for an inline keyboard . If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game.")

