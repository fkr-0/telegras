"""Telegram Bot API models.

Auto-generated from API documentation.
This module contains Methods.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

class Formattingoptions(BaseModel):
    """
    Formattingoptions method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be forwarded; required if the message is forwarded to a direct messages chat")
    from_chat_id: int | str = Field(description="Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername )")
    video_start_timestamp: None | int = Field(default=None, description="New start timestamp for the forwarded video in the message")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the forwarded message from forwarding and saving")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; only available when forwarding to private chats")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only")
    message_id: int = Field(description="Message identifier in the chat specified in from_chat_id")
class PaidBroadcasts(BaseModel):
    """
    PaidBroadcasts method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be forwarded; required if the message is forwarded to a direct messages chat")
    from_chat_id: int | str = Field(description="Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername )")
    video_start_timestamp: None | int = Field(default=None, description="New start timestamp for the forwarded video in the message")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the forwarded message from forwarding and saving")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; only available when forwarding to private chats")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only")
    message_id: int = Field(description="Message identifier in the chat specified in from_chat_id")
class answerCallbackQuery(BaseModel):
    """
    answerCallbackQuery method from Telegram Bot API.
    """

    callback_query_id: str = Field(description="Unique identifier for the query to be answered")
    text: None | str = Field(default=None, description="Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters")
    show_alert: None | bool = Field(default=None, description="If True , an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false .")
    url: None | str = Field(default=None, description="URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @BotFather , specify the URL that opens your game - note that this will only work if the query comes from a callback_game button. Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.")
    cache_time: None | int = Field(default=None, description="The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.")
class approveChatJoinRequest(BaseModel):
    """
    approveChatJoinRequest method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    user_id: int = Field(description="Unique identifier of the target user")
class banChatMember(BaseModel):
    """
    banChatMember method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername )")
    user_id: int = Field(description="Unique identifier of the target user")
    until_date: None | int = Field(default=None, description="Date when the user will be unbanned; Unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only.")
    revoke_messages: None | bool = Field(default=None, description="Pass True to delete all messages from the chat for the user that is being removed. If False , the user will be able to see messages in the group that were sent before the user was removed. Always True for supergroups and channels.")
class banChatSenderChat(BaseModel):
    """
    banChatSenderChat method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    sender_chat_id: int = Field(description="Unique identifier of the target sender chat")
class close(BaseModel):
    """
    close method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    text: str = Field(description="Text of the message to be sent, 1-4096 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the message text. See formatting options for more details.")
    entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode")
    link_preview_options: "None | LinkPreviewOptions" = Field(default=None, description="Link preview generation options for the message")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class closeForumTopic(BaseModel):
    """
    closeForumTopic method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    message_thread_id: int = Field(description="Unique identifier for the target message thread of the forum topic")
class closeGeneralForumTopic(BaseModel):
    """
    closeGeneralForumTopic method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
class convertGiftToStars(BaseModel):
    """
    convertGiftToStars method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    owned_gift_id: str = Field(description="Unique identifier of the regular gift that should be converted to Telegram Stars")
class copyMessage(BaseModel):
    """
    copyMessage method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    from_chat_id: int | str = Field(description="Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername )")
    message_id: int = Field(description="Message identifier in the chat specified in from_chat_id")
    video_start_timestamp: None | int = Field(default=None, description="New start timestamp for the copied video in the message")
    caption: None | str = Field(default=None, description="New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the new caption. See formatting options for more details.")
    caption_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Pass True , if the caption must be shown above the message media. Ignored if a new caption isn't specified.")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; only available when copying to private chats")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class copyMessages(BaseModel):
    """
    copyMessages method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat")
    from_chat_id: int | str = Field(description="Unique identifier for the chat where the original messages were sent (or channel username in the format @channelusername )")
    message_ids: list[int] = Field(description="A JSON-serialized list of 1-100 identifiers of messages in the chat from_chat_id to copy. The identifiers must be specified in a strictly increasing order.")
    disable_notification: None | bool = Field(default=None, description="Sends the messages silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent messages from forwarding and saving")
    remove_caption: None | bool = Field(default=None, description="Pass True to copy the messages without their captions")
class createChatInviteLink(BaseModel):
    """
    createChatInviteLink method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    name: None | str = Field(default=None, description="Invite link name; 0-32 characters")
    expire_date: None | int = Field(default=None, description="Point in time (Unix timestamp) when the link will expire")
    member_limit: None | int = Field(default=None, description="The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999")
    creates_join_request: None | bool = Field(default=None, description="True , if users joining the chat via the link need to be approved by chat administrators. If True , member_limit can't be specified")
class createChatSubscriptionInviteLink(BaseModel):
    """
    createChatSubscriptionInviteLink method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target channel chat or username of the target channel (in the format @channelusername )")
    name: None | str = Field(default=None, description="Invite link name; 0-32 characters")
    subscription_period: int = Field(description="The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days).")
    subscription_price: int = Field(description="The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat; 1-10000")
class createForumTopic(BaseModel):
    """
    createForumTopic method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    name: str = Field(description="Topic name, 1-128 characters")
    icon_color: None | int = Field(default=None, description="Color of the topic icon in RGB format. Currently, must be one of 7322096 (0x6FB9F0), 16766590 (0xFFD67E), 13338331 (0xCB86DB), 9367192 (0x8EEE98), 16749490 (0xFF93B2), or 16478047 (0xFB6F5F)")
    icon_custom_emoji_id: None | str = Field(default=None, description="Unique identifier of the custom emoji shown as the topic icon. Use getForumTopicIconStickers to get all allowed custom emoji identifiers.")
class declineChatJoinRequest(BaseModel):
    """
    declineChatJoinRequest method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    user_id: int = Field(description="Unique identifier of the target user")
class deleteBusinessMessages(BaseModel):
    """
    deleteBusinessMessages method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection on behalf of which to delete the messages")
    message_ids: list[int] = Field(description="A JSON-serialized list of 1-100 identifiers of messages to delete. All messages must be from the same chat. See deleteMessage for limitations on which messages can be deleted")
class deleteChatPhoto(BaseModel):
    """
    deleteChatPhoto method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
class deleteChatStickerSet(BaseModel):
    """
    deleteChatStickerSet method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
class deleteForumTopic(BaseModel):
    """
    deleteForumTopic method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    message_thread_id: int = Field(description="Unique identifier for the target message thread of the forum topic")
class deleteMyCommands(BaseModel):
    """
    deleteMyCommands method from Telegram Bot API.
    """

    scope: "None | BotCommandScope" = Field(default=None, description="A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault .")
    language_code: None | str = Field(default=None, description="A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands")
class deleteStory(BaseModel):
    """
    deleteStory method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    story_id: int = Field(description="Unique identifier of the story to delete")
class editChatInviteLink(BaseModel):
    """
    editChatInviteLink method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    invite_link: str = Field(description="The invite link to edit")
    name: None | str = Field(default=None, description="Invite link name; 0-32 characters")
    expire_date: None | int = Field(default=None, description="Point in time (Unix timestamp) when the link will expire")
    member_limit: None | int = Field(default=None, description="The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999")
    creates_join_request: None | bool = Field(default=None, description="True , if users joining the chat via the link need to be approved by chat administrators. If True , member_limit can't be specified")
class editChatSubscriptionInviteLink(BaseModel):
    """
    editChatSubscriptionInviteLink method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    invite_link: str = Field(description="The invite link to edit")
    name: None | str = Field(default=None, description="Invite link name; 0-32 characters")
class editForumTopic(BaseModel):
    """
    editForumTopic method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    message_thread_id: int = Field(description="Unique identifier for the target message thread of the forum topic")
    name: None | str = Field(default=None, description="New topic name, 0-128 characters. If not specified or empty, the current name of the topic will be kept")
    icon_custom_emoji_id: None | str = Field(default=None, description="New unique identifier of the custom emoji shown as the topic icon. Use getForumTopicIconStickers to get all allowed custom emoji identifiers. Pass an empty string to remove the icon. If not specified, the current icon will be kept")
class editGeneralForumTopic(BaseModel):
    """
    editGeneralForumTopic method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    name: str = Field(description="New topic name, 1-128 characters")
class editStory(BaseModel):
    """
    editStory method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    story_id: int = Field(description="Unique identifier of the story to edit")
    content: "InputStoryContent" = Field(description="Content of the story")
    caption: None | str = Field(default=None, description="Caption of the story, 0-2048 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the story caption. See formatting options for more details.")
    caption_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode")
    areas: None | list[StoryArea] = Field(default=None, description="A JSON-serialized list of clickable areas to be shown on the story")
class exportChatInviteLink(BaseModel):
    """
    exportChatInviteLink method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
class forwardMessage(BaseModel):
    """
    forwardMessage method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be forwarded; required if the message is forwarded to a direct messages chat")
    from_chat_id: int | str = Field(description="Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername )")
    video_start_timestamp: None | int = Field(default=None, description="New start timestamp for the forwarded video in the message")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the forwarded message from forwarding and saving")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; only available when forwarding to private chats")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only")
    message_id: int = Field(description="Message identifier in the chat specified in from_chat_id")
class forwardMessages(BaseModel):
    """
    forwardMessages method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the messages will be forwarded; required if the messages are forwarded to a direct messages chat")
    from_chat_id: int | str = Field(description="Unique identifier for the chat where the original messages were sent (or channel username in the format @channelusername )")
    message_ids: list[int] = Field(description="A JSON-serialized list of 1-100 identifiers of messages in the chat from_chat_id to forward. The identifiers must be specified in a strictly increasing order.")
    disable_notification: None | bool = Field(default=None, description="Sends the messages silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the forwarded messages from forwarding and saving")
class getAvailableGifts(BaseModel):
    """
    getAvailableGifts method from Telegram Bot API.
    """

    user_id: None | int = Field(default=None, description="Required if chat_id is not specified. Unique identifier of the target user who will receive the gift.")
    chat_id: "None | int | str" = Field(default=None, description="Required if user_id is not specified. Unique identifier for the chat or username of the channel (in the format @channelusername ) that will receive the gift.")
    gift_id: str = Field(description="Identifier of the gift; limited gifts can't be sent to channel chats")
    pay_for_upgrade: None | bool = Field(default=None, description="Pass True to pay for the gift upgrade from the bot's balance, thereby making the upgrade free for the receiver")
    text: None | str = Field(default=None, description="Text that will be shown along with the gift; 0-128 characters")
    text_parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the text. See formatting options for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.")
    text_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of text_parse_mode . Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.")
class getBusinessAccountGifts(BaseModel):
    """
    getBusinessAccountGifts method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    exclude_unsaved: None | bool = Field(default=None, description="Pass True to exclude gifts that aren't saved to the account's profile page")
    exclude_saved: None | bool = Field(default=None, description="Pass True to exclude gifts that are saved to the account's profile page")
    exclude_unlimited: None | bool = Field(default=None, description="Pass True to exclude gifts that can be purchased an unlimited number of times")
    exclude_limited_upgradable: None | bool = Field(default=None, description="Pass True to exclude gifts that can be purchased a limited number of times and can be upgraded to unique")
    exclude_limited_non_upgradable: None | bool = Field(default=None, description="Pass True to exclude gifts that can be purchased a limited number of times and can't be upgraded to unique")
    exclude_unique: None | bool = Field(default=None, description="Pass True to exclude unique gifts")
    exclude_from_blockchain: None | bool = Field(default=None, description="Pass True to exclude gifts that were assigned from the TON blockchain and can't be resold or transferred in Telegram")
    sort_by_price: None | bool = Field(default=None, description="Pass True to sort results by gift price instead of send date. Sorting is applied before pagination.")
    offset: None | str = Field(default=None, description="Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results")
    limit: None | int = Field(default=None, description="The maximum number of gifts to be returned; 1-100. Defaults to 100")
class getBusinessAccountStarBalance(BaseModel):
    """
    getBusinessAccountStarBalance method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
class getBusinessConnection(BaseModel):
    """
    getBusinessConnection method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
class getChat(BaseModel):
    """
    getChat method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername )")
class getChatAdministrators(BaseModel):
    """
    getChatAdministrators method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername )")
class getChatGifts(BaseModel):
    """
    getChatGifts method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    exclude_unsaved: None | bool = Field(default=None, description="Pass True to exclude gifts that aren't saved to the chat's profile page. Always True , unless the bot has the can_post_messages administrator right in the channel.")
    exclude_saved: None | bool = Field(default=None, description="Pass True to exclude gifts that are saved to the chat's profile page. Always False , unless the bot has the can_post_messages administrator right in the channel.")
    exclude_unlimited: None | bool = Field(default=None, description="Pass True to exclude gifts that can be purchased an unlimited number of times")
    exclude_limited_upgradable: None | bool = Field(default=None, description="Pass True to exclude gifts that can be purchased a limited number of times and can be upgraded to unique")
    exclude_limited_non_upgradable: None | bool = Field(default=None, description="Pass True to exclude gifts that can be purchased a limited number of times and can't be upgraded to unique")
    exclude_from_blockchain: None | bool = Field(default=None, description="Pass True to exclude gifts that were assigned from the TON blockchain and can't be resold or transferred in Telegram")
    exclude_unique: None | bool = Field(default=None, description="Pass True to exclude unique gifts")
    sort_by_price: None | bool = Field(default=None, description="Pass True to sort results by gift price instead of send date. Sorting is applied before pagination.")
    offset: None | str = Field(default=None, description="Offset of the first entry to return as received from the previous request; use an empty string to get the first chunk of results")
    limit: None | int = Field(default=None, description="The maximum number of gifts to be returned; 1-100. Defaults to 100")
class getChatMember(BaseModel):
    """
    getChatMember method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername )")
    user_id: int = Field(description="Unique identifier of the target user")
class getChatMemberCount(BaseModel):
    """
    getChatMemberCount method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername )")
class getChatMenuButton(BaseModel):
    """
    getChatMenuButton method from Telegram Bot API.
    """

    chat_id: None | int = Field(default=None, description="Unique identifier for the target private chat. If not specified, default bot's menu button will be returned")
class getFile(BaseModel):
    """
    getFile method from Telegram Bot API.
    """

    file_id: str = Field(description="File identifier to get information about")
class getForumTopicIconStickers(BaseModel):
    """
    getForumTopicIconStickers method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    name: str = Field(description="Topic name, 1-128 characters")
    icon_color: None | int = Field(default=None, description="Color of the topic icon in RGB format. Currently, must be one of 7322096 (0x6FB9F0), 16766590 (0xFFD67E), 13338331 (0xCB86DB), 9367192 (0x8EEE98), 16749490 (0xFF93B2), or 16478047 (0xFB6F5F)")
    icon_custom_emoji_id: None | str = Field(default=None, description="Unique identifier of the custom emoji shown as the topic icon. Use getForumTopicIconStickers to get all allowed custom emoji identifiers.")
class getMe(BaseModel):
    """
    getMe method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    text: str = Field(description="Text of the message to be sent, 1-4096 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the message text. See formatting options for more details.")
    entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode")
    link_preview_options: "None | LinkPreviewOptions" = Field(default=None, description="Link preview generation options for the message")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class getMyCommands(BaseModel):
    """
    getMyCommands method from Telegram Bot API.
    """

    scope: "None | BotCommandScope" = Field(default=None, description="A JSON-serialized object, describing scope of users. Defaults to BotCommandScopeDefault .")
    language_code: None | str = Field(default=None, description="A two-letter ISO 639-1 language code or an empty string")
class getMyDefaultAdministratorRights(BaseModel):
    """
    getMyDefaultAdministratorRights method from Telegram Bot API.
    """

    for_channels: None | bool = Field(default=None, description="Pass True to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned.")
class getMyDescription(BaseModel):
    """
    getMyDescription method from Telegram Bot API.
    """

    language_code: None | str = Field(default=None, description="A two-letter ISO 639-1 language code or an empty string")
class getMyName(BaseModel):
    """
    getMyName method from Telegram Bot API.
    """

    language_code: None | str = Field(default=None, description="A two-letter ISO 639-1 language code or an empty string")
class getMyShortDescription(BaseModel):
    """
    getMyShortDescription method from Telegram Bot API.
    """

    language_code: None | str = Field(default=None, description="A two-letter ISO 639-1 language code or an empty string")
class getUserChatBoosts(BaseModel):
    """
    getUserChatBoosts method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the chat or username of the channel (in the format @channelusername )")
    user_id: int = Field(description="Unique identifier of the target user")
class getUserGifts(BaseModel):
    """
    getUserGifts method from Telegram Bot API.
    """

    user_id: int = Field(description="Unique identifier of the user")
    exclude_unlimited: None | bool = Field(default=None, description="Pass True to exclude gifts that can be purchased an unlimited number of times")
    exclude_limited_upgradable: None | bool = Field(default=None, description="Pass True to exclude gifts that can be purchased a limited number of times and can be upgraded to unique")
    exclude_limited_non_upgradable: None | bool = Field(default=None, description="Pass True to exclude gifts that can be purchased a limited number of times and can't be upgraded to unique")
    exclude_from_blockchain: None | bool = Field(default=None, description="Pass True to exclude gifts that were assigned from the TON blockchain and can't be resold or transferred in Telegram")
    exclude_unique: None | bool = Field(default=None, description="Pass True to exclude unique gifts")
    sort_by_price: None | bool = Field(default=None, description="Pass True to sort results by gift price instead of send date. Sorting is applied before pagination.")
    offset: None | str = Field(default=None, description="Offset of the first entry to return as received from the previous request; use an empty string to get the first chunk of results")
    limit: None | int = Field(default=None, description="The maximum number of gifts to be returned; 1-100. Defaults to 100")
class getUserProfileAudios(BaseModel):
    """
    getUserProfileAudios method from Telegram Bot API.
    """

    user_id: int = Field(description="Unique identifier of the target user")
    offset: None | int = Field(default=None, description="Sequential number of the first audio to be returned. By default, all audios are returned.")
    limit: None | int = Field(default=None, description="Limits the number of audios to be retrieved. Values between 1-100 are accepted. Defaults to 100.")
class getUserProfilePhotos(BaseModel):
    """
    getUserProfilePhotos method from Telegram Bot API.
    """

    user_id: int = Field(description="Unique identifier of the target user")
    offset: None | int = Field(default=None, description="Sequential number of the first photo to be returned. By default, all photos are returned.")
    limit: None | int = Field(default=None, description="Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.")
class giftPremiumSubscription(BaseModel):
    """
    giftPremiumSubscription method from Telegram Bot API.
    """

    user_id: int = Field(description="Unique identifier of the target user who will receive a Telegram Premium subscription")
    month_count: int = Field(description="Number of months the Telegram Premium subscription will be active for the user; must be one of 3, 6, or 12")
    star_count: int = Field(description="Number of Telegram Stars to pay for the Telegram Premium subscription; must be 1000 for 3 months, 1500 for 6 months, and 2500 for 12 months")
    text: None | str = Field(default=None, description="Text that will be shown along with the service message about the subscription; 0-128 characters")
    text_parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the text. See formatting options for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.")
    text_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of text_parse_mode . Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.")
class hideGeneralForumTopic(BaseModel):
    """
    hideGeneralForumTopic method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
class leaveChat(BaseModel):
    """
    leaveChat method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername ). Channel direct messages chats aren't supported; leave the corresponding channel instead.")
class logOut(BaseModel):
    """
    logOut method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    text: str = Field(description="Text of the message to be sent, 1-4096 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the message text. See formatting options for more details.")
    entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode")
    link_preview_options: "None | LinkPreviewOptions" = Field(default=None, description="Link preview generation options for the message")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class pinChatMessage(BaseModel):
    """
    pinChatMessage method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be pinned")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: int = Field(description="Identifier of a message to pin")
    disable_notification: None | bool = Field(default=None, description="Pass True if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats.")
class postStory(BaseModel):
    """
    postStory method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    content: "InputStoryContent" = Field(description="Content of the story")
    active_period: int = Field(description="Period after which the story is moved to the archive, in seconds; must be one of 6 * 3600 , 12 * 3600 , 86400 , or 2 * 86400")
    caption: None | str = Field(default=None, description="Caption of the story, 0-2048 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the story caption. See formatting options for more details.")
    caption_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode")
    areas: None | list[StoryArea] = Field(default=None, description="A JSON-serialized list of clickable areas to be shown on the story")
    post_to_chat_page: None | bool = Field(default=None, description="Pass True to keep the story accessible after it expires")
    protect_content: None | bool = Field(default=None, description="Pass True if the content of the story must be protected from forwarding and screenshotting")
class promoteChatMember(BaseModel):
    """
    promoteChatMember method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    user_id: int = Field(description="Unique identifier of the target user")
    is_anonymous: None | bool = Field(default=None, description="Pass True if the administrator's presence in the chat is hidden")
    can_manage_chat: None | bool = Field(default=None, description="Pass True if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages, ignore slow mode, and send messages to the chat without paying Telegram Stars. Implied by any other administrator privilege.")
    can_delete_messages: None | bool = Field(default=None, description="Pass True if the administrator can delete messages of other users")
    can_manage_video_chats: None | bool = Field(default=None, description="Pass True if the administrator can manage video chats")
    can_restrict_members: None | bool = Field(default=None, description="Pass True if the administrator can restrict, ban or unban chat members, or access supergroup statistics. For backward compatibility, defaults to True for promotions of channel administrators")
    can_promote_members: None | bool = Field(default=None, description="Pass True if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by him)")
    can_change_info: None | bool = Field(default=None, description="Pass True if the administrator can change chat title, photo and other settings")
    can_invite_users: None | bool = Field(default=None, description="Pass True if the administrator can invite new users to the chat")
    can_post_stories: None | bool = Field(default=None, description="Pass True if the administrator can post stories to the chat")
    can_edit_stories: None | bool = Field(default=None, description="Pass True if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive")
    can_delete_stories: None | bool = Field(default=None, description="Pass True if the administrator can delete stories posted by other users")
    can_post_messages: None | bool = Field(default=None, description="Pass True if the administrator can post messages in the channel, approve suggested posts, or access channel statistics; for channels only")
    can_edit_messages: None | bool = Field(default=None, description="Pass True if the administrator can edit messages of other users and can pin messages; for channels only")
    can_pin_messages: None | bool = Field(default=None, description="Pass True if the administrator can pin messages; for supergroups only")
    can_manage_topics: None | bool = Field(default=None, description="Pass True if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only")
    can_manage_direct_messages: None | bool = Field(default=None, description="Pass True if the administrator can manage direct messages within the channel and decline suggested posts; for channels only")
    can_manage_tags: None | bool = Field(default=None, description="Pass True if the administrator can edit the tags of regular members; for groups and supergroups only")
class readBusinessMessage(BaseModel):
    """
    readBusinessMessage method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection on behalf of which to read the message")
    chat_id: int = Field(description="Unique identifier of the chat in which the message was received. The chat must have been active in the last 24 hours.")
    message_id: int = Field(description="Unique identifier of the message to mark as read")
class removeBusinessAccountProfilePhoto(BaseModel):
    """
    removeBusinessAccountProfilePhoto method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    is_public: None | bool = Field(default=None, description="Pass True to remove the public photo, which is visible even if the main photo is hidden by the business account's privacy settings. After the main photo is removed, the previous profile photo (if present) becomes the main photo.")
class removeChatVerification(BaseModel):
    """
    removeChatVerification method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
class removeMyProfilePhoto(BaseModel):
    """
    removeMyProfilePhoto method from Telegram Bot API.
    """

    chat_id: None | int = Field(default=None, description="Unique identifier for the target private chat. If not specified, default bot's menu button will be changed")
    menu_button: "None | MenuButton" = Field(default=None, description="A JSON-serialized object for the bot's new menu button. Defaults to MenuButtonDefault")
class removeUserVerification(BaseModel):
    """
    removeUserVerification method from Telegram Bot API.
    """

    user_id: int = Field(description="Unique identifier of the target user")
class reopenForumTopic(BaseModel):
    """
    reopenForumTopic method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    message_thread_id: int = Field(description="Unique identifier for the target message thread of the forum topic")
class reopenGeneralForumTopic(BaseModel):
    """
    reopenGeneralForumTopic method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
class repostStory(BaseModel):
    """
    repostStory method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    from_chat_id: int = Field(description="Unique identifier of the chat which posted the story that should be reposted")
    from_story_id: int = Field(description="Unique identifier of the story that should be reposted")
    active_period: int = Field(description="Period after which the story is moved to the archive, in seconds; must be one of 6 * 3600 , 12 * 3600 , 86400 , or 2 * 86400")
    post_to_chat_page: None | bool = Field(default=None, description="Pass True to keep the story accessible after it expires")
    protect_content: None | bool = Field(default=None, description="Pass True if the content of the story must be protected from forwarding and screenshotting")
class restrictChatMember(BaseModel):
    """
    restrictChatMember method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    user_id: int = Field(description="Unique identifier of the target user")
    permissions: "ChatPermissions" = Field(description="A JSON-serialized object for new user permissions")
    use_independent_chat_permissions: None | bool = Field(default=None, description="Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages , can_send_audios , can_send_documents , can_send_photos , can_send_videos , can_send_video_notes , and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.")
    until_date: None | int = Field(default=None, description="Date when restrictions will be lifted for the user; Unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever")
class revokeChatInviteLink(BaseModel):
    """
    revokeChatInviteLink method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier of the target chat or username of the target channel (in the format @channelusername )")
    invite_link: str = Field(description="The invite link to revoke")
class sendAnimation(BaseModel):
    """
    sendAnimation method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    animation: "InputFile | str" = Field(description="Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. More information on Sending Files »")
    duration: None | int = Field(default=None, description="Duration of sent animation in seconds")
    width: None | int = Field(default=None, description="Animation width")
    height: None | int = Field(default=None, description="Animation height")
    thumbnail: "None | InputFile | str" = Field(default=None, description="Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    caption: None | str = Field(default=None, description="Animation caption (may also be used when resending animation by file_id ), 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the animation caption. See formatting options for more details.")
    caption_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Pass True , if the caption must be shown above the message media")
    has_spoiler: None | bool = Field(default=None, description="Pass True if the animation needs to be covered with a spoiler animation")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendAudio(BaseModel):
    """
    sendAudio method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    audio: "InputFile | str" = Field(description="Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files »")
    caption: None | str = Field(default=None, description="Audio caption, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the audio caption. See formatting options for more details.")
    caption_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode")
    duration: None | int = Field(default=None, description="Duration of the audio in seconds")
    performer: None | str = Field(default=None, description="Performer")
    title: None | str = Field(default=None, description="Track name")
    thumbnail: "None | InputFile | str" = Field(default=None, description="Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendChatAction(BaseModel):
    """
    sendChatAction method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the action will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername ). Channel chats and channel direct messages chats aren't supported.")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread or topic of a forum; for supergroups and private chats of bots with forum topic mode enabled only")
    action: str = Field(description="Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages , upload_photo for photos , record_video or upload_video for videos , record_voice or upload_voice for voice notes , upload_document for general files , choose_sticker for stickers , find_location for location data , record_video_note or upload_video_note for video notes .")
class sendChecklist(BaseModel):
    """
    sendChecklist method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int = Field(description="Unique identifier for the target chat")
    checklist: "InputChecklist" = Field(description="A JSON-serialized object for the checklist to send")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently. Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="A JSON-serialized object for description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup" = Field(default=None, description="A JSON-serialized object for an inline keyboard")
class sendContact(BaseModel):
    """
    sendContact method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    phone_number: str = Field(description="Contact's phone number")
    first_name: str = Field(description="Contact's first name")
    last_name: None | str = Field(default=None, description="Contact's last name")
    vcard: None | str = Field(default=None, description="Additional data about the contact in the form of a vCard , 0-2048 bytes")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendDice(BaseModel):
    """
    sendDice method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    emoji: None | str = Field(default=None, description="Emoji on which the dice throw animation is based. Currently, must be one of “ ”, “ ”, “ ”, “ ”, “ ”, or “ ”. Dice can have values 1-6 for “ ”, “ ” and “ ”, values 1-5 for “ ” and “ ”, and values 1-64 for “ ”. Defaults to “ ”")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendDocument(BaseModel):
    """
    sendDocument method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    document: "InputFile | str" = Field(description="File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files »")
    thumbnail: "None | InputFile | str" = Field(default=None, description="Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    caption: None | str = Field(default=None, description="Document caption (may also be used when resending documents by file_id ), 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the document caption. See formatting options for more details.")
    caption_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode")
    disable_content_type_detection: None | bool = Field(default=None, description="Disables automatic server-side content type detection for files uploaded using multipart/form-data")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendGift(BaseModel):
    """
    sendGift method from Telegram Bot API.
    """

    user_id: None | int = Field(default=None, description="Required if chat_id is not specified. Unique identifier of the target user who will receive the gift.")
    chat_id: "None | int | str" = Field(default=None, description="Required if user_id is not specified. Unique identifier for the chat or username of the channel (in the format @channelusername ) that will receive the gift.")
    gift_id: str = Field(description="Identifier of the gift; limited gifts can't be sent to channel chats")
    pay_for_upgrade: None | bool = Field(default=None, description="Pass True to pay for the gift upgrade from the bot's balance, thereby making the upgrade free for the receiver")
    text: None | str = Field(default=None, description="Text that will be shown along with the gift; 0-128 characters")
    text_parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the text. See formatting options for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.")
    text_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of text_parse_mode . Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, and “custom_emoji” are ignored.")
class sendLocation(BaseModel):
    """
    sendLocation method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    latitude: float = Field(description="Latitude of the location")
    longitude: float = Field(description="Longitude of the location")
    horizontal_accuracy: None | float = Field(default=None, description="The radius of uncertainty for the location, measured in meters; 0-1500")
    live_period: None | int = Field(default=None, description="Period in seconds during which the location will be updated (see Live Locations , should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.")
    heading: None | int = Field(default=None, description="For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.")
    proximity_alert_radius: None | int = Field(default=None, description="For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendMediaGroup(BaseModel):
    """
    sendMediaGroup method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat")
    media: "list[InputMediaAudio , InputMediaDocument , InputMediaPhoto and InputMediaVideo]" = Field(description="A JSON-serialized array describing messages to be sent, must include 2-10 items")
    disable_notification: None | bool = Field(default=None, description="Sends messages silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent messages from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
class sendMessage(BaseModel):
    """
    sendMessage method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    text: str = Field(description="Text of the message to be sent, 1-4096 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the message text. See formatting options for more details.")
    entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode")
    link_preview_options: "None | LinkPreviewOptions" = Field(default=None, description="Link preview generation options for the message")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendMessageDraft(BaseModel):
    """
    sendMessageDraft method from Telegram Bot API.
    """

    chat_id: int = Field(description="Unique identifier for the target private chat")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread")
    draft_id: int = Field(description="Unique identifier of the message draft; must be non-zero. Changes of drafts with the same identifier are animated")
    text: str = Field(description="Text of the message to be sent, 1-4096 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the message text. See formatting options for more details.")
    entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode")
class sendPaidMedia(BaseModel):
    """
    sendPaidMedia method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername ). If the chat is a channel, all Telegram Star proceeds from this media will be credited to the chat's balance. Otherwise, they will be credited to the bot's balance.")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    star_count: int = Field(description="The number of Telegram Stars that must be paid to buy access to the media; 1-25000")
    media: "list[InputPaidMedia]" = Field(description="A JSON-serialized array describing the media to be sent; up to 10 items")
    payload: None | str = Field(default=None, description="Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes.")
    caption: None | str = Field(default=None, description="Media caption, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the media caption. See formatting options for more details.")
    caption_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Pass True , if the caption must be shown above the message media")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendPhoto(BaseModel):
    """
    sendPhoto method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    photo: "InputFile | str" = Field(description="Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. More information on Sending Files »")
    caption: None | str = Field(default=None, description="Photo caption (may also be used when resending photos by file_id ), 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the photo caption. See formatting options for more details.")
    caption_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Pass True , if the caption must be shown above the message media")
    has_spoiler: None | bool = Field(default=None, description="Pass True if the photo needs to be covered with a spoiler animation")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendPoll(BaseModel):
    """
    sendPoll method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername ). Polls can't be sent to channel direct messages chats.")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    question: str = Field(description="Poll question, 1-300 characters")
    question_parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the question. See formatting options for more details. Currently, only custom emoji entities are allowed")
    question_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the poll question. It can be specified instead of question_parse_mode")
    options: "list[InputPollOption]" = Field(description="A JSON-serialized list of 2-12 answer options")
    is_anonymous: None | bool = Field(default=None, description="True , if the poll needs to be anonymous, defaults to True")
    type: None | str = Field(default=None, description="Poll type, “quiz” or “regular”, defaults to “regular”")
    allows_multiple_answers: None | bool = Field(default=None, description="True , if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False")
    correct_option_id: None | int = Field(default=None, description="0-based identifier of the correct answer option, required for polls in quiz mode")
    explanation: None | str = Field(default=None, description="Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing")
    explanation_parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the explanation. See formatting options for more details.")
    explanation_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the poll explanation. It can be specified instead of explanation_parse_mode")
    open_period: None | int = Field(default=None, description="Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date .")
    close_date: None | int = Field(default=None, description="Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period .")
    is_closed: None | bool = Field(default=None, description="Pass True if the poll needs to be immediately closed. This can be useful for poll preview.")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendVenue(BaseModel):
    """
    sendVenue method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    latitude: float = Field(description="Latitude of the venue")
    longitude: float = Field(description="Longitude of the venue")
    title: str = Field(description="Name of the venue")
    address: str = Field(description="Address of the venue")
    foursquare_id: None | str = Field(default=None, description="Foursquare identifier of the venue")
    foursquare_type: None | str = Field(default=None, description="Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)")
    google_place_id: None | str = Field(default=None, description="Google Places identifier of the venue")
    google_place_type: None | str = Field(default=None, description="Google Places type of the venue. (See supported types .)")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendVideo(BaseModel):
    """
    sendVideo method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    video: "InputFile | str" = Field(description="Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. More information on Sending Files »")
    duration: None | int = Field(default=None, description="Duration of sent video in seconds")
    width: None | int = Field(default=None, description="Video width")
    height: None | int = Field(default=None, description="Video height")
    thumbnail: "None | InputFile | str" = Field(default=None, description="Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    cover: "None | InputFile | str" = Field(default=None, description="Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
    start_timestamp: None | int = Field(default=None, description="Start timestamp for the video in the message")
    caption: None | str = Field(default=None, description="Video caption (may also be used when resending videos by file_id ), 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the video caption. See formatting options for more details.")
    caption_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Pass True , if the caption must be shown above the message media")
    has_spoiler: None | bool = Field(default=None, description="Pass True if the video needs to be covered with a spoiler animation")
    supports_streaming: None | bool = Field(default=None, description="Pass True if the uploaded video is suitable for streaming")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendVideoNote(BaseModel):
    """
    sendVideoNote method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    video_note: "InputFile | str" = Field(description="Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. More information on Sending Files » . Sending video notes by a URL is currently unsupported")
    duration: None | int = Field(default=None, description="Duration of sent video in seconds")
    length: None | int = Field(default=None, description="Video width and height, i.e. diameter of the video message")
    thumbnail: "None | InputFile | str" = Field(default=None, description="Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class sendVoice(BaseModel):
    """
    sendVoice method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    voice: "InputFile | str" = Field(description="Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files »")
    caption: None | str = Field(default=None, description="Voice message caption, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Mode for parsing entities in the voice message caption. See formatting options for more details.")
    caption_entities: "None | list[MessageEntity]" = Field(default=None, description="A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode")
    duration: None | int = Field(default=None, description="Duration of the voice message in seconds")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: "None | SuggestedPostParameters" = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: "None | ReplyParameters" = Field(default=None, description="Description of the message to reply to")
    reply_markup: "None | InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply" = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class setBusinessAccountBio(BaseModel):
    """
    setBusinessAccountBio method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    bio: None | str = Field(default=None, description="The new value of the bio for the business account; 0-140 characters")
class setBusinessAccountGiftSettings(BaseModel):
    """
    setBusinessAccountGiftSettings method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    show_gift_button: bool = Field(description="Pass True , if a button for sending a gift to the user or by the business account must always be shown in the input field")
    accepted_gift_types: "AcceptedGiftTypes" = Field(description="Types of gifts accepted by the business account")
class setBusinessAccountName(BaseModel):
    """
    setBusinessAccountName method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    first_name: str = Field(description="The new value of the first name for the business account; 1-64 characters")
    last_name: None | str = Field(default=None, description="The new value of the last name for the business account; 0-64 characters")
class setBusinessAccountProfilePhoto(BaseModel):
    """
    setBusinessAccountProfilePhoto method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    photo: "InputProfilePhoto" = Field(description="The new profile photo to set")
    is_public: None | bool = Field(default=None, description="Pass True to set the public photo, which will be visible even if the main photo is hidden by the business account's privacy settings. An account can have only one public photo.")
class setBusinessAccountUsername(BaseModel):
    """
    setBusinessAccountUsername method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    username: None | str = Field(default=None, description="The new value of the username for the business account; 0-32 characters")
class setChatAdministratorCustomTitle(BaseModel):
    """
    setChatAdministratorCustomTitle method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    user_id: int = Field(description="Unique identifier of the target user")
    custom_title: str = Field(description="New custom title for the administrator; 0-16 characters, emoji are not allowed")
class setChatDescription(BaseModel):
    """
    setChatDescription method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    description: None | str = Field(default=None, description="New chat description, 0-255 characters")
class setChatMemberTag(BaseModel):
    """
    setChatMemberTag method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    user_id: int = Field(description="Unique identifier of the target user")
    tag: None | str = Field(default=None, description="New tag for the member; 0-16 characters, emoji are not allowed")
class setChatMenuButton(BaseModel):
    """
    setChatMenuButton method from Telegram Bot API.
    """

    chat_id: None | int = Field(default=None, description="Unique identifier for the target private chat. If not specified, default bot's menu button will be changed")
    menu_button: "None | MenuButton" = Field(default=None, description="A JSON-serialized object for the bot's new menu button. Defaults to MenuButtonDefault")
class setChatPermissions(BaseModel):
    """
    setChatPermissions method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    permissions: "ChatPermissions" = Field(description="A JSON-serialized object for new default chat permissions")
    use_independent_chat_permissions: None | bool = Field(default=None, description="Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages , can_send_audios , can_send_documents , can_send_photos , can_send_videos , can_send_video_notes , and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.")
class setChatPhoto(BaseModel):
    """
    setChatPhoto method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    photo: "InputFile" = Field(description="New chat photo, uploaded using multipart/form-data")
class setChatStickerSet(BaseModel):
    """
    setChatStickerSet method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    sticker_set_name: str = Field(description="Name of the sticker set to be set as the group sticker set")
class setChatTitle(BaseModel):
    """
    setChatTitle method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    title: str = Field(description="New chat title, 1-128 characters")
class setMessageReaction(BaseModel):
    """
    setMessageReaction method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: int = Field(description="Identifier of the target message. If the message belongs to a media group, the reaction is set to the first non-deleted message in the group instead.")
    reaction: None | list[ReactionType] = Field(default=None, description="A JSON-serialized list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators. Paid reactions can't be used by bots.")
    is_big: None | bool = Field(default=None, description="Pass True to set the reaction with a big animation")
class setMyCommands(BaseModel):
    """
    setMyCommands method from Telegram Bot API.
    """

    commands: "list[BotCommand]" = Field(description="A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified.")
    scope: "None | BotCommandScope" = Field(default=None, description="A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault .")
    language_code: None | str = Field(default=None, description="A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands")
class setMyDefaultAdministratorRights(BaseModel):
    """
    setMyDefaultAdministratorRights method from Telegram Bot API.
    """

    rights: "None | ChatAdministratorRights" = Field(default=None, description="A JSON-serialized object describing new default administrator rights. If not specified, the default administrator rights will be cleared.")
    for_channels: None | bool = Field(default=None, description="Pass True to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed.")
class setMyDescription(BaseModel):
    """
    setMyDescription method from Telegram Bot API.
    """

    description: None | str = Field(default=None, description="New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language.")
    language_code: None | str = Field(default=None, description="A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description.")
class setMyName(BaseModel):
    """
    setMyName method from Telegram Bot API.
    """

    name: None | str = Field(default=None, description="New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language.")
    language_code: None | str = Field(default=None, description="A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose language there is no dedicated name.")
class setMyProfilePhoto(BaseModel):
    """
    setMyProfilePhoto method from Telegram Bot API.
    """

    photo: "InputProfilePhoto" = Field(description="The new profile photo to set")
class setMyShortDescription(BaseModel):
    """
    setMyShortDescription method from Telegram Bot API.
    """

    short_description: None | str = Field(default=None, description="New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language.")
    language_code: None | str = Field(default=None, description="A two-letter ISO 639-1 language code. If empty, the short description will be applied to all users for whose language there is no dedicated short description.")
class setUserEmojiStatus(BaseModel):
    """
    setUserEmojiStatus method from Telegram Bot API.
    """

    user_id: int = Field(description="Unique identifier of the target user")
    emoji_status_custom_emoji_id: None | str = Field(default=None, description="Custom emoji identifier of the emoji status to set. Pass an empty string to remove the status.")
    emoji_status_expiration_date: None | int = Field(default=None, description="Expiration date of the emoji status, if any")
class transferBusinessAccountStars(BaseModel):
    """
    transferBusinessAccountStars method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    star_count: int = Field(description="Number of Telegram Stars to transfer; 1-10000")
class transferGift(BaseModel):
    """
    transferGift method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    owned_gift_id: str = Field(description="Unique identifier of the regular gift that should be transferred")
    new_owner_chat_id: int = Field(description="Unique identifier of the chat which will own the gift. The chat must be active in the last 24 hours.")
    star_count: None | int = Field(default=None, description="The amount of Telegram Stars that will be paid for the transfer from the business account balance. If positive, then the can_transfer_stars business bot right is required.")
class unbanChatMember(BaseModel):
    """
    unbanChatMember method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername )")
    user_id: int = Field(description="Unique identifier of the target user")
    only_if_banned: None | bool = Field(default=None, description="Do nothing if the user is not banned")
class unbanChatSenderChat(BaseModel):
    """
    unbanChatSenderChat method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    sender_chat_id: int = Field(description="Unique identifier of the target sender chat")
class unhideGeneralForumTopic(BaseModel):
    """
    unhideGeneralForumTopic method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
class unpinAllChatMessages(BaseModel):
    """
    unpinAllChatMessages method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
class unpinAllForumTopicMessages(BaseModel):
    """
    unpinAllForumTopicMessages method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
    message_thread_id: int = Field(description="Unique identifier for the target message thread of the forum topic")
class unpinAllGeneralForumTopicMessages(BaseModel):
    """
    unpinAllGeneralForumTopicMessages method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername )")
class unpinChatMessage(BaseModel):
    """
    unpinChatMessage method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be unpinned")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_id: None | int = Field(default=None, description="Identifier of the message to unpin. Required if business_connection_id is specified. If not specified, the most recent pinned message (by sending date) will be unpinned.")
class upgradeGift(BaseModel):
    """
    upgradeGift method from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    owned_gift_id: str = Field(description="Unique identifier of the regular gift that should be upgraded to a unique one")
    keep_original_details: None | bool = Field(default=None, description="Pass True to keep the original gift text, sender and receiver in the upgraded gift")
    star_count: None | int = Field(default=None, description="The amount of Telegram Stars that will be paid for the upgrade from the business account balance. If gift.prepaid_upgrade_star_count > 0 , then pass 0, otherwise, the can_transfer_stars business bot right is required and gift.upgrade_star_count must be passed.")
class verifyChat(BaseModel):
    """
    verifyChat method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername ). Channel direct messages chats can't be verified.")
    custom_description: None | str = Field(default=None, description="Custom description for the verification; 0-70 characters. Must be empty if the organization isn't allowed to provide a custom verification description.")
class verifyUser(BaseModel):
    """
    verifyUser method from Telegram Bot API.
    """

    user_id: int = Field(description="Unique identifier of the target user")
    custom_description: None | str = Field(default=None, description="Custom description for the verification; 0-70 characters. Must be empty if the organization isn't allowed to provide a custom verification description.")
