from __future__ import annotations

"""Telegram Bot API - Inline Mode."""

from pydantic import BaseModel, Field
from ..core import User, Chat, Message
from ..types import Update

class ChosenInlineResult(BaseModel):
    """
    ChosenInlineResult type from Telegram Bot API.
    """

    result_id: str = Field(description="The unique identifier for the result that was chosen")
    from_: User = Field(description="The user that chose the result")
    location: None | Location = Field(default=None, description="Optional . Sender location, only for bots that require user location")
    inline_message_id: None | str = Field(default=None, description="Optional . Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.")
    query: str = Field(description="The query that was used to obtain the result")
class InlineQuery(BaseModel):
    """
    InlineQuery type from Telegram Bot API.
    """

    id: str = Field(description="Unique identifier for this query")
    from_: User = Field(description="Sender")
    query: str = Field(description="Text of the query (up to 256 characters)")
    offset: str = Field(description="Offset of the results to be returned, can be controlled by the bot")
    chat_type: None | str = Field(default=None, description="Optional . Type of the chat from which the inline query was sent. Can be either “sender” for a private chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat")
    location: None | Location = Field(default=None, description="Optional . Sender location, only for bots that request user location")
class InlineQueryResult(BaseModel):
    """
    InlineQueryResult type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be article")
    id: str = Field(description="Unique identifier for this result, 1-64 Bytes")
    title: str = Field(description="Title of the result")
    input_message_content: InputMessageContent = Field(description="Content of the message to be sent")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    url: None | str = Field(default=None, description="Optional . URL of the result")
    description: None | str = Field(default=None, description="Optional . Short description of the result")
    thumbnail_url: None | str = Field(default=None, description="Optional . Url of the thumbnail for the result")
    thumbnail_width: None | int = Field(default=None, description="Optional . Thumbnail width")
    thumbnail_height: None | int = Field(default=None, description="Optional . Thumbnail height")
class InlineQueryResultArticle(BaseModel):
    """
    InlineQueryResultArticle type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be article")
    id: str = Field(description="Unique identifier for this result, 1-64 Bytes")
    title: str = Field(description="Title of the result")
    input_message_content: InputMessageContent = Field(description="Content of the message to be sent")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    url: None | str = Field(default=None, description="Optional . URL of the result")
    description: None | str = Field(default=None, description="Optional . Short description of the result")
    thumbnail_url: None | str = Field(default=None, description="Optional . Url of the thumbnail for the result")
    thumbnail_width: None | int = Field(default=None, description="Optional . Thumbnail width")
    thumbnail_height: None | int = Field(default=None, description="Optional . Thumbnail height")
class InlineQueryResultAudio(BaseModel):
    """
    InlineQueryResultAudio type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be audio")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    audio_url: str = Field(description="A valid URL for the audio file")
    title: str = Field(description="Title")
    caption: None | str = Field(default=None, description="Optional . Caption, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the audio caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    performer: None | str = Field(default=None, description="Optional . Performer")
    audio_duration: None | int = Field(default=None, description="Optional . Audio duration in seconds")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the audio")
class InlineQueryResultCachedAudio(BaseModel):
    """
    InlineQueryResultCachedAudio type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be audio")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    audio_file_id: str = Field(description="A valid file identifier for the audio file")
    caption: None | str = Field(default=None, description="Optional . Caption, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the audio caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the audio")
class InlineQueryResultCachedDocument(BaseModel):
    """
    InlineQueryResultCachedDocument type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be document")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    title: str = Field(description="Title for the result")
    document_file_id: str = Field(description="A valid file identifier for the file")
    description: None | str = Field(default=None, description="Optional . Short description of the result")
    caption: None | str = Field(default=None, description="Optional . Caption of the document to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the document caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the file")
class InlineQueryResultCachedGif(BaseModel):
    """
    InlineQueryResultCachedGif type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be gif")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    gif_file_id: str = Field(description="A valid file identifier for the GIF file")
    title: None | str = Field(default=None, description="Optional . Title for the result")
    caption: None | str = Field(default=None, description="Optional . Caption of the GIF file to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the GIF animation")
class InlineQueryResultCachedMpeg4Gif(BaseModel):
    """
    InlineQueryResultCachedMpeg4Gif type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be mpeg4_gif")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    mpeg4_file_id: str = Field(description="A valid file identifier for the MPEG4 file")
    title: None | str = Field(default=None, description="Optional . Title for the result")
    caption: None | str = Field(default=None, description="Optional . Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the video animation")
class InlineQueryResultCachedPhoto(BaseModel):
    """
    InlineQueryResultCachedPhoto type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be photo")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    photo_file_id: str = Field(description="A valid file identifier of the photo")
    title: None | str = Field(default=None, description="Optional . Title for the result")
    description: None | str = Field(default=None, description="Optional . Short description of the result")
    caption: None | str = Field(default=None, description="Optional . Caption of the photo to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the photo caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the photo")
class InlineQueryResultCachedSticker(BaseModel):
    """
    InlineQueryResultCachedSticker type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be sticker")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    sticker_file_id: str = Field(description="A valid file identifier of the sticker")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the sticker")
class InlineQueryResultCachedVideo(BaseModel):
    """
    InlineQueryResultCachedVideo type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be video")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    video_file_id: str = Field(description="A valid file identifier for the video file")
    title: str = Field(description="Title for the result")
    description: None | str = Field(default=None, description="Optional . Short description of the result")
    caption: None | str = Field(default=None, description="Optional . Caption of the video to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the video caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the video")
class InlineQueryResultCachedVoice(BaseModel):
    """
    InlineQueryResultCachedVoice type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be voice")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    voice_file_id: str = Field(description="A valid file identifier for the voice message")
    title: str = Field(description="Voice message title")
    caption: None | str = Field(default=None, description="Optional . Caption, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the voice message caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the voice message")
class InlineQueryResultContact(BaseModel):
    """
    InlineQueryResultContact type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be contact")
    id: str = Field(description="Unique identifier for this result, 1-64 Bytes")
    phone_number: str = Field(description="Contact's phone number")
    first_name: str = Field(description="Contact's first name")
    last_name: None | str = Field(default=None, description="Optional . Contact's last name")
    vcard: None | str = Field(default=None, description="Optional . Additional data about the contact in the form of a vCard , 0-2048 bytes")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the contact")
    thumbnail_url: None | str = Field(default=None, description="Optional . Url of the thumbnail for the result")
    thumbnail_width: None | int = Field(default=None, description="Optional . Thumbnail width")
    thumbnail_height: None | int = Field(default=None, description="Optional . Thumbnail height")
class InlineQueryResultDocument(BaseModel):
    """
    InlineQueryResultDocument type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be document")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    title: str = Field(description="Title for the result")
    caption: None | str = Field(default=None, description="Optional . Caption of the document to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the document caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    document_url: str = Field(description="A valid URL for the file")
    mime_type: str = Field(description="MIME type of the content of the file, either “application/pdf” or “application/zip”")
    description: None | str = Field(default=None, description="Optional . Short description of the result")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the file")
    thumbnail_url: None | str = Field(default=None, description="Optional . URL of the thumbnail (JPEG only) for the file")
    thumbnail_width: None | int = Field(default=None, description="Optional . Thumbnail width")
    thumbnail_height: None | int = Field(default=None, description="Optional . Thumbnail height")
class InlineQueryResultGame(BaseModel):
    """
    InlineQueryResultGame type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be game")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    game_short_name: str = Field(description="Short name of the game")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
class InlineQueryResultGif(BaseModel):
    """
    InlineQueryResultGif type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be gif")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    gif_url: str = Field(description="A valid URL for the GIF file")
    gif_width: None | int = Field(default=None, description="Optional . Width of the GIF")
    gif_height: None | int = Field(default=None, description="Optional . Height of the GIF")
    gif_duration: None | int = Field(default=None, description="Optional . Duration of the GIF in seconds")
    thumbnail_url: str = Field(description="URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result")
    thumbnail_mime_type: None | str = Field(default=None, description="Optional . MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”")
    title: None | str = Field(default=None, description="Optional . Title for the result")
    caption: None | str = Field(default=None, description="Optional . Caption of the GIF file to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the GIF animation")
class InlineQueryResultLocation(BaseModel):
    """
    InlineQueryResultLocation type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be location")
    id: str = Field(description="Unique identifier for this result, 1-64 Bytes")
    latitude: float = Field(description="Location latitude in degrees")
    longitude: float = Field(description="Location longitude in degrees")
    title: str = Field(description="Location title")
    horizontal_accuracy: None | float = Field(default=None, description="Optional . The radius of uncertainty for the location, measured in meters; 0-1500")
    live_period: None | int = Field(default=None, description="Optional . Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.")
    heading: None | int = Field(default=None, description="Optional . For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.")
    proximity_alert_radius: None | int = Field(default=None, description="Optional . For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the location")
    thumbnail_url: None | str = Field(default=None, description="Optional . Url of the thumbnail for the result")
    thumbnail_width: None | int = Field(default=None, description="Optional . Thumbnail width")
    thumbnail_height: None | int = Field(default=None, description="Optional . Thumbnail height")
class InlineQueryResultMpeg4Gif(BaseModel):
    """
    InlineQueryResultMpeg4Gif type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be mpeg4_gif")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    mpeg4_url: str = Field(description="A valid URL for the MPEG4 file")
    mpeg4_width: None | int = Field(default=None, description="Optional . Video width")
    mpeg4_height: None | int = Field(default=None, description="Optional . Video height")
    mpeg4_duration: None | int = Field(default=None, description="Optional . Video duration in seconds")
    thumbnail_url: str = Field(description="URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result")
    thumbnail_mime_type: None | str = Field(default=None, description="Optional . MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”")
    title: None | str = Field(default=None, description="Optional . Title for the result")
    caption: None | str = Field(default=None, description="Optional . Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the video animation")
class InlineQueryResultPhoto(BaseModel):
    """
    InlineQueryResultPhoto type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be photo")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    photo_url: str = Field(description="A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB")
    thumbnail_url: str = Field(description="URL of the thumbnail for the photo")
    photo_width: None | int = Field(default=None, description="Optional . Width of the photo")
    photo_height: None | int = Field(default=None, description="Optional . Height of the photo")
    title: None | str = Field(default=None, description="Optional . Title for the result")
    description: None | str = Field(default=None, description="Optional . Short description of the result")
    caption: None | str = Field(default=None, description="Optional . Caption of the photo to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the photo caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the photo")
class InlineQueryResultVenue(BaseModel):
    """
    InlineQueryResultVenue type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be venue")
    id: str = Field(description="Unique identifier for this result, 1-64 Bytes")
    latitude: float = Field(description="Latitude of the venue location in degrees")
    longitude: float = Field(description="Longitude of the venue location in degrees")
    title: str = Field(description="Title of the venue")
    address: str = Field(description="Address of the venue")
    foursquare_id: None | str = Field(default=None, description="Optional . Foursquare identifier of the venue if known")
    foursquare_type: None | str = Field(default=None, description="Optional . Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)")
    google_place_id: None | str = Field(default=None, description="Optional . Google Places identifier of the venue")
    google_place_type: None | str = Field(default=None, description="Optional . Google Places type of the venue. (See supported types .)")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the venue")
    thumbnail_url: None | str = Field(default=None, description="Optional . Url of the thumbnail for the result")
    thumbnail_width: None | int = Field(default=None, description="Optional . Thumbnail width")
    thumbnail_height: None | int = Field(default=None, description="Optional . Thumbnail height")
class InlineQueryResultVideo(BaseModel):
    """
    InlineQueryResultVideo type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be video")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    video_url: str = Field(description="A valid URL for the embedded video player or video file")
    mime_type: str = Field(description="MIME type of the content of the video URL, “text/html” or “video/mp4”")
    thumbnail_url: str = Field(description="URL of the thumbnail (JPEG only) for the video")
    title: str = Field(description="Title for the result")
    caption: None | str = Field(default=None, description="Optional . Caption of the video to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the video caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    video_width: None | int = Field(default=None, description="Optional . Video width")
    video_height: None | int = Field(default=None, description="Optional . Video height")
    video_duration: None | int = Field(default=None, description="Optional . Video duration in seconds")
    description: None | str = Field(default=None, description="Optional . Short description of the result")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).")
class InlineQueryResultVoice(BaseModel):
    """
    InlineQueryResultVoice type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be voice")
    id: str = Field(description="Unique identifier for this result, 1-64 bytes")
    voice_url: str = Field(description="A valid URL for the voice recording")
    title: str = Field(description="Recording title")
    caption: None | str = Field(default=None, description="Optional . Caption, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the voice message caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    voice_duration: None | int = Field(default=None, description="Optional . Recording duration in seconds")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message")
    input_message_content: None | InputMessageContent = Field(default=None, description="Optional . Content of the message to be sent instead of the voice recording")
class InlineQueryResultsButton(BaseModel):
    """
    InlineQueryResultsButton type from Telegram Bot API.
    """

    text: str = Field(description="Label text on the button")
    web_app: None | WebAppInfo = Field(default=None, description="Optional . Description of the Web App that will be launched when the user presses the button. The Web App will be able to switch back to the inline mode using the method switchInlineQuery inside the Web App.")
    start_parameter: None | str = Field(default=None, description="Optional . Deep-linking parameter for the /start message sent to the bot when a user presses the button. 1-64 characters, only A-Z , a-z , 0-9 , _ and - are allowed. Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities.")
class InputContactMessageContent(BaseModel):
    """
    InputContactMessageContent type from Telegram Bot API.
    """

    phone_number: str = Field(description="Contact's phone number")
    first_name: str = Field(description="Contact's first name")
    last_name: None | str = Field(default=None, description="Optional . Contact's last name")
    vcard: None | str = Field(default=None, description="Optional . Additional data about the contact in the form of a vCard , 0-2048 bytes")
class InputInvoiceMessageContent(BaseModel):
    """
    InputInvoiceMessageContent type from Telegram Bot API.
    """

    title: str = Field(description="Product name, 1-32 characters")
    description: str = Field(description="Product description, 1-255 characters")
    payload: str = Field(description="Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.")
    provider_token: None | str = Field(default=None, description="Optional . Payment provider token, obtained via @BotFather . Pass an empty string for payments in Telegram Stars .")
    currency: str = Field(description="Three-letter ISO 4217 currency code, see more on currencies . Pass “XTR” for payments in Telegram Stars .")
    prices: list[LabeledPrice] = Field(description="Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in Telegram Stars .")
    max_tip_amount: None | int = Field(default=None, description="Optional . The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145 . See the exp parameter in currencies.json , it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in Telegram Stars .")
    suggested_tip_amounts: None | list[int] = Field(default=None, description="Optional . A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount .")
    provider_data: None | str = Field(default=None, description="Optional . A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.")
    photo_url: None | str = Field(default=None, description="Optional . URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.")
    photo_size: None | int = Field(default=None, description="Optional . Photo size in bytes")
    photo_width: None | int = Field(default=None, description="Optional . Photo width")
    photo_height: None | int = Field(default=None, description="Optional . Photo height")
    need_name: None | bool = Field(default=None, description="Optional . Pass True if you require the user's full name to complete the order. Ignored for payments in Telegram Stars .")
    need_phone_number: None | bool = Field(default=None, description="Optional . Pass True if you require the user's phone number to complete the order. Ignored for payments in Telegram Stars .")
    need_email: None | bool = Field(default=None, description="Optional . Pass True if you require the user's email address to complete the order. Ignored for payments in Telegram Stars .")
    need_shipping_address: None | bool = Field(default=None, description="Optional . Pass True if you require the user's shipping address to complete the order. Ignored for payments in Telegram Stars .")
    send_phone_number_to_provider: None | bool = Field(default=None, description="Optional . Pass True if the user's phone number should be sent to the provider. Ignored for payments in Telegram Stars .")
    send_email_to_provider: None | bool = Field(default=None, description="Optional . Pass True if the user's email address should be sent to the provider. Ignored for payments in Telegram Stars .")
    is_flexible: None | bool = Field(default=None, description="Optional . Pass True if the final price depends on the shipping method. Ignored for payments in Telegram Stars .")
class InputLocationMessageContent(BaseModel):
    """
    InputLocationMessageContent type from Telegram Bot API.
    """

    latitude: float = Field(description="Latitude of the location in degrees")
    longitude: float = Field(description="Longitude of the location in degrees")
    horizontal_accuracy: None | float = Field(default=None, description="Optional . The radius of uncertainty for the location, measured in meters; 0-1500")
    live_period: None | int = Field(default=None, description="Optional . Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.")
    heading: None | int = Field(default=None, description="Optional . For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.")
    proximity_alert_radius: None | int = Field(default=None, description="Optional . For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.")
class InputMessageContent(BaseModel):
    """
    InputMessageContent type from Telegram Bot API.
    """

    message_text: str = Field(description="Text of the message to be sent, 1-4096 characters")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the message text. See formatting options for more details.")
    entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in message text, which can be specified instead of parse_mode")
    link_preview_options: None | LinkPreviewOptions = Field(default=None, description="Optional . Link preview generation options for the message")
class InputTextMessageContent(BaseModel):
    """
    InputTextMessageContent type from Telegram Bot API.
    """

    message_text: str = Field(description="Text of the message to be sent, 1-4096 characters")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the message text. See formatting options for more details.")
    entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in message text, which can be specified instead of parse_mode")
    link_preview_options: None | LinkPreviewOptions = Field(default=None, description="Optional . Link preview generation options for the message")
class InputVenueMessageContent(BaseModel):
    """
    InputVenueMessageContent type from Telegram Bot API.
    """

    latitude: float = Field(description="Latitude of the venue in degrees")
    longitude: float = Field(description="Longitude of the venue in degrees")
    title: str = Field(description="Name of the venue")
    address: str = Field(description="Address of the venue")
    foursquare_id: None | str = Field(default=None, description="Optional . Foursquare identifier of the venue, if known")
    foursquare_type: None | str = Field(default=None, description="Optional . Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)")
    google_place_id: None | str = Field(default=None, description="Optional . Google Places identifier of the venue")
    google_place_type: None | str = Field(default=None, description="Optional . Google Places type of the venue. (See supported types .)")
class PreparedInlineMessage(BaseModel):
    """
    PreparedInlineMessage type from Telegram Bot API.
    """

    id: str = Field(description="Unique identifier of the prepared message")
    expiration_date: int = Field(description="Expiration date of the prepared message, in Unix time. Expired prepared messages can no longer be used")
class SentWebAppMessage(BaseModel):
    """
    SentWebAppMessage type from Telegram Bot API.
    """

    inline_message_id: None | str = Field(default=None, description="Optional . Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message.")
class answerInlineQuery(BaseModel):
    """
    answerInlineQuery method from Telegram Bot API.
    """

    inline_query_id: str = Field(description="Unique identifier for the answered query")
    results: list[InlineQueryResult] = Field(description="A JSON-serialized array of results for the inline query")
    cache_time: None | int = Field(default=None, description="The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.")
    is_personal: None | bool = Field(default=None, description="Pass True if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query.")
    next_offset: None | str = Field(default=None, description="Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes.")
    button: None | InlineQueryResultsButton = Field(default=None, description="A JSON-serialized object describing a button to be shown above inline query results")
class answerWebAppQuery(BaseModel):
    """
    answerWebAppQuery method from Telegram Bot API.
    """

    web_app_query_id: str = Field(description="Unique identifier for the query to be answered")
    result: InlineQueryResult = Field(description="A JSON-serialized object describing the message to be sent")
class savePreparedInlineMessage(BaseModel):
    """
    savePreparedInlineMessage method from Telegram Bot API.
    """

    user_id: int = Field(description="Unique identifier of the target user that can use the prepared message")
    result: InlineQueryResult = Field(description="A JSON-serialized object describing the message to be sent")
    allow_user_chats: None | bool = Field(default=None, description="Pass True if the message can be sent to private chats with users")
    allow_bot_chats: None | bool = Field(default=None, description="Pass True if the message can be sent to private chats with bots")
    allow_group_chats: None | bool = Field(default=None, description="Pass True if the message can be sent to group and supergroup chats")
    allow_channel_chats: None | bool = Field(default=None, description="Pass True if the message can be sent to channel chats")
