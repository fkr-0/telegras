"""Tests for JSON serialization and deserialization of telegram_api models."""

import pytest
import json
from telegram_api import types, methods, getting_updates, stickers, payments, games


class TestTypeSerialization:
    """Tests for type model serialization."""

    def test_user_serialization(self, sample_user):
        """Test User model JSON serialization."""
        json_str = sample_user.model_dump_json()
        data = json.loads(json_str)

        assert data["id"] == 123456789
        assert data["is_bot"] is False
        assert data["first_name"] == "Test"
        assert data["username"] == "test_user"
        assert data["last_name"] is None

    def test_user_deserialization(self):
        """Test User model JSON deserialization."""
        json_data = {
            "id": 123456789,
            "is_bot": False,
            "first_name": "Test",
            "username": "test_user",
            "last_name": None,
            "language_code": None,
            "is_premium": None,
            "added_to_attachment_menu": None,
            "can_join_groups": None,
            "can_read_all_group_messages": None,
            "supports_inline_queries": None
        }

        user = types.User(**json_data)
        assert user.id == 123456789
        assert user.first_name == "Test"
        assert user.username == "test_user"

    def test_chat_serialization(self, sample_chat):
        """Test Chat model JSON serialization."""
        json_str = sample_chat.model_dump_json()
        data = json.loads(json_str)

        assert data["id"] == -100123456789
        assert data["type"] == "supergroup"
        assert data["title"] == "Test Group"

    def test_message_serialization(self, sample_message):
        """Test Message model JSON serialization."""
        json_str = sample_message.model_dump_json()
        data = json.loads(json_str)

        assert data["message_id"] == 1
        assert data["text"] == "Hello, World!"
        assert data["chat"]["id"] == 123

    def test_callback_query_serialization(self, sample_callback_query):
        """Test CallbackQuery model JSON serialization."""
        json_str = sample_callback_query.model_dump_json()
        data = json.loads(json_str)

        assert data["id"] == "callback123"
        assert data["data"] == "callback_data"

    def test_photo_size_serialization(self):
        """Test PhotoSize model JSON serialization."""
        photo = types.PhotoSize(
            file_id="photo_123",
            file_unique_id="unique_photo_123",
            width=800,
            height=600,
            file_size=102400
        )

        json_str = photo.model_dump_json()
        data = json.loads(json_str)

        assert data["file_id"] == "photo_123"
        assert data["width"] == 800
        assert data["file_size"] == 102400

    def test_message_entity_serialization(self):
        """Test MessageEntity model JSON serialization."""
        entity = types.MessageEntity(
            type="bold",
            offset=0,
            length=9,
            url="https://example.com"
        )

        json_str = entity.model_dump_json()
        data = json.loads(json_str)

        assert data["type"] == "bold"
        assert data["offset"] == 0
        assert data["length"] == 9


class TestMethodSerialization:
    """Tests for method model serialization."""

    def test_send_message_serialization(self):
        """Test sendMessage method JSON serialization."""
        msg = methods.sendMessage(
            chat_id=123,
            text="Hello, World!",
            parse_mode="Markdown",
            disable_notification=True
        )

        json_str = msg.model_dump_json()
        data = json.loads(json_str)

        assert data["chat_id"] == 123
        assert data["text"] == "Hello, World!"
        assert data["parse_mode"] == "Markdown"
        assert data["disable_notification"] is True

    def test_send_message_with_reply_markup_serialization(self):
        """Test sendMessage with InlineKeyboardMarkup serialization."""
        msg = methods.sendMessage(
            chat_id=123,
            text="Choose:",
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        types.InlineKeyboardButton(text="Option 1", callback_data="opt1"),
                        types.InlineKeyboardButton(text="Option 2", callback_data="opt2")
                    ],
                    [types.InlineKeyboardButton(text="Option 3", callback_data="opt3")]
                ]
            )
        )

        json_str = msg.model_dump_json()
        data = json.loads(json_str)

        assert data["reply_markup"]["inline_keyboard"][0][0]["text"] == "Option 1"
        assert data["reply_markup"]["inline_keyboard"][0][1]["callback_data"] == "opt2"
        assert data["reply_markup"]["inline_keyboard"][1][0]["text"] == "Option 3"

    def test_send_photo_serialization(self):
        """Test sendPhoto method JSON serialization."""
        photo = methods.sendPhoto(
            chat_id=123,
            photo="https://example.com/photo.jpg",
            caption="Photo caption"
        )

        json_str = photo.model_dump_json()
        data = json.loads(json_str)

        assert data["chat_id"] == 123
        assert data["photo"] == "https://example.com/photo.jpg"
        assert data["caption"] == "Photo caption"

    def test_send_poll_serialization(self):
        """Test sendPoll method JSON serialization."""
        poll = methods.sendPoll(
            chat_id=123,
            question="What is your favorite color?",
            options=["Red", "Blue", "Green"],
            is_anonymous=False
        )

        json_str = poll.model_dump_json()
        data = json.loads(json_str)

        assert data["question"] == "What is your favorite color?"
        assert data["options"] == ["Red", "Blue", "Green"]
        assert data["is_anonymous"] is False

    def test_edit_message_text_serialization(self):
        """Test editMessageText method JSON serialization."""
        edit = methods.editMessageText(
            chat_id=123,
            message_id=456,
            text="Updated text",
            parse_mode="HTML"
        )

        json_str = edit.model_dump_json()
        data = json.loads(json_str)

        assert data["chat_id"] == 123
        assert data["message_id"] == 456
        assert data["text"] == "Updated text"


class TestUpdateSerialization:
    """Tests for Update model serialization."""

    def test_update_serialization(self, sample_update):
        """Test Update model JSON serialization."""
        json_str = sample_update.model_dump_json()
        data = json.loads(json_str)

        assert data["update_id"] == 12345
        assert "message" in data
        assert data["message"]["text"] == "Test message"

    def test_webhook_info_serialization(self):
        """Test WebhookInfo model JSON serialization."""
        webhook = getting_updates.WebhookInfo(
            url="https://example.com/webhook",
            has_custom_certificate=True,
            pending_update_count=5,
            max_connections=40,
            allowed_updates=["message", "callback_query"]
        )

        json_str = webhook.model_dump_json()
        data = json.loads(json_str)

        assert data["url"] == "https://example.com/webhook"
        assert data["has_custom_certificate"] is True
        assert data["pending_update_count"] == 5
        assert "message" in data["allowed_updates"]


class TestStickerSerialization:
    """Tests for sticker model serialization."""

    def test_sticker_serialization(self):
        """Test Sticker model JSON serialization."""
        sticker = stickers.Sticker(
            file_id="sticker_123",
            file_unique_id="unique_sticker_123",
            type="regular",
            width=512,
            height=512,
            is_animated=False,
            is_video=False
        )

        json_str = sticker.model_dump_json()
        data = json.loads(json_str)

        assert data["file_id"] == "sticker_123"
        assert data["width"] == 512
        assert data["is_animated"] is False


class TestPaymentSerialization:
    """Tests for payment model serialization."""

    def test_labeled_price_serialization(self):
        """Test LabeledPrice model JSON serialization."""
        price = payments.LabeledPrice(
            label="Product",
            amount=1000
        )

        json_str = price.model_dump_json()
        data = json.loads(json_str)

        assert data["label"] == "Product"
        assert data["amount"] == 1000

    def test_invoice_serialization(self):
        """Test Invoice model JSON serialization."""
        invoice = payments.Invoice(
            title="Product",
            description="Product description",
            start_parameter="start_param",
            currency="USD",
            total_amount=1000
        )

        json_str = invoice.model_dump_json()
        data = json.loads(json_str)

        assert data["title"] == "Product"
        assert data["currency"] == "USD"
        assert data["total_amount"] == 1000

    def test_successful_payment_serialization(self):
        """Test SuccessfulPayment model JSON serialization."""
        payment = payments.SuccessfulPayment(
            currency="USD",
            total_amount=1000,
            invoice_payload="payload",
            telegram_payment_charge_id="charge_123",
            provider_payment_charge_id="provider_charge_123"
        )

        json_str = payment.model_dump_json()
        data = json.loads(json_str)

        assert data["currency"] == "USD"
        assert data["telegram_payment_charge_id"] == "charge_123"


class TestGameSerialization:
    """Tests for game model serialization."""

    def test_game_serialization(self):
        """Test Game model JSON serialization."""
        game = games.Game(
            title="Test Game",
            description="A test game",
            photo=[
                types.PhotoSize(
                    file_id="photo_1",
                    file_unique_id="unique_photo_1",
                    width=100,
                    height=100
                )
            ]
        )

        json_str = game.model_dump_json()
        data = json.loads(json_str)

        assert data["title"] == "Test Game"
        assert data["description"] == "A test game"
        assert len(data["photo"]) == 1

    def test_game_high_score_serialization(self):
        """Test GameHighScore model JSON serialization."""
        high_score = games.GameHighScore(
            position=1,
            user=types.User(id=123, is_bot=False, first_name="Player"),
            score=100
        )

        json_str = high_score.model_dump_json()
        data = json.loads(json_str)

        assert data["position"] == 1
        assert data["score"] == 100


class TestRoundTripSerialization:
    """Tests for serialization-deserialization round trips."""

    def test_user_round_trip(self):
        """Test User serialization and deserialization round trip."""
        original = types.User(
            id=123,
            is_bot=True,
            first_name="TestBot",
            username="bot",
            language_code="en"
        )

        json_str = original.model_dump_json()
        data = json.loads(json_str)
        restored = types.User(**data)

        assert restored.id == original.id
        assert restored.is_bot == original.is_bot
        assert restored.first_name == original.first_name
        assert restored.username == original.username
        assert restored.language_code == original.language_code

    def test_message_round_trip(self):
        """Test Message serialization and deserialization round trip."""
        original = types.Message(
            message_id=123,
            date=1234567890,
            chat=types.Chat(id=456, type="private"),
            text="Hello",
            from_=types.User(id=789, is_bot=False, first_name="User")
        )

        json_str = original.model_dump_json()
        data = json.loads(json_str)
        restored = types.Message(**data)

        assert restored.message_id == original.message_id
        assert restored.text == original.text
        assert restored.from_.id == original.from_.id

    def test_inline_keyboard_round_trip(self):
        """Test InlineKeyboardMarkup serialization and deserialization round trip."""
        original = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(text="Button 1", callback_data="data1"),
                    types.InlineKeyboardButton(text="Button 2", url="https://example.com")
                ],
                [types.InlineKeyboardButton(text="Button 3", callback_data="data3")]
            ]
        )

        json_str = original.model_dump_json()
        data = json.loads(json_str)
        restored = types.InlineKeyboardMarkup(**data)

        assert len(restored.inline_keyboard) == 2
        assert len(restored.inline_keyboard[0]) == 2
        assert restored.inline_keyboard[0][0].text == "Button 1"
        assert restored.inline_keyboard[1][0].callback_data == "data3"

    def test_send_message_round_trip(self):
        """Test sendMessage method serialization round trip."""
        original = methods.sendMessage(
            chat_id=123,
            text="Hello",
            parse_mode="Markdown",
            disable_web_page_preview=True
        )

        json_str = original.model_dump_json()
        data = json.loads(json_str)
        restored = methods.sendMessage(**data)

        assert restored.chat_id == original.chat_id
        assert restored.text == original.text
        assert restored.parse_mode == original.parse_mode
        assert restored.disable_web_page_preview == original.disable_web_page_preview


class TestSpecialValuesSerialization:
    """Tests for serialization of special values."""

    def test_large_id_serialization(self):
        """Test serialization of very large IDs."""
        user = types.User(
            id=999999999999,
            is_bot=False,
            first_name="LargeID"
        )

        json_str = user.model_dump_json()
        data = json.loads(json_str)

        assert data["id"] == 999999999999

    def test_unicode_serialization(self):
        """Test serialization of Unicode characters."""
        user = types.User(
            id=123,
            is_bot=False,
            first_name="日本語",
            last_name="Ñoño"
        )

        json_str = user.model_dump_json()
        data = json.loads(json_str)

        assert data["first_name"] == "日本語"
        assert data["last_name"] == "Ñoño"

    def test_special_characters_in_text(self):
        """Test serialization of special characters in text."""
        msg = methods.sendMessage(
            chat_id=123,
            text="Hello \"World\"!\nNew line\tTab"
        )

        json_str = msg.model_dump_json()
        data = json.loads(json_str)

        assert data["text"] == "Hello \"World\"!\nNew line\tTab"

    def test_null_values_serialization(self):
        """Test that None values are properly serialized."""
        user = types.User(
            id=123,
            is_bot=False,
            first_name="Test",
            last_name=None,
            username=None,
            language_code=None
        )

        json_str = user.model_dump_json()
        data = json.loads(json_str)

        assert data["last_name"] is None
        assert data["username"] is None
        assert data["language_code"] is None

    def test_empty_list_serialization(self):
        """Test serialization of empty lists."""
        msg = methods.sendMessage(
            chat_id=123,
            text="Test",
            entities=[]
        )

        json_str = msg.model_dump_json()
        data = json.loads(json_str)

        assert data["entities"] == []

    def test_nested_objects_serialization(self):
        """Test serialization of nested objects."""
        message = types.Message(
            message_id=1,
            date=1234567890,
            chat=types.Chat(id=123, type="private"),
            reply_to_message=types.Message(
                message_id=2,
                date=1234567889,
                chat=types.Chat(id=123, type="private"),
                from_=types.User(id=456, is_bot=False, first_name="User")
            )
        )

        json_str = message.model_dump_json()
        data = json.loads(json_str)

        assert data["reply_to_message"]["message_id"] == 2
        assert data["reply_to_message"]["from_"]["first_name"] == "User"
