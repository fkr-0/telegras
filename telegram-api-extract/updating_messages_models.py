"""Telegram Bot API - Updating Messages Pydantic Models.

Auto-generated from API documentation.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any

# External type references (would need to be imported or defined elsewhere)
# InlineKeyboardMarkup
# InputChecklist
# InputMedia
# Integer or String
# LinkPreviewOptions
# MessageEntity

class stopMessageLiveLocation(BaseModel):
    """
    stopMessageLiveLocation method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(description="Required if inline_message_id is not specified. Identifier of the message with live location to stop")
    inline_message_id: None | str = Field(description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    reply_markup: None | InlineKeyboardMarkup = Field(description="A JSON-serialized object for a new inline keyboard .")

class editMessageReplyMarkup(BaseModel):
    """
    editMessageReplyMarkup method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(description="Required if inline_message_id is not specified. Identifier of the message to edit")
    inline_message_id: None | str = Field(description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    reply_markup: None | InlineKeyboardMarkup = Field(description="A JSON-serialized object for an inline keyboard .")

class stopPoll(BaseModel):
    """
    stopPoll method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: Integer or String = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: int = Field(description="Identifier of the original message with the poll")
    reply_markup: None | InlineKeyboardMarkup = Field(description="A JSON-serialized object for a new message inline keyboard .")

class editMessageCaption(BaseModel):
    """
    editMessageCaption method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(description="Required if inline_message_id is not specified. Identifier of the message to edit")
    inline_message_id: None | str = Field(description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    caption: None | str = Field(description="New caption of the message, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(description="Mode for parsing entities in the message caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(description="Pass True , if the caption must be shown above the message media. Supported only for animation, photo and video messages.")
    reply_markup: None | InlineKeyboardMarkup = Field(description="A JSON-serialized object for an inline keyboard .")

class approveSuggestedPost(BaseModel):
    """
    approveSuggestedPost method from Telegram Bot API.
    """

    chat_id: int = Field(description="Unique identifier for the target direct messages chat")
    message_id: int = Field(description="Identifier of a suggested post message to approve")
    send_date: None | int = Field(description="Point in time (Unix timestamp) when the post is expected to be published; omit if the date has already been specified when the suggested post was created. If specified, then the date must be not more than 2678400 seconds (30 days) in the future")

class editMessageText(BaseModel):
    """
    editMessageText method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(description="Required if inline_message_id is not specified. Identifier of the message to edit")
    inline_message_id: None | str = Field(description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    text: str = Field(description="New text of the message, 1-4096 characters after entities parsing")
    parse_mode: None | str = Field(description="Mode for parsing entities in the message text. See formatting options for more details.")
    entities: None | list[MessageEntity] = Field(description="A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode")
    link_preview_options: None | LinkPreviewOptions = Field(description="Link preview generation options for the message")
    reply_markup: None | InlineKeyboardMarkup = Field(description="A JSON-serialized object for an inline keyboard .")

class declineSuggestedPost(BaseModel):
    """
    declineSuggestedPost method from Telegram Bot API.
    """

    chat_id: int = Field(description="Unique identifier for the target direct messages chat")
    message_id: int = Field(description="Identifier of a suggested post message to decline")
    comment: None | str = Field(description="Comment for the creator of the suggested post; 0-128 characters")

class deleteMessage(BaseModel):
    """
    deleteMessage method from Telegram Bot API.
    """

    chat_id: Integer or String = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: int = Field(description="Identifier of the message to delete")

class editMessageMedia(BaseModel):
    """
    editMessageMedia method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(description="Required if inline_message_id is not specified. Identifier of the message to edit")
    inline_message_id: None | str = Field(description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    media: InputMedia = Field(description="A JSON-serialized object for a new media content of the message")
    reply_markup: None | InlineKeyboardMarkup = Field(description="A JSON-serialized object for a new inline keyboard .")

class editMessageChecklist(BaseModel):
    """
    editMessageChecklist method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int = Field(description="Unique identifier for the target chat")
    message_id: int = Field(description="Unique identifier for the target message")
    checklist: InputChecklist = Field(description="A JSON-serialized object for the new checklist")
    reply_markup: None | InlineKeyboardMarkup = Field(description="A JSON-serialized object for the new inline keyboard for the message")

class editMessageLiveLocation(BaseModel):
    """
    editMessageLiveLocation method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(description="Required if inline_message_id is not specified. Identifier of the message to edit")
    inline_message_id: None | str = Field(description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    latitude: float = Field(description="Latitude of new location")
    longitude: float = Field(description="Longitude of new location")
    live_period: None | int = Field(description="New period in seconds during which the location can be updated, starting from the message send date. If 0x7FFFFFFF is specified, then the location can be updated forever. Otherwise, the new value must not exceed the current live_period by more than a day, and the live location expiration date must remain within the next 90 days. If not specified, then live_period remains unchanged")
    horizontal_accuracy: None | float = Field(description="The radius of uncertainty for the location, measured in meters; 0-1500")
    heading: None | int = Field(description="Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.")
    proximity_alert_radius: None | int = Field(description="The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.")
    reply_markup: None | InlineKeyboardMarkup = Field(description="A JSON-serialized object for a new inline keyboard .")

class deleteMessages(BaseModel):
    """
    deleteMessages method from Telegram Bot API.
    """

    chat_id: Integer or String = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_ids: list[int] = Field(description="A JSON-serialized list of 1-100 identifiers of messages to delete. See deleteMessage for limitations on which messages can be deleted")

