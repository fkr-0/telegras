from __future__ import annotations

"""Telegram Bot API - Core."""

from pydantic import BaseModel, Field

from .types import Animation
from .types import Audio
from .types import ChatBackground
from .types import ChatBoostAdded
from .types import ChatOwnerChanged
from .types import ChatOwnerLeft
from .types import ChatShared
from .types import Checklist
from .types import ChecklistTasksAdded
from .types import ChecklistTasksDone
from .types import Contact
from .types import Dice
from .types import DirectMessagePriceChanged
from .types import DirectMessagesTopic
from .types import Document
from .types import ExternalReplyInfo
from .types import ForumTopicClosed
from .types import ForumTopicCreated
from .types import ForumTopicEdited
from .types import ForumTopicReopened
from .types import GeneralForumTopicHidden
from .types import GeneralForumTopicUnhidden
from .types import GiftInfo
from .types import Giveaway
from .types import GiveawayCompleted
from .types import GiveawayCreated
from .types import GiveawayWinners
from .types import InlineKeyboardMarkup
from .types import LinkPreviewOptions
from .types import Location
from .types import MaybeInaccessibleMessage
from .types import MessageAutoDeleteTimerChanged
from .types import MessageEntity
from .types import MessageOrigin
from .types import PaidMediaInfo
from .types import PaidMessagePriceChanged
from .types import PhotoSize
from .types import Poll
from .types import ProximityAlertTriggered
from .types import RefundedPayment
from .types import Sticker
from .types import Story
from .types import SuggestedPostApprovalFailed
from .types import SuggestedPostApproved
from .types import SuggestedPostDeclined
from .types import SuggestedPostInfo
from .types import SuggestedPostPaid
from .types import SuggestedPostRefunded
from .types import TextQuote
from .types import UniqueGiftInfo
from .types import UsersShared
from .types import Venue
from .types import Video
from .types import VideoChatEnded
from .types import VideoChatParticipantsInvited
from .types import VideoChatScheduled
from .types import VideoChatStarted
from .types import VideoNote
from .types import Voice
from .types import WebAppData
from .types import WriteAccessAllowed

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
class Message(BaseModel):
    """
    Message type from Telegram Bot API.
    """

    message_id: int = Field(description="Unique message identifier inside this chat. In specific instances (e.g., message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent")
    message_thread_id: None | int = Field(default=None, description="Optional . Unique identifier of a message thread or forum topic to which the message belongs; for supergroups and private chats only")
    direct_messages_topic: None | DirectMessagesTopic = Field(default=None, description="Optional . Information about the direct messages chat topic that contains the message")
    from_: None | User = Field(default=None, description="Optional . Sender of the message; may be empty for messages sent to channels. For backward compatibility, if the message was sent on behalf of a chat, the field contains a fake sender user in non-channel chats")
    sender_chat: None | Chat = Field(default=None, description="Optional . Sender of the message when sent on behalf of a chat. For example, the supergroup itself for messages sent by its anonymous administrators or a linked channel for messages automatically forwarded to the channel's discussion group. For backward compatibility, if the message was sent on behalf of a chat, the field from contains a fake sender user in non-channel chats.")
    sender_boost_count: None | int = Field(default=None, description="Optional . If the sender of the message boosted the chat, the number of boosts added by the user")
    sender_business_bot: None | User = Field(default=None, description="Optional . The bot that actually sent the message on behalf of the business account. Available only for outgoing messages sent on behalf of the connected business account.")
    sender_tag: None | str = Field(default=None, description="Optional . Tag or custom title of the sender of the message; for supergroups only")
    date: int = Field(description="Date the message was sent in Unix time. It is always a positive number, representing a valid date.")
    business_connection_id: None | str = Field(default=None, description="Optional . Unique identifier of the business connection from which the message was received. If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier.")
    chat: Chat = Field(description="Chat the message belongs to")
    forward_origin: None | MessageOrigin = Field(default=None, description="Optional . Information about the original message for forwarded messages")
    is_topic_message: None | bool = Field(default=None, description="Optional . True , if the message is sent to a topic in a forum supergroup or a private chat with the bot")
    is_automatic_forward: None | bool = Field(default=None, description="Optional . True , if the message is a channel post that was automatically forwarded to the connected discussion group")
    reply_to_message: None | Message = Field(default=None, description="Optional . For replies in the same chat and message thread, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.")
    external_reply: None | ExternalReplyInfo = Field(default=None, description="Optional . Information about the message that is being replied to, which may come from another chat or forum topic")
    quote: None | TextQuote = Field(default=None, description="Optional . For replies that quote part of the original message, the quoted part of the message")
    reply_to_story: None | Story = Field(default=None, description="Optional . For replies to a story, the original story")
    reply_to_checklist_task_id: None | int = Field(default=None, description="Optional . Identifier of the specific checklist task that is being replied to")
    via_bot: None | User = Field(default=None, description="Optional . Bot through which the message was sent")
    edit_date: None | int = Field(default=None, description="Optional . Date the message was last edited in Unix time")
    has_protected_content: None | bool = Field(default=None, description="Optional . True , if the message can't be forwarded")
    is_from_offline: None | bool = Field(default=None, description="Optional . True , if the message was sent by an implicit action, for example, as an away or a greeting business message, or as a scheduled message")
    is_paid_post: None | bool = Field(default=None, description="Optional . True , if the message is a paid post. Note that such posts must not be deleted for 24 hours to receive the payment and can't be edited.")
    media_group_id: None | str = Field(default=None, description="Optional . The unique identifier inside this chat of a media message group this message belongs to")
    author_signature: None | str = Field(default=None, description="Optional . Signature of the post author for messages in channels, or the custom title of an anonymous group administrator")
    paid_star_count: None | int = Field(default=None, description="Optional . The number of Telegram Stars that were paid by the sender of the message to send it")
    text: None | str = Field(default=None, description="Optional . For text messages, the actual UTF-8 text of the message")
    entities: None | list[MessageEntity] = Field(default=None, description="Optional . For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text")
    link_preview_options: None | LinkPreviewOptions = Field(default=None, description="Optional . Options used for link preview generation for the message, if it is a text message and link preview options were changed")
    suggested_post_info: None | SuggestedPostInfo = Field(default=None, description="Optional . Information about suggested post parameters if the message is a suggested post in a channel direct messages chat. If the message is an approved or declined suggested post, then it can't be edited.")
    effect_id: None | str = Field(default=None, description="Optional . Unique identifier of the message effect added to the message")
    animation: None | Animation = Field(default=None, description="Optional . Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set")
    audio: None | Audio = Field(default=None, description="Optional . Message is an audio file, information about the file")
    document: None | Document = Field(default=None, description="Optional . Message is a general file, information about the file")
    paid_media: None | PaidMediaInfo = Field(default=None, description="Optional . Message contains paid media; information about the paid media")
    photo: None | list[PhotoSize] = Field(default=None, description="Optional . Message is a photo, available sizes of the photo")
    sticker: None | Sticker = Field(default=None, description="Optional . Message is a sticker, information about the sticker")
    story: None | Story = Field(default=None, description="Optional . Message is a forwarded story")
    video: None | Video = Field(default=None, description="Optional . Message is a video, information about the video")
    video_note: None | VideoNote = Field(default=None, description="Optional . Message is a video note , information about the video message")
    voice: None | Voice = Field(default=None, description="Optional . Message is a voice message, information about the file")
    caption: None | str = Field(default=None, description="Optional . Caption for the animation, audio, document, paid media, photo, video or voice")
    caption_entities: None | list[MessageEntity] = Field(default=None, description="Optional . For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption")
    show_caption_above_media: None | bool = Field(default=None, description="Optional . True , if the caption must be shown above the message media")
    has_media_spoiler: None | bool = Field(default=None, description="Optional . True , if the message media is covered by a spoiler animation")
    checklist: None | Checklist = Field(default=None, description="Optional . Message is a checklist")
    contact: None | Contact = Field(default=None, description="Optional . Message is a shared contact, information about the contact")
    dice: None | Dice = Field(default=None, description="Optional . Message is a dice with random value")
    game: None | Game = Field(default=None, description="Optional . Message is a game, information about the game. More about games »")
    poll: None | Poll = Field(default=None, description="Optional . Message is a native poll, information about the poll")
    venue: None | Venue = Field(default=None, description="Optional . Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set")
    location: None | Location = Field(default=None, description="Optional . Message is a shared location, information about the location")
    new_chat_members: None | list[User] = Field(default=None, description="Optional . New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)")
    left_chat_member: None | User = Field(default=None, description="Optional . A member was removed from the group, information about them (this member may be the bot itself)")
    chat_owner_left: None | ChatOwnerLeft = Field(default=None, description="Optional . Service message: chat owner has left")
    chat_owner_changed: None | ChatOwnerChanged = Field(default=None, description="Optional . Service message: chat owner has changed")
    new_chat_title: None | str = Field(default=None, description="Optional . A chat title was changed to this value")
    new_chat_photo: None | list[PhotoSize] = Field(default=None, description="Optional . A chat photo was change to this value")
    delete_chat_photo: None | bool = Field(default=None, description="Optional . Service message: the chat photo was deleted")
    group_chat_created: None | bool = Field(default=None, description="Optional . Service message: the group has been created")
    supergroup_chat_created: None | bool = Field(default=None, description="Optional . Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.")
    channel_chat_created: None | bool = Field(default=None, description="Optional . Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.")
    message_auto_delete_timer_changed: None | MessageAutoDeleteTimerChanged = Field(default=None, description="Optional . Service message: auto-delete timer settings changed in the chat")
    migrate_to_chat_id: None | int = Field(default=None, description="Optional . The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.")
    migrate_from_chat_id: None | int = Field(default=None, description="Optional . The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.")
    pinned_message: None | MaybeInaccessibleMessage = Field(default=None, description="Optional . Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.")
    invoice: None | Invoice = Field(default=None, description="Optional . Message is an invoice for a payment , information about the invoice. More about payments »")
    successful_payment: None | SuccessfulPayment = Field(default=None, description="Optional . Message is a service message about a successful payment, information about the payment. More about payments »")
    refunded_payment: None | RefundedPayment = Field(default=None, description="Optional . Message is a service message about a refunded payment, information about the payment. More about payments »")
    users_shared: None | UsersShared = Field(default=None, description="Optional . Service message: users were shared with the bot")
    chat_shared: None | ChatShared = Field(default=None, description="Optional . Service message: a chat was shared with the bot")
    gift: None | GiftInfo = Field(default=None, description="Optional . Service message: a regular gift was sent or received")
    unique_gift: None | UniqueGiftInfo = Field(default=None, description="Optional . Service message: a unique gift was sent or received")
    gift_upgrade_sent: None | GiftInfo = Field(default=None, description="Optional . Service message: upgrade of a gift was purchased after the gift was sent")
    connected_website: None | str = Field(default=None, description="Optional . The domain name of the website on which the user has logged in. More about Telegram Login »")
    write_access_allowed: None | WriteAccessAllowed = Field(default=None, description="Optional . Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess")
    passport_data: None | PassportData = Field(default=None, description="Optional . Telegram Passport data")
    proximity_alert_triggered: None | ProximityAlertTriggered = Field(default=None, description="Optional . Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.")
    boost_added: None | ChatBoostAdded = Field(default=None, description="Optional . Service message: user boosted the chat")
    chat_background_set: None | ChatBackground = Field(default=None, description="Optional . Service message: chat background set")
    checklist_tasks_done: None | ChecklistTasksDone = Field(default=None, description="Optional . Service message: some tasks in a checklist were marked as done or not done")
    checklist_tasks_added: None | ChecklistTasksAdded = Field(default=None, description="Optional . Service message: tasks were added to a checklist")
    direct_message_price_changed: None | DirectMessagePriceChanged = Field(default=None, description="Optional . Service message: the price for paid messages in the corresponding direct messages chat of a channel has changed")
    forum_topic_created: None | ForumTopicCreated = Field(default=None, description="Optional . Service message: forum topic created")
    forum_topic_edited: None | ForumTopicEdited = Field(default=None, description="Optional . Service message: forum topic edited")
    forum_topic_closed: None | ForumTopicClosed = Field(default=None, description="Optional . Service message: forum topic closed")
    forum_topic_reopened: None | ForumTopicReopened = Field(default=None, description="Optional . Service message: forum topic reopened")
    general_forum_topic_hidden: None | GeneralForumTopicHidden = Field(default=None, description="Optional . Service message: the 'General' forum topic hidden")
    general_forum_topic_unhidden: None | GeneralForumTopicUnhidden = Field(default=None, description="Optional . Service message: the 'General' forum topic unhidden")
    giveaway_created: None | GiveawayCreated = Field(default=None, description="Optional . Service message: a scheduled giveaway was created")
    giveaway: None | Giveaway = Field(default=None, description="Optional . The message is a scheduled giveaway message")
    giveaway_winners: None | GiveawayWinners = Field(default=None, description="Optional . A giveaway with public winners was completed")
    giveaway_completed: None | GiveawayCompleted = Field(default=None, description="Optional . Service message: a giveaway without public winners was completed")
    paid_message_price_changed: None | PaidMessagePriceChanged = Field(default=None, description="Optional . Service message: the price for paid messages has changed in the chat")
    suggested_post_approved: None | SuggestedPostApproved = Field(default=None, description="Optional . Service message: a suggested post was approved")
    suggested_post_approval_failed: None | SuggestedPostApprovalFailed = Field(default=None, description="Optional . Service message: approval of a suggested post has failed")
    suggested_post_declined: None | SuggestedPostDeclined = Field(default=None, description="Optional . Service message: a suggested post was declined")
    suggested_post_paid: None | SuggestedPostPaid = Field(default=None, description="Optional . Service message: payment for a suggested post was received")
    suggested_post_refunded: None | SuggestedPostRefunded = Field(default=None, description="Optional . Service message: payment for a suggested post was refunded")
    video_chat_scheduled: None | VideoChatScheduled = Field(default=None, description="Optional . Service message: video chat scheduled")
    video_chat_started: None | VideoChatStarted = Field(default=None, description="Optional . Service message: video chat started")
    video_chat_ended: None | VideoChatEnded = Field(default=None, description="Optional . Service message: video chat ended")
    video_chat_participants_invited: None | VideoChatParticipantsInvited = Field(default=None, description="Optional . Service message: new participants invited to a video chat")
    web_app_data: None | WebAppData = Field(default=None, description="Optional . Service message: data sent by a Web App")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="Optional . Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.")
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
