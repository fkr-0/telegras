"""Comprehensive tests for telegram_api.types module."""

import pytest
import json
from pydantic import ValidationError
from telegram_api import types


class TestUser:
    """Tests for User model."""

    def test_user_creation_required_fields(self):
        """Test creating a User with only required fields."""
        user = types.User(
            id=123456789,
            is_bot=False,
            first_name="Test"
        )
        assert user.id == 123456789
        assert user.is_bot is False
        assert user.first_name == "Test"

    def test_user_with_all_fields(self, sample_user):
        """Test creating a User with all optional fields."""
        assert sample_user.username == "test_user"
        assert sample_user.last_name is None
        assert sample_user.language_code is None

    def test_user_with_large_id(self):
        """Test User with very large ID."""
        user = types.User(
            id=999999999999,
            is_bot=True,
            first_name="LargeIDBot"
        )
        assert user.id == 999999999999

    def test_user_with_unicode_name(self):
        """Test User with Unicode characters in name."""
        user = types.User(
            id=123,
            is_bot=False,
            first_name="日本語",
            last_name="Ñoño"
        )
        assert user.first_name == "日本語"
        assert user.last_name == "Ñoño"


class TestChat:
    """Tests for Chat model."""

    def test_private_chat(self, sample_private_chat):
        """Test creating a private chat."""
        assert sample_private_chat.id == 123456789
        assert sample_private_chat.type == "private"

    def test_group_chat(self):
        """Test creating a group chat."""
        chat = types.Chat(
            id=-123456789,
            type="group",
            title="Test Group"
        )
        assert chat.type == "group"
        assert chat.title == "Test Group"

    def test_supergroup_chat(self, sample_chat):
        """Test creating a supergroup chat."""
        assert sample_chat.type == "supergroup"
        assert sample_chat.title == "Test Group"

    def test_channel_chat(self):
        """Test creating a channel."""
        chat = types.Chat(
            id=-100123456789,
            type="channel",
            title="Test Channel"
        )
        assert chat.type == "channel"
        assert chat.title == "Test Channel"


class TestMessage:
    """Tests for Message model."""

    def test_text_message(self, sample_message):
        """Test creating a text message."""
        assert sample_message.message_id == 1
        assert sample_message.text == "Hello, World!"
        assert sample_message.chat.id == 123

    def test_message_without_text(self):
        """Test creating a message without text (e.g., photo message)."""
        message = types.Message(
            message_id=2,
            date=1234567890,
            chat=types.Chat(id=123, type="private"),
            photo=[
                types.PhotoSize(
                    file_id="photo_123",
                    file_unique_id="unique_photo_123",
                    width=100,
                    height=100
                )
            ]
        )
        assert message.text is None
        assert message.photo is not None
        assert len(message.photo) == 1

    def test_message_with_entities(self):
        """Test creating a message with message entities."""
        message = types.Message(
            message_id=3,
            date=1234567890,
            chat=types.Chat(id=123, type="private"),
            text="Bold text",
            entities=[
                types.MessageEntity(
                    type="bold",
                    offset=0,
                    length=9
                )
            ]
        )
        assert message.entities is not None
        assert message.entities[0].type == "bold"

    def test_message_with_reply_to_message(self):
        """Test creating a message with a reply to another message."""
        original = types.Message(
            message_id=1,
            date=1234567890,
            chat=types.Chat(id=123, type="private"),
            text="Original message"
        )
        reply = types.Message(
            message_id=2,
            date=1234567891,
            chat=types.Chat(id=123, type="private"),
            text="Reply",
            reply_to_message=original
        )
        assert reply.reply_to_message is not None
        assert reply.reply_to_message.message_id == 1


class TestCallbackQuery:
    """Tests for CallbackQuery model."""

    def test_callback_query_creation(self, sample_callback_query):
        """Test creating a callback query."""
        assert sample_callback_query.id == "callback123"
        assert sample_callback_query.data == "callback_data"
        assert sample_callback_query.message.message_id == 1

    def test_callback_query_without_message(self):
        """Test creating a callback query with inline message (no regular message)."""
        callback = types.CallbackQuery(
            id="callback456",
            from_=types.User(id=123, is_bot=False, first_name="User"),
            inline_message_id="inline_msg_123",
            data="callback_data"
        )
        assert callback.inline_message_id == "inline_msg_123"
        assert callback.message is None


class TestInlineQuery:
    """Tests for InlineQuery model."""

    def test_inline_query_creation(self, sample_inline_query):
        """Test creating an inline query."""
        assert sample_inline_query.id == "inline_query_123"
        assert sample_inline_query.query == "test query"
        assert sample_inline_query.offset == "0"

    def test_inline_query_with_location(self):
        """Test creating an inline query with user location."""
        inline_query = types.InlineQuery(
            id="inline_query_456",
            from_=types.User(id=123, is_bot=False, first_name="User"),
            query="weather",
            offset="0",
            location=types.Location(
                latitude=37.7749,
                longitude=-122.4194
            )
        )
        assert inline_query.location is not None
        assert inline_query.location.latitude == 37.7749


class TestPoll:
    """Tests for Poll model."""

    def test_poll_creation(self):
        """Test creating a poll."""
        poll = types.Poll(
            id="poll_123",
            question="What is your favorite color?",
            options=[
                types.PollOption(text="Red", voter_count=5),
                types.PollOption(text="Blue", voter_count=10),
                types.PollOption(text="Green", voter_count=3)
            ],
            total_voter_count=18,
            is_closed=False,
            type="regular"
        )
        assert poll.question == "What is your favorite color?"
        assert len(poll.options) == 3
        assert poll.options[1].text == "Blue"
        assert poll.options[1].voter_count == 10


class TestBotCommand:
    """Tests for BotCommand model."""

    def test_bot_command_creation(self):
        """Test creating a bot command."""
        command = types.BotCommand(
            command="start",
            description="Start the bot"
        )
        assert command.command == "start"
        assert command.description == "Start the bot"

    def test_bot_command_with_special_characters(self):
        """Test bot command with various characters."""
        command = types.BotCommand(
            command="help",
            description="Get help & support"
        )
        assert command.description == "Get help & support"


class TestInputMedia:
    """Tests for InputMedia models."""

    def test_input_media_photo(self):
        """Test creating InputMediaPhoto."""
        media = types.InputMediaPhoto(
            media="https://example.com/photo.jpg",
            caption="Photo caption"
        )
        assert media.type == "photo"
        assert media.media == "https://example.com/photo.jpg"
        assert media.caption == "Photo caption"

    def test_input_media_video(self):
        """Test creating InputMediaVideo."""
        media = types.InputMediaVideo(
            media="https://example.com/video.mp4",
            caption="Video caption",
            width=1920,
            height=1080,
            duration=60
        )
        assert media.type == "video"
        assert media.width == 1920
        assert media.duration == 60


class TestAnimation:
    """Tests for Animation model."""

    def test_animation_creation(self):
        """Test creating an Animation."""
        animation = types.Animation(
            file_id="anim_123",
            file_unique_id="unique_anim_123",
            width=640,
            height=480,
            duration=10
        )
        assert animation.file_id == "anim_123"
        assert animation.width == 640
        assert animation.duration == 10


class TestAudio:
    """Tests for Audio model."""

    def test_audio_creation(self):
        """Test creating an Audio."""
        audio = types.Audio(
            file_id="audio_123",
            file_unique_id="unique_audio_123",
            duration=180
        )
        assert audio.file_id == "audio_123"
        assert audio.duration == 180

    def test_audio_with_metadata(self):
        """Test creating an Audio with full metadata."""
        audio = types.Audio(
            file_id="audio_456",
            file_unique_id="unique_audio_456",
            duration=240,
            performer="Artist Name",
            title="Song Title",
            file_name="song.mp3",
            mime_type="audio/mpeg",
            file_size=5000000
        )
        assert audio.performer == "Artist Name"
        assert audio.title == "Song Title"
        assert audio.file_size == 5000000


class TestDocument:
    """Tests for Document model."""

    def test_document_creation(self):
        """Test creating a Document."""
        document = types.Document(
            file_id="doc_123",
            file_unique_id="unique_doc_123"
        )
        assert document.file_id == "doc_123"

    def test_document_with_thumbnail(self):
        """Test creating a Document with thumbnail."""
        document = types.Document(
            file_id="doc_456",
            file_unique_id="unique_doc_456",
            file_name="document.pdf",
            mime_type="application/pdf",
            file_size=1024000,
            thumbnail=types.PhotoSize(
                file_id="thumb_123",
                file_unique_id="unique_thumb_123",
                width=100,
                height=100
            )
        )
        assert document.file_name == "document.pdf"
        assert document.thumbnail is not None
        assert document.thumbnail.width == 100


class TestPhotoSize:
    """Tests for PhotoSize model."""

    def test_photo_size_creation(self):
        """Test creating a PhotoSize."""
        photo = types.PhotoSize(
            file_id="photo_123",
            file_unique_id="unique_photo_123",
            width=800,
            height=600
        )
        assert photo.file_id == "photo_123"
        assert photo.width == 800
        assert photo.height == 600

    def test_photo_size_with_file_size(self):
        """Test PhotoSize with file size."""
        photo = types.PhotoSize(
            file_id="photo_456",
            file_unique_id="unique_photo_456",
            width=1920,
            height=1080,
            file_size=1024000
        )
        assert photo.file_size == 1024000


class TestSticker:
    """Tests for Sticker model."""

    def test_sticker_creation(self, sample_sticker):
        """Test creating a Sticker."""
        assert sample_sticker.file_id == "sticker_123"
        assert sample_sticker.width == 512
        assert sample_sticker.is_animated is False

    def test_animated_sticker(self):
        """Test creating an animated sticker."""
        sticker = types.Sticker(
            file_id="anim_sticker_123",
            file_unique_id="unique_anim_sticker_123",
            type="regular",
            width=512,
            height=512,
            is_animated=True,
            is_video=False
        )
        assert sticker.is_animated is True


class TestVideo:
    """Tests for Video model."""

    def test_video_creation(self):
        """Test creating a Video."""
        video = types.Video(
            file_id="video_123",
            file_unique_id="unique_video_123",
            width=1920,
            height=1080,
            duration=120
        )
        assert video.file_id == "video_123"
        assert video.width == 1920
        assert video.duration == 120

    def test_video_with_thumbnail(self):
        """Test creating a Video with thumbnail."""
        video = types.Video(
            file_id="video_456",
            file_unique_id="unique_video_456",
            width=1280,
            height=720,
            duration=60,
            thumbnail=types.PhotoSize(
                file_id="thumb_123",
                file_unique_id="unique_thumb_123",
                width=320,
                height=180
            )
        )
        assert video.thumbnail is not None
        assert video.thumbnail.width == 320


class TestVoice:
    """Tests for Voice model."""

    def test_voice_creation(self):
        """Test creating a Voice."""
        voice = types.Voice(
            file_id="voice_123",
            file_unique_id="unique_voice_123",
            duration=30
        )
        assert voice.file_id == "voice_123"
        assert voice.duration == 30

    def test_voice_with_file_size(self):
        """Test creating a Voice with file size."""
        voice = types.Voice(
            file_id="voice_456",
            file_unique_id="unique_voice_456",
            duration=45,
            mime_type="audio/ogg",
            file_size=500000
        )
        assert voice.mime_type == "audio/ogg"
        assert voice.file_size == 500000


class TestVenue:
    """Tests for Venue model."""

    def test_venue_creation(self):
        """Test creating a Venue."""
        venue = types.Venue(
            location=types.Location(
                latitude=37.7749,
                longitude=-122.4194
            ),
            title="Golden Gate Park",
            address="San Francisco, CA"
        )
        assert venue.title == "Golden Gate Park"
        assert venue.location.latitude == 37.7749

    def test_venue_with_foursquare(self):
        """Test creating a Venue with Foursquare data."""
        venue = types.Venue(
            location=types.Location(latitude=40.7589, longitude=-73.9851),
            title="Times Square",
            address="Manhattan, NY 10036",
            foursquare_id="4b0f9624f964a5205a3326e3",
            foursquare_type="arts_entertainment/default"
        )
        assert venue.foursquare_id == "4b0f9624f964a5205a3326e3"


class TestLocation:
    """Tests for Location model."""

    def test_location_creation(self):
        """Test creating a Location."""
        location = types.Location(
            latitude=51.5074,
            longitude=-0.1278
        )
        assert abs(location.latitude - 51.5074) < 0.0001
        assert abs(location.longitude - (-0.1278)) < 0.0001


class TestContact:
    """Tests for Contact model."""

    def test_contact_creation(self):
        """Test creating a Contact."""
        contact = types.Contact(
            phone_number="+1234567890",
            first_name="John",
            user_id=123456789
        )
        assert contact.phone_number == "+1234567890"
        assert contact.first_name == "John"
        assert contact.user_id == 123456789


class TestLoginUrl:
    """Tests for LoginUrl model."""

    def test_login_url_creation(self):
        """Test creating a LoginUrl."""
        login_url = types.LoginUrl(
            url="https://example.com/auth"
        )
        assert login_url.url == "https://example.com/auth"

    def test_login_url_with_all_options(self):
        """Test creating a LoginUrl with all optional fields."""
        login_url = types.LoginUrl(
            url="https://example.com/auth",
            forward_text="Continue",
            bot_username="example_bot",
            request_write_access=True
        )
        assert login_url.forward_text == "Continue"
        assert login_url.request_write_access is True


class TestProximityAlertTriggered:
    """Tests for ProximityAlertTriggered model."""

    def test_proximity_alert_creation(self):
        """Test creating a ProximityAlertTriggered."""
        alert = types.ProximityAlertTriggered(
            traveler=types.User(id=1, is_bot=False, first_name="Traveler"),
            watcher=types.User(id=2, is_bot=False, first_name="Watcher"),
            distance=50
        )
        assert alert.traveler.id == 1
        assert alert.watcher.id == 2
        assert alert.distance == 50


class TestChatAdministratorRights:
    """Tests for ChatAdministratorRights model."""

    def test_admin_rights_creation(self):
        """Test creating ChatAdministratorRights."""
        rights = types.ChatAdministratorRights(
            is_anonymous=False,
            can_manage_chat=True,
            can_change_info=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_delete_messages=True
        )
        assert rights.is_anonymous is False
        assert rights.can_manage_chat is True

    def test_all_admin_rights(self):
        """Test creating ChatAdministratorRights with all rights."""
        rights = types.ChatAdministratorRights(
            is_anonymous=True,
            can_manage_chat=True,
            can_change_info=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_manage_topics=True,
            can_promote_members=True,
            can_manage_video_chats=True,
            can_manage_gifts=True
        )
        assert rights.can_invite_users is True
        assert rights.can_restrict_members is True


class TestChatMember:
    """Tests for ChatMember model."""

    def test_chat_member_creator(self):
        """Test creating ChatMember with creator status."""
        member = types.ChatMember(
            status="creator",
            user=types.User(id=1, is_bot=False, first_name="Creator"),
            is_anonymous=False
        )
        assert member.status == "creator"
        assert member.user.id == 1

    def test_chat_member_administrator(self):
        """Test creating ChatMember with administrator status."""
        member = types.ChatMember(
            status="administrator",
            user=types.User(id=2, is_bot=False, first_name="Admin"),
            can_be_edited=False,
            is_anonymous=False,
            can_manage_chat=True,
            can_change_info=True,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=False,
            can_manage_video_chats=True
        )
        assert member.status == "administrator"
        assert member.can_manage_chat is True

    def test_chat_member_member(self):
        """Test creating ChatMember with member status."""
        member = types.ChatMember(
            status="member",
            user=types.User(id=3, is_bot=False, first_name="Member")
        )
        assert member.status == "member"
        assert member.user.first_name == "Member"


class TestGame:
    """Tests for Game model."""

    def test_game_creation(self, sample_game):
        """Test creating a Game."""
        assert sample_game.title == "Test Game"
        assert sample_game.description == "A test game"
        assert len(sample_game.photo) == 1

    def test_game_with_all_fields(self):
        """Test creating a Game with all optional fields."""
        game = types.Game(
            title="Complete Game",
            description="A complete game example",
            photo=[
                types.PhotoSize(
                    file_id="photo_123",
                    file_unique_id="unique_photo_123",
                    width=100,
                    height=100
                )
            ],
            text="Game text",
            text_entities=[
                types.MessageEntity(type="bold", offset=0, length=4)
            ],
            animation=types.Animation(
                file_id="anim_123",
                file_unique_id="unique_anim_123",
                width=200,
                height=200,
                duration=5
            )
        )
        assert game.text == "Game text"
        assert game.animation is not None


class TestInvoice:
    """Tests for Invoice model."""

    def test_invoice_creation(self):
        """Test creating an Invoice."""
        invoice = types.Invoice(
            title="Product",
            description="Product description",
            start_parameter="start_param",
            currency="USD",
            total_amount=1000
        )
        assert invoice.title == "Product"
        assert invoice.currency == "USD"
        assert invoice.total_amount == 1000


class TestSuccessfulPayment:
    """Tests for SuccessfulPayment model."""

    def test_successful_payment_creation(self, sample_successful_payment):
        """Test creating a SuccessfulPayment."""
        assert sample_successful_payment.currency == "USD"
        assert sample_successful_payment.total_amount == 1000
        assert sample_successful_payment.invoice_payload == "invoice_payload"


class TestPassportData:
    """Tests for PassportData model."""

    def test_passport_data_creation(self):
        """Test creating PassportData."""
        passport_data = types.PassportData(
            data=[
                types.EncryptedPassportElement(
                    type="personal_details",
                    data="encrypted_data",
                    hash="element_hash"
                )
            ],
            credentials=types.EncryptedCredentials(
                data="encrypted_credentials",
                hash="credentials_hash",
                secret="secret"
            )
        )
        assert len(passport_data.data) == 1
        assert passport_data.data[0].type == "personal_details"


class TestWebhookInfo:
    """Tests for WebhookInfo model (from getting_updates module)."""

    def test_webhook_info_basic(self):
        """Test creating a basic WebhookInfo."""
        webhook = types.WebhookInfo(
            url="https://example.com/webhook",
            has_custom_certificate=False,
            pending_update_count=0
        )
        assert webhook.url == "https://example.com/webhook"
        assert webhook.pending_update_count == 0

    def test_webhook_info_with_all_fields(self):
        """Test creating WebhookInfo with all fields."""
        webhook = types.WebhookInfo(
            url="https://example.com/webhook",
            has_custom_certificate=True,
            pending_update_count=5,
            last_error_date=1234567890,
            last_error_message="Connection timeout",
            max_connections=40,
            allowed_updates=["message", "callback_query"]
        )
        assert webhook.has_custom_certificate is True
        assert webhook.pending_update_count == 5
        assert "message" in webhook.allowed_updates
