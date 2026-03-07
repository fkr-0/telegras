"""Telegram Bot API - Getting Updates Pydantic Models.

Auto-generated from API documentation.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any

# External type references (would need to be imported or defined elsewhere)
# BusinessConnection
# BusinessMessagesDeleted
# CallbackQuery
# ChatBoostRemoved
# ChatBoostUpdated
# ChatJoinRequest
# ChatMemberUpdated
# ChosenInlineResult
# InlineQuery
# InputFile
# Message
# MessageReactionCountUpdated
# MessageReactionUpdated
# PaidMediaPurchased
# Poll
# PollAnswer
# PreCheckoutQuery
# ShippingQuery

class setWebhook(BaseModel):
    """
    setWebhook method from Telegram Bot API.
    """

    url: str = Field(description="HTTPS URL to send updates to. Use an empty string to remove webhook integration")
    certificate: None | InputFile = Field(description="Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details.")
    ip_address: None | str = Field(description="The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS")
    max_connections: None | int = Field(description="The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to 40 . Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput.")
    allowed_updates: None | list[str] = Field(description="A JSON-serialized list of the update types you want your bot to receive. For example, specify [\"message\", \"edited_channel_post\", \"callback_query\"] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member , message_reaction , and message_reaction_count (default). If not specified, the previous setting will be used. Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time.")
    drop_pending_updates: None | bool = Field(description="Pass True to drop all pending updates")
    secret_token: None | str = Field(description="A secret token to be sent in a header “X-Telegram-Bot-Api-Secret-Token” in every webhook request, 1-256 characters. Only characters A-Z , a-z , 0-9 , _ and - are allowed. The header is useful to ensure that the request comes from a webhook set by you.")

class getUpdates(BaseModel):
    """
    getUpdates method from Telegram Bot API.
    """

    offset: None | int = Field(description="Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id . The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will be forgotten.")
    limit: None | int = Field(description="Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.")
    timeout: None | int = Field(description="Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.")
    allowed_updates: None | list[str] = Field(description="A JSON-serialized list of the update types you want your bot to receive. For example, specify [\"message\", \"edited_channel_post\", \"callback_query\"] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member , message_reaction , and message_reaction_count (default). If not specified, the previous setting will be used. Please note that this parameter doesn't affect updates created before the call to getUpdates, so unwanted updates may be received for a short period of time.")

class deleteWebhook(BaseModel):
    """
    deleteWebhook method from Telegram Bot API.
    """

    drop_pending_updates: None | bool = Field(description="Pass True to drop all pending updates")

class Update(BaseModel):
    """
    Update type from Telegram Bot API.
    """

    update_id: int = Field(description="The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This identifier becomes especially handy if you're using webhooks , since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.")
    message: None | Message = Field(description="Optional . New incoming message of any kind - text, photo, sticker, etc.")
    edited_message: None | Message = Field(description="Optional . New version of a message that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot.")
    channel_post: None | Message = Field(description="Optional . New incoming channel post of any kind - text, photo, sticker, etc.")
    edited_channel_post: None | Message = Field(description="Optional . New version of a channel post that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot.")
    business_connection: None | BusinessConnection = Field(description="Optional . The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot")
    business_message: None | Message = Field(description="Optional . New message from a connected business account")
    edited_business_message: None | Message = Field(description="Optional . New version of a message from a connected business account")
    deleted_business_messages: None | BusinessMessagesDeleted = Field(description="Optional . Messages were deleted from a connected business account")
    message_reaction: None | MessageReactionUpdated = Field(description="Optional . A reaction to a message was changed by a user. The bot must be an administrator in the chat and must explicitly specify \"message_reaction\" in the list of allowed_updates to receive these updates. The update isn't received for reactions set by bots.")
    message_reaction_count: None | MessageReactionCountUpdated = Field(description="Optional . Reactions to a message with anonymous reactions were changed. The bot must be an administrator in the chat and must explicitly specify \"message_reaction_count\" in the list of allowed_updates to receive these updates. The updates are grouped and can be sent with delay up to a few minutes.")
    inline_query: None | InlineQuery = Field(description="Optional . New incoming inline query")
    chosen_inline_result: None | ChosenInlineResult = Field(description="Optional . The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.")
    callback_query: None | CallbackQuery = Field(description="Optional . New incoming callback query")
    shipping_query: None | ShippingQuery = Field(description="Optional . New incoming shipping query. Only for invoices with flexible price")
    pre_checkout_query: None | PreCheckoutQuery = Field(description="Optional . New incoming pre-checkout query. Contains full information about checkout")
    purchased_paid_media: None | PaidMediaPurchased = Field(description="Optional . A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat")
    poll: None | Poll = Field(description="Optional . New poll state. Bots receive only updates about manually stopped polls and polls, which are sent by the bot")
    poll_answer: None | PollAnswer = Field(description="Optional . A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.")
    my_chat_member: None | ChatMemberUpdated = Field(description="Optional . The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.")
    chat_member: None | ChatMemberUpdated = Field(description="Optional . A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify \"chat_member\" in the list of allowed_updates to receive these updates.")
    chat_join_request: None | ChatJoinRequest = Field(description="Optional . A request to join the chat has been sent. The bot must have the can_invite_users administrator right in the chat to receive these updates.")
    chat_boost: None | ChatBoostUpdated = Field(description="Optional . A chat boost was added or changed. The bot must be an administrator in the chat to receive these updates.")
    removed_chat_boost: None | ChatBoostRemoved = Field(description="Optional . A boost was removed from a chat. The bot must be an administrator in the chat to receive these updates.")

class WebhookInfo(BaseModel):
    """
    WebhookInfo type from Telegram Bot API.
    """

    url: str = Field(description="Webhook URL, may be empty if webhook is not set up")
    has_custom_certificate: bool = Field(description="True , if a custom certificate was provided for webhook certificate checks")
    pending_update_count: int = Field(description="Number of updates awaiting delivery")
    ip_address: None | str = Field(description="Optional . Currently used webhook IP address")
    last_error_date: None | int = Field(description="Optional . Unix time for the most recent error that happened when trying to deliver an update via webhook")
    last_error_message: None | str = Field(description="Optional . Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook")
    last_synchronization_error_date: None | int = Field(description="Optional . Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters")
    max_connections: None | int = Field(description="Optional . The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery")
    allowed_updates: None | list[str] = Field(description="Optional . A list of update types the bot is subscribed to. Defaults to all update types except chat_member")

class getWebhookInfo(BaseModel):
    """
    getWebhookInfo type from Telegram Bot API.
    """

    url: str = Field(description="Webhook URL, may be empty if webhook is not set up")
    has_custom_certificate: bool = Field(description="True , if a custom certificate was provided for webhook certificate checks")
    pending_update_count: int = Field(description="Number of updates awaiting delivery")
    ip_address: None | str = Field(description="Optional . Currently used webhook IP address")
    last_error_date: None | int = Field(description="Optional . Unix time for the most recent error that happened when trying to deliver an update via webhook")
    last_error_message: None | str = Field(description="Optional . Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook")
    last_synchronization_error_date: None | int = Field(description="Optional . Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters")
    max_connections: None | int = Field(description="Optional . The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery")
    allowed_updates: None | list[str] = Field(description="Optional . A list of update types the bot is subscribed to. Defaults to all update types except chat_member")

