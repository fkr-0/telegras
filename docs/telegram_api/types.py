"""Telegram Bot API models.

Auto-generated from API documentation.
This module contains Types.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

class Accentcolors(BaseModel):
    """
    Accentcolors type from Telegram Bot API.
    """
class AcceptedGiftTypes(BaseModel):
    """
    AcceptedGiftTypes type from Telegram Bot API.
    """

    unlimited_gifts: bool = Field(description="True , if unlimited regular gifts are accepted")
    limited_gifts: bool = Field(description="True , if limited regular gifts are accepted")
    unique_gifts: bool = Field(description="True , if unique gifts or gifts that can be upgraded to unique for free are accepted")
    premium_subscription: bool = Field(description="True , if a Telegram Premium subscription is accepted")
    gifts_from_channels: bool = Field(description="True , if transfers of unique gifts from channels are accepted")
class Animation(BaseModel):
    """
    Animation type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    width: int = Field(description="Video width as defined by the sender")
    height: int = Field(description="Video height as defined by the sender")
    duration: int = Field(description="Duration of the video in seconds as defined by the sender")
    thumbnail: "None | PhotoSize" = Field(default=None, description="Optional . Animation thumbnail as defined by the sender")
    file_name: None | str = Field(default=None, description="Optional . Original animation filename as defined by the sender")
    mime_type: None | str = Field(default=None, description="Optional . MIME type of the file as defined by the sender")
    file_size: None | int = Field(default=None, description="Optional . File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.")
class Audio(BaseModel):
    """
    Audio type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    duration: int = Field(description="Duration of the audio in seconds as defined by the sender")
    performer: None | str = Field(default=None, description="Optional . Performer of the audio as defined by the sender or by audio tags")
    title: None | str = Field(default=None, description="Optional . Title of the audio as defined by the sender or by audio tags")
    file_name: None | str = Field(default=None, description="Optional . Original filename as defined by the sender")
    mime_type: None | str = Field(default=None, description="Optional . MIME type of the file as defined by the sender")
    file_size: None | int = Field(default=None, description="Optional . File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.")
    thumbnail: "None | PhotoSize" = Field(default=None, description="Optional . Thumbnail of the album cover to which the music file belongs")
class BackgroundFill(BaseModel):
    """
    BackgroundFill type from Telegram Bot API.
    """

    type: str = Field(description="Type of the background fill, always “solid”")
    color: int = Field(description="The color of the background fill in the RGB24 format")
class BackgroundFillFreeformGradient(BaseModel):
    """
    BackgroundFillFreeformGradient type from Telegram Bot API.
    """

    type: str = Field(description="Type of the background fill, always “freeform_gradient”")
    colors: list[int] = Field(description="A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format")
class BackgroundFillGradient(BaseModel):
    """
    BackgroundFillGradient type from Telegram Bot API.
    """

    type: str = Field(description="Type of the background fill, always “gradient”")
    top_color: int = Field(description="Top color of the gradient in the RGB24 format")
    bottom_color: int = Field(description="Bottom color of the gradient in the RGB24 format")
    rotation_angle: int = Field(description="Clockwise rotation angle of the background fill in degrees; 0-359")
class BackgroundFillSolid(BaseModel):
    """
    BackgroundFillSolid type from Telegram Bot API.
    """

    type: str = Field(description="Type of the background fill, always “solid”")
    color: int = Field(description="The color of the background fill in the RGB24 format")
class BackgroundType(BaseModel):
    """
    BackgroundType type from Telegram Bot API.
    """

    type: str = Field(description="Type of the background, always “fill”")
    fill: "BackgroundFill" = Field(description="The background fill")
    dark_theme_dimming: int = Field(description="Dimming of the background in dark themes, as a percentage; 0-100")
class BackgroundTypeChatTheme(BaseModel):
    """
    BackgroundTypeChatTheme type from Telegram Bot API.
    """

    type: str = Field(description="Type of the background, always “chat_theme”")
    theme_name: str = Field(description="Name of the chat theme, which is usually an emoji")
class BackgroundTypeFill(BaseModel):
    """
    BackgroundTypeFill type from Telegram Bot API.
    """

    type: str = Field(description="Type of the background, always “fill”")
    fill: "BackgroundFill" = Field(description="The background fill")
    dark_theme_dimming: int = Field(description="Dimming of the background in dark themes, as a percentage; 0-100")
class BackgroundTypePattern(BaseModel):
    """
    BackgroundTypePattern type from Telegram Bot API.
    """

    type: str = Field(description="Type of the background, always “pattern”")
    document: "Document" = Field(description="Document with the pattern")
    fill: "BackgroundFill" = Field(description="The background fill that is combined with the pattern")
    intensity: int = Field(description="Intensity of the pattern when it is shown above the filled background; 0-100")
    is_inverted: None | bool = Field(default=None, description="Optional . True , if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only")
    is_moving: None | bool = Field(default=None, description="Optional . True , if the background moves slightly when the device is tilted")
class BackgroundTypeWallpaper(BaseModel):
    """
    BackgroundTypeWallpaper type from Telegram Bot API.
    """

    type: str = Field(description="Type of the background, always “wallpaper”")
    document: "Document" = Field(description="Document with the wallpaper")
    dark_theme_dimming: int = Field(description="Dimming of the background in dark themes, as a percentage; 0-100")
    is_blurred: None | bool = Field(default=None, description="Optional . True , if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12")
    is_moving: None | bool = Field(default=None, description="Optional . True , if the background moves slightly when the device is tilted")
class Birthdate(BaseModel):
    """
    Birthdate type from Telegram Bot API.
    """

    day: int = Field(description="Day of the user's birth; 1-31")
    month: int = Field(description="Month of the user's birth; 1-12")
    year: None | int = Field(default=None, description="Optional . Year of the user's birth")
class BotCommand(BaseModel):
    """
    BotCommand type from Telegram Bot API.
    """

    command: str = Field(description="Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores.")
    description: str = Field(description="Description of the command; 1-256 characters.")
class BotCommandScope(BaseModel):
    """
    BotCommandScope type from Telegram Bot API.
    """

    type: str = Field(description="Scope type, must be default")
class BotCommandScopeAllChatAdministrators(BaseModel):
    """
    BotCommandScopeAllChatAdministrators type from Telegram Bot API.
    """

    type: str = Field(description="Scope type, must be all_chat_administrators")
class BotCommandScopeAllGroupChats(BaseModel):
    """
    BotCommandScopeAllGroupChats type from Telegram Bot API.
    """

    type: str = Field(description="Scope type, must be all_group_chats")
class BotCommandScopeAllPrivateChats(BaseModel):
    """
    BotCommandScopeAllPrivateChats type from Telegram Bot API.
    """

    type: str = Field(description="Scope type, must be all_private_chats")
class BotCommandScopeChat(BaseModel):
    """
    BotCommandScopeChat type from Telegram Bot API.
    """

    type: str = Field(description="Scope type, must be chat")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername ). Channel direct messages chats and channel chats aren't supported.")
class BotCommandScopeChatAdministrators(BaseModel):
    """
    BotCommandScopeChatAdministrators type from Telegram Bot API.
    """

    type: str = Field(description="Scope type, must be chat_administrators")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername ). Channel direct messages chats and channel chats aren't supported.")
class BotCommandScopeChatMember(BaseModel):
    """
    BotCommandScopeChatMember type from Telegram Bot API.
    """

    type: str = Field(description="Scope type, must be chat_member")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername ). Channel direct messages chats and channel chats aren't supported.")
    user_id: int = Field(description="Unique identifier of the target user")
class BotCommandScopeDefault(BaseModel):
    """
    BotCommandScopeDefault type from Telegram Bot API.
    """

    type: str = Field(description="Scope type, must be default")
class BotDescription(BaseModel):
    """
    BotDescription type from Telegram Bot API.
    """

    description: str = Field(description="The bot's description")
class BotName(BaseModel):
    """
    BotName type from Telegram Bot API.
    """

    name: str = Field(description="The bot's name")
class BotShortDescription(BaseModel):
    """
    BotShortDescription type from Telegram Bot API.
    """

    short_description: str = Field(description="The bot's short description")
class BusinessBotRights(BaseModel):
    """
    BusinessBotRights type from Telegram Bot API.
    """

    can_reply: None | bool = Field(default=None, description="Optional . True , if the bot can send and edit messages in the private chats that had incoming messages in the last 24 hours")
    can_read_messages: None | bool = Field(default=None, description="Optional . True , if the bot can mark incoming private messages as read")
    can_delete_sent_messages: None | bool = Field(default=None, description="Optional . True , if the bot can delete messages sent by the bot")
    can_delete_all_messages: None | bool = Field(default=None, description="Optional . True , if the bot can delete all private messages in managed chats")
    can_edit_name: None | bool = Field(default=None, description="Optional . True , if the bot can edit the first and last name of the business account")
    can_edit_bio: None | bool = Field(default=None, description="Optional . True , if the bot can edit the bio of the business account")
    can_edit_profile_photo: None | bool = Field(default=None, description="Optional . True , if the bot can edit the profile photo of the business account")
    can_edit_username: None | bool = Field(default=None, description="Optional . True , if the bot can edit the username of the business account")
    can_change_gift_settings: None | bool = Field(default=None, description="Optional . True , if the bot can change the privacy settings pertaining to gifts for the business account")
    can_view_gifts_and_stars: None | bool = Field(default=None, description="Optional . True , if the bot can view gifts and the amount of Telegram Stars owned by the business account")
    can_convert_gifts_to_stars: None | bool = Field(default=None, description="Optional . True , if the bot can convert regular gifts owned by the business account to Telegram Stars")
    can_transfer_and_upgrade_gifts: None | bool = Field(default=None, description="Optional . True , if the bot can transfer and upgrade gifts owned by the business account")
    can_transfer_stars: None | bool = Field(default=None, description="Optional . True , if the bot can transfer Telegram Stars received by the business account to its own account, or use them to upgrade and transfer gifts")
    can_manage_stories: None | bool = Field(default=None, description="Optional . True , if the bot can post, edit and delete stories on behalf of the business account")
class BusinessConnection(BaseModel):
    """
    BusinessConnection type from Telegram Bot API.
    """

    id: str = Field(description="Unique identifier of the business connection")
    user: "User" = Field(description="Business account user that created the business connection")
    user_chat_id: int = Field(description="Identifier of a private chat with the user who created the business connection. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.")
    date: int = Field(description="Date the connection was established in Unix time")
    rights: "None | BusinessBotRights" = Field(default=None, description="Optional . Rights of the business bot")
    is_enabled: bool = Field(description="True , if the connection is active")
class BusinessIntro(BaseModel):
    """
    BusinessIntro type from Telegram Bot API.
    """

    title: None | str = Field(default=None, description="Optional . Title text of the business intro")
    message: None | str = Field(default=None, description="Optional . Message text of the business intro")
    sticker: "None | Sticker" = Field(default=None, description="Optional . Sticker of the business intro")
class BusinessLocation(BaseModel):
    """
    BusinessLocation type from Telegram Bot API.
    """

    address: str = Field(description="Address of the business")
    location: "None | Location" = Field(default=None, description="Optional . Location of the business")
class BusinessMessagesDeleted(BaseModel):
    """
    BusinessMessagesDeleted type from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    chat: "Chat" = Field(description="Information about a chat in the business account. The bot may not have access to the chat or the corresponding user.")
    message_ids: list[int] = Field(description="The list of identifiers of deleted messages in the chat of the business account")
class BusinessOpeningHours(BaseModel):
    """
    BusinessOpeningHours type from Telegram Bot API.
    """

    time_zone_name: str = Field(description="Unique name of the time zone for which the opening hours are defined")
    opening_hours: "list[BusinessOpeningHoursInterval]" = Field(description="List of time intervals describing business opening hours")
class BusinessOpeningHoursInterval(BaseModel):
    """
    BusinessOpeningHoursInterval type from Telegram Bot API.
    """

    opening_minute: int = Field(description="The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 * 24 * 60")
    closing_minute: int = Field(description="The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 * 24 * 60")
class CallbackQuery(BaseModel):
    """
    CallbackQuery type from Telegram Bot API.
    """

    id: str = Field(description="Unique identifier for this query")
    from_: "User" = Field(description="Sender")
    message: "None | MaybeInaccessibleMessage" = Field(default=None, description="Optional . Message sent by the bot with the callback button that originated the query")
    inline_message_id: None | str = Field(default=None, description="Optional . Identifier of the message sent via the bot in inline mode, that originated the query.")
    chat_instance: str = Field(description="Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games .")
    data: None | str = Field(default=None, description="Optional . Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data.")
    game_short_name: None | str = Field(default=None, description="Optional . Short name of a Game to be returned, serves as the unique identifier for the game")
class Chat(BaseModel):
    """
    Chat type from Telegram Bot API.
    """

    id: int = Field(description="Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.")
    type: str = Field(description="Type of the chat, can be either “private”, “group”, “supergroup” or “channel”")
    title: None | str = Field(default=None, description="Optional . Title, for supergroups, channels and group chats")
    username: None | str = Field(default=None, description="Optional . Username, for private chats, supergroups and channels if available")
    first_name: None | str = Field(default=None, description="Optional . First name of the other party in a private chat")
    last_name: None | str = Field(default=None, description="Optional . Last name of the other party in a private chat")
    is_forum: None | bool = Field(default=None, description="Optional . True , if the supergroup chat is a forum (has topics enabled)")
    is_direct_messages: None | bool = Field(default=None, description="Optional . True , if the chat is the direct messages chat of a channel")
class ChatAdministratorRights(BaseModel):
    """
    ChatAdministratorRights type from Telegram Bot API.
    """

    is_anonymous: bool = Field(description="True , if the user's presence in the chat is hidden")
    can_manage_chat: bool = Field(description="True , if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages, ignore slow mode, and send messages to the chat without paying Telegram Stars. Implied by any other administrator privilege.")
    can_delete_messages: bool = Field(description="True , if the administrator can delete messages of other users")
    can_manage_video_chats: bool = Field(description="True , if the administrator can manage video chats")
    can_restrict_members: bool = Field(description="True , if the administrator can restrict, ban or unban chat members, or access supergroup statistics")
    can_promote_members: bool = Field(description="True , if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user)")
    can_change_info: bool = Field(description="True , if the user is allowed to change the chat title, photo and other settings")
    can_invite_users: bool = Field(description="True , if the user is allowed to invite new users to the chat")
    can_post_stories: bool = Field(description="True , if the administrator can post stories to the chat")
    can_edit_stories: bool = Field(description="True , if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive")
    can_delete_stories: bool = Field(description="True , if the administrator can delete stories posted by other users")
    can_post_messages: None | bool = Field(default=None, description="Optional . True , if the administrator can post messages in the channel, approve suggested posts, or access channel statistics; for channels only")
    can_edit_messages: None | bool = Field(default=None, description="Optional . True , if the administrator can edit messages of other users and can pin messages; for channels only")
    can_pin_messages: None | bool = Field(default=None, description="Optional . True , if the user is allowed to pin messages; for groups and supergroups only")
    can_manage_topics: None | bool = Field(default=None, description="Optional . True , if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only")
    can_manage_direct_messages: None | bool = Field(default=None, description="Optional . True , if the administrator can manage direct messages of the channel and decline suggested posts; for channels only")
    can_manage_tags: None | bool = Field(default=None, description="Optional . True , if the administrator can edit the tags of regular members; for groups and supergroups only. If omitted defaults to the value of can_pin_messages.")
class ChatBackground(BaseModel):
    """
    ChatBackground type from Telegram Bot API.
    """

    type: "BackgroundType" = Field(description="Type of the background")
class ChatBoost(BaseModel):
    """
    ChatBoost type from Telegram Bot API.
    """

    boost_id: str = Field(description="Unique identifier of the boost")
    add_date: int = Field(description="Point in time (Unix timestamp) when the chat was boosted")
    expiration_date: int = Field(description="Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged")
    source: "ChatBoostSource" = Field(description="Source of the added boost")
class ChatBoostAdded(BaseModel):
    """
    ChatBoostAdded type from Telegram Bot API.
    """

    boost_count: int = Field(description="Number of boosts added by the user")
class ChatBoostRemoved(BaseModel):
    """
    ChatBoostRemoved type from Telegram Bot API.
    """

    chat: "Chat" = Field(description="Chat which was boosted")
    boost_id: str = Field(description="Unique identifier of the boost")
    remove_date: int = Field(description="Point in time (Unix timestamp) when the boost was removed")
    source: "ChatBoostSource" = Field(description="Source of the removed boost")
class ChatBoostSource(BaseModel):
    """
    ChatBoostSource type from Telegram Bot API.
    """

    source: str = Field(description="Source of the boost, always “premium”")
    user: "User" = Field(description="User that boosted the chat")
class ChatBoostSourceGiftCode(BaseModel):
    """
    ChatBoostSourceGiftCode type from Telegram Bot API.
    """

    source: str = Field(description="Source of the boost, always “gift_code”")
    user: "User" = Field(description="User for which the gift code was created")
class ChatBoostSourceGiveaway(BaseModel):
    """
    ChatBoostSourceGiveaway type from Telegram Bot API.
    """

    source: str = Field(description="Source of the boost, always “giveaway”")
    giveaway_message_id: int = Field(description="Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn't sent yet.")
    user: "None | User" = Field(default=None, description="Optional . User that won the prize in the giveaway if any; for Telegram Premium giveaways only")
    prize_star_count: None | int = Field(default=None, description="Optional . The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only")
    is_unclaimed: None | bool = Field(default=None, description="Optional . True , if the giveaway was completed, but there was no user to win the prize")
class ChatBoostSourcePremium(BaseModel):
    """
    ChatBoostSourcePremium type from Telegram Bot API.
    """

    source: str = Field(description="Source of the boost, always “premium”")
    user: "User" = Field(description="User that boosted the chat")
class ChatBoostUpdated(BaseModel):
    """
    ChatBoostUpdated type from Telegram Bot API.
    """

    chat: "Chat" = Field(description="Chat which was boosted")
    boost: "ChatBoost" = Field(description="Information about the chat boost")
class ChatFullInfo(BaseModel):
    """
    ChatFullInfo type from Telegram Bot API.
    """

    id: int = Field(description="Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.")
    type: str = Field(description="Type of the chat, can be either “private”, “group”, “supergroup” or “channel”")
    title: None | str = Field(default=None, description="Optional . Title, for supergroups, channels and group chats")
    username: None | str = Field(default=None, description="Optional . Username, for private chats, supergroups and channels if available")
    first_name: None | str = Field(default=None, description="Optional . First name of the other party in a private chat")
    last_name: None | str = Field(default=None, description="Optional . Last name of the other party in a private chat")
    is_forum: None | bool = Field(default=None, description="Optional . True , if the supergroup chat is a forum (has topics enabled)")
    is_direct_messages: None | bool = Field(default=None, description="Optional . True , if the chat is the direct messages chat of a channel")
    accent_color_id: int = Field(description="Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See accent colors for more details.")
    max_reaction_count: int = Field(description="The maximum number of reactions that can be set on a message in the chat")
    photo: "None | ChatPhoto" = Field(default=None, description="Optional . Chat photo")
    active_usernames: None | list[str] = Field(default=None, description="Optional . If non-empty, the list of all active chat usernames ; for private chats, supergroups and channels")
    birthdate: "None | Birthdate" = Field(default=None, description="Optional . For private chats, the date of birth of the user")
    business_intro: "None | BusinessIntro" = Field(default=None, description="Optional . For private chats with business accounts, the intro of the business")
    business_location: "None | BusinessLocation" = Field(default=None, description="Optional . For private chats with business accounts, the location of the business")
    business_opening_hours: "None | BusinessOpeningHours" = Field(default=None, description="Optional . For private chats with business accounts, the opening hours of the business")
    personal_chat: "None | Chat" = Field(default=None, description="Optional . For private chats, the personal channel of the user")
    parent_chat: "None | Chat" = Field(default=None, description="Optional . Information about the corresponding channel chat; for direct messages chats only")
    available_reactions: None | list[ReactionType] = Field(default=None, description="Optional . List of available reactions allowed in the chat. If omitted, then all emoji reactions are allowed.")
    background_custom_emoji_id: None | str = Field(default=None, description="Optional . Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background")
    profile_accent_color_id: None | int = Field(default=None, description="Optional . Identifier of the accent color for the chat's profile background. See profile accent colors for more details.")
    profile_background_custom_emoji_id: None | str = Field(default=None, description="Optional . Custom emoji identifier of the emoji chosen by the chat for its profile background")
    emoji_status_custom_emoji_id: None | str = Field(default=None, description="Optional . Custom emoji identifier of the emoji status of the chat or the other party in a private chat")
    emoji_status_expiration_date: None | int = Field(default=None, description="Optional . Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any")
    bio: None | str = Field(default=None, description="Optional . Bio of the other party in a private chat")
    has_private_forwards: None | bool = Field(default=None, description="Optional . True , if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user")
    has_restricted_voice_and_video_messages: None | bool = Field(default=None, description="Optional . True , if the privacy settings of the other party restrict sending voice and video note messages in the private chat")
    join_to_send_messages: None | bool = Field(default=None, description="Optional . True , if users need to join the supergroup before they can send messages")
    join_by_request: None | bool = Field(default=None, description="Optional . True , if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators")
    description: None | str = Field(default=None, description="Optional . Description, for groups, supergroups and channel chats")
    invite_link: None | str = Field(default=None, description="Optional . Primary invite link, for groups, supergroups and channel chats")
    pinned_message: "None | Message" = Field(default=None, description="Optional . The most recent pinned message (by sending date)")
    permissions: "None | ChatPermissions" = Field(default=None, description="Optional . Default chat member permissions, for groups and supergroups")
    accepted_gift_types: "AcceptedGiftTypes" = Field(description="Information about types of gifts that are accepted by the chat or by the corresponding user for private chats")
    can_send_paid_media: None | bool = Field(default=None, description="Optional . True , if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats.")
    slow_mode_delay: None | int = Field(default=None, description="Optional . For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds")
    unrestrict_boost_count: None | int = Field(default=None, description="Optional . For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions")
    message_auto_delete_time: None | int = Field(default=None, description="Optional . The time after which all messages sent to the chat will be automatically deleted; in seconds")
    has_aggressive_anti_spam_enabled: None | bool = Field(default=None, description="Optional . True , if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators.")
    has_hidden_members: None | bool = Field(default=None, description="Optional . True , if non-administrators can only get the list of bots and administrators in the chat")
    has_protected_content: None | bool = Field(default=None, description="Optional . True , if messages from the chat can't be forwarded to other chats")
    has_visible_history: None | bool = Field(default=None, description="Optional . True , if new chat members will have access to old messages; available only to chat administrators")
    sticker_set_name: None | str = Field(default=None, description="Optional . For supergroups, name of the group sticker set")
    can_set_sticker_set: None | bool = Field(default=None, description="Optional . True , if the bot can change the group sticker set")
    custom_emoji_sticker_set_name: None | str = Field(default=None, description="Optional . For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group.")
    linked_chat_id: None | int = Field(default=None, description="Optional . Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.")
    location: "None | ChatLocation" = Field(default=None, description="Optional . For supergroups, the location to which the supergroup is connected")
    rating: "None | UserRating" = Field(default=None, description="Optional . For private chats, the rating of the user if any")
    first_profile_audio: "None | Audio" = Field(default=None, description="Optional . For private chats, the first audio added to the profile of the user")
    unique_gift_colors: "None | UniqueGiftColors" = Field(default=None, description="Optional . The color scheme based on a unique gift that must be used for the chat's name, message replies and link previews")
    paid_message_star_count: None | int = Field(default=None, description="Optional . The number of Telegram Stars a general user have to pay to send a message to the chat")
class ChatInviteLink(BaseModel):
    """
    ChatInviteLink type from Telegram Bot API.
    """

    invite_link: str = Field(description="The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”.")
    creator: "User" = Field(description="Creator of the link")
    creates_join_request: bool = Field(description="True , if users joining the chat via the link need to be approved by chat administrators")
    is_primary: bool = Field(description="True , if the link is primary")
    is_revoked: bool = Field(description="True , if the link is revoked")
    name: None | str = Field(default=None, description="Optional . Invite link name")
    expire_date: None | int = Field(default=None, description="Optional . Point in time (Unix timestamp) when the link will expire or has been expired")
    member_limit: None | int = Field(default=None, description="Optional . The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999")
    pending_join_request_count: None | int = Field(default=None, description="Optional . Number of pending join requests created using this link")
    subscription_period: None | int = Field(default=None, description="Optional . The number of seconds the subscription will be active for before the next payment")
    subscription_price: None | int = Field(default=None, description="Optional . The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat using the link")
class ChatJoinRequest(BaseModel):
    """
    ChatJoinRequest type from Telegram Bot API.
    """

    chat: "Chat" = Field(description="Chat to which the request was sent")
    from_: "User" = Field(description="User that sent the join request")
    user_chat_id: int = Field(description="Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user.")
    date: int = Field(description="Date the request was sent in Unix time")
    bio: None | str = Field(default=None, description="Optional . Bio of the user.")
    invite_link: "None | ChatInviteLink" = Field(default=None, description="Optional . Chat invite link that was used by the user to send the join request")
class ChatLocation(BaseModel):
    """
    ChatLocation type from Telegram Bot API.
    """

    location: "Location" = Field(description="The location to which the supergroup is connected. Can't be a live location.")
    address: str = Field(description="Location address; 1-64 characters, as defined by the chat owner")
class ChatMember(BaseModel):
    """
    ChatMember type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “creator”")
    user: "User" = Field(description="Information about the user")
    is_anonymous: bool = Field(description="True , if the user's presence in the chat is hidden")
    custom_title: None | str = Field(default=None, description="Optional . Custom title for this user")
class ChatMemberAdministrator(BaseModel):
    """
    ChatMemberAdministrator type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “administrator”")
    user: "User" = Field(description="Information about the user")
    can_be_edited: bool = Field(description="True , if the bot is allowed to edit administrator privileges of that user")
    is_anonymous: bool = Field(description="True , if the user's presence in the chat is hidden")
    can_manage_chat: bool = Field(description="True , if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages, ignore slow mode, and send messages to the chat without paying Telegram Stars. Implied by any other administrator privilege.")
    can_delete_messages: bool = Field(description="True , if the administrator can delete messages of other users")
    can_manage_video_chats: bool = Field(description="True , if the administrator can manage video chats")
    can_restrict_members: bool = Field(description="True , if the administrator can restrict, ban or unban chat members, or access supergroup statistics")
    can_promote_members: bool = Field(description="True , if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user)")
    can_change_info: bool = Field(description="True , if the user is allowed to change the chat title, photo and other settings")
    can_invite_users: bool = Field(description="True , if the user is allowed to invite new users to the chat")
    can_post_stories: bool = Field(description="True , if the administrator can post stories to the chat")
    can_edit_stories: bool = Field(description="True , if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive")
    can_delete_stories: bool = Field(description="True , if the administrator can delete stories posted by other users")
    can_post_messages: None | bool = Field(default=None, description="Optional . True , if the administrator can post messages in the channel, approve suggested posts, or access channel statistics; for channels only")
    can_edit_messages: None | bool = Field(default=None, description="Optional . True , if the administrator can edit messages of other users and can pin messages; for channels only")
    can_pin_messages: None | bool = Field(default=None, description="Optional . True , if the user is allowed to pin messages; for groups and supergroups only")
    can_manage_topics: None | bool = Field(default=None, description="Optional . True , if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only")
    can_manage_direct_messages: None | bool = Field(default=None, description="Optional . True , if the administrator can manage direct messages of the channel and decline suggested posts; for channels only")
    can_manage_tags: None | bool = Field(default=None, description="Optional . True , if the administrator can edit the tags of regular members; for groups and supergroups only. If omitted defaults to the value of can_pin_messages.")
    custom_title: None | str = Field(default=None, description="Optional . Custom title for this user")
class ChatMemberBanned(BaseModel):
    """
    ChatMemberBanned type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “kicked”")
    user: "User" = Field(description="Information about the user")
    until_date: int = Field(description="Date when restrictions will be lifted for this user; Unix time. If 0, then the user is banned forever")
class ChatMemberLeft(BaseModel):
    """
    ChatMemberLeft type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “left”")
    user: "User" = Field(description="Information about the user")
class ChatMemberMember(BaseModel):
    """
    ChatMemberMember type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “member”")
    tag: None | str = Field(default=None, description="Optional . Tag of the member")
    user: "User" = Field(description="Information about the user")
    until_date: None | int = Field(default=None, description="Optional . Date when the user's subscription will expire; Unix time")
class ChatMemberOwner(BaseModel):
    """
    ChatMemberOwner type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “creator”")
    user: "User" = Field(description="Information about the user")
    is_anonymous: bool = Field(description="True , if the user's presence in the chat is hidden")
    custom_title: None | str = Field(default=None, description="Optional . Custom title for this user")
class ChatMemberRestricted(BaseModel):
    """
    ChatMemberRestricted type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “restricted”")
    tag: None | str = Field(default=None, description="Optional . Tag of the member")
    user: "User" = Field(description="Information about the user")
    is_member: bool = Field(description="True , if the user is a member of the chat at the moment of the request")
    can_send_messages: bool = Field(description="True , if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues")
    can_send_audios: bool = Field(description="True , if the user is allowed to send audios")
    can_send_documents: bool = Field(description="True , if the user is allowed to send documents")
    can_send_photos: bool = Field(description="True , if the user is allowed to send photos")
    can_send_videos: bool = Field(description="True , if the user is allowed to send videos")
    can_send_video_notes: bool = Field(description="True , if the user is allowed to send video notes")
    can_send_voice_notes: bool = Field(description="True , if the user is allowed to send voice notes")
    can_send_polls: bool = Field(description="True , if the user is allowed to send polls and checklists")
    can_send_other_messages: bool = Field(description="True , if the user is allowed to send animations, games, stickers and use inline bots")
    can_add_web_page_previews: bool = Field(description="True , if the user is allowed to add web page previews to their messages")
    can_edit_tag: bool = Field(description="True , if the user is allowed to edit their own tag")
    can_change_info: bool = Field(description="True , if the user is allowed to change the chat title, photo and other settings")
    can_invite_users: bool = Field(description="True , if the user is allowed to invite new users to the chat")
    can_pin_messages: bool = Field(description="True , if the user is allowed to pin messages")
    can_manage_topics: bool = Field(description="True , if the user is allowed to create forum topics")
    until_date: int = Field(description="Date when restrictions will be lifted for this user; Unix time. If 0, then the user is restricted forever")
class ChatMemberUpdated(BaseModel):
    """
    ChatMemberUpdated type from Telegram Bot API.
    """

    chat: "Chat" = Field(description="Chat the user belongs to")
    from_: "User" = Field(description="Performer of the action, which resulted in the change")
    date: int = Field(description="Date the change was done in Unix time")
    old_chat_member: "ChatMember" = Field(description="Previous information about the chat member")
    new_chat_member: "ChatMember" = Field(description="New information about the chat member")
    invite_link: "None | ChatInviteLink" = Field(default=None, description="Optional . Chat invite link, which was used by the user to join the chat; for joining by invite link events only.")
    via_join_request: None | bool = Field(default=None, description="Optional . True , if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator")
    via_chat_folder_invite_link: None | bool = Field(default=None, description="Optional . True , if the user joined the chat via a chat folder invite link")
class ChatOwnerChanged(BaseModel):
    """
    ChatOwnerChanged type from Telegram Bot API.
    """

    new_owner: "User" = Field(description="The new owner of the chat")
class ChatOwnerLeft(BaseModel):
    """
    ChatOwnerLeft type from Telegram Bot API.
    """

    new_owner: "None | User" = Field(default=None, description="Optional . The user which will be the new owner of the chat if the previous owner does not return to the chat")
class ChatPermissions(BaseModel):
    """
    ChatPermissions type from Telegram Bot API.
    """

    can_send_messages: None | bool = Field(default=None, description="Optional . True , if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues")
    can_send_audios: None | bool = Field(default=None, description="Optional . True , if the user is allowed to send audios")
    can_send_documents: None | bool = Field(default=None, description="Optional . True , if the user is allowed to send documents")
    can_send_photos: None | bool = Field(default=None, description="Optional . True , if the user is allowed to send photos")
    can_send_videos: None | bool = Field(default=None, description="Optional . True , if the user is allowed to send videos")
    can_send_video_notes: None | bool = Field(default=None, description="Optional . True , if the user is allowed to send video notes")
    can_send_voice_notes: None | bool = Field(default=None, description="Optional . True , if the user is allowed to send voice notes")
    can_send_polls: None | bool = Field(default=None, description="Optional . True , if the user is allowed to send polls and checklists")
    can_send_other_messages: None | bool = Field(default=None, description="Optional . True , if the user is allowed to send animations, games, stickers and use inline bots")
    can_add_web_page_previews: None | bool = Field(default=None, description="Optional . True , if the user is allowed to add web page previews to their messages")
    can_edit_tag: None | bool = Field(default=None, description="Optional . True , if the user is allowed to edit their own tag")
    can_change_info: None | bool = Field(default=None, description="Optional . True , if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups")
    can_invite_users: None | bool = Field(default=None, description="Optional . True , if the user is allowed to invite new users to the chat")
    can_pin_messages: None | bool = Field(default=None, description="Optional . True , if the user is allowed to pin messages. Ignored in public supergroups")
    can_manage_topics: None | bool = Field(default=None, description="Optional . True , if the user is allowed to create forum topics. If omitted defaults to the value of can_pin_messages")
class ChatPhoto(BaseModel):
    """
    ChatPhoto type from Telegram Bot API.
    """

    small_file_id: str = Field(description="File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.")
    small_file_unique_id: str = Field(description="Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    big_file_id: str = Field(description="File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.")
    big_file_unique_id: str = Field(description="Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
class ChatShared(BaseModel):
    """
    ChatShared type from Telegram Bot API.
    """

    request_id: int = Field(description="Identifier of the request")
    chat_id: int = Field(description="Identifier of the shared chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the chat and could be unable to use this identifier, unless the chat is already known to the bot by some other means.")
    title: None | str = Field(default=None, description="Optional . Title of the chat, if the title was requested by the bot.")
    username: None | str = Field(default=None, description="Optional . Username of the chat, if the username was requested by the bot and available.")
    photo: None | list[PhotoSize] = Field(default=None, description="Optional . Available sizes of the chat photo, if the photo was requested by the bot")
class Checklist(BaseModel):
    """
    Checklist type from Telegram Bot API.
    """

    title: str = Field(description="Title of the checklist")
    title_entities: None | list[MessageEntity] = Field(default=None, description="Optional . Special entities that appear in the checklist title")
    tasks: "list[ChecklistTask]" = Field(description="List of tasks in the checklist")
    others_can_add_tasks: None | bool = Field(default=None, description="Optional . True , if users other than the creator of the list can add tasks to the list")
    others_can_mark_tasks_as_done: None | bool = Field(default=None, description="Optional . True , if users other than the creator of the list can mark tasks as done or not done")
class ChecklistTask(BaseModel):
    """
    ChecklistTask type from Telegram Bot API.
    """

    id: int = Field(description="Unique identifier of the task")
    text: str = Field(description="Text of the task")
    text_entities: None | list[MessageEntity] = Field(default=None, description="Optional . Special entities that appear in the task text")
    completed_by_user: "None | User" = Field(default=None, description="Optional . User that completed the task; omitted if the task wasn't completed by a user")
    completed_by_chat: "None | Chat" = Field(default=None, description="Optional . Chat that completed the task; omitted if the task wasn't completed by a chat")
    completion_date: None | int = Field(default=None, description="Optional . Point in time (Unix timestamp) when the task was completed; 0 if the task wasn't completed")
class ChecklistTasksAdded(BaseModel):
    """
    ChecklistTasksAdded type from Telegram Bot API.
    """

    checklist_message: "None | Message" = Field(default=None, description="Optional . Message containing the checklist to which the tasks were added. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    tasks: "list[ChecklistTask]" = Field(description="List of tasks added to the checklist")
class ChecklistTasksDone(BaseModel):
    """
    ChecklistTasksDone type from Telegram Bot API.
    """

    checklist_message: "None | Message" = Field(default=None, description="Optional . Message containing the checklist whose tasks were marked as done or not done. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    marked_as_done_task_ids: None | list[int] = Field(default=None, description="Optional . Identifiers of the tasks that were marked as done")
    marked_as_not_done_task_ids: None | list[int] = Field(default=None, description="Optional . Identifiers of the tasks that were marked as not done")
class Contact(BaseModel):
    """
    Contact type from Telegram Bot API.
    """

    phone_number: str = Field(description="Contact's phone number")
    first_name: str = Field(description="Contact's first name")
    last_name: None | str = Field(default=None, description="Optional . Contact's last name")
    user_id: None | int = Field(default=None, description="Optional . Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.")
    vcard: None | str = Field(default=None, description="Optional . Additional data about the contact in the form of a vCard")
class CopyTextButton(BaseModel):
    """
    CopyTextButton type from Telegram Bot API.
    """

    text: str = Field(description="The text to be copied to the clipboard; 1-256 characters")
class Determininglistofcommands(BaseModel):
    """
    Determininglistofcommands type from Telegram Bot API.
    """

    type: str = Field(description="Scope type, must be default")
class Dice(BaseModel):
    """
    Dice type from Telegram Bot API.
    """

    emoji: str = Field(description="Emoji on which the dice throw animation is based")
    value: int = Field(description="Value of the dice, 1-6 for “ ”, “ ” and “ ” base emoji, 1-5 for “ ” and “ ” base emoji, 1-64 for “ ” base emoji")
class DirectMessagePriceChanged(BaseModel):
    """
    DirectMessagePriceChanged type from Telegram Bot API.
    """

    are_direct_messages_enabled: bool = Field(description="True , if direct messages are enabled for the channel chat; false otherwise")
    direct_message_star_count: None | int = Field(default=None, description="Optional . The new number of Telegram Stars that must be paid by users for each direct message sent to the channel. Does not apply to users who have been exempted by administrators. Defaults to 0.")
class DirectMessagesTopic(BaseModel):
    """
    DirectMessagesTopic type from Telegram Bot API.
    """

    topic_id: int = Field(description="Unique identifier of the topic. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.")
    user: "None | User" = Field(default=None, description="Optional . Information about the user that created the topic. Currently, it is always present")
class Document(BaseModel):
    """
    Document type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    thumbnail: "None | PhotoSize" = Field(default=None, description="Optional . Document thumbnail as defined by the sender")
    file_name: None | str = Field(default=None, description="Optional . Original filename as defined by the sender")
    mime_type: None | str = Field(default=None, description="Optional . MIME type of the file as defined by the sender")
    file_size: None | int = Field(default=None, description="Optional . File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.")
class ExternalReplyInfo(BaseModel):
    """
    ExternalReplyInfo type from Telegram Bot API.
    """

    origin: "MessageOrigin" = Field(description="Origin of the message replied to by the given message")
    chat: "None | Chat" = Field(default=None, description="Optional . Chat the original message belongs to. Available only if the chat is a supergroup or a channel.")
    message_id: None | int = Field(default=None, description="Optional . Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.")
    link_preview_options: "None | LinkPreviewOptions" = Field(default=None, description="Optional . Options used for link preview generation for the original message, if it is a text message")
    animation: "None | Animation" = Field(default=None, description="Optional . Message is an animation, information about the animation")
    audio: "None | Audio" = Field(default=None, description="Optional . Message is an audio file, information about the file")
    document: "None | Document" = Field(default=None, description="Optional . Message is a general file, information about the file")
    paid_media: "None | PaidMediaInfo" = Field(default=None, description="Optional . Message contains paid media; information about the paid media")
    photo: None | list[PhotoSize] = Field(default=None, description="Optional . Message is a photo, available sizes of the photo")
    sticker: "None | Sticker" = Field(default=None, description="Optional . Message is a sticker, information about the sticker")
    story: "None | Story" = Field(default=None, description="Optional . Message is a forwarded story")
    video: "None | Video" = Field(default=None, description="Optional . Message is a video, information about the video")
    video_note: "None | VideoNote" = Field(default=None, description="Optional . Message is a video note , information about the video message")
    voice: "None | Voice" = Field(default=None, description="Optional . Message is a voice message, information about the file")
    has_media_spoiler: None | bool = Field(default=None, description="Optional . True , if the message media is covered by a spoiler animation")
    checklist: "None | Checklist" = Field(default=None, description="Optional . Message is a checklist")
    contact: "None | Contact" = Field(default=None, description="Optional . Message is a shared contact, information about the contact")
    dice: "None | Dice" = Field(default=None, description="Optional . Message is a dice with random value")
    game: "None | Game" = Field(default=None, description="Optional . Message is a game, information about the game. More about games »")
    giveaway: "None | Giveaway" = Field(default=None, description="Optional . Message is a scheduled giveaway, information about the giveaway")
    giveaway_winners: "None | GiveawayWinners" = Field(default=None, description="Optional . A giveaway with public winners was completed")
    invoice: "None | Invoice" = Field(default=None, description="Optional . Message is an invoice for a payment , information about the invoice. More about payments »")
    location: "None | Location" = Field(default=None, description="Optional . Message is a shared location, information about the location")
    poll: "None | Poll" = Field(default=None, description="Optional . Message is a native poll, information about the poll")
    venue: "None | Venue" = Field(default=None, description="Optional . Message is a venue, information about the venue")
class File(BaseModel):
    """
    File type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    file_size: None | int = Field(default=None, description="Optional . File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.")
    file_path: None | str = Field(default=None, description="Optional . File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.")
class ForceReply(BaseModel):
    """
    ForceReply type from Telegram Bot API.
    """

    force_reply: bool = Field(description="Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'")
    input_field_placeholder: None | str = Field(default=None, description="Optional . The placeholder to be shown in the input field when the reply is active; 1-64 characters")
    selective: None | bool = Field(default=None, description="Optional . Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message.")
class ForumTopic(BaseModel):
    """
    ForumTopic type from Telegram Bot API.
    """

    message_thread_id: int = Field(description="Unique identifier of the forum topic")
    name: str = Field(description="Name of the topic")
    icon_color: int = Field(description="Color of the topic icon in RGB format")
    icon_custom_emoji_id: None | str = Field(default=None, description="Optional . Unique identifier of the custom emoji shown as the topic icon")
    is_name_implicit: None | bool = Field(default=None, description="Optional . True , if the name of the topic wasn't specified explicitly by its creator and likely needs to be changed by the bot")
class ForumTopicClosed(BaseModel):
    """
    ForumTopicClosed type from Telegram Bot API.
    """

    name: None | str = Field(default=None, description="Optional . New name of the topic, if it was edited")
    icon_custom_emoji_id: None | str = Field(default=None, description="Optional . New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed")
class ForumTopicCreated(BaseModel):
    """
    ForumTopicCreated type from Telegram Bot API.
    """

    name: str = Field(description="Name of the topic")
    icon_color: int = Field(description="Color of the topic icon in RGB format")
    icon_custom_emoji_id: None | str = Field(default=None, description="Optional . Unique identifier of the custom emoji shown as the topic icon")
    is_name_implicit: None | bool = Field(default=None, description="Optional . True , if the name of the topic wasn't specified explicitly by its creator and likely needs to be changed by the bot")
class ForumTopicEdited(BaseModel):
    """
    ForumTopicEdited type from Telegram Bot API.
    """

    name: None | str = Field(default=None, description="Optional . New name of the topic, if it was edited")
    icon_custom_emoji_id: None | str = Field(default=None, description="Optional . New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed")
class ForumTopicReopened(BaseModel):
    """
    ForumTopicReopened type from Telegram Bot API.
    """

    user_id: int = Field(description="Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means.")
    first_name: None | str = Field(default=None, description="Optional . First name of the user, if the name was requested by the bot")
    last_name: None | str = Field(default=None, description="Optional . Last name of the user, if the name was requested by the bot")
    username: None | str = Field(default=None, description="Optional . Username of the user, if the username was requested by the bot")
    photo: None | list[PhotoSize] = Field(default=None, description="Optional . Available sizes of the chat photo, if the photo was requested by the bot")
class GeneralForumTopicHidden(BaseModel):
    """
    GeneralForumTopicHidden type from Telegram Bot API.
    """

    user_id: int = Field(description="Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means.")
    first_name: None | str = Field(default=None, description="Optional . First name of the user, if the name was requested by the bot")
    last_name: None | str = Field(default=None, description="Optional . Last name of the user, if the name was requested by the bot")
    username: None | str = Field(default=None, description="Optional . Username of the user, if the username was requested by the bot")
    photo: None | list[PhotoSize] = Field(default=None, description="Optional . Available sizes of the chat photo, if the photo was requested by the bot")
class GeneralForumTopicUnhidden(BaseModel):
    """
    GeneralForumTopicUnhidden type from Telegram Bot API.
    """

    user_id: int = Field(description="Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means.")
    first_name: None | str = Field(default=None, description="Optional . First name of the user, if the name was requested by the bot")
    last_name: None | str = Field(default=None, description="Optional . Last name of the user, if the name was requested by the bot")
    username: None | str = Field(default=None, description="Optional . Username of the user, if the username was requested by the bot")
    photo: None | list[PhotoSize] = Field(default=None, description="Optional . Available sizes of the chat photo, if the photo was requested by the bot")
class Gift(BaseModel):
    """
    Gift type from Telegram Bot API.
    """

    id: str = Field(description="Unique identifier of the gift")
    sticker: "Sticker" = Field(description="The sticker that represents the gift")
    star_count: int = Field(description="The number of Telegram Stars that must be paid to send the sticker")
    upgrade_star_count: None | int = Field(default=None, description="Optional . The number of Telegram Stars that must be paid to upgrade the gift to a unique one")
    is_premium: None | bool = Field(default=None, description="Optional . True , if the gift can only be purchased by Telegram Premium subscribers")
    has_colors: None | bool = Field(default=None, description="Optional . True , if the gift can be used (after being upgraded) to customize a user's appearance")
    total_count: None | int = Field(default=None, description="Optional . The total number of gifts of this type that can be sent by all users; for limited gifts only")
    remaining_count: None | int = Field(default=None, description="Optional . The number of remaining gifts of this type that can be sent by all users; for limited gifts only")
    personal_total_count: None | int = Field(default=None, description="Optional . The total number of gifts of this type that can be sent by the bot; for limited gifts only")
    personal_remaining_count: None | int = Field(default=None, description="Optional . The number of remaining gifts of this type that can be sent by the bot; for limited gifts only")
    background: "None | GiftBackground" = Field(default=None, description="Optional . Background of the gift")
    unique_gift_variant_count: None | int = Field(default=None, description="Optional . The total number of different unique gifts that can be obtained by upgrading the gift")
    publisher_chat: "None | Chat" = Field(default=None, description="Optional . Information about the chat that published the gift")
class GiftBackground(BaseModel):
    """
    GiftBackground type from Telegram Bot API.
    """

    center_color: int = Field(description="Center color of the background in RGB format")
    edge_color: int = Field(description="Edge color of the background in RGB format")
    text_color: int = Field(description="Text color of the background in RGB format")
class GiftInfo(BaseModel):
    """
    GiftInfo type from Telegram Bot API.
    """

    gift: "Gift" = Field(description="Information about the gift")
    owned_gift_id: None | str = Field(default=None, description="Optional . Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts")
    convert_star_count: None | int = Field(default=None, description="Optional . Number of Telegram Stars that can be claimed by the receiver by converting the gift; omitted if conversion to Telegram Stars is impossible")
    prepaid_upgrade_star_count: None | int = Field(default=None, description="Optional . Number of Telegram Stars that were prepaid for the ability to upgrade the gift")
    is_upgrade_separate: None | bool = Field(default=None, description="Optional . True , if the gift's upgrade was purchased after the gift was sent")
    can_be_upgraded: None | bool = Field(default=None, description="Optional . True , if the gift can be upgraded to a unique gift")
    text: None | str = Field(default=None, description="Optional . Text of the message that was added to the gift")
    entities: None | list[MessageEntity] = Field(default=None, description="Optional . Special entities that appear in the text")
    is_private: None | bool = Field(default=None, description="Optional . True , if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them")
    unique_gift_number: None | int = Field(default=None, description="Optional . Unique number reserved for this gift when upgraded. See the number field in UniqueGift")
class Gifts(BaseModel):
    """
    Gifts type from Telegram Bot API.
    """

    gifts: "list[Gift]" = Field(description="The list of gifts")
class Giveaway(BaseModel):
    """
    Giveaway type from Telegram Bot API.
    """

    chats: "list[Chat]" = Field(description="The list of chats which the user must join to participate in the giveaway")
    winners_selection_date: int = Field(description="Point in time (Unix timestamp) when winners of the giveaway will be selected")
    winner_count: int = Field(description="The number of users which are supposed to be selected as winners of the giveaway")
    only_new_members: None | bool = Field(default=None, description="Optional . True , if only users who join the chats after the giveaway started should be eligible to win")
    has_public_winners: None | bool = Field(default=None, description="Optional . True , if the list of giveaway winners will be visible to everyone")
    prize_description: None | str = Field(default=None, description="Optional . Description of additional giveaway prize")
    country_codes: None | list[str] = Field(default=None, description="Optional . A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways.")
    prize_star_count: None | int = Field(default=None, description="Optional . The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only")
    premium_subscription_month_count: None | int = Field(default=None, description="Optional . The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only")
class GiveawayCompleted(BaseModel):
    """
    GiveawayCompleted type from Telegram Bot API.
    """

    winner_count: int = Field(description="Number of winners in the giveaway")
    unclaimed_prize_count: None | int = Field(default=None, description="Optional . Number of undistributed prizes")
    giveaway_message: "None | Message" = Field(default=None, description="Optional . Message with the giveaway that was completed, if it wasn't deleted")
    is_star_giveaway: None | bool = Field(default=None, description="Optional . True , if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway.")
class GiveawayCreated(BaseModel):
    """
    GiveawayCreated type from Telegram Bot API.
    """

    prize_star_count: None | int = Field(default=None, description="Optional . The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only")
class GiveawayWinners(BaseModel):
    """
    GiveawayWinners type from Telegram Bot API.
    """

    chat: "Chat" = Field(description="The chat that created the giveaway")
    giveaway_message_id: int = Field(description="Identifier of the message with the giveaway in the chat")
    winners_selection_date: int = Field(description="Point in time (Unix timestamp) when winners of the giveaway were selected")
    winner_count: int = Field(description="Total number of winners in the giveaway")
    winners: "list[User]" = Field(description="List of up to 100 winners of the giveaway")
    additional_chat_count: None | int = Field(default=None, description="Optional . The number of other chats the user had to join in order to be eligible for the giveaway")
    prize_star_count: None | int = Field(default=None, description="Optional . The number of Telegram Stars that were split between giveaway winners; for Telegram Star giveaways only")
    premium_subscription_month_count: None | int = Field(default=None, description="Optional . The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only")
    unclaimed_prize_count: None | int = Field(default=None, description="Optional . Number of undistributed prizes")
    only_new_members: None | bool = Field(default=None, description="Optional . True , if only users who had joined the chats after the giveaway started were eligible to win")
    was_refunded: None | bool = Field(default=None, description="Optional . True , if the giveaway was canceled because the payment for it was refunded")
    prize_description: None | str = Field(default=None, description="Optional . Description of additional giveaway prize")
class InaccessibleMessage(BaseModel):
    """
    InaccessibleMessage type from Telegram Bot API.
    """

    chat: "Chat" = Field(description="Chat the message belonged to")
    message_id: int = Field(description="Unique message identifier inside the chat")
    date: int = Field(description="Always 0. The field can be used to differentiate regular and inaccessible messages.")
class InlineKeyboardButton(BaseModel):
    """
    InlineKeyboardButton type from Telegram Bot API.
    """

    text: str = Field(description="Label text on the button")
    icon_custom_emoji_id: None | str = Field(default=None, description="Optional . Unique identifier of the custom emoji shown before the text of the button. Can only be used by bots that purchased additional usernames on Fragment or in the messages directly sent by the bot to private, group and supergroup chats if the owner of the bot has a Telegram Premium subscription.")
    style: None | str = Field(default=None, description="Optional . Style of the button. Must be one of “danger” (red), “success” (green) or “primary” (blue). If omitted, then an app-specific style is used.")
    url: None | str = Field(default=None, description="Optional . HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their identifier without using a username, if this is allowed by their privacy settings.")
    callback_data: None | str = Field(default=None, description="Optional . Data to be sent in a callback query to the bot when the button is pressed, 1-64 bytes")
    web_app: "None | WebAppInfo" = Field(default=None, description="Optional . Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery . Available only in private chats between a user and the bot. Not supported for messages sent on behalf of a Telegram Business account.")
    login_url: "None | LoginUrl" = Field(default=None, description="Optional . An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget .")
    switch_inline_query: None | str = Field(default=None, description="Optional . If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. Not supported for messages sent in channel direct messages chats and on behalf of a Telegram Business account.")
    switch_inline_query_current_chat: None | str = Field(default=None, description="Optional . If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted. This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. Not supported in channels and for messages sent in channel direct messages chats and on behalf of a Telegram Business account.")
    switch_inline_query_chosen_chat: "None | SwitchInlineQueryChosenChat" = Field(default=None, description="Optional . If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot's username and the specified inline query in the input field. Not supported for messages sent in channel direct messages chats and on behalf of a Telegram Business account.")
    copy_text: "None | CopyTextButton" = Field(default=None, description="Optional . Description of the button that copies the specified text to the clipboard.")
    callback_game: "None | CallbackGame" = Field(default=None, description="Optional . Description of the game that will be launched when the user presses the button. NOTE: This type of button must always be the first button in the first row.")
    pay: None | bool = Field(default=None, description="Optional . Specify True , to send a Pay button . Substrings “ ” and “XTR” in the buttons's text will be replaced with a Telegram Star icon. NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages.")
class InlineKeyboardMarkup(BaseModel):
    """
    InlineKeyboardMarkup type from Telegram Bot API.
    """

    inline_keyboard: "list[InlineKeyboardButton]" = Field(description="Array of button rows, each represented by an Array of InlineKeyboardButton objects")
class InputChecklist(BaseModel):
    """
    InputChecklist type from Telegram Bot API.
    """

    title: str = Field(description="Title of the checklist; 1-255 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the title. See formatting options for more details.")
    title_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the title, which can be specified instead of parse_mode. Currently, only bold , italic , underline , strikethrough , spoiler , and custom_emoji entities are allowed.")
    tasks: "list[InputChecklistTask]" = Field(description="List of 1-30 tasks in the checklist")
    others_can_add_tasks: None | bool = Field(default=None, description="Optional . Pass True if other users can add tasks to the checklist")
    others_can_mark_tasks_as_done: None | bool = Field(default=None, description="Optional . Pass True if other users can mark tasks as done or not done in the checklist")
class InputChecklistTask(BaseModel):
    """
    InputChecklistTask type from Telegram Bot API.
    """

    id: int = Field(description="Unique identifier of the task; must be positive and unique among all task identifiers currently present in the checklist")
    text: str = Field(description="Text of the task; 1-100 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the text. See formatting options for more details.")
    text_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the text, which can be specified instead of parse_mode. Currently, only bold , italic , underline , strikethrough , spoiler , and custom_emoji entities are allowed.")
class InputFile(BaseModel):
    """
    InputFile type from Telegram Bot API.
    """

    type: str = Field(description="Type of the media, must be photo")
    media: str = Field(description="File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
class InputMedia(BaseModel):
    """
    InputMedia type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be photo")
    media: str = Field(description="File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
    caption: None | str = Field(default=None, description="Optional . Caption of the photo to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the photo caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    has_spoiler: None | bool = Field(default=None, description="Optional . Pass True if the photo needs to be covered with a spoiler animation")
class InputMediaAnimation(BaseModel):
    """
    InputMediaAnimation type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be animation")
    media: str = Field(description="File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
    thumbnail: None | str = Field(default=None, description="Optional . Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    caption: None | str = Field(default=None, description="Optional . Caption of the animation to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the animation caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    width: None | int = Field(default=None, description="Optional . Animation width")
    height: None | int = Field(default=None, description="Optional . Animation height")
    duration: None | int = Field(default=None, description="Optional . Animation duration in seconds")
    has_spoiler: None | bool = Field(default=None, description="Optional . Pass True if the animation needs to be covered with a spoiler animation")
class InputMediaAudio(BaseModel):
    """
    InputMediaAudio type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be audio")
    media: str = Field(description="File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
    thumbnail: None | str = Field(default=None, description="Optional . Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    caption: None | str = Field(default=None, description="Optional . Caption of the audio to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the audio caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    duration: None | int = Field(default=None, description="Optional . Duration of the audio in seconds")
    performer: None | str = Field(default=None, description="Optional . Performer of the audio")
    title: None | str = Field(default=None, description="Optional . Title of the audio")
class InputMediaDocument(BaseModel):
    """
    InputMediaDocument type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be document")
    media: str = Field(description="File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
    thumbnail: None | str = Field(default=None, description="Optional . Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    caption: None | str = Field(default=None, description="Optional . Caption of the document to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the document caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    disable_content_type_detection: None | bool = Field(default=None, description="Optional . Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always True , if the document is sent as part of an album.")
class InputMediaPhoto(BaseModel):
    """
    InputMediaPhoto type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be photo")
    media: str = Field(description="File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
    caption: None | str = Field(default=None, description="Optional . Caption of the photo to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the photo caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    has_spoiler: None | bool = Field(default=None, description="Optional . Pass True if the photo needs to be covered with a spoiler animation")
class InputMediaVideo(BaseModel):
    """
    InputMediaVideo type from Telegram Bot API.
    """

    type: str = Field(description="Type of the result, must be video")
    media: str = Field(description="File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
    thumbnail: None | str = Field(default=None, description="Optional . Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    cover: None | str = Field(default=None, description="Optional . Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
    start_timestamp: None | int = Field(default=None, description="Optional . Start timestamp for the video in the message")
    caption: None | str = Field(default=None, description="Optional . Caption of the video to be sent, 0-1024 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the video caption. See formatting options for more details.")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the caption, which can be specified instead of parse_mode")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . Pass True , if the caption must be shown above the message media")
    width: None | int = Field(default=None, description="Optional . Video width")
    height: None | int = Field(default=None, description="Optional . Video height")
    duration: None | int = Field(default=None, description="Optional . Video duration in seconds")
    supports_streaming: None | bool = Field(default=None, description="Optional . Pass True if the uploaded video is suitable for streaming")
    has_spoiler: None | bool = Field(default=None, description="Optional . Pass True if the video needs to be covered with a spoiler animation")
class InputPaidMedia(BaseModel):
    """
    InputPaidMedia type from Telegram Bot API.
    """

    type: str = Field(description="Type of the media, must be photo")
    media: str = Field(description="File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
class InputPaidMediaPhoto(BaseModel):
    """
    InputPaidMediaPhoto type from Telegram Bot API.
    """

    type: str = Field(description="Type of the media, must be photo")
    media: str = Field(description="File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
class InputPaidMediaVideo(BaseModel):
    """
    InputPaidMediaVideo type from Telegram Bot API.
    """

    type: str = Field(description="Type of the media, must be video")
    media: str = Field(description="File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
    thumbnail: None | str = Field(default=None, description="Optional . Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    cover: None | str = Field(default=None, description="Optional . Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
    start_timestamp: None | int = Field(default=None, description="Optional . Start timestamp for the video in the message")
    width: None | int = Field(default=None, description="Optional . Video width")
    height: None | int = Field(default=None, description="Optional . Video height")
    duration: None | int = Field(default=None, description="Optional . Video duration in seconds")
    supports_streaming: None | bool = Field(default=None, description="Optional . Pass True if the uploaded video is suitable for streaming")
class InputPollOption(BaseModel):
    """
    InputPollOption type from Telegram Bot API.
    """

    text: str = Field(description="Option text, 1-100 characters")
    text_parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the text. See formatting options for more details. Currently, only custom emoji entities are allowed")
    text_entities: None | list[MessageEntity] = Field(default=None, description="Optional . A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of text_parse_mode")
class InputProfilePhoto(BaseModel):
    """
    InputProfilePhoto type from Telegram Bot API.
    """

    type: str = Field(description="Type of the profile photo, must be static")
    photo: str = Field(description="The static profile photo. Profile photos can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
class InputProfilePhotoAnimated(BaseModel):
    """
    InputProfilePhotoAnimated type from Telegram Bot API.
    """

    type: str = Field(description="Type of the profile photo, must be animated")
    animation: str = Field(description="The animated profile photo. Profile photos can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    main_frame_timestamp: None | float = Field(default=None, description="Optional . Timestamp in seconds of the frame that will be used as the static profile photo. Defaults to 0.0.")
class InputProfilePhotoStatic(BaseModel):
    """
    InputProfilePhotoStatic type from Telegram Bot API.
    """

    type: str = Field(description="Type of the profile photo, must be static")
    photo: str = Field(description="The static profile photo. Profile photos can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
class InputStoryContent(BaseModel):
    """
    InputStoryContent type from Telegram Bot API.
    """

    type: str = Field(description="Type of the content, must be photo")
    photo: str = Field(description="The photo to post as a story. The photo must be of the size 1080x1920 and must not exceed 10 MB. The photo can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
class InputStoryContentPhoto(BaseModel):
    """
    InputStoryContentPhoto type from Telegram Bot API.
    """

    type: str = Field(description="Type of the content, must be photo")
    photo: str = Field(description="The photo to post as a story. The photo must be of the size 1080x1920 and must not exceed 10 MB. The photo can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the photo was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
class InputStoryContentVideo(BaseModel):
    """
    InputStoryContentVideo type from Telegram Bot API.
    """

    type: str = Field(description="Type of the content, must be video")
    video: str = Field(description="The video to post as a story. The video must be of the size 720x1280, streamable, encoded with H.265 codec, with key frames added each second in the MPEG4 format, and must not exceed 30 MB. The video can't be reused and can only be uploaded as a new file, so you can pass “attach://<file_attach_name>” if the video was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »")
    duration: None | float = Field(default=None, description="Optional . Precise duration of the video in seconds; 0-60")
    cover_frame_timestamp: None | float = Field(default=None, description="Optional . Timestamp in seconds of the frame that will be used as the static cover for the story. Defaults to 0.0.")
    is_animation: None | bool = Field(default=None, description="Optional . Pass True if the video has no sound")
class KeyboardButton(BaseModel):
    """
    KeyboardButton type from Telegram Bot API.
    """

    text: str = Field(description="Text of the button. If none of the fields other than text , icon_custom_emoji_id , and style are used, it will be sent as a message when the button is pressed")
    icon_custom_emoji_id: None | str = Field(default=None, description="Optional . Unique identifier of the custom emoji shown before the text of the button. Can only be used by bots that purchased additional usernames on Fragment or in the messages directly sent by the bot to private, group and supergroup chats if the owner of the bot has a Telegram Premium subscription.")
    style: None | str = Field(default=None, description="Optional . Style of the button. Must be one of “danger” (red), “success” (green) or “primary” (blue). If omitted, then an app-specific style is used.")
    request_users: "None | KeyboardButtonRequestUsers" = Field(default=None, description="Optional . If specified, pressing the button will open a list of suitable users. Identifiers of selected users will be sent to the bot in a “users_shared” service message. Available in private chats only.")
    request_chat: "None | KeyboardButtonRequestChat" = Field(default=None, description="Optional . If specified, pressing the button will open a list of suitable chats. Tapping on a chat will send its identifier to the bot in a “chat_shared” service message. Available in private chats only.")
    request_contact: None | bool = Field(default=None, description="Optional . If True , the user's phone number will be sent as a contact when the button is pressed. Available in private chats only.")
    request_location: None | bool = Field(default=None, description="Optional . If True , the user's current location will be sent when the button is pressed. Available in private chats only.")
    request_poll: "None | KeyboardButtonPollType" = Field(default=None, description="Optional . If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only.")
    web_app: "None | WebAppInfo" = Field(default=None, description="Optional . If specified, the described Web App will be launched when the button is pressed. The Web App will be able to send a “web_app_data” service message. Available in private chats only.")
class KeyboardButtonPollType(BaseModel):
    """
    KeyboardButtonPollType type from Telegram Bot API.
    """

    type: None | str = Field(default=None, description="Optional . If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.")
class KeyboardButtonRequestChat(BaseModel):
    """
    KeyboardButtonRequestChat type from Telegram Bot API.
    """

    request_id: int = Field(description="Signed 32-bit identifier of the request, which will be received back in the ChatShared object. Must be unique within the message")
    chat_is_channel: bool = Field(description="Pass True to request a channel chat, pass False to request a group or a supergroup chat.")
    chat_is_forum: None | bool = Field(default=None, description="Optional . Pass True to request a forum supergroup, pass False to request a non-forum chat. If not specified, no additional restrictions are applied.")
    chat_has_username: None | bool = Field(default=None, description="Optional . Pass True to request a supergroup or a channel with a username, pass False to request a chat without a username. If not specified, no additional restrictions are applied.")
    chat_is_created: None | bool = Field(default=None, description="Optional . Pass True to request a chat owned by the user. Otherwise, no additional restrictions are applied.")
    user_administrator_rights: "None | ChatAdministratorRights" = Field(default=None, description="Optional . A JSON-serialized object listing the required administrator rights of the user in the chat. The rights must be a superset of bot_administrator_rights . If not specified, no additional restrictions are applied.")
    bot_administrator_rights: "None | ChatAdministratorRights" = Field(default=None, description="Optional . A JSON-serialized object listing the required administrator rights of the bot in the chat. The rights must be a subset of user_administrator_rights . If not specified, no additional restrictions are applied.")
    bot_is_member: None | bool = Field(default=None, description="Optional . Pass True to request a chat with the bot as a member. Otherwise, no additional restrictions are applied.")
    request_title: None | bool = Field(default=None, description="Optional . Pass True to request the chat's title")
    request_username: None | bool = Field(default=None, description="Optional . Pass True to request the chat's username")
    request_photo: None | bool = Field(default=None, description="Optional . Pass True to request the chat's photo")
class KeyboardButtonRequestUsers(BaseModel):
    """
    KeyboardButtonRequestUsers type from Telegram Bot API.
    """

    request_id: int = Field(description="Signed 32-bit identifier of the request that will be received back in the UsersShared object. Must be unique within the message")
    user_is_bot: None | bool = Field(default=None, description="Optional . Pass True to request bots, pass False to request regular users. If not specified, no additional restrictions are applied.")
    user_is_premium: None | bool = Field(default=None, description="Optional . Pass True to request premium users, pass False to request non-premium users. If not specified, no additional restrictions are applied.")
    max_quantity: None | int = Field(default=None, description="Optional . The maximum number of users to be selected; 1-10. Defaults to 1.")
    request_name: None | bool = Field(default=None, description="Optional . Pass True to request the users' first and last names")
    request_username: None | bool = Field(default=None, description="Optional . Pass True to request the users' usernames")
    request_photo: None | bool = Field(default=None, description="Optional . Pass True to request the users' photos")
class LinkPreviewOptions(BaseModel):
    """
    LinkPreviewOptions type from Telegram Bot API.
    """

    is_disabled: None | bool = Field(default=None, description="Optional . True , if the link preview is disabled")
    url: None | str = Field(default=None, description="Optional . URL to use for the link preview. If empty, then the first URL found in the message text will be used")
    prefer_small_media: None | bool = Field(default=None, description="Optional . True , if the media in the link preview is supposed to be shrunk; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview")
    prefer_large_media: None | bool = Field(default=None, description="Optional . True , if the media in the link preview is supposed to be enlarged; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview")
    show_above_text: None | bool = Field(default=None, description="Optional . True , if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text")
class Location(BaseModel):
    """
    Location type from Telegram Bot API.
    """

    latitude: float = Field(description="Latitude as defined by the sender")
    longitude: float = Field(description="Longitude as defined by the sender")
    horizontal_accuracy: None | float = Field(default=None, description="Optional . The radius of uncertainty for the location, measured in meters; 0-1500")
    live_period: None | int = Field(default=None, description="Optional . Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only.")
    heading: None | int = Field(default=None, description="Optional . The direction in which user is moving, in degrees; 1-360. For active live locations only.")
    proximity_alert_radius: None | int = Field(default=None, description="Optional . The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.")
class LocationAddress(BaseModel):
    """
    LocationAddress type from Telegram Bot API.
    """

    country_code: str = Field(description="The two-letter ISO 3166-1 alpha-2 country code of the country where the location is located")
    state: None | str = Field(default=None, description="Optional . State of the location")
    city: None | str = Field(default=None, description="Optional . City of the location")
    street: None | str = Field(default=None, description="Optional . Street address of the location")
class LoginUrl(BaseModel):
    """
    LoginUrl type from Telegram Bot API.
    """

    url: str = Field(description="An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data . NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization .")
    forward_text: None | str = Field(default=None, description="Optional . New text of the button in forwarded messages.")
    bot_username: None | str = Field(default=None, description="Optional . Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url 's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.")
    request_write_access: None | bool = Field(default=None, description="Optional . Pass True to request the permission for your bot to send messages to the user.")
class MaybeInaccessibleMessage(BaseModel):
    """
    MaybeInaccessibleMessage type from Telegram Bot API.
    """

    type: str = Field(description="Type of the entity. Currently, can be “mention” ( @username ), “hashtag” ( #hashtag or #hashtag@chatusername ), “cashtag” ( $USD or $USD@chatusername ), “bot_command” ( /start@jobs_bot ), “url” ( https://telegram.org ), “email” ( do-not-reply@telegram.org ), “phone_number” ( +1-212-555-0123 ), “bold” ( bold text ), “italic” ( italic text ), “underline” (underlined text), “strikethrough” (strikethrough text), “spoiler” (spoiler message), “blockquote” (block quotation), “expandable_blockquote” (collapsed-by-default block quotation), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users without usernames ), “custom_emoji” (for inline custom emoji stickers), or “date_time” (for formatted date and time)")
    offset: int = Field(description="Offset in UTF-16 code units to the start of the entity")
    length: int = Field(description="Length of the entity in UTF-16 code units")
    url: None | str = Field(default=None, description="Optional . For “text_link” only, URL that will be opened after user taps on the text")
    user: "None | User" = Field(default=None, description="Optional . For “text_mention” only, the mentioned user")
    language: None | str = Field(default=None, description="Optional . For “pre” only, the programming language of the entity text")
    custom_emoji_id: None | str = Field(default=None, description="Optional . For “custom_emoji” only, unique identifier of the custom emoji. Use getCustomEmojiStickers to get full information about the sticker")
    unix_time: None | int = Field(default=None, description="Optional . For “date_time” only, the Unix time associated with the entity")
    date_time_format: None | str = Field(default=None, description="Optional . For “date_time” only, the string that defines the formatting of the date and time. See date-time entity formatting for more details.")
class MenuButton(BaseModel):
    """
    MenuButton type from Telegram Bot API.
    """

    type: str = Field(description="Type of the button, must be commands")
class MenuButtonCommands(BaseModel):
    """
    MenuButtonCommands type from Telegram Bot API.
    """

    type: str = Field(description="Type of the button, must be commands")
class MenuButtonDefault(BaseModel):
    """
    MenuButtonDefault type from Telegram Bot API.
    """

    type: str = Field(description="Type of the button, must be default")
class MenuButtonWebApp(BaseModel):
    """
    MenuButtonWebApp type from Telegram Bot API.
    """

    type: str = Field(description="Type of the button, must be web_app")
    text: str = Field(description="Text on the button")
    web_app: "WebAppInfo" = Field(description="Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery . Alternatively, a t.me link to a Web App of the bot can be specified in the object instead of the Web App's URL, in which case the Web App will be opened as if the user pressed the link.")
class Message(BaseModel):
    """
    Message type from Telegram Bot API.
    """

    message_id: int = Field(description="Unique message identifier inside this chat. In specific instances (e.g., message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent")
    message_thread_id: None | int = Field(default=None, description="Optional . Unique identifier of a message thread or forum topic to which the message belongs; for supergroups and private chats only")
    direct_messages_topic: "None | DirectMessagesTopic" = Field(default=None, description="Optional . Information about the direct messages chat topic that contains the message")
    from_: "None | User" = Field(default=None, description="Optional . Sender of the message; may be empty for messages sent to channels. For backward compatibility, if the message was sent on behalf of a chat, the field contains a fake sender user in non-channel chats")
    sender_chat: "None | Chat" = Field(default=None, description="Optional . Sender of the message when sent on behalf of a chat. For example, the supergroup itself for messages sent by its anonymous administrators or a linked channel for messages automatically forwarded to the channel's discussion group. For backward compatibility, if the message was sent on behalf of a chat, the field from contains a fake sender user in non-channel chats.")
    sender_boost_count: None | int = Field(default=None, description="Optional . If the sender of the message boosted the chat, the number of boosts added by the user")
    sender_business_bot: "None | User" = Field(default=None, description="Optional . The bot that actually sent the message on behalf of the business account. Available only for outgoing messages sent on behalf of the connected business account.")
    sender_tag: None | str = Field(default=None, description="Optional . Tag or custom title of the sender of the message; for supergroups only")
    date: int = Field(description="Date the message was sent in Unix time. It is always a positive number, representing a valid date.")
    business_connection_id: None | str = Field(default=None, description="Optional . Unique identifier of the business connection from which the message was received. If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier.")
    chat: "Chat" = Field(description="Chat the message belongs to")
    forward_origin: "None | MessageOrigin" = Field(default=None, description="Optional . Information about the original message for forwarded messages")
    is_topic_message: None | bool = Field(default=None, description="Optional . True , if the message is sent to a topic in a forum supergroup or a private chat with the bot")
    is_automatic_forward: None | bool = Field(default=None, description="Optional . True , if the message is a channel post that was automatically forwarded to the connected discussion group")
    reply_to_message: "None | Message" = Field(default=None, description="Optional . For replies in the same chat and message thread, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.")
    external_reply: "None | ExternalReplyInfo" = Field(default=None, description="Optional . Information about the message that is being replied to, which may come from another chat or forum topic")
    quote: "None | TextQuote" = Field(default=None, description="Optional . For replies that quote part of the original message, the quoted part of the message")
    reply_to_story: "None | Story" = Field(default=None, description="Optional . For replies to a story, the original story")
    reply_to_checklist_task_id: None | int = Field(default=None, description="Optional . Identifier of the specific checklist task that is being replied to")
    via_bot: "None | User" = Field(default=None, description="Optional . Bot through which the message was sent")
    edit_date: None | int = Field(default=None, description="Optional . Date the message was last edited in Unix time")
    has_protected_content: None | bool = Field(default=None, description="Optional . True , if the message can't be forwarded")
    is_from_offline: None | bool = Field(default=None, description="Optional . True , if the message was sent by an implicit action, for example, as an away or a greeting business message, or as a scheduled message")
    is_paid_post: None | bool = Field(default=None, description="Optional . True , if the message is a paid post. Note that such posts must not be deleted for 24 hours to receive the payment and can't be edited.")
    media_group_id: None | str = Field(default=None, description="Optional . The unique identifier inside this chat of a media message group this message belongs to")
    author_signature: None | str = Field(default=None, description="Optional . Signature of the post author for messages in channels, or the custom title of an anonymous group administrator")
    paid_star_count: None | int = Field(default=None, description="Optional . The number of Telegram Stars that were paid by the sender of the message to send it")
    text: None | str = Field(default=None, description="Optional . For text messages, the actual UTF-8 text of the message")
    entities: None | list[MessageEntity] = Field(default=None, description="Optional . For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text")
    link_preview_options: "None | LinkPreviewOptions" = Field(default=None, description="Optional . Options used for link preview generation for the message, if it is a text message and link preview options were changed")
    suggested_post_info: "None | SuggestedPostInfo" = Field(default=None, description="Optional . Information about suggested post parameters if the message is a suggested post in a channel direct messages chat. If the message is an approved or declined suggested post, then it can't be edited.")
    effect_id: None | str = Field(default=None, description="Optional . Unique identifier of the message effect added to the message")
    animation: "None | Animation" = Field(default=None, description="Optional . Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set")
    audio: "None | Audio" = Field(default=None, description="Optional . Message is an audio file, information about the file")
    document: "None | Document" = Field(default=None, description="Optional . Message is a general file, information about the file")
    paid_media: "None | PaidMediaInfo" = Field(default=None, description="Optional . Message contains paid media; information about the paid media")
    photo: None | list[PhotoSize] = Field(default=None, description="Optional . Message is a photo, available sizes of the photo")
    sticker: "None | Sticker" = Field(default=None, description="Optional . Message is a sticker, information about the sticker")
    story: "None | Story" = Field(default=None, description="Optional . Message is a forwarded story")
    video: "None | Video" = Field(default=None, description="Optional . Message is a video, information about the video")
    video_note: "None | VideoNote" = Field(default=None, description="Optional . Message is a video note , information about the video message")
    voice: "None | Voice" = Field(default=None, description="Optional . Message is a voice message, information about the file")
    caption: None | str = Field(default=None, description="Optional . Caption for the animation, audio, document, paid media, photo, video or voice")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . True , if the caption must be shown above the message media")
    has_media_spoiler: None | bool = Field(default=None, description="Optional . True , if the message media is covered by a spoiler animation")
    checklist: "None | Checklist" = Field(default=None, description="Optional . Message is a checklist")
    contact: "None | Contact" = Field(default=None, description="Optional . Message is a shared contact, information about the contact")
    dice: "None | Dice" = Field(default=None, description="Optional . Message is a dice with random value")
    game: "None | Game" = Field(default=None, description="Optional . Message is a game, information about the game. More about games »")
    poll: "None | Poll" = Field(default=None, description="Optional . Message is a native poll, information about the poll")
    venue: "None | Venue" = Field(default=None, description="Optional . Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set")
    location: "None | Location" = Field(default=None, description="Optional . Message is a shared location, information about the location")
    new_chat_members: None | list[User] = Field(default=None, description="Optional . New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)")
    left_chat_member: "None | User" = Field(default=None, description="Optional . A member was removed from the group, information about them (this member may be the bot itself)")
    chat_owner_left: "None | ChatOwnerLeft" = Field(default=None, description="Optional . Service message: chat owner has left")
    chat_owner_changed: "None | ChatOwnerChanged" = Field(default=None, description="Optional . Service message: chat owner has changed")
    new_chat_title: None | str = Field(default=None, description="Optional . A chat title was changed to this value")
    new_chat_photo: None | list[PhotoSize] = Field(default=None, description="Optional . A chat photo was change to this value")
    delete_chat_photo: None | bool = Field(default=None, description="Optional . Service message: the chat photo was deleted")
    group_chat_created: None | bool = Field(default=None, description="Optional . Service message: the group has been created")
    supergroup_chat_created: None | bool = Field(default=None, description="Optional . Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.")
    channel_chat_created: None | bool = Field(default=None, description="Optional . Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.")
    message_auto_delete_timer_changed: "None | MessageAutoDeleteTimerChanged" = Field(default=None, description="Optional . Service message: auto-delete timer settings changed in the chat")
    migrate_to_chat_id: None | int = Field(default=None, description="Optional . The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.")
    migrate_from_chat_id: None | int = Field(default=None, description="Optional . The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.")
    pinned_message: "None | MaybeInaccessibleMessage" = Field(default=None, description="Optional . Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.")
    invoice: "None | Invoice" = Field(default=None, description="Optional . Message is an invoice for a payment , information about the invoice. More about payments »")
    successful_payment: "None | SuccessfulPayment" = Field(default=None, description="Optional . Message is a service message about a successful payment, information about the payment. More about payments »")
    refunded_payment: "None | RefundedPayment" = Field(default=None, description="Optional . Message is a service message about a refunded payment, information about the payment. More about payments »")
    users_shared: "None | UsersShared" = Field(default=None, description="Optional . Service message: users were shared with the bot")
    chat_shared: "None | ChatShared" = Field(default=None, description="Optional . Service message: a chat was shared with the bot")
    gift: "None | GiftInfo" = Field(default=None, description="Optional . Service message: a regular gift was sent or received")
    unique_gift: "None | UniqueGiftInfo" = Field(default=None, description="Optional . Service message: a unique gift was sent or received")
    gift_upgrade_sent: "None | GiftInfo" = Field(default=None, description="Optional . Service message: upgrade of a gift was purchased after the gift was sent")
    connected_website: None | str = Field(default=None, description="Optional . The domain name of the website on which the user has logged in. More about Telegram Login »")
    write_access_allowed: "None | WriteAccessAllowed" = Field(default=None, description="Optional . Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess")
    passport_data: "None | PassportData" = Field(default=None, description="Optional . Telegram Passport data")
    proximity_alert_triggered: "None | ProximityAlertTriggered" = Field(default=None, description="Optional . Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.")
    boost_added: "None | ChatBoostAdded" = Field(default=None, description="Optional . Service message: user boosted the chat")
    chat_background_set: "None | ChatBackground" = Field(default=None, description="Optional . Service message: chat background set")
    checklist_tasks_done: "None | ChecklistTasksDone" = Field(default=None, description="Optional . Service message: some tasks in a checklist were marked as done or not done")
    checklist_tasks_added: "None | ChecklistTasksAdded" = Field(default=None, description="Optional . Service message: tasks were added to a checklist")
    direct_message_price_changed: "None | DirectMessagePriceChanged" = Field(default=None, description="Optional . Service message: the price for paid messages in the corresponding direct messages chat of a channel has changed")
    forum_topic_created: "None | ForumTopicCreated" = Field(default=None, description="Optional . Service message: forum topic created")
    forum_topic_edited: "None | ForumTopicEdited" = Field(default=None, description="Optional . Service message: forum topic edited")
    forum_topic_closed: "None | ForumTopicClosed" = Field(default=None, description="Optional . Service message: forum topic closed")
    forum_topic_reopened: "None | ForumTopicReopened" = Field(default=None, description="Optional . Service message: forum topic reopened")
    general_forum_topic_hidden: "None | GeneralForumTopicHidden" = Field(default=None, description="Optional . Service message: the 'General' forum topic hidden")
    general_forum_topic_unhidden: "None | GeneralForumTopicUnhidden" = Field(default=None, description="Optional . Service message: the 'General' forum topic unhidden")
    giveaway_created: "None | GiveawayCreated" = Field(default=None, description="Optional . Service message: a scheduled giveaway was created")
    giveaway: "None | Giveaway" = Field(default=None, description="Optional . The message is a scheduled giveaway message")
    giveaway_winners: "None | GiveawayWinners" = Field(default=None, description="Optional . A giveaway with public winners was completed")
    giveaway_completed: "None | GiveawayCompleted" = Field(default=None, description="Optional . Service message: a giveaway without public winners was completed")
    paid_message_price_changed: "None | PaidMessagePriceChanged" = Field(default=None, description="Optional . Service message: the price for paid messages has changed in the chat")
    suggested_post_approved: "None | SuggestedPostApproved" = Field(default=None, description="Optional . Service message: a suggested post was approved")
    suggested_post_approval_failed: "None | SuggestedPostApprovalFailed" = Field(default=None, description="Optional . Service message: approval of a suggested post has failed")
    suggested_post_declined: "None | SuggestedPostDeclined" = Field(default=None, description="Optional . Service message: a suggested post was declined")
    suggested_post_paid: "None | SuggestedPostPaid" = Field(default=None, description="Optional . Service message: payment for a suggested post was received")
    suggested_post_refunded: "None | SuggestedPostRefunded" = Field(default=None, description="Optional . Service message: payment for a suggested post was refunded")
    video_chat_scheduled: "None | VideoChatScheduled" = Field(default=None, description="Optional . Service message: video chat scheduled")
    video_chat_started: "None | VideoChatStarted" = Field(default=None, description="Optional . Service message: video chat started")
    video_chat_ended: "None | VideoChatEnded" = Field(default=None, description="Optional . Service message: video chat ended")
    video_chat_participants_invited: "None | VideoChatParticipantsInvited" = Field(default=None, description="Optional . Service message: new participants invited to a video chat")
    web_app_data: "None | WebAppData" = Field(default=None, description="Optional . Service message: data sent by a Web App")
    reply_markup: "None | InlineKeyboardMarkup" = Field(default=None, description="Optional . Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.")
class MessageAutoDeleteTimerChanged(BaseModel):
    """
    MessageAutoDeleteTimerChanged type from Telegram Bot API.
    """

    message_auto_delete_time: int = Field(description="New auto-delete time for messages in the chat; in seconds")
class MessageEntity(BaseModel):
    """
    MessageEntity type from Telegram Bot API.
    """

    type: str = Field(description="Type of the entity. Currently, can be “mention” ( @username ), “hashtag” ( #hashtag or #hashtag@chatusername ), “cashtag” ( $USD or $USD@chatusername ), “bot_command” ( /start@jobs_bot ), “url” ( https://telegram.org ), “email” ( do-not-reply@telegram.org ), “phone_number” ( +1-212-555-0123 ), “bold” ( bold text ), “italic” ( italic text ), “underline” (underlined text), “strikethrough” (strikethrough text), “spoiler” (spoiler message), “blockquote” (block quotation), “expandable_blockquote” (collapsed-by-default block quotation), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users without usernames ), “custom_emoji” (for inline custom emoji stickers), or “date_time” (for formatted date and time)")
    offset: int = Field(description="Offset in UTF-16 code units to the start of the entity")
    length: int = Field(description="Length of the entity in UTF-16 code units")
    url: None | str = Field(default=None, description="Optional . For “text_link” only, URL that will be opened after user taps on the text")
    user: "None | User" = Field(default=None, description="Optional . For “text_mention” only, the mentioned user")
    language: None | str = Field(default=None, description="Optional . For “pre” only, the programming language of the entity text")
    custom_emoji_id: None | str = Field(default=None, description="Optional . For “custom_emoji” only, unique identifier of the custom emoji. Use getCustomEmojiStickers to get full information about the sticker")
    unix_time: None | int = Field(default=None, description="Optional . For “date_time” only, the Unix time associated with the entity")
    date_time_format: None | str = Field(default=None, description="Optional . For “date_time” only, the string that defines the formatting of the date and time. See date-time entity formatting for more details.")
class MessageId(BaseModel):
    """
    MessageId type from Telegram Bot API.
    """

    message_id: int = Field(description="Unique message identifier. In specific instances (e.g., message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent")
class MessageOrigin(BaseModel):
    """
    MessageOrigin type from Telegram Bot API.
    """

    type: str = Field(description="Type of the message origin, always “user”")
    date: int = Field(description="Date the message was sent originally in Unix time")
    sender_user: "User" = Field(description="User that sent the message originally")
class MessageOriginChannel(BaseModel):
    """
    MessageOriginChannel type from Telegram Bot API.
    """

    type: str = Field(description="Type of the message origin, always “channel”")
    date: int = Field(description="Date the message was sent originally in Unix time")
    chat: "Chat" = Field(description="Channel chat to which the message was originally sent")
    message_id: int = Field(description="Unique message identifier inside the chat")
    author_signature: None | str = Field(default=None, description="Optional . Signature of the original post author")
class MessageOriginChat(BaseModel):
    """
    MessageOriginChat type from Telegram Bot API.
    """

    type: str = Field(description="Type of the message origin, always “chat”")
    date: int = Field(description="Date the message was sent originally in Unix time")
    sender_chat: "Chat" = Field(description="Chat that sent the message originally")
    author_signature: None | str = Field(default=None, description="Optional . For messages originally sent by an anonymous chat administrator, original message author signature")
class MessageOriginHiddenUser(BaseModel):
    """
    MessageOriginHiddenUser type from Telegram Bot API.
    """

    type: str = Field(description="Type of the message origin, always “hidden_user”")
    date: int = Field(description="Date the message was sent originally in Unix time")
    sender_user_name: str = Field(description="Name of the user that sent the message originally")
class MessageOriginUser(BaseModel):
    """
    MessageOriginUser type from Telegram Bot API.
    """

    type: str = Field(description="Type of the message origin, always “user”")
    date: int = Field(description="Date the message was sent originally in Unix time")
    sender_user: "User" = Field(description="User that sent the message originally")
class MessageReactionCountUpdated(BaseModel):
    """
    MessageReactionCountUpdated type from Telegram Bot API.
    """

    chat: "Chat" = Field(description="The chat containing the message")
    message_id: int = Field(description="Unique message identifier inside the chat")
    date: int = Field(description="Date of the change in Unix time")
    reactions: "list[ReactionCount]" = Field(description="List of reactions that are present on the message")
class MessageReactionUpdated(BaseModel):
    """
    MessageReactionUpdated type from Telegram Bot API.
    """

    chat: "Chat" = Field(description="The chat containing the message the user reacted to")
    message_id: int = Field(description="Unique identifier of the message inside the chat")
    user: "None | User" = Field(default=None, description="Optional . The user that changed the reaction, if the user isn't anonymous")
    actor_chat: "None | Chat" = Field(default=None, description="Optional . The chat on behalf of which the reaction was changed, if the user is anonymous")
    date: int = Field(description="Date of the change in Unix time")
    old_reaction: "list[ReactionType]" = Field(description="Previous list of reaction types that were set by the user")
    new_reaction: "list[ReactionType]" = Field(description="New list of reaction types that have been set by the user")
class OwnedGift(BaseModel):
    """
    OwnedGift type from Telegram Bot API.
    """

    type: str = Field(description="Type of the gift, always “regular”")
    gift: "Gift" = Field(description="Information about the regular gift")
    owned_gift_id: None | str = Field(default=None, description="Optional . Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only")
    sender_user: "None | User" = Field(default=None, description="Optional . Sender of the gift if it is a known user")
    send_date: int = Field(description="Date the gift was sent in Unix time")
    text: None | str = Field(default=None, description="Optional . Text of the message that was added to the gift")
    entities: None | list[MessageEntity] = Field(default=None, description="Optional . Special entities that appear in the text")
    is_private: None | bool = Field(default=None, description="Optional . True , if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them")
    is_saved: None | bool = Field(default=None, description="Optional . True , if the gift is displayed on the account's profile page; for gifts received on behalf of business accounts only")
    can_be_upgraded: None | bool = Field(default=None, description="Optional . True , if the gift can be upgraded to a unique gift; for gifts received on behalf of business accounts only")
    was_refunded: None | bool = Field(default=None, description="Optional . True , if the gift was refunded and isn't available anymore")
    convert_star_count: None | int = Field(default=None, description="Optional . Number of Telegram Stars that can be claimed by the receiver instead of the gift; omitted if the gift cannot be converted to Telegram Stars; for gifts received on behalf of business accounts only")
    prepaid_upgrade_star_count: None | int = Field(default=None, description="Optional . Number of Telegram Stars that were paid for the ability to upgrade the gift")
    is_upgrade_separate: None | bool = Field(default=None, description="Optional . True , if the gift's upgrade was purchased after the gift was sent; for gifts received on behalf of business accounts only")
    unique_gift_number: None | int = Field(default=None, description="Optional . Unique number reserved for this gift when upgraded. See the number field in UniqueGift")
class OwnedGiftRegular(BaseModel):
    """
    OwnedGiftRegular type from Telegram Bot API.
    """

    type: str = Field(description="Type of the gift, always “regular”")
    gift: "Gift" = Field(description="Information about the regular gift")
    owned_gift_id: None | str = Field(default=None, description="Optional . Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only")
    sender_user: "None | User" = Field(default=None, description="Optional . Sender of the gift if it is a known user")
    send_date: int = Field(description="Date the gift was sent in Unix time")
    text: None | str = Field(default=None, description="Optional . Text of the message that was added to the gift")
    entities: None | list[MessageEntity] = Field(default=None, description="Optional . Special entities that appear in the text")
    is_private: None | bool = Field(default=None, description="Optional . True , if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them")
    is_saved: None | bool = Field(default=None, description="Optional . True , if the gift is displayed on the account's profile page; for gifts received on behalf of business accounts only")
    can_be_upgraded: None | bool = Field(default=None, description="Optional . True , if the gift can be upgraded to a unique gift; for gifts received on behalf of business accounts only")
    was_refunded: None | bool = Field(default=None, description="Optional . True , if the gift was refunded and isn't available anymore")
    convert_star_count: None | int = Field(default=None, description="Optional . Number of Telegram Stars that can be claimed by the receiver instead of the gift; omitted if the gift cannot be converted to Telegram Stars; for gifts received on behalf of business accounts only")
    prepaid_upgrade_star_count: None | int = Field(default=None, description="Optional . Number of Telegram Stars that were paid for the ability to upgrade the gift")
    is_upgrade_separate: None | bool = Field(default=None, description="Optional . True , if the gift's upgrade was purchased after the gift was sent; for gifts received on behalf of business accounts only")
    unique_gift_number: None | int = Field(default=None, description="Optional . Unique number reserved for this gift when upgraded. See the number field in UniqueGift")
class OwnedGiftUnique(BaseModel):
    """
    OwnedGiftUnique type from Telegram Bot API.
    """

    type: str = Field(description="Type of the gift, always “unique”")
    gift: "UniqueGift" = Field(description="Information about the unique gift")
    owned_gift_id: None | str = Field(default=None, description="Optional . Unique identifier of the received gift for the bot; for gifts received on behalf of business accounts only")
    sender_user: "None | User" = Field(default=None, description="Optional . Sender of the gift if it is a known user")
    send_date: int = Field(description="Date the gift was sent in Unix time")
    is_saved: None | bool = Field(default=None, description="Optional . True , if the gift is displayed on the account's profile page; for gifts received on behalf of business accounts only")
    can_be_transferred: None | bool = Field(default=None, description="Optional . True , if the gift can be transferred to another owner; for gifts received on behalf of business accounts only")
    transfer_star_count: None | int = Field(default=None, description="Optional . Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift")
    next_transfer_date: None | int = Field(default=None, description="Optional . Point in time (Unix timestamp) when the gift can be transferred. If it is in the past, then the gift can be transferred now")
class OwnedGifts(BaseModel):
    """
    OwnedGifts type from Telegram Bot API.
    """

    total_count: int = Field(description="The total number of gifts owned by the user or the chat")
    gifts: "list[OwnedGift]" = Field(description="The list of gifts")
    next_offset: None | str = Field(default=None, description="Optional . Offset for the next request. If empty, then there are no more results")
class PaidMedia(BaseModel):
    """
    PaidMedia type from Telegram Bot API.
    """

    type: str = Field(description="Type of the paid media, always “preview”")
    width: None | int = Field(default=None, description="Optional . Media width as defined by the sender")
    height: None | int = Field(default=None, description="Optional . Media height as defined by the sender")
    duration: None | int = Field(default=None, description="Optional . Duration of the media in seconds as defined by the sender")
class PaidMediaInfo(BaseModel):
    """
    PaidMediaInfo type from Telegram Bot API.
    """

    star_count: int = Field(description="The number of Telegram Stars that must be paid to buy access to the media")
    paid_media: "list[PaidMedia]" = Field(description="Information about the paid media")
class PaidMediaPhoto(BaseModel):
    """
    PaidMediaPhoto type from Telegram Bot API.
    """

    type: str = Field(description="Type of the paid media, always “photo”")
    photo: "list[PhotoSize]" = Field(description="The photo")
class PaidMediaPreview(BaseModel):
    """
    PaidMediaPreview type from Telegram Bot API.
    """

    type: str = Field(description="Type of the paid media, always “preview”")
    width: None | int = Field(default=None, description="Optional . Media width as defined by the sender")
    height: None | int = Field(default=None, description="Optional . Media height as defined by the sender")
    duration: None | int = Field(default=None, description="Optional . Duration of the media in seconds as defined by the sender")
class PaidMediaVideo(BaseModel):
    """
    PaidMediaVideo type from Telegram Bot API.
    """

    type: str = Field(description="Type of the paid media, always “video”")
    video: "Video" = Field(description="The video")
class PaidMessagePriceChanged(BaseModel):
    """
    PaidMessagePriceChanged type from Telegram Bot API.
    """

    paid_message_star_count: int = Field(description="The new number of Telegram Stars that must be paid by non-administrator users of the supergroup chat for each sent message")
class PhotoSize(BaseModel):
    """
    PhotoSize type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    width: int = Field(description="Photo width")
    height: int = Field(description="Photo height")
    file_size: None | int = Field(default=None, description="Optional . File size in bytes")
class Poll(BaseModel):
    """
    Poll type from Telegram Bot API.
    """

    id: str = Field(description="Unique poll identifier")
    question: str = Field(description="Poll question, 1-300 characters")
    question_entities: None | list[MessageEntity] = Field(default=None, description="Optional . Special entities that appear in the question . Currently, only custom emoji entities are allowed in poll questions")
    options: "list[PollOption]" = Field(description="List of poll options")
    total_voter_count: int = Field(description="Total number of users that voted in the poll")
    is_closed: bool = Field(description="True , if the poll is closed")
    is_anonymous: bool = Field(description="True , if the poll is anonymous")
    type: str = Field(description="Poll type, currently can be “regular” or “quiz”")
    allows_multiple_answers: bool = Field(description="True , if the poll allows multiple answers")
    correct_option_id: None | int = Field(default=None, description="Optional . 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.")
    explanation: None | str = Field(default=None, description="Optional . Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters")
    explanation_entities: None | list[MessageEntity] = Field(default=None, description="Optional . Special entities like usernames, URLs, bot commands, etc. that appear in the explanation")
    open_period: None | int = Field(default=None, description="Optional . Amount of time in seconds the poll will be active after creation")
    close_date: None | int = Field(default=None, description="Optional . Point in time (Unix timestamp) when the poll will be automatically closed")
class PollAnswer(BaseModel):
    """
    PollAnswer type from Telegram Bot API.
    """

    poll_id: str = Field(description="Unique poll identifier")
    voter_chat: "None | Chat" = Field(default=None, description="Optional . The chat that changed the answer to the poll, if the voter is anonymous")
    user: "None | User" = Field(default=None, description="Optional . The user that changed the answer to the poll, if the voter isn't anonymous")
    option_ids: list[int] = Field(description="0-based identifiers of chosen answer options. May be empty if the vote was retracted.")
class PollOption(BaseModel):
    """
    PollOption type from Telegram Bot API.
    """

    text: str = Field(description="Option text, 1-100 characters")
    text_entities: None | list[MessageEntity] = Field(default=None, description="Optional . Special entities that appear in the option text . Currently, only custom emoji entities are allowed in poll option texts")
    voter_count: int = Field(description="Number of users that voted for this option")
class Profileaccentcolors(BaseModel):
    """
    Profileaccentcolors type from Telegram Bot API.
    """
class ProximityAlertTriggered(BaseModel):
    """
    ProximityAlertTriggered type from Telegram Bot API.
    """

    traveler: "User" = Field(description="User that triggered the alert")
    watcher: "User" = Field(description="User that set the alert")
    distance: int = Field(description="The distance between the users")
class ReactionCount(BaseModel):
    """
    ReactionCount type from Telegram Bot API.
    """

    type: "ReactionType" = Field(description="Type of the reaction")
    total_count: int = Field(description="Number of times the reaction was added")
class ReactionType(BaseModel):
    """
    ReactionType type from Telegram Bot API.
    """

    type: str = Field(description="Type of the reaction, always “emoji”")
    emoji: str = Field(description="Reaction emoji. Currently, it can be one of \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \"")
class ReactionTypeCustomEmoji(BaseModel):
    """
    ReactionTypeCustomEmoji type from Telegram Bot API.
    """

    type: str = Field(description="Type of the reaction, always “custom_emoji”")
    custom_emoji_id: str = Field(description="Custom emoji identifier")
class ReactionTypeEmoji(BaseModel):
    """
    ReactionTypeEmoji type from Telegram Bot API.
    """

    type: str = Field(description="Type of the reaction, always “emoji”")
    emoji: str = Field(description="Reaction emoji. Currently, it can be one of \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \", \" \"")
class ReactionTypePaid(BaseModel):
    """
    ReactionTypePaid type from Telegram Bot API.
    """

    type: str = Field(description="Type of the reaction, always “paid”")
class ReplyKeyboardMarkup(BaseModel):
    """
    ReplyKeyboardMarkup type from Telegram Bot API.
    """

    keyboard: "list[KeyboardButton]" = Field(description="Array of button rows, each represented by an Array of KeyboardButton objects")
    is_persistent: None | bool = Field(default=None, description="Optional . Requests clients to always show the keyboard when the regular keyboard is hidden. Defaults to false , in which case the custom keyboard can be hidden and opened with a keyboard icon.")
    resize_keyboard: None | bool = Field(default=None, description="Optional . Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false , in which case the custom keyboard is always of the same height as the app's standard keyboard.")
    one_time_keyboard: None | bool = Field(default=None, description="Optional . Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat - the user can press a special button in the input field to see the custom keyboard again. Defaults to false .")
    input_field_placeholder: None | str = Field(default=None, description="Optional . The placeholder to be shown in the input field when the keyboard is active; 1-64 characters")
    selective: None | bool = Field(default=None, description="Optional . Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message. Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.")
class ReplyKeyboardRemove(BaseModel):
    """
    ReplyKeyboardRemove type from Telegram Bot API.
    """

    remove_keyboard: bool = Field(description="Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup )")
    selective: None | bool = Field(default=None, description="Optional . Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message. Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.")
class ReplyParameters(BaseModel):
    """
    ReplyParameters type from Telegram Bot API.
    """

    message_id: int = Field(description="Identifier of the message that will be replied to in the current chat, or in the chat chat_id if it is specified")
    chat_id: "None | int | str" = Field(default=None, description="Optional . If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format @channelusername ). Not supported for messages sent on behalf of a business account and messages from channel direct messages chats.")
    allow_sending_without_reply: None | bool = Field(default=None, description="Optional . Pass True if the message should be sent even if the specified message to be replied to is not found. Always False for replies in another chat or forum topic. Always True for messages sent on behalf of a business account.")
    quote: None | str = Field(default=None, description="Optional . Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including bold , italic , underline , strikethrough , spoiler , and custom_emoji entities. The message will fail to send if the quote isn't found in the original message.")
    quote_parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the quote. See formatting options for more details.")
    quote_entities: None | list[MessageEntity] = Field(default=None, description="Optional . A JSON-serialized list of special entities that appear in the quote. It can be specified instead of quote_parse_mode .")
    quote_position: None | int = Field(default=None, description="Optional . Position of the quote in the original message in UTF-16 code units")
    checklist_task_id: None | int = Field(default=None, description="Optional . Identifier of the specific checklist task to be replied to")
class ResponseParameters(BaseModel):
    """
    ResponseParameters type from Telegram Bot API.
    """

    migrate_to_chat_id: None | int = Field(default=None, description="Optional . The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.")
    retry_after: None | int = Field(default=None, description="Optional . In case of exceeding flood control, the number of seconds left to wait before the request can be repeated")
class Sendingfiles(BaseModel):
    """
    Sendingfiles type from Telegram Bot API.
    """
class SharedUser(BaseModel):
    """
    SharedUser type from Telegram Bot API.
    """

    user_id: int = Field(description="Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means.")
    first_name: None | str = Field(default=None, description="Optional . First name of the user, if the name was requested by the bot")
    last_name: None | str = Field(default=None, description="Optional . Last name of the user, if the name was requested by the bot")
    username: None | str = Field(default=None, description="Optional . Username of the user, if the username was requested by the bot")
    photo: None | list[PhotoSize] = Field(default=None, description="Optional . Available sizes of the chat photo, if the photo was requested by the bot")
class StarAmount(BaseModel):
    """
    StarAmount type from Telegram Bot API.
    """

    amount: int = Field(description="Integer amount of Telegram Stars, rounded to 0; can be negative")
    nanostar_amount: None | int = Field(default=None, description="Optional . The number of 1/1000000000 shares of Telegram Stars; from -999999999 to 999999999; can be negative if and only if amount is non-positive")
class Story(BaseModel):
    """
    Story type from Telegram Bot API.
    """

    chat: "Chat" = Field(description="Chat that posted the story")
    id: int = Field(description="Unique identifier for the story in the chat")
class StoryArea(BaseModel):
    """
    StoryArea type from Telegram Bot API.
    """

    position: "StoryAreaPosition" = Field(description="Position of the area")
    type: "StoryAreaType" = Field(description="Type of the area")
class StoryAreaPosition(BaseModel):
    """
    StoryAreaPosition type from Telegram Bot API.
    """

    x_percentage: float = Field(description="The abscissa of the area's center, as a percentage of the media width")
    y_percentage: float = Field(description="The ordinate of the area's center, as a percentage of the media height")
    width_percentage: float = Field(description="The width of the area's rectangle, as a percentage of the media width")
    height_percentage: float = Field(description="The height of the area's rectangle, as a percentage of the media height")
    rotation_angle: float = Field(description="The clockwise rotation angle of the rectangle, in degrees; 0-360")
    corner_radius_percentage: float = Field(description="The radius of the rectangle corner rounding, as a percentage of the media width")
class StoryAreaType(BaseModel):
    """
    StoryAreaType type from Telegram Bot API.
    """

    type: str = Field(description="Type of the area, always “location”")
    latitude: float = Field(description="Location latitude in degrees")
    longitude: float = Field(description="Location longitude in degrees")
    address: "None | LocationAddress" = Field(default=None, description="Optional . Address of the location")
class StoryAreaTypeLink(BaseModel):
    """
    StoryAreaTypeLink type from Telegram Bot API.
    """

    type: str = Field(description="Type of the area, always “link”")
    url: str = Field(description="HTTP or tg:// URL to be opened when the area is clicked")
class StoryAreaTypeLocation(BaseModel):
    """
    StoryAreaTypeLocation type from Telegram Bot API.
    """

    type: str = Field(description="Type of the area, always “location”")
    latitude: float = Field(description="Location latitude in degrees")
    longitude: float = Field(description="Location longitude in degrees")
    address: "None | LocationAddress" = Field(default=None, description="Optional . Address of the location")
class StoryAreaTypeSuggestedReaction(BaseModel):
    """
    StoryAreaTypeSuggestedReaction type from Telegram Bot API.
    """

    type: str = Field(description="Type of the area, always “suggested_reaction”")
    reaction_type: "ReactionType" = Field(description="Type of the reaction")
    is_dark: None | bool = Field(default=None, description="Optional . Pass True if the reaction area has a dark background")
    is_flipped: None | bool = Field(default=None, description="Optional . Pass True if reaction area corner is flipped")
class StoryAreaTypeUniqueGift(BaseModel):
    """
    StoryAreaTypeUniqueGift type from Telegram Bot API.
    """

    type: str = Field(description="Type of the area, always “unique_gift”")
    name: str = Field(description="Unique name of the gift")
class StoryAreaTypeWeather(BaseModel):
    """
    StoryAreaTypeWeather type from Telegram Bot API.
    """

    type: str = Field(description="Type of the area, always “weather”")
    temperature: float = Field(description="Temperature, in degree Celsius")
    emoji: str = Field(description="Emoji representing the weather")
    background_color: int = Field(description="A color of the area background in the ARGB format")
class SuggestedPostApprovalFailed(BaseModel):
    """
    SuggestedPostApprovalFailed type from Telegram Bot API.
    """

    suggested_post_message: "None | Message" = Field(default=None, description="Optional . Message containing the suggested post whose approval has failed. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    price: "SuggestedPostPrice" = Field(description="Expected price of the post")
class SuggestedPostApproved(BaseModel):
    """
    SuggestedPostApproved type from Telegram Bot API.
    """

    suggested_post_message: "None | Message" = Field(default=None, description="Optional . Message containing the suggested post. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    price: "None | SuggestedPostPrice" = Field(default=None, description="Optional . Amount paid for the post")
    send_date: int = Field(description="Date when the post will be published")
class SuggestedPostDeclined(BaseModel):
    """
    SuggestedPostDeclined type from Telegram Bot API.
    """

    suggested_post_message: "None | Message" = Field(default=None, description="Optional . Message containing the suggested post. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    comment: None | str = Field(default=None, description="Optional . Comment with which the post was declined")
class SuggestedPostInfo(BaseModel):
    """
    SuggestedPostInfo type from Telegram Bot API.
    """

    state: str = Field(description="State of the suggested post. Currently, it can be one of “pending”, “approved”, “declined”.")
    price: "None | SuggestedPostPrice" = Field(default=None, description="Optional . Proposed price of the post. If the field is omitted, then the post is unpaid.")
    send_date: None | int = Field(default=None, description="Optional . Proposed send date of the post. If the field is omitted, then the post can be published at any time within 30 days at the sole discretion of the user or administrator who approves it.")
class SuggestedPostPaid(BaseModel):
    """
    SuggestedPostPaid type from Telegram Bot API.
    """

    suggested_post_message: "None | Message" = Field(default=None, description="Optional . Message containing the suggested post. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    currency: str = Field(description="Currency in which the payment was made. Currently, one of “XTR” for Telegram Stars or “TON” for toncoins")
    amount: None | int = Field(default=None, description="Optional . The amount of the currency that was received by the channel in nanotoncoins; for payments in toncoins only")
    star_amount: "None | StarAmount" = Field(default=None, description="Optional . The amount of Telegram Stars that was received by the channel; for payments in Telegram Stars only")
class SuggestedPostParameters(BaseModel):
    """
    SuggestedPostParameters type from Telegram Bot API.
    """

    price: "None | SuggestedPostPrice" = Field(default=None, description="Optional . Proposed price for the post. If the field is omitted, then the post is unpaid.")
    send_date: None | int = Field(default=None, description="Optional . Proposed send date of the post. If specified, then the date must be between 300 second and 2678400 seconds (30 days) in the future. If the field is omitted, then the post can be published at any time within 30 days at the sole discretion of the user who approves it.")
class SuggestedPostPrice(BaseModel):
    """
    SuggestedPostPrice type from Telegram Bot API.
    """

    currency: str = Field(description="Currency in which the post will be paid. Currently, must be one of “XTR” for Telegram Stars or “TON” for toncoins")
    amount: int = Field(description="The amount of the currency that will be paid for the post in the smallest units of the currency, i.e. Telegram Stars or nanotoncoins. Currently, price in Telegram Stars must be between 5 and 100000, and price in nanotoncoins must be between 10000000 and 10000000000000.")
class SuggestedPostRefunded(BaseModel):
    """
    SuggestedPostRefunded type from Telegram Bot API.
    """

    suggested_post_message: "None | Message" = Field(default=None, description="Optional . Message containing the suggested post. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    reason: str = Field(description="Reason for the refund. Currently, one of “post_deleted” if the post was deleted within 24 hours of being posted or removed from scheduled messages without being posted, or “payment_refunded” if the payer refunded their payment.")
class SwitchInlineQueryChosenChat(BaseModel):
    """
    SwitchInlineQueryChosenChat type from Telegram Bot API.
    """

    query: None | str = Field(default=None, description="Optional . The default inline query to be inserted in the input field. If left empty, only the bot's username will be inserted")
    allow_user_chats: None | bool = Field(default=None, description="Optional . True , if private chats with users can be chosen")
    allow_bot_chats: None | bool = Field(default=None, description="Optional . True , if private chats with bots can be chosen")
    allow_group_chats: None | bool = Field(default=None, description="Optional . True , if group and supergroup chats can be chosen")
    allow_channel_chats: None | bool = Field(default=None, description="Optional . True , if channel chats can be chosen")
class TextQuote(BaseModel):
    """
    TextQuote type from Telegram Bot API.
    """

    text: str = Field(description="Text of the quoted part of a message that is replied to by the given message")
    entities: None | list[MessageEntity] = Field(default=None, description="Optional . Special entities that appear in the quote. Currently, only bold , italic , underline , strikethrough , spoiler , and custom_emoji entities are kept in quotes.")
    position: int = Field(description="Approximate quote position in the original message in UTF-16 code units as specified by the sender")
    is_manual: None | bool = Field(default=None, description="Optional . True , if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server.")
class UniqueGift(BaseModel):
    """
    UniqueGift type from Telegram Bot API.
    """

    gift_id: str = Field(description="Identifier of the regular gift from which the gift was upgraded")
    base_name: str = Field(description="Human-readable name of the regular gift from which this unique gift was upgraded")
    name: str = Field(description="Unique name of the gift. This name can be used in https://t.me/nft/... links and story areas")
    number: int = Field(description="Unique number of the upgraded gift among gifts upgraded from the same regular gift")
    model: "UniqueGiftModel" = Field(description="Model of the gift")
    symbol: "UniqueGiftSymbol" = Field(description="Symbol of the gift")
    backdrop: "UniqueGiftBackdrop" = Field(description="Backdrop of the gift")
    is_premium: None | bool = Field(default=None, description="Optional . True , if the original regular gift was exclusively purchaseable by Telegram Premium subscribers")
    is_burned: None | bool = Field(default=None, description="Optional . True , if the gift was used to craft another gift and isn't available anymore")
    is_from_blockchain: None | bool = Field(default=None, description="Optional . True , if the gift is assigned from the TON blockchain and can't be resold or transferred in Telegram")
    colors: "None | UniqueGiftColors" = Field(default=None, description="Optional . The color scheme that can be used by the gift's owner for the chat's name, replies to messages and link previews; for business account gifts and gifts that are currently on sale only")
    publisher_chat: "None | Chat" = Field(default=None, description="Optional . Information about the chat that published the gift")
class UniqueGiftBackdrop(BaseModel):
    """
    UniqueGiftBackdrop type from Telegram Bot API.
    """

    name: str = Field(description="Name of the backdrop")
    colors: "UniqueGiftBackdropColors" = Field(description="Colors of the backdrop")
    rarity_per_mille: int = Field(description="The number of unique gifts that receive this backdrop for every 1000 gifts upgraded")
class UniqueGiftBackdropColors(BaseModel):
    """
    UniqueGiftBackdropColors type from Telegram Bot API.
    """

    center_color: int = Field(description="The color in the center of the backdrop in RGB format")
    edge_color: int = Field(description="The color on the edges of the backdrop in RGB format")
    symbol_color: int = Field(description="The color to be applied to the symbol in RGB format")
    text_color: int = Field(description="The color for the text on the backdrop in RGB format")
class UniqueGiftColors(BaseModel):
    """
    UniqueGiftColors type from Telegram Bot API.
    """

    model_custom_emoji_id: str = Field(description="Custom emoji identifier of the unique gift's model")
    symbol_custom_emoji_id: str = Field(description="Custom emoji identifier of the unique gift's symbol")
    light_theme_main_color: int = Field(description="Main color used in light themes; RGB format")
    light_theme_other_colors: list[int] = Field(description="List of 1-3 additional colors used in light themes; RGB format")
    dark_theme_main_color: int = Field(description="Main color used in dark themes; RGB format")
    dark_theme_other_colors: list[int] = Field(description="List of 1-3 additional colors used in dark themes; RGB format")
class UniqueGiftInfo(BaseModel):
    """
    UniqueGiftInfo type from Telegram Bot API.
    """

    gift: "UniqueGift" = Field(description="Information about the gift")
    origin: str = Field(description="Origin of the gift. Currently, either “upgrade” for gifts upgraded from regular gifts, “transfer” for gifts transferred from other users or channels, “resale” for gifts bought from other users, “gifted_upgrade” for upgrades purchased after the gift was sent, or “offer” for gifts bought or sold through gift purchase offers")
    last_resale_currency: None | str = Field(default=None, description="Optional . For gifts bought from other users, the currency in which the payment for the gift was done. Currently, one of “XTR” for Telegram Stars or “TON” for toncoins.")
    last_resale_amount: None | int = Field(default=None, description="Optional . For gifts bought from other users, the price paid for the gift in either Telegram Stars or nanotoncoins")
    owned_gift_id: None | str = Field(default=None, description="Optional . Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts")
    transfer_star_count: None | int = Field(default=None, description="Optional . Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift")
    next_transfer_date: None | int = Field(default=None, description="Optional . Point in time (Unix timestamp) when the gift can be transferred. If it is in the past, then the gift can be transferred now")
class UniqueGiftModel(BaseModel):
    """
    UniqueGiftModel type from Telegram Bot API.
    """

    name: str = Field(description="Name of the model")
    sticker: "Sticker" = Field(description="The sticker that represents the unique gift")
    rarity_per_mille: int = Field(description="The number of unique gifts that receive this model for every 1000 gift upgrades. Always 0 for crafted gifts.")
    rarity: None | str = Field(default=None, description="Optional . Rarity of the model if it is a crafted model. Currently, can be “uncommon”, “rare”, “epic”, or “legendary”.")
class UniqueGiftSymbol(BaseModel):
    """
    UniqueGiftSymbol type from Telegram Bot API.
    """

    name: str = Field(description="Name of the symbol")
    sticker: "Sticker" = Field(description="The sticker that represents the unique gift")
    rarity_per_mille: int = Field(description="The number of unique gifts that receive this model for every 1000 gifts upgraded")
class User(BaseModel):
    """
    User type from Telegram Bot API.
    """

    id: int = Field(description="Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.")
    is_bot: bool = Field(description="True , if this user is a bot")
    first_name: str = Field(description="User's or bot's first name")
    last_name: None | str = Field(default=None, description="Optional . User's or bot's last name")
    username: None | str = Field(default=None, description="Optional . User's or bot's username")
    language_code: None | str = Field(default=None, description="Optional . IETF language tag of the user's language")
    is_premium: None | bool = Field(default=None, description="Optional . True , if this user is a Telegram Premium user")
    added_to_attachment_menu: None | bool = Field(default=None, description="Optional . True , if this user added the bot to the attachment menu")
    can_join_groups: None | bool = Field(default=None, description="Optional . True , if the bot can be invited to groups. Returned only in getMe .")
    can_read_all_group_messages: None | bool = Field(default=None, description="Optional . True , if privacy mode is disabled for the bot. Returned only in getMe .")
    supports_inline_queries: None | bool = Field(default=None, description="Optional . True , if the bot supports inline queries. Returned only in getMe .")
    can_connect_to_business: None | bool = Field(default=None, description="Optional . True , if the bot can be connected to a Telegram Business account to receive its messages. Returned only in getMe .")
    has_main_web_app: None | bool = Field(default=None, description="Optional . True , if the bot has a main Web App. Returned only in getMe .")
    has_topics_enabled: None | bool = Field(default=None, description="Optional . True , if the bot has forum topic mode enabled in private chats. Returned only in getMe .")
    allows_users_to_create_topics: None | bool = Field(default=None, description="Optional . True , if the bot allows users to create and delete topics in private chats. Returned only in getMe .")
class UserChatBoosts(BaseModel):
    """
    UserChatBoosts type from Telegram Bot API.
    """

    boosts: "list[ChatBoost]" = Field(description="The list of boosts added to the chat by the user")
class UserProfileAudios(BaseModel):
    """
    UserProfileAudios type from Telegram Bot API.
    """

    total_count: int = Field(description="Total number of profile audios for the target user")
    audios: "list[Audio]" = Field(description="Requested profile audios")
class UserProfilePhotos(BaseModel):
    """
    UserProfilePhotos type from Telegram Bot API.
    """

    total_count: int = Field(description="Total number of profile pictures the target user has")
    photos: "list[PhotoSize]" = Field(description="Requested profile pictures (in up to 4 sizes each)")
class UserRating(BaseModel):
    """
    UserRating type from Telegram Bot API.
    """

    level: int = Field(description="Current level of the user, indicating their reliability when purchasing digital goods and services. A higher level suggests a more trustworthy customer; a negative level is likely reason for concern.")
    rating: int = Field(description="Numerical value of the user's rating; the higher the rating, the better")
    current_level_rating: int = Field(description="The rating value required to get the current level")
    next_level_rating: None | int = Field(default=None, description="Optional . The rating value required to get to the next level; omitted if the maximum level was reached")
class UsersShared(BaseModel):
    """
    UsersShared type from Telegram Bot API.
    """

    request_id: int = Field(description="Identifier of the request")
    users: "list[SharedUser]" = Field(description="Information about users shared with the bot.")
class Venue(BaseModel):
    """
    Venue type from Telegram Bot API.
    """

    location: "Location" = Field(description="Venue location. Can't be a live location")
    title: str = Field(description="Name of the venue")
    address: str = Field(description="Address of the venue")
    foursquare_id: None | str = Field(default=None, description="Optional . Foursquare identifier of the venue")
    foursquare_type: None | str = Field(default=None, description="Optional . Foursquare type of the venue. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)")
    google_place_id: None | str = Field(default=None, description="Optional . Google Places identifier of the venue")
    google_place_type: None | str = Field(default=None, description="Optional . Google Places type of the venue. (See supported types .)")
class Video(BaseModel):
    """
    Video type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    width: int = Field(description="Video width as defined by the sender")
    height: int = Field(description="Video height as defined by the sender")
    duration: int = Field(description="Duration of the video in seconds as defined by the sender")
    thumbnail: "None | PhotoSize" = Field(default=None, description="Optional . Video thumbnail")
    cover: None | list[PhotoSize] = Field(default=None, description="Optional . Available sizes of the cover of the video in the message")
    start_timestamp: None | int = Field(default=None, description="Optional . Timestamp in seconds from which the video will play in the message")
    qualities: None | list[VideoQuality] = Field(default=None, description="Optional . List of available qualities of the video")
    file_name: None | str = Field(default=None, description="Optional . Original filename as defined by the sender")
    mime_type: None | str = Field(default=None, description="Optional . MIME type of the file as defined by the sender")
    file_size: None | int = Field(default=None, description="Optional . File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.")
class VideoChatEnded(BaseModel):
    """
    VideoChatEnded type from Telegram Bot API.
    """

    duration: int = Field(description="Video chat duration in seconds")
class VideoChatParticipantsInvited(BaseModel):
    """
    VideoChatParticipantsInvited type from Telegram Bot API.
    """

    users: "list[User]" = Field(description="New members that were invited to the video chat")
class VideoChatScheduled(BaseModel):
    """
    VideoChatScheduled type from Telegram Bot API.
    """

    start_date: int = Field(description="Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator")
class VideoChatStarted(BaseModel):
    """
    VideoChatStarted type from Telegram Bot API.
    """

    duration: int = Field(description="Video chat duration in seconds")
class VideoNote(BaseModel):
    """
    VideoNote type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    length: int = Field(description="Video width and height (diameter of the video message) as defined by the sender")
    duration: int = Field(description="Duration of the video in seconds as defined by the sender")
    thumbnail: "None | PhotoSize" = Field(default=None, description="Optional . Video thumbnail")
    file_size: None | int = Field(default=None, description="Optional . File size in bytes")
class VideoQuality(BaseModel):
    """
    VideoQuality type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    width: int = Field(description="Video width")
    height: int = Field(description="Video height")
    codec: str = Field(description="Codec that was used to encode the video, for example, “h264”, “h265”, or “av01”")
    file_size: None | int = Field(default=None, description="Optional . File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.")
class Voice(BaseModel):
    """
    Voice type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    duration: int = Field(description="Duration of the audio in seconds as defined by the sender")
    mime_type: None | str = Field(default=None, description="Optional . MIME type of the file as defined by the sender")
    file_size: None | int = Field(default=None, description="Optional . File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.")
class WebAppData(BaseModel):
    """
    WebAppData type from Telegram Bot API.
    """

    data: str = Field(description="The data. Be aware that a bad client can send arbitrary data in this field.")
    button_text: str = Field(description="Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field.")
class WebAppInfo(BaseModel):
    """
    WebAppInfo type from Telegram Bot API.
    """

    url: str = Field(description="An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps")
class WriteAccessAllowed(BaseModel):
    """
    WriteAccessAllowed type from Telegram Bot API.
    """

    from_request: None | bool = Field(default=None, description="Optional . True , if the access was granted after the user accepted an explicit request from a Web App sent by the method requestWriteAccess")
    web_app_name: None | str = Field(default=None, description="Optional . Name of the Web App, if the access was granted when the Web App was launched from a link")
    from_attachment_menu: None | bool = Field(default=None, description="Optional . True , if the access was granted when the bot was added to the attachment or side menu")
