from __future__ import annotations

"""Telegram Bot API - Types."""

from pydantic import BaseModel, Field

from .core import Chat
from .core import Message
from .core import User

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
class AffiliateInfo(BaseModel):
    """
    AffiliateInfo type from Telegram Bot API.
    """

    affiliate_user: None | User = Field(default=None, description="Optional . The bot or the user that received an affiliate commission if it was received by a bot or a user")
    affiliate_chat: None | Chat = Field(default=None, description="Optional . The chat that received an affiliate commission if it was received by a chat")
    commission_per_mille: int = Field(description="The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the bot from referred users")
    amount: int = Field(description="Integer amount of Telegram Stars received by the affiliate from the transaction, rounded to 0; can be negative for refunds")
    nanostar_amount: None | int = Field(default=None, description="Optional . The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from -999999999 to 999999999; can be negative for refunds")
class Animation(BaseModel):
    """
    Animation type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    width: int = Field(description="Video width as defined by the sender")
    height: int = Field(description="Video height as defined by the sender")
    duration: int = Field(description="Duration of the video in seconds as defined by the sender")
    thumbnail: None | PhotoSize = Field(default=None, description="Optional . Animation thumbnail as defined by the sender")
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
    thumbnail: None | PhotoSize = Field(default=None, description="Optional . Thumbnail of the album cover to which the music file belongs")
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
    fill: BackgroundFill = Field(description="The background fill")
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
    fill: BackgroundFill = Field(description="The background fill")
    dark_theme_dimming: int = Field(description="Dimming of the background in dark themes, as a percentage; 0-100")
class BackgroundTypePattern(BaseModel):
    """
    BackgroundTypePattern type from Telegram Bot API.
    """

    type: str = Field(description="Type of the background, always “pattern”")
    document: Document = Field(description="Document with the pattern")
    fill: BackgroundFill = Field(description="The background fill that is combined with the pattern")
    intensity: int = Field(description="Intensity of the pattern when it is shown above the filled background; 0-100")
    is_inverted: None | bool = Field(default=None, description="Optional . True , if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only")
    is_moving: None | bool = Field(default=None, description="Optional . True , if the background moves slightly when the device is tilted")
class BackgroundTypeWallpaper(BaseModel):
    """
    BackgroundTypeWallpaper type from Telegram Bot API.
    """

    type: str = Field(description="Type of the background, always “wallpaper”")
    document: Document = Field(description="Document with the wallpaper")
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
    user: User = Field(description="Business account user that created the business connection")
    user_chat_id: int = Field(description="Identifier of a private chat with the user who created the business connection. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.")
    date: int = Field(description="Date the connection was established in Unix time")
    rights: None | BusinessBotRights = Field(default=None, description="Optional . Rights of the business bot")
    is_enabled: bool = Field(description="True , if the connection is active")
class BusinessIntro(BaseModel):
    """
    BusinessIntro type from Telegram Bot API.
    """

    title: None | str = Field(default=None, description="Optional . Title text of the business intro")
    message: None | str = Field(default=None, description="Optional . Message text of the business intro")
    sticker: None | Sticker = Field(default=None, description="Optional . Sticker of the business intro")
class BusinessLocation(BaseModel):
    """
    BusinessLocation type from Telegram Bot API.
    """

    address: str = Field(description="Address of the business")
    location: None | Location = Field(default=None, description="Optional . Location of the business")
class BusinessMessagesDeleted(BaseModel):
    """
    BusinessMessagesDeleted type from Telegram Bot API.
    """

    business_connection_id: str = Field(description="Unique identifier of the business connection")
    chat: Chat = Field(description="Information about a chat in the business account. The bot may not have access to the chat or the corresponding user.")
    message_ids: list[int] = Field(description="The list of identifiers of deleted messages in the chat of the business account")
class BusinessOpeningHours(BaseModel):
    """
    BusinessOpeningHours type from Telegram Bot API.
    """

    time_zone_name: str = Field(description="Unique name of the time zone for which the opening hours are defined")
    opening_hours: list[BusinessOpeningHoursInterval] = Field(description="List of time intervals describing business opening hours")
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
    from_: User = Field(description="Sender")
    message: None | MaybeInaccessibleMessage = Field(default=None, description="Optional . Message sent by the bot with the callback button that originated the query")
    inline_message_id: None | str = Field(default=None, description="Optional . Identifier of the message sent via the bot in inline mode, that originated the query.")
    chat_instance: str = Field(description="Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games .")
    data: None | str = Field(default=None, description="Optional . Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data.")
    game_short_name: None | str = Field(default=None, description="Optional . Short name of a Game to be returned, serves as the unique identifier for the game")
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

    type: BackgroundType = Field(description="Type of the background")
class ChatBoost(BaseModel):
    """
    ChatBoost type from Telegram Bot API.
    """

    boost_id: str = Field(description="Unique identifier of the boost")
    add_date: int = Field(description="Point in time (Unix timestamp) when the chat was boosted")
    expiration_date: int = Field(description="Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged")
    source: ChatBoostSource = Field(description="Source of the added boost")
class ChatBoostAdded(BaseModel):
    """
    ChatBoostAdded type from Telegram Bot API.
    """

    boost_count: int = Field(description="Number of boosts added by the user")
class ChatBoostRemoved(BaseModel):
    """
    ChatBoostRemoved type from Telegram Bot API.
    """

    chat: Chat = Field(description="Chat which was boosted")
    boost_id: str = Field(description="Unique identifier of the boost")
    remove_date: int = Field(description="Point in time (Unix timestamp) when the boost was removed")
    source: ChatBoostSource = Field(description="Source of the removed boost")
class ChatBoostSource(BaseModel):
    """
    ChatBoostSource type from Telegram Bot API.
    """

    source: str = Field(description="Source of the boost, always “premium”")
    user: User = Field(description="User that boosted the chat")
class ChatBoostSourceGiftCode(BaseModel):
    """
    ChatBoostSourceGiftCode type from Telegram Bot API.
    """

    source: str = Field(description="Source of the boost, always “gift_code”")
    user: User = Field(description="User for which the gift code was created")
class ChatBoostSourceGiveaway(BaseModel):
    """
    ChatBoostSourceGiveaway type from Telegram Bot API.
    """

    source: str = Field(description="Source of the boost, always “giveaway”")
    giveaway_message_id: int = Field(description="Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn't sent yet.")
    user: None | User = Field(default=None, description="Optional . User that won the prize in the giveaway if any; for Telegram Premium giveaways only")
    prize_star_count: None | int = Field(default=None, description="Optional . The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only")
    is_unclaimed: None | bool = Field(default=None, description="Optional . True , if the giveaway was completed, but there was no user to win the prize")
class ChatBoostSourcePremium(BaseModel):
    """
    ChatBoostSourcePremium type from Telegram Bot API.
    """

    source: str = Field(description="Source of the boost, always “premium”")
    user: User = Field(description="User that boosted the chat")
class ChatBoostUpdated(BaseModel):
    """
    ChatBoostUpdated type from Telegram Bot API.
    """

    chat: Chat = Field(description="Chat which was boosted")
    boost: ChatBoost = Field(description="Information about the chat boost")
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
    photo: None | ChatPhoto = Field(default=None, description="Optional . Chat photo")
    active_usernames: None | list[str] = Field(default=None, description="Optional . If non-empty, the list of all active chat usernames ; for private chats, supergroups and channels")
    birthdate: None | Birthdate = Field(default=None, description="Optional . For private chats, the date of birth of the user")
    business_intro: None | BusinessIntro = Field(default=None, description="Optional . For private chats with business accounts, the intro of the business")
    business_location: None | BusinessLocation = Field(default=None, description="Optional . For private chats with business accounts, the location of the business")
    business_opening_hours: None | BusinessOpeningHours = Field(default=None, description="Optional . For private chats with business accounts, the opening hours of the business")
    personal_chat: None | Chat = Field(default=None, description="Optional . For private chats, the personal channel of the user")
    parent_chat: None | Chat = Field(default=None, description="Optional . Information about the corresponding channel chat; for direct messages chats only")
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
    pinned_message: None | Message = Field(default=None, description="Optional . The most recent pinned message (by sending date)")
    permissions: None | ChatPermissions = Field(default=None, description="Optional . Default chat member permissions, for groups and supergroups")
    accepted_gift_types: AcceptedGiftTypes = Field(description="Information about types of gifts that are accepted by the chat or by the corresponding user for private chats")
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
    location: None | ChatLocation = Field(default=None, description="Optional . For supergroups, the location to which the supergroup is connected")
    rating: None | UserRating = Field(default=None, description="Optional . For private chats, the rating of the user if any")
    first_profile_audio: None | Audio = Field(default=None, description="Optional . For private chats, the first audio added to the profile of the user")
    unique_gift_colors: None | UniqueGiftColors = Field(default=None, description="Optional . The color scheme based on a unique gift that must be used for the chat's name, message replies and link previews")
    paid_message_star_count: None | int = Field(default=None, description="Optional . The number of Telegram Stars a general user have to pay to send a message to the chat")
class ChatInviteLink(BaseModel):
    """
    ChatInviteLink type from Telegram Bot API.
    """

    invite_link: str = Field(description="The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”.")
    creator: User = Field(description="Creator of the link")
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

    chat: Chat = Field(description="Chat to which the request was sent")
    from_: User = Field(description="User that sent the join request")
    user_chat_id: int = Field(description="Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user.")
    date: int = Field(description="Date the request was sent in Unix time")
    bio: None | str = Field(default=None, description="Optional . Bio of the user.")
    invite_link: None | ChatInviteLink = Field(default=None, description="Optional . Chat invite link that was used by the user to send the join request")
class ChatLocation(BaseModel):
    """
    ChatLocation type from Telegram Bot API.
    """

    location: Location = Field(description="The location to which the supergroup is connected. Can't be a live location.")
    address: str = Field(description="Location address; 1-64 characters, as defined by the chat owner")
class ChatMember(BaseModel):
    """
    ChatMember type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “creator”")
    user: User = Field(description="Information about the user")
    is_anonymous: bool = Field(description="True , if the user's presence in the chat is hidden")
    custom_title: None | str = Field(default=None, description="Optional . Custom title for this user")
class ChatMemberAdministrator(BaseModel):
    """
    ChatMemberAdministrator type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “administrator”")
    user: User = Field(description="Information about the user")
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
    user: User = Field(description="Information about the user")
    until_date: int = Field(description="Date when restrictions will be lifted for this user; Unix time. If 0, then the user is banned forever")
class ChatMemberLeft(BaseModel):
    """
    ChatMemberLeft type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “left”")
    user: User = Field(description="Information about the user")
class ChatMemberMember(BaseModel):
    """
    ChatMemberMember type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “member”")
    tag: None | str = Field(default=None, description="Optional . Tag of the member")
    user: User = Field(description="Information about the user")
    until_date: None | int = Field(default=None, description="Optional . Date when the user's subscription will expire; Unix time")
class ChatMemberOwner(BaseModel):
    """
    ChatMemberOwner type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “creator”")
    user: User = Field(description="Information about the user")
    is_anonymous: bool = Field(description="True , if the user's presence in the chat is hidden")
    custom_title: None | str = Field(default=None, description="Optional . Custom title for this user")
class ChatMemberRestricted(BaseModel):
    """
    ChatMemberRestricted type from Telegram Bot API.
    """

    status: str = Field(description="The member's status in the chat, always “restricted”")
    tag: None | str = Field(default=None, description="Optional . Tag of the member")
    user: User = Field(description="Information about the user")
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

    chat: Chat = Field(description="Chat the user belongs to")
    from_: User = Field(description="Performer of the action, which resulted in the change")
    date: int = Field(description="Date the change was done in Unix time")
    old_chat_member: ChatMember = Field(description="Previous information about the chat member")
    new_chat_member: ChatMember = Field(description="New information about the chat member")
    invite_link: None | ChatInviteLink = Field(default=None, description="Optional . Chat invite link, which was used by the user to join the chat; for joining by invite link events only.")
    via_join_request: None | bool = Field(default=None, description="Optional . True , if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator")
    via_chat_folder_invite_link: None | bool = Field(default=None, description="Optional . True , if the user joined the chat via a chat folder invite link")
class ChatOwnerChanged(BaseModel):
    """
    ChatOwnerChanged type from Telegram Bot API.
    """

    new_owner: User = Field(description="The new owner of the chat")
class ChatOwnerLeft(BaseModel):
    """
    ChatOwnerLeft type from Telegram Bot API.
    """

    new_owner: None | User = Field(default=None, description="Optional . The user which will be the new owner of the chat if the previous owner does not return to the chat")
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
    tasks: list[ChecklistTask] = Field(description="List of tasks in the checklist")
    others_can_add_tasks: None | bool = Field(default=None, description="Optional . True , if users other than the creator of the list can add tasks to the list")
    others_can_mark_tasks_as_done: None | bool = Field(default=None, description="Optional . True , if users other than the creator of the list can mark tasks as done or not done")
class ChecklistTask(BaseModel):
    """
    ChecklistTask type from Telegram Bot API.
    """

    id: int = Field(description="Unique identifier of the task")
    text: str = Field(description="Text of the task")
    text_entities: None | list[MessageEntity] = Field(default=None, description="Optional . Special entities that appear in the task text")
    completed_by_user: None | User = Field(default=None, description="Optional . User that completed the task; omitted if the task wasn't completed by a user")
    completed_by_chat: None | Chat = Field(default=None, description="Optional . Chat that completed the task; omitted if the task wasn't completed by a chat")
    completion_date: None | int = Field(default=None, description="Optional . Point in time (Unix timestamp) when the task was completed; 0 if the task wasn't completed")
class ChecklistTasksAdded(BaseModel):
    """
    ChecklistTasksAdded type from Telegram Bot API.
    """

    checklist_message: None | Message = Field(default=None, description="Optional . Message containing the checklist to which the tasks were added. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    tasks: list[ChecklistTask] = Field(description="List of tasks added to the checklist")
class ChecklistTasksDone(BaseModel):
    """
    ChecklistTasksDone type from Telegram Bot API.
    """

    checklist_message: None | Message = Field(default=None, description="Optional . Message containing the checklist whose tasks were marked as done or not done. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
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
    user: None | User = Field(default=None, description="Optional . Information about the user that created the topic. Currently, it is always present")
class Document(BaseModel):
    """
    Document type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    thumbnail: None | PhotoSize = Field(default=None, description="Optional . Document thumbnail as defined by the sender")
    file_name: None | str = Field(default=None, description="Optional . Original filename as defined by the sender")
    mime_type: None | str = Field(default=None, description="Optional . MIME type of the file as defined by the sender")
    file_size: None | int = Field(default=None, description="Optional . File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.")
class EncryptedCredentials(BaseModel):
    """
    EncryptedCredentials type from Telegram Bot API.
    """

    data: str = Field(description="Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication")
    hash: str = Field(description="Base64-encoded data hash for data authentication")
    secret: str = Field(description="Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption")
class ExternalReplyInfo(BaseModel):
    """
    ExternalReplyInfo type from Telegram Bot API.
    """

    origin: MessageOrigin = Field(description="Origin of the message replied to by the given message")
    chat: None | Chat = Field(default=None, description="Optional . Chat the original message belongs to. Available only if the chat is a supergroup or a channel.")
    message_id: None | int = Field(default=None, description="Optional . Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.")
    link_preview_options: None | LinkPreviewOptions = Field(default=None, description="Optional . Options used for link preview generation for the original message, if it is a text message")
    animation: None | Animation = Field(default=None, description="Optional . Message is an animation, information about the animation")
    audio: None | Audio = Field(default=None, description="Optional . Message is an audio file, information about the file")
    document: None | Document = Field(default=None, description="Optional . Message is a general file, information about the file")
    paid_media: None | PaidMediaInfo = Field(default=None, description="Optional . Message contains paid media; information about the paid media")
    photo: None | list[PhotoSize] = Field(default=None, description="Optional . Message is a photo, available sizes of the photo")
    sticker: None | Sticker = Field(default=None, description="Optional . Message is a sticker, information about the sticker")
    story: None | Story = Field(default=None, description="Optional . Message is a forwarded story")
    video: None | Video = Field(default=None, description="Optional . Message is a video, information about the video")
    video_note: None | VideoNote = Field(default=None, description="Optional . Message is a video note , information about the video message")
    voice: None | Voice = Field(default=None, description="Optional . Message is a voice message, information about the file")
    has_media_spoiler: None | bool = Field(default=None, description="Optional . True , if the message media is covered by a spoiler animation")
    checklist: None | Checklist = Field(default=None, description="Optional . Message is a checklist")
    contact: None | Contact = Field(default=None, description="Optional . Message is a shared contact, information about the contact")
    dice: None | Dice = Field(default=None, description="Optional . Message is a dice with random value")
    game: None | Game = Field(default=None, description="Optional . Message is a game, information about the game. More about games »")
    giveaway: None | Giveaway = Field(default=None, description="Optional . Message is a scheduled giveaway, information about the giveaway")
    giveaway_winners: None | GiveawayWinners = Field(default=None, description="Optional . A giveaway with public winners was completed")
    invoice: None | Invoice = Field(default=None, description="Optional . Message is an invoice for a payment , information about the invoice. More about payments »")
    location: None | Location = Field(default=None, description="Optional . Message is a shared location, information about the location")
    poll: None | Poll = Field(default=None, description="Optional . Message is a native poll, information about the poll")
    venue: None | Venue = Field(default=None, description="Optional . Message is a venue, information about the venue")
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
    sticker: Sticker = Field(description="The sticker that represents the gift")
    star_count: int = Field(description="The number of Telegram Stars that must be paid to send the sticker")
    upgrade_star_count: None | int = Field(default=None, description="Optional . The number of Telegram Stars that must be paid to upgrade the gift to a unique one")
    is_premium: None | bool = Field(default=None, description="Optional . True , if the gift can only be purchased by Telegram Premium subscribers")
    has_colors: None | bool = Field(default=None, description="Optional . True , if the gift can be used (after being upgraded) to customize a user's appearance")
    total_count: None | int = Field(default=None, description="Optional . The total number of gifts of this type that can be sent by all users; for limited gifts only")
    remaining_count: None | int = Field(default=None, description="Optional . The number of remaining gifts of this type that can be sent by all users; for limited gifts only")
    personal_total_count: None | int = Field(default=None, description="Optional . The total number of gifts of this type that can be sent by the bot; for limited gifts only")
    personal_remaining_count: None | int = Field(default=None, description="Optional . The number of remaining gifts of this type that can be sent by the bot; for limited gifts only")
    background: None | GiftBackground = Field(default=None, description="Optional . Background of the gift")
    unique_gift_variant_count: None | int = Field(default=None, description="Optional . The total number of different unique gifts that can be obtained by upgrading the gift")
    publisher_chat: None | Chat = Field(default=None, description="Optional . Information about the chat that published the gift")
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

    gift: Gift = Field(description="Information about the gift")
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

    gifts: list[Gift] = Field(description="The list of gifts")
class Giveaway(BaseModel):
    """
    Giveaway type from Telegram Bot API.
    """

    chats: list[Chat] = Field(description="The list of chats which the user must join to participate in the giveaway")
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
    giveaway_message: None | Message = Field(default=None, description="Optional . Message with the giveaway that was completed, if it wasn't deleted")
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

    chat: Chat = Field(description="The chat that created the giveaway")
    giveaway_message_id: int = Field(description="Identifier of the message with the giveaway in the chat")
    winners_selection_date: int = Field(description="Point in time (Unix timestamp) when winners of the giveaway were selected")
    winner_count: int = Field(description="Total number of winners in the giveaway")
    winners: list[User] = Field(description="List of up to 100 winners of the giveaway")
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

    chat: Chat = Field(description="Chat the message belonged to")
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
    web_app: None | WebAppInfo = Field(default=None, description="Optional . Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery . Available only in private chats between a user and the bot. Not supported for messages sent on behalf of a Telegram Business account.")
    login_url: None | LoginUrl = Field(default=None, description="Optional . An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget .")
    switch_inline_query: None | str = Field(default=None, description="Optional . If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. Not supported for messages sent in channel direct messages chats and on behalf of a Telegram Business account.")
    switch_inline_query_current_chat: None | str = Field(default=None, description="Optional . If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted. This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. Not supported in channels and for messages sent in channel direct messages chats and on behalf of a Telegram Business account.")
    switch_inline_query_chosen_chat: None | SwitchInlineQueryChosenChat = Field(default=None, description="Optional . If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot's username and the specified inline query in the input field. Not supported for messages sent in channel direct messages chats and on behalf of a Telegram Business account.")
    copy_text: None | CopyTextButton = Field(default=None, description="Optional . Description of the button that copies the specified text to the clipboard.")
    callback_game: None | CallbackGame = Field(default=None, description="Optional . Description of the game that will be launched when the user presses the button. NOTE: This type of button must always be the first button in the first row.")
    pay: None | bool = Field(default=None, description="Optional . Specify True , to send a Pay button . Substrings “ ” and “XTR” in the buttons's text will be replaced with a Telegram Star icon. NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages.")
class InlineKeyboardMarkup(BaseModel):
    """
    InlineKeyboardMarkup type from Telegram Bot API.
    """

    inline_keyboard: list[InlineKeyboardButton] = Field(description="Array of button rows, each represented by an Array of InlineKeyboardButton objects")
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
class InputChecklist(BaseModel):
    """
    InputChecklist type from Telegram Bot API.
    """

    title: str = Field(description="Title of the checklist; 1-255 characters after entities parsing")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the title. See formatting options for more details.")
    title_entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in the title, which can be specified instead of parse_mode. Currently, only bold , italic , underline , strikethrough , spoiler , and custom_emoji entities are allowed.")
    tasks: list[InputChecklistTask] = Field(description="List of 1-30 tasks in the checklist")
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
class InputContactMessageContent(BaseModel):
    """
    InputContactMessageContent type from Telegram Bot API.
    """

    phone_number: str = Field(description="Contact's phone number")
    first_name: str = Field(description="Contact's first name")
    last_name: None | str = Field(default=None, description="Optional . Contact's last name")
    vcard: None | str = Field(default=None, description="Optional . Additional data about the contact in the form of a vCard , 0-2048 bytes")
class InputFile(BaseModel):
    """
    InputFile type from Telegram Bot API.
    """

    type: str = Field(description="Type of the media, must be photo")
    media: str = Field(description="File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »")
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
class InputMessageContent(BaseModel):
    """
    InputMessageContent type from Telegram Bot API.
    """

    message_text: str = Field(description="Text of the message to be sent, 1-4096 characters")
    parse_mode: None | str = Field(default=None, description="Optional . Mode for parsing entities in the message text. See formatting options for more details.")
    entities: None | list[MessageEntity] = Field(default=None, description="Optional . List of special entities that appear in message text, which can be specified instead of parse_mode")
    link_preview_options: None | LinkPreviewOptions = Field(default=None, description="Optional . Link preview generation options for the message")
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
class InputSticker(BaseModel):
    """
    InputSticker type from Telegram Bot API.
    """

    sticker: str = Field(description="The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new file using multipart/form-data under <file_attach_name> name. Animated and video stickers can't be uploaded via HTTP URL. More information on Sending Files »")
    format: str = Field(description="Format of the added sticker, must be one of “static” for a .WEBP or .PNG image, “animated” for a .TGS animation, “video” for a .WEBM video")
    emoji_list: list[str] = Field(description="List of 1-20 emoji associated with the sticker")
    mask_position: None | MaskPosition = Field(default=None, description="Optional . Position where the mask should be placed on faces. For “mask” stickers only.")
    keywords: None | list[str] = Field(default=None, description="Optional . List of 0-20 search keywords for the sticker with total length of up to 64 characters. For “regular” and “custom_emoji” stickers only.")
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
class KeyboardButton(BaseModel):
    """
    KeyboardButton type from Telegram Bot API.
    """

    text: str = Field(description="Text of the button. If none of the fields other than text , icon_custom_emoji_id , and style are used, it will be sent as a message when the button is pressed")
    icon_custom_emoji_id: None | str = Field(default=None, description="Optional . Unique identifier of the custom emoji shown before the text of the button. Can only be used by bots that purchased additional usernames on Fragment or in the messages directly sent by the bot to private, group and supergroup chats if the owner of the bot has a Telegram Premium subscription.")
    style: None | str = Field(default=None, description="Optional . Style of the button. Must be one of “danger” (red), “success” (green) or “primary” (blue). If omitted, then an app-specific style is used.")
    request_users: None | KeyboardButtonRequestUsers = Field(default=None, description="Optional . If specified, pressing the button will open a list of suitable users. Identifiers of selected users will be sent to the bot in a “users_shared” service message. Available in private chats only.")
    request_chat: None | KeyboardButtonRequestChat = Field(default=None, description="Optional . If specified, pressing the button will open a list of suitable chats. Tapping on a chat will send its identifier to the bot in a “chat_shared” service message. Available in private chats only.")
    request_contact: None | bool = Field(default=None, description="Optional . If True , the user's phone number will be sent as a contact when the button is pressed. Available in private chats only.")
    request_location: None | bool = Field(default=None, description="Optional . If True , the user's current location will be sent when the button is pressed. Available in private chats only.")
    request_poll: None | KeyboardButtonPollType = Field(default=None, description="Optional . If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only.")
    web_app: None | WebAppInfo = Field(default=None, description="Optional . If specified, the described Web App will be launched when the button is pressed. The Web App will be able to send a “web_app_data” service message. Available in private chats only.")
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
    user_administrator_rights: None | ChatAdministratorRights = Field(default=None, description="Optional . A JSON-serialized object listing the required administrator rights of the user in the chat. The rights must be a superset of bot_administrator_rights . If not specified, no additional restrictions are applied.")
    bot_administrator_rights: None | ChatAdministratorRights = Field(default=None, description="Optional . A JSON-serialized object listing the required administrator rights of the bot in the chat. The rights must be a subset of user_administrator_rights . If not specified, no additional restrictions are applied.")
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
class MaskPosition(BaseModel):
    """
    MaskPosition type from Telegram Bot API.
    """

    point: str = Field(description="The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.")
    x_shift: float = Field(description="Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.")
    y_shift: float = Field(description="Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.")
    scale: float = Field(description="Mask scaling coefficient. For example, 2.0 means double size.")
class MaybeInaccessibleMessage(BaseModel):
    """
    MaybeInaccessibleMessage type from Telegram Bot API.
    """

    type: str = Field(description="Type of the entity. Currently, can be “mention” ( @username ), “hashtag” ( #hashtag or #hashtag@chatusername ), “cashtag” ( $USD or $USD@chatusername ), “bot_command” ( /start@jobs_bot ), “url” ( https://telegram.org ), “email” ( do-not-reply@telegram.org ), “phone_number” ( +1-212-555-0123 ), “bold” ( bold text ), “italic” ( italic text ), “underline” (underlined text), “strikethrough” (strikethrough text), “spoiler” (spoiler message), “blockquote” (block quotation), “expandable_blockquote” (collapsed-by-default block quotation), “code” (monowidth string), “pre” (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users without usernames ), “custom_emoji” (for inline custom emoji stickers), or “date_time” (for formatted date and time)")
    offset: int = Field(description="Offset in UTF-16 code units to the start of the entity")
    length: int = Field(description="Length of the entity in UTF-16 code units")
    url: None | str = Field(default=None, description="Optional . For “text_link” only, URL that will be opened after user taps on the text")
    user: None | User = Field(default=None, description="Optional . For “text_mention” only, the mentioned user")
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
    web_app: WebAppInfo = Field(description="Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery . Alternatively, a t.me link to a Web App of the bot can be specified in the object instead of the Web App's URL, in which case the Web App will be opened as if the user pressed the link.")
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
    user: None | User = Field(default=None, description="Optional . For “text_mention” only, the mentioned user")
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
    sender_user: User = Field(description="User that sent the message originally")
class MessageOriginChannel(BaseModel):
    """
    MessageOriginChannel type from Telegram Bot API.
    """

    type: str = Field(description="Type of the message origin, always “channel”")
    date: int = Field(description="Date the message was sent originally in Unix time")
    chat: Chat = Field(description="Channel chat to which the message was originally sent")
    message_id: int = Field(description="Unique message identifier inside the chat")
    author_signature: None | str = Field(default=None, description="Optional . Signature of the original post author")
class MessageOriginChat(BaseModel):
    """
    MessageOriginChat type from Telegram Bot API.
    """

    type: str = Field(description="Type of the message origin, always “chat”")
    date: int = Field(description="Date the message was sent originally in Unix time")
    sender_chat: Chat = Field(description="Chat that sent the message originally")
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
    sender_user: User = Field(description="User that sent the message originally")
class MessageReactionCountUpdated(BaseModel):
    """
    MessageReactionCountUpdated type from Telegram Bot API.
    """

    chat: Chat = Field(description="The chat containing the message")
    message_id: int = Field(description="Unique message identifier inside the chat")
    date: int = Field(description="Date of the change in Unix time")
    reactions: list[ReactionCount] = Field(description="List of reactions that are present on the message")
class MessageReactionUpdated(BaseModel):
    """
    MessageReactionUpdated type from Telegram Bot API.
    """

    chat: Chat = Field(description="The chat containing the message the user reacted to")
    message_id: int = Field(description="Unique identifier of the message inside the chat")
    user: None | User = Field(default=None, description="Optional . The user that changed the reaction, if the user isn't anonymous")
    actor_chat: None | Chat = Field(default=None, description="Optional . The chat on behalf of which the reaction was changed, if the user is anonymous")
    date: int = Field(description="Date of the change in Unix time")
    old_reaction: list[ReactionType] = Field(description="Previous list of reaction types that were set by the user")
    new_reaction: list[ReactionType] = Field(description="New list of reaction types that have been set by the user")
class OwnedGift(BaseModel):
    """
    OwnedGift type from Telegram Bot API.
    """

    type: str = Field(description="Type of the gift, always “regular”")
    gift: Gift = Field(description="Information about the regular gift")
    owned_gift_id: None | str = Field(default=None, description="Optional . Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only")
    sender_user: None | User = Field(default=None, description="Optional . Sender of the gift if it is a known user")
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
    gift: Gift = Field(description="Information about the regular gift")
    owned_gift_id: None | str = Field(default=None, description="Optional . Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only")
    sender_user: None | User = Field(default=None, description="Optional . Sender of the gift if it is a known user")
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
    gift: UniqueGift = Field(description="Information about the unique gift")
    owned_gift_id: None | str = Field(default=None, description="Optional . Unique identifier of the received gift for the bot; for gifts received on behalf of business accounts only")
    sender_user: None | User = Field(default=None, description="Optional . Sender of the gift if it is a known user")
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
    gifts: list[OwnedGift] = Field(description="The list of gifts")
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
    paid_media: list[PaidMedia] = Field(description="Information about the paid media")
class PaidMediaPhoto(BaseModel):
    """
    PaidMediaPhoto type from Telegram Bot API.
    """

    type: str = Field(description="Type of the paid media, always “photo”")
    photo: list[PhotoSize] = Field(description="The photo")
class PaidMediaPreview(BaseModel):
    """
    PaidMediaPreview type from Telegram Bot API.
    """

    type: str = Field(description="Type of the paid media, always “preview”")
    width: None | int = Field(default=None, description="Optional . Media width as defined by the sender")
    height: None | int = Field(default=None, description="Optional . Media height as defined by the sender")
    duration: None | int = Field(default=None, description="Optional . Duration of the media in seconds as defined by the sender")
class PaidMediaPurchased(BaseModel):
    """
    PaidMediaPurchased type from Telegram Bot API.
    """

    from_: User = Field(description="User who purchased the media")
    paid_media_payload: str = Field(description="Bot-specified paid media payload")
class PaidMediaVideo(BaseModel):
    """
    PaidMediaVideo type from Telegram Bot API.
    """

    type: str = Field(description="Type of the paid media, always “video”")
    video: Video = Field(description="The video")
class PaidMessagePriceChanged(BaseModel):
    """
    PaidMessagePriceChanged type from Telegram Bot API.
    """

    paid_message_star_count: int = Field(description="The new number of Telegram Stars that must be paid by non-administrator users of the supergroup chat for each sent message")
class PassportElementErrorDataField(BaseModel):
    """
    PassportElementErrorDataField type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be data")
    type: str = Field(description="The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”")
    field_name: str = Field(description="Name of the data field which has the error")
    data_hash: str = Field(description="Base64-encoded data hash")
    message: str = Field(description="Error message")
class PassportElementErrorFile(BaseModel):
    """
    PassportElementErrorFile type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be file")
    type: str = Field(description="The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”")
    file_hash: str = Field(description="Base64-encoded file hash")
    message: str = Field(description="Error message")
class PassportElementErrorFiles(BaseModel):
    """
    PassportElementErrorFiles type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be files")
    type: str = Field(description="The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”")
    file_hashes: list[str] = Field(description="List of base64-encoded file hashes")
    message: str = Field(description="Error message")
class PassportElementErrorFrontSide(BaseModel):
    """
    PassportElementErrorFrontSide type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be front_side")
    type: str = Field(description="The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”")
    file_hash: str = Field(description="Base64-encoded hash of the file with the front side of the document")
    message: str = Field(description="Error message")
class PassportElementErrorReverseSide(BaseModel):
    """
    PassportElementErrorReverseSide type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be reverse_side")
    type: str = Field(description="The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”")
    file_hash: str = Field(description="Base64-encoded hash of the file with the reverse side of the document")
    message: str = Field(description="Error message")
class PassportElementErrorSelfie(BaseModel):
    """
    PassportElementErrorSelfie type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be selfie")
    type: str = Field(description="The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”")
    file_hash: str = Field(description="Base64-encoded hash of the file with the selfie")
    message: str = Field(description="Error message")
class PassportElementErrorTranslationFile(BaseModel):
    """
    PassportElementErrorTranslationFile type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be translation_file")
    type: str = Field(description="Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”")
    file_hash: str = Field(description="Base64-encoded file hash")
    message: str = Field(description="Error message")
class PassportElementErrorTranslationFiles(BaseModel):
    """
    PassportElementErrorTranslationFiles type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be translation_files")
    type: str = Field(description="Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”")
    file_hashes: list[str] = Field(description="List of base64-encoded file hashes")
    message: str = Field(description="Error message")
class PassportElementErrorUnspecified(BaseModel):
    """
    PassportElementErrorUnspecified type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be unspecified")
    type: str = Field(description="Type of element of the user's Telegram Passport which has the issue")
    element_hash: str = Field(description="Base64-encoded element hash")
    message: str = Field(description="Error message")
class PassportFile(BaseModel):
    """
    PassportFile type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    file_size: int = Field(description="File size in bytes")
    file_date: int = Field(description="Unix time when the file was uploaded")
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
    options: list[PollOption] = Field(description="List of poll options")
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
    voter_chat: None | Chat = Field(default=None, description="Optional . The chat that changed the answer to the poll, if the voter is anonymous")
    user: None | User = Field(default=None, description="Optional . The user that changed the answer to the poll, if the voter isn't anonymous")
    option_ids: list[int] = Field(description="0-based identifiers of chosen answer options. May be empty if the vote was retracted.")
class PollOption(BaseModel):
    """
    PollOption type from Telegram Bot API.
    """

    text: str = Field(description="Option text, 1-100 characters")
    text_entities: None | list[MessageEntity] = Field(default=None, description="Optional . Special entities that appear in the option text . Currently, only custom emoji entities are allowed in poll option texts")
    voter_count: int = Field(description="Number of users that voted for this option")
class PreparedInlineMessage(BaseModel):
    """
    PreparedInlineMessage type from Telegram Bot API.
    """

    id: str = Field(description="Unique identifier of the prepared message")
    expiration_date: int = Field(description="Expiration date of the prepared message, in Unix time. Expired prepared messages can no longer be used")
class Profileaccentcolors(BaseModel):
    """
    Profileaccentcolors type from Telegram Bot API.
    """
class ProximityAlertTriggered(BaseModel):
    """
    ProximityAlertTriggered type from Telegram Bot API.
    """

    traveler: User = Field(description="User that triggered the alert")
    watcher: User = Field(description="User that set the alert")
    distance: int = Field(description="The distance between the users")
class ReactionCount(BaseModel):
    """
    ReactionCount type from Telegram Bot API.
    """

    type: ReactionType = Field(description="Type of the reaction")
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
class RefundedPayment(BaseModel):
    """
    RefundedPayment type from Telegram Bot API.
    """

    currency: str = Field(description="Three-letter ISO 4217 currency code, or “XTR” for payments in Telegram Stars . Currently, always “XTR”")
    total_amount: int = Field(description="Total refunded price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 , total_amount = 145 . See the exp parameter in currencies.json , it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).")
    invoice_payload: str = Field(description="Bot-specified invoice payload")
    telegram_payment_charge_id: str = Field(description="Telegram payment identifier")
    provider_payment_charge_id: None | str = Field(default=None, description="Optional . Provider payment identifier")
class ReplyKeyboardMarkup(BaseModel):
    """
    ReplyKeyboardMarkup type from Telegram Bot API.
    """

    keyboard: list[KeyboardButton] = Field(description="Array of button rows, each represented by an Array of KeyboardButton objects")
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
    chat_id: None | Integer or String = Field(default=None, description="Optional . If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format @channelusername ). Not supported for messages sent on behalf of a business account and messages from channel direct messages chats.")
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
class RevenueWithdrawalState(BaseModel):
    """
    RevenueWithdrawalState type from Telegram Bot API.
    """

    type: str = Field(description="Type of the state, always “pending”")
class RevenueWithdrawalStateFailed(BaseModel):
    """
    RevenueWithdrawalStateFailed type from Telegram Bot API.
    """

    type: str = Field(description="Type of the state, always “failed”")
class RevenueWithdrawalStatePending(BaseModel):
    """
    RevenueWithdrawalStatePending type from Telegram Bot API.
    """

    type: str = Field(description="Type of the state, always “pending”")
class RevenueWithdrawalStateSucceeded(BaseModel):
    """
    RevenueWithdrawalStateSucceeded type from Telegram Bot API.
    """

    type: str = Field(description="Type of the state, always “succeeded”")
    date: int = Field(description="Date the withdrawal was completed in Unix time")
    url: str = Field(description="An HTTPS URL that can be used to see transaction details")
class Sendingfiles(BaseModel):
    """
    Sendingfiles type from Telegram Bot API.
    """
class SentWebAppMessage(BaseModel):
    """
    SentWebAppMessage type from Telegram Bot API.
    """

    inline_message_id: None | str = Field(default=None, description="Optional . Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message.")
class SharedUser(BaseModel):
    """
    SharedUser type from Telegram Bot API.
    """

    user_id: int = Field(description="Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means.")
    first_name: None | str = Field(default=None, description="Optional . First name of the user, if the name was requested by the bot")
    last_name: None | str = Field(default=None, description="Optional . Last name of the user, if the name was requested by the bot")
    username: None | str = Field(default=None, description="Optional . Username of the user, if the username was requested by the bot")
    photo: None | list[PhotoSize] = Field(default=None, description="Optional . Available sizes of the chat photo, if the photo was requested by the bot")
class ShippingAddress(BaseModel):
    """
    ShippingAddress type from Telegram Bot API.
    """

    country_code: str = Field(description="Two-letter ISO 3166-1 alpha-2 country code")
    state: str = Field(description="State, if applicable")
    city: str = Field(description="City")
    street_line1: str = Field(description="First line for the address")
    street_line2: str = Field(description="Second line for the address")
    post_code: str = Field(description="Address post code")
class StarAmount(BaseModel):
    """
    StarAmount type from Telegram Bot API.
    """

    amount: int = Field(description="Integer amount of Telegram Stars, rounded to 0; can be negative")
    nanostar_amount: None | int = Field(default=None, description="Optional . The number of 1/1000000000 shares of Telegram Stars; from -999999999 to 999999999; can be negative if and only if amount is non-positive")
class StarTransaction(BaseModel):
    """
    StarTransaction type from Telegram Bot API.
    """

    id: str = Field(description="Unique identifier of the transaction. Coincides with the identifier of the original transaction for refund transactions. Coincides with SuccessfulPayment.telegram_payment_charge_id for successful incoming payments from users.")
    amount: int = Field(description="Integer amount of Telegram Stars transferred by the transaction")
    nanostar_amount: None | int = Field(default=None, description="Optional . The number of 1/1000000000 shares of Telegram Stars transferred by the transaction; from 0 to 999999999")
    date: int = Field(description="Date the transaction was created in Unix time")
    source: None | TransactionPartner = Field(default=None, description="Optional . Source of an incoming transaction (e.g., a user purchasing goods or services, Fragment refunding a failed withdrawal). Only for incoming transactions")
    receiver: None | TransactionPartner = Field(default=None, description="Optional . Receiver of an outgoing transaction (e.g., a user for a purchase refund, Fragment for a withdrawal). Only for outgoing transactions")
class StarTransactions(BaseModel):
    """
    StarTransactions type from Telegram Bot API.
    """

    transactions: list[StarTransaction] = Field(description="The list of transactions")
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
    thumbnail: None | PhotoSize = Field(default=None, description="Optional . Sticker thumbnail in the .WEBP or .JPG format")
    emoji: None | str = Field(default=None, description="Optional . Emoji associated with the sticker")
    set_name: None | str = Field(default=None, description="Optional . Name of the sticker set to which the sticker belongs")
    premium_animation: None | File = Field(default=None, description="Optional . For premium regular stickers, premium animation for the sticker")
    mask_position: None | MaskPosition = Field(default=None, description="Optional . For mask stickers, the position where the mask should be placed")
    custom_emoji_id: None | str = Field(default=None, description="Optional . For custom emoji stickers, unique identifier of the custom emoji")
    needs_repainting: None | bool = Field(default=None, description="Optional . True , if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places")
    file_size: None | int = Field(default=None, description="Optional . File size in bytes")
class StickerSet(BaseModel):
    """
    StickerSet type from Telegram Bot API.
    """

    name: str = Field(description="Sticker set name")
    title: str = Field(description="Sticker set title")
    sticker_type: str = Field(description="Type of stickers in the set, currently one of “regular”, “mask”, “custom_emoji”")
    stickers: list[Sticker] = Field(description="List of all set stickers")
    thumbnail: None | PhotoSize = Field(default=None, description="Optional . Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format")
class Story(BaseModel):
    """
    Story type from Telegram Bot API.
    """

    chat: Chat = Field(description="Chat that posted the story")
    id: int = Field(description="Unique identifier for the story in the chat")
class StoryArea(BaseModel):
    """
    StoryArea type from Telegram Bot API.
    """

    position: StoryAreaPosition = Field(description="Position of the area")
    type: StoryAreaType = Field(description="Type of the area")
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
    address: None | LocationAddress = Field(default=None, description="Optional . Address of the location")
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
    address: None | LocationAddress = Field(default=None, description="Optional . Address of the location")
class StoryAreaTypeSuggestedReaction(BaseModel):
    """
    StoryAreaTypeSuggestedReaction type from Telegram Bot API.
    """

    type: str = Field(description="Type of the area, always “suggested_reaction”")
    reaction_type: ReactionType = Field(description="Type of the reaction")
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

    suggested_post_message: None | Message = Field(default=None, description="Optional . Message containing the suggested post whose approval has failed. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    price: SuggestedPostPrice = Field(description="Expected price of the post")
class SuggestedPostApproved(BaseModel):
    """
    SuggestedPostApproved type from Telegram Bot API.
    """

    suggested_post_message: None | Message = Field(default=None, description="Optional . Message containing the suggested post. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    price: None | SuggestedPostPrice = Field(default=None, description="Optional . Amount paid for the post")
    send_date: int = Field(description="Date when the post will be published")
class SuggestedPostDeclined(BaseModel):
    """
    SuggestedPostDeclined type from Telegram Bot API.
    """

    suggested_post_message: None | Message = Field(default=None, description="Optional . Message containing the suggested post. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    comment: None | str = Field(default=None, description="Optional . Comment with which the post was declined")
class SuggestedPostInfo(BaseModel):
    """
    SuggestedPostInfo type from Telegram Bot API.
    """

    state: str = Field(description="State of the suggested post. Currently, it can be one of “pending”, “approved”, “declined”.")
    price: None | SuggestedPostPrice = Field(default=None, description="Optional . Proposed price of the post. If the field is omitted, then the post is unpaid.")
    send_date: None | int = Field(default=None, description="Optional . Proposed send date of the post. If the field is omitted, then the post can be published at any time within 30 days at the sole discretion of the user or administrator who approves it.")
class SuggestedPostPaid(BaseModel):
    """
    SuggestedPostPaid type from Telegram Bot API.
    """

    suggested_post_message: None | Message = Field(default=None, description="Optional . Message containing the suggested post. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
    currency: str = Field(description="Currency in which the payment was made. Currently, one of “XTR” for Telegram Stars or “TON” for toncoins")
    amount: None | int = Field(default=None, description="Optional . The amount of the currency that was received by the channel in nanotoncoins; for payments in toncoins only")
    star_amount: None | StarAmount = Field(default=None, description="Optional . The amount of Telegram Stars that was received by the channel; for payments in Telegram Stars only")
class SuggestedPostParameters(BaseModel):
    """
    SuggestedPostParameters type from Telegram Bot API.
    """

    price: None | SuggestedPostPrice = Field(default=None, description="Optional . Proposed price for the post. If the field is omitted, then the post is unpaid.")
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

    suggested_post_message: None | Message = Field(default=None, description="Optional . Message containing the suggested post. Note that the Message object in this field will not contain the reply_to_message field even if it itself is a reply.")
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
class TransactionPartner(BaseModel):
    """
    TransactionPartner type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “user”")
    transaction_type: str = Field(description="Type of the transaction, currently one of “invoice_payment” for payments via invoices, “paid_media_payment” for payments for paid media, “gift_purchase” for gifts sent by the bot, “premium_purchase” for Telegram Premium subscriptions gifted by the bot, “business_account_transfer” for direct transfers from managed business accounts")
    user: User = Field(description="Information about the user")
    affiliate: None | AffiliateInfo = Field(default=None, description="Optional . Information about the affiliate that received a commission via this transaction. Can be available only for “invoice_payment” and “paid_media_payment” transactions.")
    invoice_payload: None | str = Field(default=None, description="Optional . Bot-specified invoice payload. Can be available only for “invoice_payment” transactions.")
    subscription_period: None | int = Field(default=None, description="Optional . The duration of the paid subscription. Can be available only for “invoice_payment” transactions.")
    paid_media: None | list[PaidMedia] = Field(default=None, description="Optional . Information about the paid media bought by the user; for “paid_media_payment” transactions only")
    paid_media_payload: None | str = Field(default=None, description="Optional . Bot-specified paid media payload. Can be available only for “paid_media_payment” transactions.")
    gift: None | Gift = Field(default=None, description="Optional . The gift sent to the user by the bot; for “gift_purchase” transactions only")
    premium_subscription_duration: None | int = Field(default=None, description="Optional . Number of months the gifted Telegram Premium subscription will be active for; for “premium_purchase” transactions only")
class TransactionPartnerAffiliateProgram(BaseModel):
    """
    TransactionPartnerAffiliateProgram type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “affiliate_program”")
    sponsor_user: None | User = Field(default=None, description="Optional . Information about the bot that sponsored the affiliate program")
    commission_per_mille: int = Field(description="The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users")
class TransactionPartnerChat(BaseModel):
    """
    TransactionPartnerChat type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “chat”")
    chat: Chat = Field(description="Information about the chat")
    gift: None | Gift = Field(default=None, description="Optional . The gift sent to the chat by the bot")
class TransactionPartnerFragment(BaseModel):
    """
    TransactionPartnerFragment type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “fragment”")
    withdrawal_state: None | RevenueWithdrawalState = Field(default=None, description="Optional . State of the transaction if the transaction is outgoing")
class TransactionPartnerOther(BaseModel):
    """
    TransactionPartnerOther type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “other”")
class TransactionPartnerTelegramAds(BaseModel):
    """
    TransactionPartnerTelegramAds type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “telegram_ads”")
class TransactionPartnerTelegramApi(BaseModel):
    """
    TransactionPartnerTelegramApi type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “telegram_api”")
    request_count: int = Field(description="The number of successful requests that exceeded regular limits and were therefore billed")
class TransactionPartnerUser(BaseModel):
    """
    TransactionPartnerUser type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “user”")
    transaction_type: str = Field(description="Type of the transaction, currently one of “invoice_payment” for payments via invoices, “paid_media_payment” for payments for paid media, “gift_purchase” for gifts sent by the bot, “premium_purchase” for Telegram Premium subscriptions gifted by the bot, “business_account_transfer” for direct transfers from managed business accounts")
    user: User = Field(description="Information about the user")
    affiliate: None | AffiliateInfo = Field(default=None, description="Optional . Information about the affiliate that received a commission via this transaction. Can be available only for “invoice_payment” and “paid_media_payment” transactions.")
    invoice_payload: None | str = Field(default=None, description="Optional . Bot-specified invoice payload. Can be available only for “invoice_payment” transactions.")
    subscription_period: None | int = Field(default=None, description="Optional . The duration of the paid subscription. Can be available only for “invoice_payment” transactions.")
    paid_media: None | list[PaidMedia] = Field(default=None, description="Optional . Information about the paid media bought by the user; for “paid_media_payment” transactions only")
    paid_media_payload: None | str = Field(default=None, description="Optional . Bot-specified paid media payload. Can be available only for “paid_media_payment” transactions.")
    gift: None | Gift = Field(default=None, description="Optional . The gift sent to the user by the bot; for “gift_purchase” transactions only")
    premium_subscription_duration: None | int = Field(default=None, description="Optional . Number of months the gifted Telegram Premium subscription will be active for; for “premium_purchase” transactions only")
class UniqueGift(BaseModel):
    """
    UniqueGift type from Telegram Bot API.
    """

    gift_id: str = Field(description="Identifier of the regular gift from which the gift was upgraded")
    base_name: str = Field(description="Human-readable name of the regular gift from which this unique gift was upgraded")
    name: str = Field(description="Unique name of the gift. This name can be used in https://t.me/nft/... links and story areas")
    number: int = Field(description="Unique number of the upgraded gift among gifts upgraded from the same regular gift")
    model: UniqueGiftModel = Field(description="Model of the gift")
    symbol: UniqueGiftSymbol = Field(description="Symbol of the gift")
    backdrop: UniqueGiftBackdrop = Field(description="Backdrop of the gift")
    is_premium: None | bool = Field(default=None, description="Optional . True , if the original regular gift was exclusively purchaseable by Telegram Premium subscribers")
    is_burned: None | bool = Field(default=None, description="Optional . True , if the gift was used to craft another gift and isn't available anymore")
    is_from_blockchain: None | bool = Field(default=None, description="Optional . True , if the gift is assigned from the TON blockchain and can't be resold or transferred in Telegram")
    colors: None | UniqueGiftColors = Field(default=None, description="Optional . The color scheme that can be used by the gift's owner for the chat's name, replies to messages and link previews; for business account gifts and gifts that are currently on sale only")
    publisher_chat: None | Chat = Field(default=None, description="Optional . Information about the chat that published the gift")
class UniqueGiftBackdrop(BaseModel):
    """
    UniqueGiftBackdrop type from Telegram Bot API.
    """

    name: str = Field(description="Name of the backdrop")
    colors: UniqueGiftBackdropColors = Field(description="Colors of the backdrop")
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

    gift: UniqueGift = Field(description="Information about the gift")
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
    sticker: Sticker = Field(description="The sticker that represents the unique gift")
    rarity_per_mille: int = Field(description="The number of unique gifts that receive this model for every 1000 gift upgrades. Always 0 for crafted gifts.")
    rarity: None | str = Field(default=None, description="Optional . Rarity of the model if it is a crafted model. Currently, can be “uncommon”, “rare”, “epic”, or “legendary”.")
class UniqueGiftSymbol(BaseModel):
    """
    UniqueGiftSymbol type from Telegram Bot API.
    """

    name: str = Field(description="Name of the symbol")
    sticker: Sticker = Field(description="The sticker that represents the unique gift")
    rarity_per_mille: int = Field(description="The number of unique gifts that receive this model for every 1000 gifts upgraded")
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
class UserChatBoosts(BaseModel):
    """
    UserChatBoosts type from Telegram Bot API.
    """

    boosts: list[ChatBoost] = Field(description="The list of boosts added to the chat by the user")
class UserProfileAudios(BaseModel):
    """
    UserProfileAudios type from Telegram Bot API.
    """

    total_count: int = Field(description="Total number of profile audios for the target user")
    audios: list[Audio] = Field(description="Requested profile audios")
class UserProfilePhotos(BaseModel):
    """
    UserProfilePhotos type from Telegram Bot API.
    """

    total_count: int = Field(description="Total number of profile pictures the target user has")
    photos: list[PhotoSize] = Field(description="Requested profile pictures (in up to 4 sizes each)")
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
    users: list[SharedUser] = Field(description="Information about users shared with the bot.")
class Venue(BaseModel):
    """
    Venue type from Telegram Bot API.
    """

    location: Location = Field(description="Venue location. Can't be a live location")
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
    thumbnail: None | PhotoSize = Field(default=None, description="Optional . Video thumbnail")
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

    users: list[User] = Field(description="New members that were invited to the video chat")
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
    thumbnail: None | PhotoSize = Field(default=None, description="Optional . Video thumbnail")
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
class WriteAccessAllowed(BaseModel):
    """
    WriteAccessAllowed type from Telegram Bot API.
    """

    from_request: None | bool = Field(default=None, description="Optional . True , if the access was granted after the user accepted an explicit request from a Web App sent by the method requestWriteAccess")
    web_app_name: None | str = Field(default=None, description="Optional . Name of the Web App, if the access was granted when the Web App was launched from a link")
    from_attachment_menu: None | bool = Field(default=None, description="Optional . True , if the access was granted when the bot was added to the attachment or side menu")
class addStickerToSet(BaseModel):
    """
    addStickerToSet method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier of sticker set owner")
    name: str = Field(description="Sticker set name")
    sticker: InputSticker = Field(description="A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set isn't changed.")
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
class answerPreCheckoutQuery(BaseModel):
    """
    answerPreCheckoutQuery method from Telegram Bot API.
    """

    pre_checkout_query_id: str = Field(description="Unique identifier for the query to be answered")
    ok: bool = Field(description="Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.")
    error_message: None | str = Field(default=None, description="Required if ok is False . Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. \"Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!\"). Telegram will display this message to the user.")
class answerShippingQuery(BaseModel):
    """
    answerShippingQuery method from Telegram Bot API.
    """

    shipping_query_id: str = Field(description="Unique identifier for the query to be answered")
    ok: bool = Field(description="Pass True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)")
    shipping_options: None | list[ShippingOption] = Field(default=None, description="Required if ok is True . A JSON-serialized array of available shipping options.")
    error_message: None | str = Field(default=None, description="Required if ok is False . Error message in human readable form that explains why it is impossible to complete the order (e.g. “Sorry, delivery to your desired address is unavailable”). Telegram will display this message to the user.")
class answerWebAppQuery(BaseModel):
    """
    answerWebAppQuery method from Telegram Bot API.
    """

    web_app_query_id: str = Field(description="Unique identifier for the query to be answered")
    result: InlineQueryResult = Field(description="A JSON-serialized object describing the message to be sent")
class approveSuggestedPost(BaseModel):
    """
    approveSuggestedPost method from Telegram Bot API.
    """

    chat_id: int = Field(description="Unique identifier for the target direct messages chat")
    message_id: int = Field(description="Identifier of a suggested post message to approve")
    send_date: None | int = Field(default=None, description="Point in time (Unix timestamp) when the post is expected to be published; omit if the date has already been specified when the suggested post was created. If specified, then the date must be not more than 2678400 seconds (30 days) in the future")
class createInvoiceLink(BaseModel):
    """
    createInvoiceLink method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the link will be created. For payments in Telegram Stars only.")
    title: str = Field(description="Product name, 1-32 characters")
    description: str = Field(description="Product description, 1-255 characters")
    payload: str = Field(description="Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.")
    provider_token: None | str = Field(default=None, description="Payment provider token, obtained via @BotFather . Pass an empty string for payments in Telegram Stars .")
    currency: str = Field(description="Three-letter ISO 4217 currency code, see more on currencies . Pass “XTR” for payments in Telegram Stars .")
    prices: list[LabeledPrice] = Field(description="Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in Telegram Stars .")
    subscription_period: None | int = Field(default=None, description="The number of seconds the subscription will be active for before the next payment. The currency must be set to “XTR” (Telegram Stars) if the parameter is used. Currently, it must always be 2592000 (30 days) if specified. Any number of subscriptions can be active for a given bot at the same time, including multiple concurrent subscriptions from the same user. Subscription price must no exceed 10000 Telegram Stars.")
    max_tip_amount: None | int = Field(default=None, description="The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145 . See the exp parameter in currencies.json , it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in Telegram Stars .")
    suggested_tip_amounts: None | list[int] = Field(default=None, description="A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount .")
    provider_data: None | str = Field(default=None, description="JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.")
    photo_url: None | str = Field(default=None, description="URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.")
    photo_size: None | int = Field(default=None, description="Photo size in bytes")
    photo_width: None | int = Field(default=None, description="Photo width")
    photo_height: None | int = Field(default=None, description="Photo height")
    need_name: None | bool = Field(default=None, description="Pass True if you require the user's full name to complete the order. Ignored for payments in Telegram Stars .")
    need_phone_number: None | bool = Field(default=None, description="Pass True if you require the user's phone number to complete the order. Ignored for payments in Telegram Stars .")
    need_email: None | bool = Field(default=None, description="Pass True if you require the user's email address to complete the order. Ignored for payments in Telegram Stars .")
    need_shipping_address: None | bool = Field(default=None, description="Pass True if you require the user's shipping address to complete the order. Ignored for payments in Telegram Stars .")
    send_phone_number_to_provider: None | bool = Field(default=None, description="Pass True if the user's phone number should be sent to the provider. Ignored for payments in Telegram Stars .")
    send_email_to_provider: None | bool = Field(default=None, description="Pass True if the user's email address should be sent to the provider. Ignored for payments in Telegram Stars .")
    is_flexible: None | bool = Field(default=None, description="Pass True if the final price depends on the shipping method. Ignored for payments in Telegram Stars .")
class createNewStickerSet(BaseModel):
    """
    createNewStickerSet method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier of created sticker set owner")
    name: str = Field(description="Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals ). Can contain only English letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in \"_by_<bot_username>\" . <bot_username> is case insensitive. 1-64 characters.")
    title: str = Field(description="Sticker set title, 1-64 characters")
    stickers: list[InputSticker] = Field(description="A JSON-serialized list of 1-50 initial stickers to be added to the sticker set")
    sticker_type: None | str = Field(default=None, description="Type of stickers in the set, pass “regular”, “mask”, or “custom_emoji”. By default, a regular sticker set is created.")
    needs_repainting: None | bool = Field(default=None, description="Pass True if stickers in the sticker set must be repainted to the color of text when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context; for custom emoji sticker sets only")
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
class deleteStickerFromSet(BaseModel):
    """
    deleteStickerFromSet method from Telegram Bot API.
    """

    sticker: str = Field(description="File identifier of the sticker")
class deleteStickerSet(BaseModel):
    """
    deleteStickerSet method from Telegram Bot API.
    """

    name: str = Field(description="Sticker set name")
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
class editUserStarSubscription(BaseModel):
    """
    editUserStarSubscription method from Telegram Bot API.
    """

    user_id: int = Field(description="Identifier of the user whose subscription will be edited")
    telegram_payment_charge_id: str = Field(description="Telegram payment identifier for the subscription")
    is_canceled: bool = Field(description="Pass True to cancel extension of the user subscription; the subscription must be active up to the end of the current subscription period. Pass False to allow the user to re-enable a subscription that was previously canceled by the bot.")
class getCustomEmojiStickers(BaseModel):
    """
    getCustomEmojiStickers method from Telegram Bot API.
    """

    custom_emoji_ids: list[str] = Field(description="A JSON-serialized list of custom emoji identifiers. At most 200 custom emoji identifiers can be specified.")
class getGameHighScores(BaseModel):
    """
    getGameHighScores method from Telegram Bot API.
    """

    user_id: int = Field(description="Target user id")
    chat_id: None | int = Field(default=None, description="Required if inline_message_id is not specified. Unique identifier for the target chat")
    message_id: None | int = Field(default=None, description="Required if inline_message_id is not specified. Identifier of the sent message")
    inline_message_id: None | str = Field(default=None, description="Required if chat_id and message_id are not specified. Identifier of the inline message")
class getMyStarBalance(BaseModel):
    """
    getMyStarBalance method from Telegram Bot API.
    """

    offset: None | int = Field(default=None, description="Number of transactions to skip in the response")
    limit: None | int = Field(default=None, description="The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100.")
class getStarTransactions(BaseModel):
    """
    getStarTransactions method from Telegram Bot API.
    """

    offset: None | int = Field(default=None, description="Number of transactions to skip in the response")
    limit: None | int = Field(default=None, description="The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100.")
class getStickerSet(BaseModel):
    """
    getStickerSet method from Telegram Bot API.
    """

    name: str = Field(description="Name of the sticker set")
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
class refundStarPayment(BaseModel):
    """
    refundStarPayment method from Telegram Bot API.
    """

    user_id: int = Field(description="Identifier of the user whose payment will be refunded")
    telegram_payment_charge_id: str = Field(description="Telegram payment identifier")
class replaceStickerInSet(BaseModel):
    """
    replaceStickerInSet method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier of the sticker set owner")
    name: str = Field(description="Sticker set name")
    old_sticker: str = Field(description="File identifier of the replaced sticker")
    sticker: InputSticker = Field(description="A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged.")
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
class sendGame(BaseModel):
    """
    sendGame method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int = Field(description="Unique identifier for the target chat. Games can't be sent to channel direct messages chats and channel chats.")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    game_short_name: str = Field(description="Short name of the game, serves as the unique identifier for the game. Set up your games via @BotFather .")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    reply_parameters: None | ReplyParameters = Field(default=None, description="Description of the message to reply to")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="A JSON-serialized object for an inline keyboard . If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game.")
class sendInvoice(BaseModel):
    """
    sendInvoice method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    title: str = Field(description="Product name, 1-32 characters")
    description: str = Field(description="Product description, 1-255 characters")
    payload: str = Field(description="Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.")
    provider_token: None | str = Field(default=None, description="Payment provider token, obtained via @BotFather . Pass an empty string for payments in Telegram Stars .")
    currency: str = Field(description="Three-letter ISO 4217 currency code, see more on currencies . Pass “XTR” for payments in Telegram Stars .")
    prices: list[LabeledPrice] = Field(description="Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in Telegram Stars .")
    max_tip_amount: None | int = Field(default=None, description="The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145 . See the exp parameter in currencies.json , it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in Telegram Stars .")
    suggested_tip_amounts: None | list[int] = Field(default=None, description="A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount .")
    start_parameter: None | str = Field(default=None, description="Unique deep-linking parameter. If left empty, forwarded copies of the sent message will have a Pay button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a URL button with a deep link to the bot (instead of a Pay button), with the value used as the start parameter")
    provider_data: None | str = Field(default=None, description="JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.")
    photo_url: None | str = Field(default=None, description="URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.")
    photo_size: None | int = Field(default=None, description="Photo size in bytes")
    photo_width: None | int = Field(default=None, description="Photo width")
    photo_height: None | int = Field(default=None, description="Photo height")
    need_name: None | bool = Field(default=None, description="Pass True if you require the user's full name to complete the order. Ignored for payments in Telegram Stars .")
    need_phone_number: None | bool = Field(default=None, description="Pass True if you require the user's phone number to complete the order. Ignored for payments in Telegram Stars .")
    need_email: None | bool = Field(default=None, description="Pass True if you require the user's email address to complete the order. Ignored for payments in Telegram Stars .")
    need_shipping_address: None | bool = Field(default=None, description="Pass True if you require the user's shipping address to complete the order. Ignored for payments in Telegram Stars .")
    send_phone_number_to_provider: None | bool = Field(default=None, description="Pass True if the user's phone number should be sent to the provider. Ignored for payments in Telegram Stars .")
    send_email_to_provider: None | bool = Field(default=None, description="Pass True if the user's email address should be sent to the provider. Ignored for payments in Telegram Stars .")
    is_flexible: None | bool = Field(default=None, description="Pass True if the final price depends on the shipping method. Ignored for payments in Telegram Stars .")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: None | SuggestedPostParameters = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: None | ReplyParameters = Field(default=None, description="Description of the message to reply to")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="A JSON-serialized object for an inline keyboard . If empty, one 'Pay total price ' button will be shown. If not empty, the first button must be a Pay button.")
class sendSticker(BaseModel):
    """
    sendSticker method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the message will be sent")
    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    sticker: InputFile | str = Field(description="Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data. More information on Sending Files » . Video and animated stickers can't be sent via an HTTP URL.")
    emoji: None | str = Field(default=None, description="Emoji associated with the sticker; only for just uploaded stickers")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: None | SuggestedPostParameters = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: None | ReplyParameters = Field(default=None, description="Description of the message to reply to")
    reply_markup: None | InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply = Field(default=None, description="Additional interface options. A JSON-serialized object for an inline keyboard , custom reply keyboard , instructions to remove a reply keyboard or to force a reply from the user")
class setCustomEmojiStickerSetThumbnail(BaseModel):
    """
    setCustomEmojiStickerSetThumbnail method from Telegram Bot API.
    """

    name: str = Field(description="Sticker set name")
    custom_emoji_id: None | str = Field(default=None, description="Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail.")
class setGameScore(BaseModel):
    """
    setGameScore method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier")
    score: int = Field(description="New score, must be non-negative")
    force: None | bool = Field(default=None, description="Pass True if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters")
    disable_edit_message: None | bool = Field(default=None, description="Pass True if the game message should not be automatically edited to include the current scoreboard")
    chat_id: None | int = Field(default=None, description="Required if inline_message_id is not specified. Unique identifier for the target chat")
    message_id: None | int = Field(default=None, description="Required if inline_message_id is not specified. Identifier of the sent message")
    inline_message_id: None | str = Field(default=None, description="Required if chat_id and message_id are not specified. Identifier of the inline message")
class setPassportDataErrors(BaseModel):
    """
    setPassportDataErrors method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier")
    errors: list[PassportElementError] = Field(description="A JSON-serialized array describing the errors")
class setStickerEmojiList(BaseModel):
    """
    setStickerEmojiList method from Telegram Bot API.
    """

    sticker: str = Field(description="File identifier of the sticker")
    emoji_list: list[str] = Field(description="A JSON-serialized list of 1-20 emoji associated with the sticker")
class setStickerKeywords(BaseModel):
    """
    setStickerKeywords method from Telegram Bot API.
    """

    sticker: str = Field(description="File identifier of the sticker")
    keywords: None | list[str] = Field(default=None, description="A JSON-serialized list of 0-20 search keywords for the sticker with total length of up to 64 characters")
class setStickerMaskPosition(BaseModel):
    """
    setStickerMaskPosition method from Telegram Bot API.
    """

    sticker: str = Field(description="File identifier of the sticker")
    mask_position: None | MaskPosition = Field(default=None, description="A JSON-serialized object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position.")
class setStickerPositionInSet(BaseModel):
    """
    setStickerPositionInSet method from Telegram Bot API.
    """

    sticker: str = Field(description="File identifier of the sticker")
    position: int = Field(description="New sticker position in the set, zero-based")
class setStickerSetThumbnail(BaseModel):
    """
    setStickerSetThumbnail method from Telegram Bot API.
    """

    name: str = Field(description="Sticker set name")
    user_id: int = Field(description="User identifier of the sticker set owner")
    thumbnail: None | InputFile or String = Field(default=None, description="A .WEBP or .PNG image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a .TGS animation with a thumbnail up to 32 kilobytes in size (see https://core.telegram.org/stickers#animation-requirements for animated sticker technical requirements), or a .WEBM video with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#video-requirements for video sticker technical requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files » . Animated and video sticker set thumbnails can't be uploaded via HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail.")
    format: str = Field(description="Format of the thumbnail, must be one of “static” for a .WEBP or .PNG image, “animated” for a .TGS animation, or “video” for a .WEBM video")
class setStickerSetTitle(BaseModel):
    """
    setStickerSetTitle method from Telegram Bot API.
    """

    name: str = Field(description="Sticker set name")
    title: str = Field(description="Sticker set title, 1-64 characters")
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
class uploadStickerFile(BaseModel):
    """
    uploadStickerFile method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier of sticker file owner")
    sticker: InputFile = Field(description="A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format. See https://core.telegram.org/stickers for technical requirements. More information on Sending Files »")
    sticker_format: str = Field(description="Format of the sticker, must be one of “static”, “animated”, “video”")
