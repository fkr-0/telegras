"""Telegram Bot API - Stickers Pydantic Models.

Auto-generated from API documentation.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any

# External type references (would need to be imported or defined elsewhere)
# File
# InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply
# InputFile
# InputFile or String
# Integer or String
# PhotoSize
# ReplyParameters
# SuggestedPostParameters

class setStickerEmojiList(BaseModel):
    """
    setStickerEmojiList method from Telegram Bot API.
    """

    sticker: str = Field(description="File identifier of the sticker")
    emoji_list: list[str] = Field(description="A JSON-serialized list of 1-20 emoji associated with the sticker")

class setStickerPositionInSet(BaseModel):
    """
    setStickerPositionInSet method from Telegram Bot API.
    """

    sticker: str = Field(description="File identifier of the sticker")
    position: int = Field(description="New sticker position in the set, zero-based")

class setStickerSetTitle(BaseModel):
    """
    setStickerSetTitle method from Telegram Bot API.
    """

    name: str = Field(description="Sticker set name")
    title: str = Field(description="Sticker set title, 1-64 characters")

class deleteStickerFromSet(BaseModel):
    """
    deleteStickerFromSet method from Telegram Bot API.
    """

    sticker: str = Field(description="File identifier of the sticker")

class setCustomEmojiStickerSetThumbnail(BaseModel):
    """
    setCustomEmojiStickerSetThumbnail method from Telegram Bot API.
    """

    name: str = Field(description="Sticker set name")
    custom_emoji_id: None | str = Field(description="Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail.")

class MaskPosition(BaseModel):
    """
    MaskPosition type from Telegram Bot API.
    """

    point: str = Field(description="The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.")
    x_shift: float = Field(description="Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.")
    y_shift: float = Field(description="Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.")
    scale: float = Field(description="Mask scaling coefficient. For example, 2.0 means double size.")

class getStickerSet(BaseModel):
    """
    getStickerSet method from Telegram Bot API.
    """

    name: str = Field(description="Name of the sticker set")

class getCustomEmojiStickers(BaseModel):
    """
    getCustomEmojiStickers method from Telegram Bot API.
    """

    custom_emoji_ids: list[str] = Field(description="A JSON-serialized list of custom emoji identifiers. At most 200 custom emoji identifiers can be specified.")

class setStickerSetThumbnail(BaseModel):
    """
    setStickerSetThumbnail method from Telegram Bot API.
    """

    name: str = Field(description="Sticker set name")
    user_id: int = Field(description="User identifier of the sticker set owner")
    thumbnail: None | InputFile or String = Field(description="A .WEBP or .PNG image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a .TGS animation with a thumbnail up to 32 kilobytes in size (see https://core.telegram.org/stickers#animation-requirements for animated sticker technical requirements), or a .WEBM video with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#video-requirements for video sticker technical requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files » . Animated and video sticker set thumbnails can't be uploaded via HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail.")
    format: str = Field(description="Format of the thumbnail, must be one of “static” for a .WEBP or .PNG image, “animated” for a .TGS animation, or “video” for a .WEBM video")

class deleteStickerSet(BaseModel):
    """
    deleteStickerSet method from Telegram Bot API.
    """

    name: str = Field(description="Sticker set name")

class sendSticker(BaseModel):
    """
    sendSticker method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: Integer or String = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    sticker: InputFile or String = Field(description="Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data. More information on Sending Files » . Video and animated stickers can't be sent via an HTTP URL.")
    emoji: None | str = Field(description="Emoji associated with the sticker; only for just uploaded stickers")
    disable_notification: None | bool = Field(description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: None | SuggestedPostParameters = Field(description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: None | ReplyParameters = Field(description="Description of the message to reply to")
    reply_markup: None | InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply = Field(description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")

class uploadStickerFile(BaseModel):
    """
    uploadStickerFile method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier of sticker file owner")
    sticker: InputFile = Field(description="A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format. See https://core.telegram.org/stickers for technical requirements. More information on Sending Files »")
    sticker_format: str = Field(description="Format of the sticker, must be one of “static”, “animated”, “video”")

class setStickerKeywords(BaseModel):
    """
    setStickerKeywords method from Telegram Bot API.
    """

    sticker: str = Field(description="File identifier of the sticker")
    keywords: None | list[str] = Field(description="A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters")

class setStickerMaskPosition(BaseModel):
    """
    setStickerMaskPosition method from Telegram Bot API.
    """

    sticker: str = Field(description="File identifier of the sticker")
    mask_position: None | MaskPosition = Field(description="A JSON-serialized object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position.")

class Sticker(BaseModel):
    """
    Sticker type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    type: str = Field(description="Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”. The type of the sticker is independent from its format, which is determined by the fields is_animated and is_video .")
    width: int = Field(description="Sticker width")
    height: int = Field(description="Sticker height")
    is_animated: bool = Field(description="True , if the sticker is animated")
    is_video: bool = Field(description="True , if the sticker is a video sticker")
    thumbnail: None | PhotoSize = Field(description="Optional . Sticker thumbnail in the .WEBP or .JPG format")
    emoji: None | str = Field(description="Optional . Emoji associated with the sticker")
    set_name: None | str = Field(description="Optional . Name of the sticker set to which the sticker belongs")
    premium_animation: None | File = Field(description="Optional . For premium regular stickers, premium animation for the sticker")
    mask_position: None | MaskPosition = Field(description="Optional . For mask stickers, the position where the mask should be placed")
    custom_emoji_id: None | str = Field(description="Optional . For custom emoji stickers, unique identifier of the custom emoji")
    needs_repainting: None | bool = Field(description="Optional . True , if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places")
    file_size: None | int = Field(description="Optional . File size in bytes")

class InputSticker(BaseModel):
    """
    InputSticker type from Telegram Bot API.
    """

    sticker: str = Field(description="The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new file using multipart/form-data under <file_attach_name> name. Animated and video stickers can't be uploaded via HTTP URL. More information on Sending Files »")
    format: str = Field(description="Format of the added sticker, must be one of “static” for a .WEBP or .PNG image, “animated” for a .TGS animation, “video” for a .WEBM video")
    emoji_list: list[str] = Field(description="List of 1-20 emoji associated with the sticker")
    mask_position: None | MaskPosition = Field(description="Optional . Position where the mask should be placed on faces. For “mask” stickers only.")
    keywords: None | list[str] = Field(description="Optional . List of 0-20 search keywords for the sticker with total length of up to 64 characters. For “regular” and “custom_emoji” stickers only.")

class StickerSet(BaseModel):
    """
    StickerSet type from Telegram Bot API.
    """

    name: str = Field(description="Sticker set name")
    title: str = Field(description="Sticker set title")
    sticker_type: str = Field(description="Type of stickers in the set, currently one of “regular”, “mask”, “custom_emoji”")
    stickers: list[Sticker] = Field(description="List of all set stickers")
    thumbnail: None | PhotoSize = Field(description="Optional . Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format")

class addStickerToSet(BaseModel):
    """
    addStickerToSet method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier of sticker set owner")
    name: str = Field(description="Sticker set name")
    sticker: InputSticker = Field(description="A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set isn't changed.")

class replaceStickerInSet(BaseModel):
    """
    replaceStickerInSet method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier of the sticker set owner")
    name: str = Field(description="Sticker set name")
    old_sticker: str = Field(description="File identifier of the replaced sticker")
    sticker: InputSticker = Field(description="A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged.")

class createNewStickerSet(BaseModel):
    """
    createNewStickerSet method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier of created sticker set owner")
    name: str = Field(description="Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals ). Can contain only English letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in \"_by_<bot_username>\" . <bot_username> is case insensitive. 1-64 characters.")
    title: str = Field(description="Sticker set title, 1-64 characters")
    stickers: list[InputSticker] = Field(description="A JSON-serialized list of 1-50 initial stickers to be added to the sticker set")
    sticker_type: None | str = Field(description="Type of stickers in the set, pass “regular”, “mask”, or “custom_emoji”. By default, a regular sticker set is created.")
    needs_repainting: None | bool = Field(description="Pass True if stickers in the sticker set must be repainted to the color of text when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context; for custom emoji sticker sets only")

