"""Comprehensive tests for telegram_api.methods module."""

import pytest
import json
from pydantic import ValidationError
from telegram_api import types, methods


class TestGetMe:
    """Tests for getMe method."""

    def test_getme_creation(self):
        """Test creating getMe method."""
        get_me = methods.getMe()
        assert get_me is not None

    def test_getme_serialization(self):
        """Test getMe JSON serialization."""
        get_me = methods.getMe()
        json_str = get_me.model_dump_json()
        data = json.loads(json_str)
        assert data == {}


class TestSendMessage:
    """Tests for sendMessage method."""

    def test_sendmessage_required_only(self):
        """Test sendMessage with required fields only."""
        msg = methods.sendMessage(
            chat_id=123456789,
            text="Hello, World!"
        )
        assert msg.chat_id == 123456789
        assert msg.text == "Hello, World!"
        assert msg.parse_mode is None

    def test_sendmessage_with_chat_id_string(self):
        """Test sendMessage with string chat_id."""
        msg = methods.sendMessage(
            chat_id="@channel",
            text="Hello channel!"
        )
        assert msg.chat_id == "@channel"

    def test_sendmessage_with_parse_mode(self):
        """Test sendMessage with parse_mode."""
        msg = methods.sendMessage(
            chat_id=123,
            text="*Bold* text",
            parse_mode="Markdown"
        )
        assert msg.parse_mode == "Markdown"

    def test_sendmessage_with_all_optional_fields(self):
        """Test sendMessage with all optional fields."""
        msg = methods.sendMessage(
            chat_id=123,
            text="Test message",
            message_thread_id=1,
            parse_mode="HTML",
            entities=[
                types.MessageEntity(type="bold", offset=0, length=4)
            ],
            disable_web_page_preview=True,
            disable_notification=True,
            protect_content=True,
            reply_to_message_id=456,
            allow_sending_without_reply=True,
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton(text="Button", callback_data="data")]
                ]
            )
        )
        assert msg.disable_web_page_preview is True
        assert msg.reply_markup is not None
        assert len(msg.reply_markup.inline_keyboard) == 1

    def test_sendmessage_with_reply_markup(self):
        """Test sendMessage with inline keyboard."""
        msg = methods.sendMessage(
            chat_id=123,
            text="Choose an option:",
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        types.InlineKeyboardButton(text="Option 1", callback_data="opt1"),
                        types.InlineKeyboardButton(text="Option 2", callback_data="opt2")
                    ],
                    [
                        types.InlineKeyboardButton(text="Option 3", callback_data="opt3")
                    ]
                ]
            )
        )
        keyboard = msg.reply_markup.inline_keyboard
        assert len(keyboard) == 2
        assert len(keyboard[0]) == 2
        assert len(keyboard[1]) == 1


class TestForwardMessage:
    """Tests for forwardMessage method."""

    def test_forwardmessage_required_fields(self):
        """Test forwardMessage with required fields."""
        fwd = methods.forwardMessage(
            chat_id=123,
            from_chat_id=456,
            message_id=789
        )
        assert fwd.chat_id == 123
        assert fwd.from_chat_id == 456
        assert fwd.message_id == 789

    def test_forwardmessage_with_thread_id(self):
        """Test forwardMessage with message_thread_id."""
        fwd = methods.forwardMessage(
            chat_id=123,
            from_chat_id=456,
            message_id=789,
            message_thread_id=1
        )
        assert fwd.message_thread_id == 1


class TestCopyMessage:
    """Tests for copyMessage method."""

    def test_copymessage_required_fields(self):
        """Test copyMessage with required fields."""
        copy = methods.copyMessage(
            chat_id=123,
            from_chat_id=456,
            message_id=789
        )
        assert copy.chat_id == 123
        assert copy.from_chat_id == 456
        assert copy.message_id == 789

    def test_copymessage_with_caption(self):
        """Test copyMessage with caption."""
        copy = methods.copyMessage(
            chat_id=123,
            from_chat_id=456,
            message_id=789,
            caption="New caption"
        )
        assert copy.caption == "New caption"


class TestSendPhoto:
    """Tests for sendPhoto method."""

    def test_sendphoto_required_fields(self):
        """Test sendPhoto with required fields."""
        photo = methods.sendPhoto(
            chat_id=123,
            photo="https://example.com/photo.jpg"
        )
        assert photo.chat_id == 123
        assert photo.photo == "https://example.com/photo.jpg"

    def test_sendphoto_with_file_id(self):
        """Test sendPhoto with file_id."""
        photo = methods.sendPhoto(
            chat_id=123,
            photo="AgACAgIAAxkBAAI..."
        )
        assert photo.photo == "AgACAgIAAxkBAAI..."

    def test_sendphoto_with_caption(self):
        """Test sendPhoto with caption."""
        photo = methods.sendPhoto(
            chat_id=123,
            photo="https://example.com/photo.jpg",
            caption="Beautiful photo!",
            parse_mode="Markdown"
        )
        assert photo.caption == "Beautiful photo!"


class TestSendAudio:
    """Tests for sendAudio method."""

    def test_sendaudio_required_fields(self):
        """Test sendAudio with required fields."""
        audio = methods.sendAudio(
            chat_id=123,
            audio="https://example.com/audio.mp3"
        )
        assert audio.chat_id == 123
        assert audio.audio == "https://example.com/audio.mp3"

    def test_sendaudio_with_metadata(self):
        """Test sendAudio with full metadata."""
        audio = methods.sendAudio(
            chat_id=123,
            audio="https://example.com/audio.mp3",
            caption="Audio caption",
            duration=180,
            performer="Artist",
            title="Song Title",
            thumbnail="https://example.com/thumb.jpg"
        )
        assert audio.duration == 180
        assert audio.performer == "Artist"
        assert audio.title == "Song Title"


class TestSendDocument:
    """Tests for sendDocument method."""

    def test_senddocument_required_fields(self):
        """Test sendDocument with required fields."""
        doc = methods.sendDocument(
            chat_id=123,
            document="https://example.com/file.pdf"
        )
        assert doc.chat_id == 123
        assert doc.document == "https://example.com/file.pdf"

    def test_senddocument_with_thumbnail(self):
        """Test sendDocument with thumbnail."""
        doc = methods.sendDocument(
            chat_id=123,
            document="https://example.com/file.pdf",
            thumbnail="https://example.com/thumb.jpg",
            caption="Document caption"
        )
        assert doc.thumbnail == "https://example.com/thumb.jpg"
        assert doc.caption == "Document caption"


class TestSendVideo:
    """Tests for sendVideo method."""

    def test_sendvideo_required_fields(self):
        """Test sendVideo with required fields."""
        video = methods.sendVideo(
            chat_id=123,
            video="https://example.com/video.mp4"
        )
        assert video.chat_id == 123
        assert video.video == "https://example.com/video.mp4"

    def test_sendvideo_with_all_options(self):
        """Test sendVideo with all optional fields."""
        video = methods.sendVideo(
            chat_id=123,
            video="https://example.com/video.mp4",
            duration=120,
            width=1920,
            height=1080,
            thumbnail="https://example.com/thumb.jpg",
            caption="Video caption",
            supports_streaming=True
        )
        assert video.duration == 120
        assert video.width == 1920
        assert video.supports_streaming is True


class TestSendAnimation:
    """Tests for sendAnimation method."""

    def test_sendanimation_required_fields(self):
        """Test sendAnimation with required fields."""
        anim = methods.sendAnimation(
            chat_id=123,
            animation="https://example.com/anim.gif"
        )
        assert anim.chat_id == 123
        assert anim.animation == "https://example.com/anim.gif"

    def test_sendanimation_with_duration(self):
        """Test sendAnimation with duration."""
        anim = methods.sendAnimation(
            chat_id=123,
            animation="https://example.com/anim.gif",
            duration=5,
            width=512,
            height=512
        )
        assert anim.duration == 5
        assert anim.width == 512


class TestSendVoice:
    """Tests for sendVoice method."""

    def test_sendvoice_required_fields(self):
        """Test sendVoice with required fields."""
        voice = methods.sendVoice(
            chat_id=123,
            voice="https://example.com/voice.ogg"
        )
        assert voice.chat_id == 123
        assert voice.voice == "https://example.com/voice.ogg"

    def test_sendvoice_with_duration(self):
        """Test sendVoice with duration and caption."""
        voice = methods.sendVoice(
            chat_id=123,
            voice="https://example.com/voice.ogg",
            duration=30,
            caption="Voice message"
        )
        assert voice.duration == 30
        assert voice.caption == "Voice message"


class TestSendVideoNote:
    """Tests for sendVideoNote method."""

    def test_sendvideonote_required_fields(self):
        """Test sendVideoNote with required fields."""
        vn = methods.sendVideoNote(
            chat_id=123,
            video_note="https://example.com/videonote.mp4"
        )
        assert vn.chat_id == 123
        assert vn.video_note == "https://example.com/videonote.mp4"

    def test_sendvideonote_with_duration(self):
        """Test sendVideoNote with duration."""
        vn = methods.sendVideoNote(
            chat_id=123,
            video_note="https://example.com/videonote.mp4",
            duration=59,
            length=640
        )
        assert vn.duration == 59
        assert vn.length == 640


class TestSendMediaGroup:
    """Tests for sendMediaGroup method."""

    def test_sendmediagroup_required_fields(self):
        """Test sendMediaGroup with required fields."""
        group = methods.sendMediaGroup(
            chat_id=123,
            media=[
                types.InputMediaPhoto(
                    media="https://example.com/photo1.jpg"
                ),
                types.InputMediaPhoto(
                    media="https://example.com/photo2.jpg"
                )
            ]
        )
        assert group.chat_id == 123
        assert len(group.media) == 2

    def test_sendmediagroup_with_mixed_media(self):
        """Test sendMediaGroup with mixed media types."""
        group = methods.sendMediaGroup(
            chat_id=123,
            media=[
                types.InputMediaPhoto(
                    media="https://example.com/photo1.jpg",
                    caption="Photo 1"
                ),
                types.InputMediaVideo(
                    media="https://example.com/video1.mp4",
                    caption="Video 1",
                    duration=30,
                    width=1920,
                    height=1080
                )
            ]
        )
        assert len(group.media) == 2


class TestSendLocation:
    """Tests for sendLocation method."""

    def test_sendlocation_required_fields(self):
        """Test sendLocation with required fields."""
        loc = methods.sendLocation(
            chat_id=123,
            latitude=37.7749,
            longitude=-122.4194
        )
        assert abs(loc.latitude - 37.7749) < 0.0001
        assert abs(loc.longitude - (-122.4194)) < 0.0001

    def test_sendlocation_with_live_period(self):
        """Test sendLocation with live_period."""
        loc = methods.sendLocation(
            chat_id=123,
            latitude=37.7749,
            longitude=-122.4194,
            live_period=86400
        )
        assert loc.live_period == 86400


class TestSendVenue:
    """Tests for sendVenue method."""

    def test_sendvenue_required_fields(self):
        """Test sendVenue with required fields."""
        venue = methods.sendVenue(
            chat_id=123,
            latitude=37.7749,
            longitude=-122.4194,
            title="Test Venue",
            address="123 Test St"
        )
        assert venue.title == "Test Venue"
        assert venue.address == "123 Test St"

    def test_sendvenue_with_foursquare(self):
        """Test sendVenue with Foursquare data."""
        venue = methods.sendVenue(
            chat_id=123,
            latitude=40.7589,
            longitude=-73.9851,
            title="Times Square",
            address="Manhattan, NY",
            foursquare_id="4b0f9624f964a5205a3326e3",
            foursquare_type="arts_entertainment/default"
        )
        assert venue.foursquare_id == "4b0f9624f964a5205a3326e3"


class TestSendContact:
    """Tests for sendContact method."""

    def test_sendcontact_required_fields(self):
        """Test sendContact with required fields."""
        contact = methods.sendContact(
            chat_id=123,
            phone_number="+1234567890",
            first_name="John"
        )
        assert contact.phone_number == "+1234567890"
        assert contact.first_name == "John"

    def test_sendcontact_with_last_name(self):
        """Test sendContact with last_name."""
        contact = methods.sendContact(
            chat_id=123,
            phone_number="+1234567890",
            first_name="John",
            last_name="Doe"
        )
        assert contact.last_name == "Doe"


class TestSendPoll:
    """Tests for sendPoll method."""

    def test_sendpoll_required_fields(self):
        """Test sendPoll with required fields."""
        poll = methods.sendPoll(
            chat_id=123,
            question="What is your favorite color?",
            options=["Red", "Blue", "Green"]
        )
        assert poll.question == "What is your favorite color?"
        assert len(poll.options) == 3

    def test_sendpoll_with_is_anonymous(self):
        """Test sendPoll with is_anonymous=False."""
        poll = methods.sendPoll(
            chat_id=123,
            question="Public poll",
            options=["Option A", "Option B"],
            is_anonymous=False
        )
        assert poll.is_anonymous is False

    def test_sendpoll_with_type(self):
        """Test sendPoll with quiz type."""
        poll = methods.sendPoll(
            chat_id=123,
            question="Quiz question",
            options=["Correct", "Wrong"],
            type="quiz",
            correct_option_id=0,
            explanation="This is the correct answer"
        )
        assert poll.type == "quiz"
        assert poll.correct_option_id == 0
        assert poll.explanation == "This is the correct answer"


class TestSendDice:
    """Tests for sendDice method."""

    def test_senddice_default(self):
        """Test sendDice with default emoji."""
        dice = methods.sendDice(
            chat_id=123
        )
        assert dice.chat_id == 123

    def test_senddice_with_custom_emoji(self):
        """Test sendDice with custom emoji."""
        dice = methods.sendDice(
            chat_id=123,
            emoji="🎯"
        )
        assert dice.emoji == "🎯"


class TestSendChatAction:
    """Tests for sendChatAction method."""

    def test_sendchataction_typing(self):
        """Test sendChatAction with typing action."""
        action = methods.sendChatAction(
            chat_id=123,
            action="typing"
        )
        assert action.action == "typing"

    def test_sendchataction_upload_photo(self):
        """Test sendChatAction with upload_photo action."""
        action = methods.sendChatAction(
            chat_id=123,
            action="upload_photo"
        )
        assert action.action == "upload_photo"

    def test_sendchataction_record_video(self):
        """Test sendChatAction with record_video action."""
        action = methods.sendChatAction(
            chat_id=123,
            action="record_video"
        )
        assert action.action == "record_video"

    def test_sendchataction_record_voice(self):
        """Test sendChatAction with record_voice action."""
        action = methods.sendChatAction(
            chat_id=123,
            action="record_voice"
        )
        assert action.action == "record_voice"

    def test_sendchataction_upload_document(self):
        """Test sendChatAction with upload_document action."""
        action = methods.sendChatAction(
            chat_id=123,
            action="upload_document"
        )
        assert action.action == "upload_document"

    def test_sendchataction_choose_sticker(self):
        """Test sendChatAction with choose_sticker action."""
        action = methods.sendChatAction(
            chat_id=123,
            action="choose_sticker"
        )
        assert action.action == "choose_sticker"

    def test_sendchataction_find_location(self):
        """Test sendChatAction with find_location action."""
        action = methods.sendChatAction(
            chat_id=123,
            action="find_location"
        )
        assert action.action == "find_location"

    def test_sendchataction_record_video_note(self):
        """Test sendChatAction with record_video_note action."""
        action = methods.sendChatAction(
            chat_id=123,
            action="record_video_note"
        )
        assert action.action == "record_video_note"


class TestGetUserProfilePhotos:
    """Tests for getUserProfilePhotos method."""

    def test_getuserprofilephotos_required_fields(self):
        """Test getUserProfilePhotos with required fields."""
        photos = methods.getUserProfilePhotos(
            user_id=123
        )
        assert photos.user_id == 123

    def test_getuserprofilephotos_with_offset(self):
        """Test getUserProfilePhotos with offset and limit."""
        photos = methods.getUserProfilePhotos(
            user_id=123,
            offset=10,
            limit=50
        )
        assert photos.offset == 10
        assert photos.limit == 50


class TestGetFile:
    """Tests for getFile method."""

    def test_getfile_required_fields(self):
        """Test getFile with required fields."""
        file = methods.getFile(
            file_id="AgACAgIAAxkBAAI..."
        )
        assert file.file_id == "AgACAgIAAxkBAAI..."


class TestBanChatMember:
    """Tests for banChatMember method."""

    def test_banchatmember_required_fields(self):
        """Test banChatMember with required fields."""
        ban = methods.banChatMember(
            chat_id=-100123456789,
            user_id=123456
        )
        assert ban.chat_id == -100123456789
        assert ban.user_id == 123456

    def test_banchatmember_with_until_date(self):
        """Test banChatMember with until_date."""
        ban = methods.banChatMember(
            chat_id=-100123456789,
            user_id=123456,
            until_date=1234567890
        )
        assert ban.until_date == 1234567890


class TestUnbanChatMember:
    """Tests for unbanChatMember method."""

    def test_unbanchatmember_required_fields(self):
        """Test unbanChatMember with required fields."""
        unban = methods.unbanChatMember(
            chat_id=-100123456789,
            user_id=123456
        )
        assert unban.chat_id == -100123456789
        assert unban.user_id == 123456

    def test_unbanchatmember_with_only_if_banned(self):
        """Test unbanChatMember with only_if_banned."""
        unban = methods.unbanChatMember(
            chat_id=-100123456789,
            user_id=123456,
            only_if_banned=True
        )
        assert unban.only_if_banned is True


class TestRestrictChatMember:
    """Tests for restrictChatMember method."""

    def test_restrictchatmember_required_fields(self):
        """Test restrictChatMember with required fields."""
        restrict = methods.restrictChatMember(
            chat_id=-100123456789,
            user_id=123456,
            permissions=types.ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_polls=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False
            )
        )
        assert restrict.chat_id == -100123456789
        assert restrict.permissions.can_send_messages is False


class TestPromoteChatMember:
    """Tests for promoteChatMember method."""

    def test_promotechatmember_required_fields(self):
        """Test promoteChatMember with required fields."""
        promote = methods.promoteChatMember(
            chat_id=-100123456789,
            user_id=123456
        )
        assert promote.chat_id == -100123456789
        assert promote.user_id == 123456

    def test_promotechatmember_with_all_permissions(self):
        """Test promoteChatMember with all permissions."""
        promote = methods.promoteChatMember(
            chat_id=-100123456789,
            user_id=123456,
            is_anonymous=False,
            can_manage_chat=True,
            can_change_info=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_manage_topics=True,
            can_promote_members=True
        )
        assert promote.can_manage_chat is True
        assert promote.can_promote_members is True


class TestSetChatAdministratorTitle:
    """Tests for setChatAdministratorTitle method."""

    def test_setchatadministratortitle_required_fields(self):
        """Test setChatAdministratorTitle with required fields."""
        title = methods.setChatAdministratorTitle(
            chat_id=-100123456789,
            user_id=123456,
            custom_title="Custom Admin"
        )
        assert title.chat_id == -100123456789
        assert title.custom_title == "Custom Admin"


class TestBanChatSenderChat:
    """Tests for banChatSenderChat method."""

    def test_banchatsenderchat_required_fields(self):
        """Test banChatSenderChat with required fields."""
        ban = methods.banChatSenderChat(
            chat_id=-100123456789,
            sender_chat_id=-100987654321
        )
        assert ban.chat_id == -100123456789
        assert ban.sender_chat_id == -100987654321


class TestUnbanChatSenderChat:
    """Tests for unbanChatSenderChat method."""

    def test_unbanchatsenderchat_required_fields(self):
        """Test unbanChatSenderChat with required fields."""
        unban = methods.unbanChatSenderChat(
            chat_id=-100123456789,
            sender_chat_id=-100987654321
        )
        assert unban.chat_id == -100123456789
        assert unban.sender_chat_id == -100987654321


class TestSetChatPermissions:
    """Tests for setChatPermissions method."""

    def test_setchatpermissions_required_fields(self):
        """Test setChatPermissions with required fields."""
        perms = methods.setChatPermissions(
            chat_id=-100123456789,
            permissions=types.ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_polls=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=False
            )
        )
        assert perms.chat_id == -100123456789
        assert perms.permissions.can_send_messages is True
        assert perms.permissions.can_change_info is False


class TestExportChatInviteLink:
    """Tests for exportChatInviteLink method."""

    def test_exportchatinvitelink_required_fields(self):
        """Test exportChatInviteLink with required fields."""
        link = methods.exportChatInviteLink(
            chat_id=-100123456789
        )
        assert link.chat_id == -100123456789


class TestCreateChatInviteLink:
    """Tests for createChatInviteLink method."""

    def test_createchatinvitelink_required_fields(self):
        """Test createChatInviteLink with required fields."""
        link = methods.createChatInviteLink(
            chat_id=-100123456789
        )
        assert link.chat_id == -100123456789

    def test_createchatinvitelink_with_expiration(self):
        """Test createChatInviteLink with expiration and member limit."""
        link = methods.createChatInviteLink(
            chat_id=-100123456789,
            expire_date=1234567890,
            member_limit=100,
            creates_join_request=True
        )
        assert link.expire_date == 1234567890
        assert link.member_limit == 100
        assert link.creates_join_request is True


class TestEditChatInviteLink:
    """Tests for editChatInviteLink method."""

    def test_editchatinvitelink_required_fields(self):
        """Test editChatInviteLink with required fields."""
        link = methods.editChatInviteLink(
            chat_id=-100123456789,
            invite_link="https://t.me/+example"
        )
        assert link.chat_id == -100123456789
        assert link.invite_link == "https://t.me/+example"


class TestRevokeChatInviteLink:
    """Tests for revokeChatInviteLink method."""

    def test_revokechatinvitelink_required_fields(self):
        """Test revokeChatInviteLink with required fields."""
        link = methods.revokeChatInviteLink(
            chat_id=-100123456789,
            invite_link="https://t.me/+example"
        )
        assert link.chat_id == -100123456789
        assert link.invite_link == "https://t.me/+example"


class TestApproveChatJoinRequest:
    """Tests for approveChatJoinRequest method."""

    def test_approvechatjoinrequest_required_fields(self):
        """Test approveChatJoinRequest with required fields."""
        approve = methods.approveChatJoinRequest(
            chat_id=-100123456789,
            user_id=123456
        )
        assert approve.chat_id == -100123456789
        assert approve.user_id == 123456


class TestDeclineChatJoinRequest:
    """Tests for declineChatJoinRequest method."""

    def test_declinechatjoinrequest_required_fields(self):
        """Test declineChatJoinRequest with required fields."""
        decline = methods.declineChatJoinRequest(
            chat_id=-100123456789,
            user_id=123456
        )
        assert decline.chat_id == -100123456789
        assert decline.user_id == 123456


class TestSetChatPhoto:
    """Tests for setChatPhoto method."""

    def test_setchatphoto_required_fields(self):
        """Test setChatPhoto with required fields."""
        photo = methods.setChatPhoto(
            chat_id=-100123456789,
            photo="https://example.com/photo.jpg"
        )
        assert photo.chat_id == -100123456789
        assert photo.photo == "https://example.com/photo.jpg"


class TestDeleteChatPhoto:
    """Tests for deleteChatPhoto method."""

    def test_deletechatphoto_required_fields(self):
        """Test deleteChatPhoto with required fields."""
        delete = methods.deleteChatPhoto(
            chat_id=-100123456789
        )
        assert delete.chat_id == -100123456789


class TestSetChatTitle:
    """Tests for setChatTitle method."""

    def test_setchattitle_required_fields(self):
        """Test setChatTitle with required fields."""
        title = methods.setChatTitle(
            chat_id=-100123456789,
            title="New Chat Title"
        )
        assert title.chat_id == -100123456789
        assert title.title == "New Chat Title"


class TestSetChatDescription:
    """Tests for setChatDescription method."""

    def test_setchatdescription_required_fields(self):
        """Test setChatDescription with required fields."""
        desc = methods.setChatDescription(
            chat_id=-100123456789,
            description="New chat description"
        )
        assert desc.chat_id == -100123456789
        assert desc.description == "New chat description"

    def test_setchatdescription_remove(self):
        """Test setChatDescription with empty description to remove."""
        desc = methods.setChatDescription(
            chat_id=-100123456789,
            description=""
        )
        assert desc.description == ""


class TestPinChatMessage:
    """Tests for pinChatMessage method."""

    def test_pinchatmessage_required_fields(self):
        """Test pinChatMessage with required fields."""
        pin = methods.pinChatMessage(
            chat_id=-100123456789,
            message_id=123,
            disable_notification=False
        )
        assert pin.chat_id == -100123456789
        assert pin.message_id == 123


class TestUnpinChatMessage:
    """Tests for unpinChatMessage method."""

    def test_unpinchatmessage_required_fields(self):
        """Test unpinChatMessage with required fields."""
        unpin = methods.unpinChatMessage(
            chat_id=-100123456789
        )
        assert unpin.chat_id == -100123456789

    def test_unpinchatmessage_with_message_id(self):
        """Test unpinChatMessage with specific message_id."""
        unpin = methods.unpinChatMessage(
            chat_id=-100123456789,
            message_id=123
        )
        assert unpin.message_id == 123


class TestUnpinAllChatMessages:
    """Tests for unpinAllChatMessages method."""

    def test_unpinallchatmessages_required_fields(self):
        """Test unpinAllChatMessages with required fields."""
        unpin = methods.unpinAllChatMessages(
            chat_id=-100123456789
        )
        assert unpin.chat_id == -100123456789


class TestLeaveChat:
    """Tests for leaveChat method."""

    def test_leavechat_required_fields(self):
        """Test leaveChat with required fields."""
        leave = methods.leaveChat(
            chat_id=-100123456789
        )
        assert leave.chat_id == -100123456789


class TestGetChat:
    """Tests for getChat method."""

    def test_getchat_required_fields(self):
        """Test getChat with required fields."""
        chat = methods.getChat(
            chat_id=-100123456789
        )
        assert chat.chat_id == -100123456789


class TestGetChatAdministrators:
    """Tests for getChatAdministrators method."""

    def test_getchatadministrators_required_fields(self):
        """Test getChatAdministrators with required fields."""
        admins = methods.getChatAdministrators(
            chat_id=-100123456789
        )
        assert admins.chat_id == -100123456789


class TestGetChatMemberCount:
    """Tests for getChatMemberCount method."""

    def test_getchatmembercount_required_fields(self):
        """Test getChatMemberCount with required fields."""
        count = methods.getChatMemberCount(
            chat_id=-100123456789
        )
        assert count.chat_id == -100123456789


class TestGetChatMember:
    """Tests for getChatMember method."""

    def test_getchatmember_required_fields(self):
        """Test getChatMember with required fields."""
        member = methods.getChatMember(
            chat_id=-100123456789,
            user_id=123456
        )
        assert member.chat_id == -100123456789
        assert member.user_id == 123456


class TestSetChatStickerSet:
    """Tests for setChatStickerSet method."""

    def test_setchatstickerset_required_fields(self):
        """Test setChatStickerSet with required fields."""
        sticker_set = methods.setChatStickerSet(
            chat_id=-100123456789,
            sticker_set_name="MyStickerSet"
        )
        assert sticker_set.chat_id == -100123456789
        assert sticker_set.sticker_set_name == "MyStickerSet"


class TestDeleteChatStickerSet:
    """Tests for deleteChatStickerSet method."""

    def test_deletechatstickerset_required_fields(self):
        """Test deleteChatStickerSet with required fields."""
        delete = methods.deleteChatStickerSet(
            chat_id=-100123456789
        )
        assert delete.chat_id == -100123456789


class TestGetForumTopicIconStickers:
    """Tests for getForumTopicIconStickers method."""

    def test_getforumtopiciconstickers_creation(self):
        """Test getForumTopicIconStickers creation."""
        stickers = methods.getForumTopicIconStickers()
        assert stickers is not None


class TestCreateForumTopic:
    """Tests for createForumTopic method."""

    def test_createforumtopic_required_fields(self):
        """Test createForumTopic with required fields."""
        topic = methods.createForumTopic(
            chat_id=-100123456789,
            name="New Topic",
            icon_color=0x6FB9F0
        )
        assert topic.chat_id == -100123456789
        assert topic.name == "New Topic"
        assert topic.icon_color == 0x6FB9F0


class TestEditForumTopic:
    """Tests for editForumTopic method."""

    def test_editforumtopic_required_fields(self):
        """Test editForumTopic with required fields."""
        edit = methods.editForumTopic(
            chat_id=-100123456789,
            message_thread_id=123,
            name="Updated Topic Name"
        )
        assert edit.chat_id == -100123456789
        assert edit.message_thread_id == 123


class TestCloseForumTopic:
    """Tests for closeForumTopic method."""

    def test_closeforumtopic_required_fields(self):
        """Test closeForumTopic with required fields."""
        close = methods.closeForumTopic(
            chat_id=-100123456789,
            message_thread_id=123
        )
        assert close.chat_id == -100123456789
        assert close.message_thread_id == 123


class TestReopenForumTopic:
    """Tests for reopenForumTopic method."""

    def test_reopenforumtopic_required_fields(self):
        """Test reopenForumTopic with required fields."""
        reopen = methods.reopenForumTopic(
            chat_id=-100123456789,
            message_thread_id=123
        )
        assert reopen.chat_id == -100123456789
        assert reopen.message_thread_id == 123


class TestDeleteForumTopic:
    """Tests for deleteForumTopic method."""

    def test_deleteforumtopic_required_fields(self):
        """Test deleteForumTopic with required fields."""
        delete = methods.deleteForumTopic(
            chat_id=-100123456789,
            message_thread_id=123
        )
        assert delete.chat_id == -100123456789
        assert delete.message_thread_id == 123


class TestUnpinAllForumTopicMessages:
    """Tests for unpinAllForumTopicMessages method."""

    def test_unpinallforumtopicmessages_required_fields(self):
        """Test unpinAllForumTopicMessages with required fields."""
        unpin = methods.unpinAllForumTopicMessages(
            chat_id=-100123456789,
            message_thread_id=123
        )
        assert unpin.chat_id == -100123456789
        assert unpin.message_thread_id == 123


class TestEditGeneralForumTopic:
    """Tests for editGeneralForumTopic method."""

    def test_editgeneralforumtopic_required_fields(self):
        """Test editGeneralForumTopic with required fields."""
        edit = methods.editGeneralForumTopic(
            chat_id=-100123456789,
            name="General Discussion"
        )
        assert edit.chat_id == -100123456789
        assert edit.name == "General Discussion"


class TestCloseGeneralForumTopic:
    """Tests for closeGeneralForumTopic method."""

    def test_closegeneralforumtopic_required_fields(self):
        """Test closeGeneralForumTopic with required fields."""
        close = methods.closeGeneralForumTopic(
            chat_id=-100123456789
        )
        assert close.chat_id == -100123456789


class TestReopenGeneralForumTopic:
    """Tests for reopenGeneralForumTopic method."""

    def test_reopengeneralforumtopic_required_fields(self):
        """Test reopenGeneralForumTopic with required fields."""
        reopen = methods.reopenGeneralForumTopic(
            chat_id=-100123456789
        )
        assert reopen.chat_id == -100123456789


class TestHideGeneralForumTopic:
    """Tests for hideGeneralForumTopic method."""

    def test_hidegeneralforumtopic_required_fields(self):
        """Test hideGeneralForumTopic with required fields."""
        hide = methods.hideGeneralForumTopic(
            chat_id=-100123456789
        )
        assert hide.chat_id == -100123456789


class TestUnhideGeneralForumTopic:
    """Tests for unhideGeneralForumTopic method."""

    def test_unhidegeneralforumtopic_required_fields(self):
        """Test unhideGeneralForumTopic with required fields."""
        unhide = methods.unhideGeneralForumTopic(
            chat_id=-100123456789
        )
        assert unhide.chat_id == -100123456789


class TestUnpinAllGeneralForumTopicMessages:
    """Tests for unpinAllGeneralForumTopicMessages method."""

    def test_unpinallgeneralforumtopicmessages_required_fields(self):
        """Test unpinAllGeneralForumTopicMessages with required fields."""
        unpin = methods.unpinAllGeneralForumTopicMessages(
            chat_id=-100123456789
        )
        assert unpin.chat_id == -100123456789


class TestAnswerCallbackQuery:
    """Tests for answerCallbackQuery method."""

    def test_answercallbackquery_required_fields(self):
        """Test answerCallbackQuery with required fields."""
        answer = methods.answerCallbackQuery(
            callback_query_id="callback_123"
        )
        assert answer.callback_query_id == "callback_123"

    def test_answercallbackquery_with_text(self):
        """Test answerCallbackQuery with text."""
        answer = methods.answerCallbackQuery(
            callback_query_id="callback_123",
            text="Callback received!",
            show_alert=True
        )
        assert answer.text == "Callback received!"
        assert answer.show_alert is True


class TestGetUserChatBoosts:
    """Tests for getUserChatBoosts method."""

    def test_getuserchatboosts_required_fields(self):
        """Test getUserChatBoosts with required fields."""
        boosts = methods.getUserChatBoosts(
            chat_id=-100123456789,
            user_id=123456
        )
        assert boosts.chat_id == -100123456789
        assert boosts.user_id == 123456


class TestSetMyCommands:
    """Tests for setMyCommands method."""

    def test_setmycommands_required_fields(self):
        """Test setMyCommands with required fields."""
        commands = methods.setMyCommands(
            commands=[
                types.BotCommand(command="start", description="Start the bot"),
                types.BotCommand(command="help", description="Get help")
            ]
        )
        assert len(commands.commands) == 2
        assert commands.commands[0].command == "start"

    def test_setmycommands_with_scope(self):
        """Test setMyCommands with scope and language code."""
        commands = methods.setMyCommands(
            commands=[
                types.BotCommand(command="start", description="Start")
            ],
            scope=types.BotCommandScopeDefault(),
            language_code="en"
        )
        assert commands.scope is not None
        assert commands.language_code == "en"


class TestDeleteMyCommands:
    """Tests for deleteMyCommands method."""

    def test_deletemycommands_required_fields(self):
        """Test deleteMyCommands with no parameters."""
        delete = methods.deleteMyCommands()
        assert delete is not None

    def test_deletemycommands_with_scope(self):
        """Test deleteMyCommands with scope."""
        delete = methods.deleteMyCommands(
            scope=types.BotCommandScopeChat(chat_id=123),
            language_code="en"
        )
        assert delete.scope is not None
        assert delete.language_code == "en"


class TestGetMyCommands:
    """Tests for getMyCommands method."""

    def test_getmycommands_required_fields(self):
        """Test getMyCommands with no parameters."""
        commands = methods.getMyCommands()
        assert commands is not None

    def test_getmycommands_with_scope(self):
        """Test getMyCommands with scope."""
        commands = methods.getMyCommands(
            scope=types.BotCommandScopeDefault(),
            language_code="en"
        )
        assert commands.scope is not None


class TestSetMyName:
    """Tests for setMyName method."""

    def test_setmyname_required_fields(self):
        """Test setMyName with name."""
        name = methods.setMyName(name="My Bot Name")
        assert name.name == "My Bot Name"

    def test_setmyname_with_language_code(self):
        """Test setMyName with language code."""
        name = methods.setMyName(
            name="My Bot",
            language_code="en"
        )
        assert name.language_code == "en"


class TestGetMyName:
    """Tests for getMyName method."""

    def test_getmyname_required_fields(self):
        """Test getMyName with no parameters."""
        name = methods.getMyName()
        assert name is not None

    def test_getmyname_with_language_code(self):
        """Test getMyName with language code."""
        name = methods.getMyName(language_code="en")
        assert name.language_code == "en"


class TestSetMyDescription:
    """Tests for setMyDescription method."""

    def test_setmydescription_required_fields(self):
        """Test setMyDescription with description."""
        desc = methods.setMyDescription(description="Bot description")
        assert desc.description == "Bot description"

    def test_setmydescription_with_language_code(self):
        """Test setMyDescription with language code."""
        desc = methods.setMyDescription(
            description="Bot description",
            language_code="en"
        )
        assert desc.language_code == "en"


class TestGetMyDescription:
    """Tests for getMyDescription method."""

    def test_getmydescription_required_fields(self):
        """Test getMyDescription with no parameters."""
        desc = methods.getMyDescription()
        assert desc is not None

    def test_getmydescription_with_language_code(self):
        """Test getMyDescription with language code."""
        desc = methods.getMyDescription(language_code="en")
        assert desc.language_code == "en"


class TestSetMyShortDescription:
    """Tests for setMyShortDescription method."""

    def test_setmyshortdescription_required_fields(self):
        """Test setMyShortDescription with short_description."""
        desc = methods.setMyShortDescription(short_description="Short desc")
        assert desc.short_description == "Short desc"

    def test_setmyshortdescription_with_language_code(self):
        """Test setMyShortDescription with language code."""
        desc = methods.setMyShortDescription(
            short_description="Short",
            language_code="en"
        )
        assert desc.language_code == "en"


class TestGetMyShortDescription:
    """Tests for getMyShortDescription method."""

    def test_getmyshortdescription_required_fields(self):
        """Test getMyShortDescription with no parameters."""
        desc = methods.getMyShortDescription()
        assert desc is not None

    def test_getmyshortdescription_with_language_code(self):
        """Test getMyShortDescription with language code."""
        desc = methods.getMyShortDescription(language_code="en")
        assert desc.language_code == "en"


class TestSetChatMenuButton:
    """Tests for setChatMenuButton method."""

    def test_setchatmenubutton_required_fields(self):
        """Test setChatMenuButton with no parameters."""
        button = methods.setChatMenuButton()
        assert button is not None

    def test_setchatmenubutton_with_button(self):
        """Test setChatMenuButton with button."""
        button = methods.setChatMenuButton(
            menu_button=types.MenuButtonWebApp(
                type="web_app",
                text="Open App",
                web_app_url="https://example.com"
            )
        )
        assert button.menu_button is not None


class TestGetChatMenuButton:
    """Tests for getChatMenuButton method."""

    def test_getchatmenubutton_required_fields(self):
        """Test getChatMenuButton with no parameters."""
        button = methods.getChatMenuButton()
        assert button is not None

    def test_getchatmenubutton_with_chat_id(self):
        """Test getChatMenuButton with chat_id."""
        button = methods.getChatMenuButton(chat_id=123)
        assert button.chat_id == 123


class TestSetMyDefaultAdministratorRights:
    """Tests for setMyDefaultAdministratorRights method."""

    def test_setmydefaultadministratorrights_required_fields(self):
        """Test setMyDefaultAdministratorRights with no parameters."""
        rights = methods.setMyDefaultAdministratorRights()
        assert rights is not None

    def test_setmydefaultadministratorrights_with_rights(self):
        """Test setMyDefaultAdministratorRights with rights."""
        rights = methods.setMyDefaultAdministratorRights(
            rights=types.ChatAdministratorRights(
                is_anonymous=True,
                can_manage_chat=True,
                can_change_info=True
            ),
            for_channels=True
        )
        assert rights.rights is not None
        assert rights.for_channels is True


class TestGetMyDefaultAdministratorRights:
    """Tests for getMyDefaultAdministratorRights method."""

    def test_getmydefaultadministratorrights_required_fields(self):
        """Test getMyDefaultAdministratorRights with no parameters."""
        rights = methods.getMyDefaultAdministratorRights()
        assert rights is not None

    def test_getmydefaultadministratorrights_with_for_channels(self):
        """Test getMyDefaultAdministratorRights with for_channels."""
        rights = methods.getMyDefaultAdministratorRights(
            for_channels=True
        )
        assert rights.for_channels is True
