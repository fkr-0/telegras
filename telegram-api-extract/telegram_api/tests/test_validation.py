"""Tests for Pydantic validation of telegram_api models."""

import pytest
from pydantic import ValidationError
from telegram_api import types, methods, getting_updates, stickers, payments


class TestTypeValidation:
    """Tests for type model validation."""

    def test_user_required_fields(self):
        """Test that User requires id, is_bot, and first_name."""
        # Valid user
        user = types.User(
            id=123,
            is_bot=False,
            first_name="Test"
        )
        assert user.id == 123

        # Missing required field
        with pytest.raises(ValidationError):
            types.User(
                is_bot=False,
                first_name="Test"
            )

    def test_chat_required_fields(self):
        """Test that Chat requires id and type."""
        # Valid chat
        chat = types.Chat(
            id=-100123456789,
            type="supergroup"
        )
        assert chat.type == "supergroup"

        # Missing required field
        with pytest.raises(ValidationError):
            types.Chat(
                id=-100123456789
            )

    def test_message_required_fields(self):
        """Test that Message requires message_id, date, and chat."""
        # Valid message
        message = types.Message(
            message_id=1,
            date=1234567890,
            chat=types.Chat(id=123, type="private")
        )
        assert message.message_id == 1

        # Missing required field
        with pytest.raises(ValidationError):
            types.Message(
                message_id=1,
                date=1234567890
            )

    def test_photo_size_validation(self):
        """Test PhotoSize field validation."""
        # Valid photo size
        photo = types.PhotoSize(
            file_id="photo_123",
            file_unique_id="unique_photo_123",
            width=800,
            height=600
        )
        assert photo.width == 800

    def test_message_entity_validation(self):
        """Test MessageEntity field validation."""
        # Valid message entity
        entity = types.MessageEntity(
            type="bold",
            offset=0,
            length=10
        )
        assert entity.type == "bold"

        # Negative offset should work (it's allowed)
        entity_negative = types.MessageEntity(
            type="bold",
            offset=-1,
            length=10
        )
        assert entity_negative.offset == -1


class TestMethodValidation:
    """Tests for method model validation."""

    def test_send_message_required_fields(self):
        """Test that sendMessage requires chat_id and text."""
        # Valid message
        msg = methods.sendMessage(
            chat_id=123,
            text="Hello"
        )
        assert msg.text == "Hello"

        # Missing required field
        with pytest.raises(ValidationError):
            methods.sendMessage(
                chat_id=123
            )

    def test_send_photo_required_fields(self):
        """Test that sendPhoto requires chat_id and photo."""
        # Valid photo
        photo = methods.sendPhoto(
            chat_id=123,
            photo="https://example.com/photo.jpg"
        )
        assert photo.photo == "https://example.com/photo.jpg"

        # Missing required field
        with pytest.raises(ValidationError):
            methods.sendPhoto(
                chat_id=123
            )

    def test_send_poll_required_fields(self):
        """Test that sendPoll requires chat_id, question, and options."""
        # Valid poll
        poll = methods.sendPoll(
            chat_id=123,
            question="What is your favorite color?",
            options=["Red", "Blue", "Green"]
        )
        assert len(poll.options) == 3

        # Missing required field
        with pytest.raises(ValidationError):
            methods.sendPoll(
                chat_id=123,
                question="Question"
            )

    def test_edit_message_text_required_fields(self):
        """Test that editMessageText requires appropriate identifier and text."""
        # Valid with chat_id and message_id
        edit1 = methods.editMessageText(
            chat_id=123,
            message_id=456,
            text="Updated"
        )
        assert edit1.text == "Updated"

        # Valid with inline_message_id
        edit2 = methods.editMessageText(
            inline_message_id="inline_123",
            text="Updated"
        )
        assert edit2.inline_message_id == "inline_123"

        # Missing both chat_id/message_id and inline_message_id
        with pytest.raises(ValidationError):
            methods.editMessageText(
                text="Updated"
            )

    def test_inline_keyboard_button_validation(self):
        """Test InlineKeyboardButton validation."""
        # Valid button with callback_data
        button1 = types.InlineKeyboardButton(
            text="Button",
            callback_data="data"
        )
        assert button1.callback_data == "data"

        # Valid button with url
        button2 = types.InlineKeyboardButton(
            text="Button",
            url="https://example.com"
        )
        assert button2.url == "https://example.com"

    def test_reply_keyboard_markup_validation(self):
        """Test ReplyKeyboardMarkup validation."""
        # Valid keyboard
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="Button 1"), types.KeyboardButton(text="Button 2")],
                [types.KeyboardButton(text="Button 3")]
            ]
        )
        assert len(keyboard.keyboard) == 2

    def test_keyboard_button_validation(self):
        """Test KeyboardButton validation."""
        # Valid button
        button = types.KeyboardButton(
            text="Button"
        )
        assert button.text == "Button"

        # Button with request_contact
        button_contact = types.KeyboardButton(
            text="Share Contact",
            request_contact=True
        )
        assert button_contact.request_contact is True

        # Button with request_location
        button_location = types.KeyboardButton(
            text="Share Location",
            request_location=True
        )
        assert button_location.request_location is True


class TestUpdateValidation:
    """Tests for Update model validation."""

    def test_update_requires_update_id(self):
        """Test that Update requires update_id."""
        # Valid update
        update = getting_updates.Update(update_id=123)
        assert update.update_id == 123

        # Missing required field
        with pytest.raises(ValidationError):
            getting_updates.Update()

    def test_update_with_message(self):
        """Test Update with message field."""
        update = getting_updates.Update(
            update_id=123,
            message=types.Message(
                message_id=1,
                date=1234567890,
                chat=types.Chat(id=123, type="private")
            )
        )
        assert update.message is not None

    def test_webhook_info_validation(self):
        """Test WebhookInfo validation."""
        # Valid webhook info
        webhook = getting_updates.WebhookInfo(
            url="https://example.com/webhook",
            has_custom_certificate=False,
            pending_update_count=0
        )
        assert webhook.url == "https://example.com/webhook"


class TestStickerValidation:
    """Tests for sticker model validation."""

    def test_sticker_required_fields(self):
        """Test that Sticker requires all required fields."""
        # Valid sticker
        sticker = stickers.Sticker(
            file_id="sticker_123",
            file_unique_id="unique_sticker_123",
            type="regular",
            width=512,
            height=512,
            is_animated=False,
            is_video=False
        )
        assert sticker.file_id == "sticker_123"

        # Missing required field
        with pytest.raises(ValidationError):
            stickers.Sticker(
                file_id="sticker_123",
                file_unique_id="unique_sticker_123",
                type="regular"
            )

    def test_input_sticker_required_fields(self):
        """Test that InputSticker requires sticker and emoji_list."""
        # Valid input sticker
        input_sticker = stickers.InputSticker(
            sticker="https://example.com/sticker.png",
            emoji_list=["😀", "😃"]
        )
        assert len(input_sticker.emoji_list) == 2

        # Missing required field
        with pytest.raises(ValidationError):
            stickers.InputSticker(
                sticker="https://example.com/sticker.png"
            )


class TestPaymentValidation:
    """Tests for payment model validation."""

    def test_labeled_price_required_fields(self):
        """Test that LabeledPrice requires label and amount."""
        # Valid price
        price = payments.LabeledPrice(
            label="Product",
            amount=1000
        )
        assert price.amount == 1000

        # Missing required field
        with pytest.raises(ValidationError):
            payments.LabeledPrice(
                label="Product"
            )

    def test_invoice_required_fields(self):
        """Test that Invoice requires all required fields."""
        # Valid invoice
        invoice = payments.Invoice(
            title="Product",
            description="Product description",
            start_parameter="start_param",
            currency="USD",
            total_amount=1000
        )
        assert invoice.currency == "USD"

        # Missing required field
        with pytest.raises(ValidationError):
            payments.Invoice(
                title="Product",
                description="Product description"
            )

    def test_successful_payment_required_fields(self):
        """Test that SuccessfulPayment requires all required fields."""
        # Valid payment
        payment = payments.SuccessfulPayment(
            currency="USD",
            total_amount=1000,
            invoice_payload="payload",
            telegram_payment_charge_id="charge_123",
            provider_payment_charge_id="provider_charge_123"
        )
        assert payment.currency == "USD"

        # Missing required field
        with pytest.raises(ValidationError):
            payments.SuccessfulPayment(
                currency="USD",
                total_amount=1000
            )

    def test_shipping_address_required_fields(self):
        """Test that ShippingAddress requires all required fields."""
        # Valid address
        address = payments.ShippingAddress(
            country_code="US",
            state="CA",
            city="San Francisco",
            street_line1="123 Main St",
            post_code="94102"
        )
        assert address.country_code == "US"

        # Missing required field
        with pytest.raises(ValidationError):
            payments.ShippingAddress(
                country_code="US",
                state="CA"
            )


class TestGameValidation:
    """Tests for game model validation."""

    def test_game_required_fields(self):
        """Test that Game requires title, description, and photo."""
        # Valid game
        game = payments.Game(
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
        assert game.title == "Test Game"

        # Missing required field
        with pytest.raises(ValidationError):
            payments.Game(
                title="Test Game"
            )

    def test_game_high_score_required_fields(self):
        """Test that GameHighScore requires all required fields."""
        # Valid high score
        high_score = payments.GameHighScore(
            position=1,
            user=types.User(id=123, is_bot=False, first_name="Player"),
            score=100
        )
        assert high_score.position == 1

        # Missing required field
        with pytest.raises(ValidationError):
            payments.GameHighScore(
                position=1,
                user=types.User(id=123, is_bot=False, first_name="Player")
            )


class TestInputMediaValidation:
    """Tests for InputMedia model validation."""

    def test_input_media_photo_required_fields(self):
        """Test that InputMediaPhoto requires media."""
        # Valid photo
        photo = types.InputMediaPhoto(
            media="https://example.com/photo.jpg"
        )
        assert photo.media == "https://example.com/photo.jpg"

        # Missing required field
        with pytest.raises(ValidationError):
            types.InputMediaPhoto(
                caption="Photo"
            )

    def test_input_media_video_required_fields(self):
        """Test that InputMediaVideo requires media."""
        # Valid video
        video = types.InputMediaVideo(
            media="https://example.com/video.mp4"
        )
        assert video.media == "https://example.com/video.mp4"

    def test_input_media_document_required_fields(self):
        """Test that InputMediaDocument requires media."""
        # Valid document
        document = types.InputMediaDocument(
            media="https://example.com/document.pdf"
        )
        assert document.media == "https://example.com/document.pdf"


class TestTypeCoercion:
    """Tests for type coercion in models."""

    def test_chat_id_string_to_int(self):
        """Test that string chat_id is accepted."""
        # String chat_id should work
        msg = methods.sendMessage(
            chat_id=123,
            text="Test"
        )
        # The type is int | str, so both should work
        msg_string = methods.sendMessage(
            chat_id="@channel",
            text="Test"
        )
        assert msg_string.chat_id == "@channel"

    def test_boolean_field_validation(self):
        """Test boolean field validation."""
        # True/False should work
        msg1 = methods.sendMessage(
            chat_id=123,
            text="Test",
            disable_notification=True
        )
        assert msg1.disable_notification is True

        msg2 = methods.sendMessage(
            chat_id=123,
            text="Test",
            disable_notification=False
        )
        assert msg2.disable_notification is False

    def test_integer_field_validation(self):
        """Test integer field validation."""
        # Integer should work
        msg = methods.sendMessage(
            chat_id=123,
            text="Test",
            message_thread_id=5
        )
        assert msg.message_thread_id == 5


class TestValidationErrors:
    """Tests for validation error messages."""

    def test_missing_required_field_error(self):
        """Test that missing required field produces helpful error."""
        with pytest.raises(ValidationError) as exc_info:
            types.User(
                is_bot=False,
                first_name="Test"
            )

        errors = exc_info.value.errors()
        assert any(error["loc"][0] == "id" for error in errors)

    def test_wrong_type_error(self):
        """Test that wrong type produces helpful error."""
        with pytest.raises(ValidationError) as exc_info:
            types.User(
                id="not_an_int",
                is_bot=False,
                first_name="Test"
            )

        errors = exc_info.value.errors()
        assert any("int" in str(error.get("msg", "")).lower() for error in errors)
