from __future__ import annotations

"""Telegram Bot API - Updates."""

from pydantic import BaseModel, Field
from ..core import User, Chat, Message
from ..types import Update

class Update(BaseModel):
    """
    Update type from Telegram Bot API.
    """

    update_id: int = Field(description="The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This identifier becomes especially handy if you're using webhooks , since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.")
    message: None | Message = Field(default=None, description="Optional . New incoming message of any kind - text, photo, sticker, etc.")
    edited_message: None | Message = Field(default=None, description="Optional . New version of a message that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot.")
    channel_post: None | Message = Field(default=None, description="Optional . New incoming channel post of any kind - text, photo, sticker, etc.")
    edited_channel_post: None | Message = Field(default=None, description="Optional . New version of a channel post that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot.")
    business_connection: None | BusinessConnection = Field(default=None, description="Optional . The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot")
    business_message: None | Message = Field(default=None, description="Optional . New message from a connected business account")
    edited_business_message: None | Message = Field(default=None, description="Optional . New version of a message from a connected business account")
    deleted_business_messages: None | BusinessMessagesDeleted = Field(default=None, description="Optional . Messages were deleted from a connected business account")
    message_reaction: None | MessageReactionUpdated = Field(default=None, description="Optional . A reaction to a message was changed by a user. The bot must be an administrator in the chat and must explicitly specify \"message_reaction\" in the list of allowed_updates to receive these updates. The update isn't received for reactions set by bots.")
    message_reaction_count: None | MessageReactionCountUpdated = Field(default=None, description="Optional . Reactions to a message with anonymous reactions were changed. The bot must be an administrator in the chat and must explicitly specify \"message_reaction_count\" in the list of allowed_updates to receive these updates. The updates are grouped and can be sent with delay up to a few minutes.")
    inline_query: None | InlineQuery = Field(default=None, description="Optional . New incoming inline query")
    chosen_inline_result: None | ChosenInlineResult = Field(default=None, description="Optional . The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.")
    callback_query: None | CallbackQuery = Field(default=None, description="Optional . New incoming callback query")
    shipping_query: None | ShippingQuery = Field(default=None, description="Optional . New incoming shipping query. Only for invoices with flexible price")
    pre_checkout_query: None | PreCheckoutQuery = Field(default=None, description="Optional . New incoming pre-checkout query. Contains full information about checkout")
    purchased_paid_media: None | PaidMediaPurchased = Field(default=None, description="Optional . A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat")
    poll: None | Poll = Field(default=None, description="Optional . New poll state. Bots receive only updates about manually stopped polls and polls, which are sent by the bot")
    poll_answer: None | PollAnswer = Field(default=None, description="Optional . A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.")
    my_chat_member: None | ChatMemberUpdated = Field(default=None, description="Optional . The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.")
    chat_member: None | ChatMemberUpdated = Field(default=None, description="Optional . A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify \"chat_member\" in the list of allowed_updates to receive these updates.")
    chat_join_request: None | ChatJoinRequest = Field(default=None, description="Optional . A request to join the chat has been sent. The bot must have the can_invite_users administrator right in the chat to receive these updates.")
    chat_boost: None | ChatBoostUpdated = Field(default=None, description="Optional . A chat boost was added or changed. The bot must be an administrator in the chat to receive these updates.")
    removed_chat_boost: None | ChatBoostRemoved = Field(default=None, description="Optional . A boost was removed from a chat. The bot must be an administrator in the chat to receive these updates.")
class WebhookInfo(BaseModel):
    """
    WebhookInfo type from Telegram Bot API.
    """

    url: str = Field(description="Webhook URL, may be empty if webhook is not set up")
    has_custom_certificate: bool = Field(description="True , if a custom certificate was provided for webhook certificate checks")
    pending_update_count: int = Field(description="Number of updates awaiting delivery")
    ip_address: None | str = Field(default=None, description="Optional . Currently used webhook IP address")
    last_error_date: None | int = Field(default=None, description="Optional . Unix time for the most recent error that happened when trying to deliver an update via webhook")
    last_error_message: None | str = Field(default=None, description="Optional . Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook")
    last_synchronization_error_date: None | int = Field(default=None, description="Optional . Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters")
    max_connections: None | int = Field(default=None, description="Optional . The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery")
    allowed_updates: None | list[str] = Field(default=None, description="Optional . A list of update types the bot is subscribed to. Defaults to all update types except chat_member")
class approveSuggestedPost(BaseModel):
    """
    approveSuggestedPost method from Telegram Bot API.
    """

    chat_id: int = Field(description="Unique identifier for the target direct messages chat")
    message_id: int = Field(description="Identifier of a suggested post message to approve")
    send_date: None | int = Field(default=None, description="Point in time (Unix timestamp) when the post is expected to be published; omit if the date has already been specified when the suggested post was created. If specified, then the date must be not more than 2678400 seconds (30 days) in the future")
class declineSuggestedPost(BaseModel):
    """
    declineSuggestedPost method from Telegram Bot API.
    """

    chat_id: int = Field(description="Unique identifier for the target direct messages chat")
    message_id: int = Field(description="Identifier of a suggested post message to decline")
    comment: None | str = Field(default=None, description="Comment for the creator of the suggested post; 0-128 characters")
class deleteMessage(BaseModel):
    """
    deleteMessage method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: int = Field(description="Identifier of the message to delete")
class deleteMessages(BaseModel):
    """
    deleteMessages method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_ids: list[int] = Field(description="A JSON-serialized list of 1-100 identifiers of messages to delete. See deleteMessage for limitations on which messages can be deleted")
class deleteWebhook(BaseModel):
    """
    deleteWebhook method from Telegram Bot API.
    """

    drop_pending_updates: None | bool = Field(default=None, description="Pass True to drop all pending updates")
class editMessageCaption(BaseModel):
    """
    editMessageCaption method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(default=None, description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(default=None, description="Required if inline_message_id is not specified. Identifier of the message to edit")
    inline_message_id: None | str = Field(default=None, description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    caption: None | str = Field(default=None, description="New caption of the message, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the message caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Pass True , if the caption must be shown above the message media. Supported only for animation, photo and video messages.")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="A JSON-serialized object for an inline keyboard .")
class editMessageChecklist(BaseModel):
    """
    editMessageChecklist method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int = Field(description="Unique identifier for the target chat")
    message_id: int = Field(description="Unique identifier for the target message")
    checklist: InputChecklist = Field(description="A JSON-serialized object for the new checklist")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="A JSON-serialized object for the new inline keyboard for the message")
class editMessageLiveLocation(BaseModel):
    """
    editMessageLiveLocation method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(default=None, description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(default=None, description="Required if inline_message_id is not specified. Identifier of the message to edit")
    inline_message_id: None | str = Field(default=None, description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    latitude: float = Field(description="Latitude of new location")
    longitude: float = Field(description="Longitude of new location")
    live_period: None | int = Field(default=None, description="New period in seconds during which the location can be updated, starting from the message send date. If 0x7FFFFFFF is specified, then the location can be updated forever. Otherwise, the new value must not exceed the current live_period by more than a day, and the live location expiration date must remain within the next 90 days. If not specified, then live_period remains unchanged")
    horizontal_accuracy: None | float = Field(default=None, description="The radius of uncertainty for the location, measured in meters; 0-1500")
    heading: None | int = Field(default=None, description="Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.")
    proximity_alert_radius: None | int = Field(default=None, description="The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="A JSON-serialized object for a new inline keyboard .")
class editMessageMedia(BaseModel):
    """
    editMessageMedia method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(default=None, description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(default=None, description="Required if inline_message_id is not specified. Identifier of the message to edit")
    inline_message_id: None | str = Field(default=None, description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    media: InputMedia = Field(description="A JSON-serialized object for a new media content of the message")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="A JSON-serialized object for a new inline keyboard .")
class editMessageReplyMarkup(BaseModel):
    """
    editMessageReplyMarkup method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(default=None, description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(default=None, description="Required if inline_message_id is not specified. Identifier of the message to edit")
    inline_message_id: None | str = Field(default=None, description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="A JSON-serialized object for an inline keyboard .")
class editMessageText(BaseModel):
    """
    editMessageText method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(default=None, description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(default=None, description="Required if inline_message_id is not specified. Identifier of the message to edit")
    inline_message_id: None | str = Field(default=None, description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    text: str = Field(description="New text of the message, 1-4096 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the message text. See formatting options for more details.")
    entities: None | list[MessageEntity] = Field(default=None, description="A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode")
    link_preview_options: None | LinkPreviewOptions = Field(default=None, description="Link preview generation options for the message")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="A JSON-serialized object for an inline keyboard .")
class getUpdates(BaseModel):
    """
    getUpdates method from Telegram Bot API.
    """

    offset: None | int = Field(default=None, description="Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id . The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will be forgotten.")
    limit: None | int = Field(default=None, description="Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.")
    timeout: None | int = Field(default=None, description="Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.")
    allowed_updates: None | list[str] = Field(default=None, description="A JSON-serialized list of the update types you want your bot to receive. For example, specify [\"message\", \"edited_channel_post\", \"callback_query\"] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member , message_reaction , and message_reaction_count (default). If not specified, the previous setting will be used. Please note that this parameter doesn't affect updates created before the call to getUpdates, so unwanted updates may be received for a short period of time.")
class getWebhookInfo(BaseModel):
    """
    getWebhookInfo type from Telegram Bot API.
    """

    url: str = Field(description="Webhook URL, may be empty if webhook is not set up")
    has_custom_certificate: bool = Field(description="True , if a custom certificate was provided for webhook certificate checks")
    pending_update_count: int = Field(description="Number of updates awaiting delivery")
    ip_address: None | str = Field(default=None, description="Optional . Currently used webhook IP address")
    last_error_date: None | int = Field(default=None, description="Optional . Unix time for the most recent error that happened when trying to deliver an update via webhook")
    last_error_message: None | str = Field(default=None, description="Optional . Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook")
    last_synchronization_error_date: None | int = Field(default=None, description="Optional . Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters")
    max_connections: None | int = Field(default=None, description="Optional . The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery")
    allowed_updates: None | list[str] = Field(default=None, description="Optional . A list of update types the bot is subscribed to. Defaults to all update types except chat_member")
class setWebhook(BaseModel):
    """
    setWebhook method from Telegram Bot API.
    """

    url: str = Field(description="HTTPS URL to send updates to. Use an empty string to remove webhook integration")
    certificate: None | InputFile = Field(default=None, description="Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details.")
    ip_address: None | str = Field(default=None, description="The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS")
    max_connections: None | int = Field(default=None, description="The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to 40 . Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput.")
    allowed_updates: None | list[str] = Field(default=None, description="A JSON-serialized list of the update types you want your bot to receive. For example, specify [\"message\", \"edited_channel_post\", \"callback_query\"] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member , message_reaction , and message_reaction_count (default). If not specified, the previous setting will be used. Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time.")
    drop_pending_updates: None | bool = Field(default=None, description="Pass True to drop all pending updates")
    secret_token: None | str = Field(default=None, description="A secret token to be sent in a header “X-Telegram-Bot-Api-Secret-Token” in every webhook request, 1-256 characters. Only characters A-Z , a-z , 0-9 , _ and - are allowed. The header is useful to ensure that the request comes from a webhook set by you.")
class stopMessageLiveLocation(BaseModel):
    """
    stopMessageLiveLocation method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: None | Integer or String = Field(default=None, description="Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(default=None, description="Required if inline_message_id is not specified. Identifier of the message with live location to stop")
    inline_message_id: None | str = Field(default=None, description="Required if chat_id and message_id are not specified. Identifier of the inline message")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="A JSON-serialized object for a new inline keyboard .")
class stopPoll(BaseModel):
    """
    stopPoll method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message to be edited was sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: int = Field(description="Identifier of the original message with the poll")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="A JSON-serialized object for a new message inline keyboard .")
