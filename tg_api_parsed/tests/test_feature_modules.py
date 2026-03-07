"""Comprehensive tests for telegram_api feature modules."""

import pytest
import json
from pydantic import ValidationError
from telegram_api import types, stickers, payments, games, inline_mode, passport, updating_messages


# ============== STICKERS MODULE TESTS ==============

class TestStickerSet:
    """Tests for StickerSet model (stickers module)."""

    def test_sticker_set_creation(self):
        """Test creating a StickerSet."""
        sticker_set = stickers.StickerSet(
            name="MyStickerSet",
            title="My Sticker Set",
            sticker_type="regular",
            is_animated=False,
            is_video=False,
            stickers=[
                stickers.Sticker(
                    file_id="sticker_1",
                    file_unique_id="unique_1",
                    type="regular",
                    width=512,
                    height=512,
                    is_animated=False,
                    is_video=False
                )
            ]
        )
        assert sticker_set.name == "MyStickerSet"
        assert sticker_set.title == "My Sticker Set"
        assert len(sticker_set.stickers) == 1


class TestSticker:
    """Tests for Sticker model (stickers module)."""

    def test_sticker_creation(self):
        """Test creating a Sticker."""
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
        assert sticker.width == 512

    def test_sticker_with_thumbnail(self):
        """Test creating a Sticker with thumbnail."""
        sticker = stickers.Sticker(
            file_id="sticker_456",
            file_unique_id="unique_sticker_456",
            type="regular",
            width=512,
            height=512,
            is_animated=False,
            is_video=False,
            thumbnail=types.PhotoSize(
                file_id="thumb_123",
                file_unique_id="unique_thumb_123",
                width=100,
                height=100
            )
        )
        assert sticker.thumbnail is not None
        assert sticker.thumbnail.width == 100


class TestInputSticker:
    """Tests for InputSticker model."""

    def test_input_sticker_creation(self):
        """Test creating an InputSticker."""
        input_sticker = stickers.InputSticker(
            sticker="https://example.com/sticker.png",
            emoji_list=["😀", "😃"]
        )
        assert input_sticker.sticker == "https://example.com/sticker.png"
        assert input_sticker.emoji_list == ["😀", "😃"]

    def test_input_sticker_with_keywords(self):
        """Test creating an InputSticker with keywords."""
        input_sticker = stickers.InputSticker(
            sticker="https://example.com/sticker.png",
            emoji_list=["😀"],
            keywords=["happy", "smile"]
        )
        assert input_sticker.keywords == ["happy", "smile"]


# ============== PAYMENTS MODULE TESTS ==============

class TestLabeledPrice:
    """Tests for LabeledPrice model."""

    def test_labeled_price_creation(self):
        """Test creating a LabeledPrice."""
        price = payments.LabeledPrice(
            label="Product",
            amount=1000
        )
        assert price.label == "Product"
        assert price.amount == 1000


class TestInvoice:
    """Tests for Invoice model."""

    def test_invoice_creation(self):
        """Test creating an Invoice."""
        invoice = payments.Invoice(
            title="Product",
            description="Product description",
            start_parameter="start_param",
            currency="USD",
            total_amount=1000
        )
        assert invoice.title == "Product"
        assert invoice.currency == "USD"
        assert invoice.total_amount == 1000


class TestShippingAddress:
    """Tests for ShippingAddress model."""

    def test_shipping_address_creation(self):
        """Test creating a ShippingAddress."""
        address = payments.ShippingAddress(
            country_code="US",
            state="CA",
            city="San Francisco",
            street_line1="123 Main St",
            post_code="94102"
        )
        assert address.country_code == "US"
        assert address.city == "San Francisco"

    def test_shipping_address_with_line2(self):
        """Test creating a ShippingAddress with street_line2."""
        address = payments.ShippingAddress(
            country_code="US",
            state="NY",
            city="New York",
            street_line1="123 Main St",
            street_line2="Apt 4B",
            post_code="10001"
        )
        assert address.street_line2 == "Apt 4B"


class TestShippingOption:
    """Tests for ShippingOption model."""

    def test_shipping_option_creation(self):
        """Test creating a ShippingOption."""
        option = payments.ShippingOption(
            id="shipping_1",
            title="Standard Shipping",
            prices=[
                payments.LabeledPrice(label="Shipping", amount=500)
            ]
        )
        assert option.id == "shipping_1"
        assert option.title == "Standard Shipping"
        assert len(option.prices) == 1


class TestSuccessfulPayment:
    """Tests for SuccessfulPayment model."""

    def test_successful_payment_creation(self):
        """Test creating a SuccessfulPayment."""
        payment = payments.SuccessfulPayment(
            currency="USD",
            total_amount=1000,
            invoice_payload="invoice_payload",
            telegram_payment_charge_id="tg_charge_123",
            provider_payment_charge_id="provider_charge_123"
        )
        assert payment.currency == "USD"
        assert payment.total_amount == 1000

    def test_successful_payment_with_optional_fields(self):
        """Test creating a SuccessfulPayment with optional fields."""
        payment = payments.SuccessfulPayment(
            currency="EUR",
            total_amount=2000,
            invoice_payload="payload",
            telegram_payment_charge_id="tg_charge_456",
            provider_payment_charge_id="provider_charge_456",
            shipping_option_id="shipping_1",
            order_info=payments.OrderInfo(
                name="John Doe",
                phone_number="+1234567890",
                email="john@example.com"
            )
        )
        assert payment.currency == "EUR"
        assert payment.shipping_option_id == "shipping_1"
        assert payment.order_info is not None


class TestRefundedPayment:
    """Tests for RefundedPayment model."""

    def test_refunded_payment_creation(self):
        """Test creating a RefundedPayment."""
        refund = payments.RefundedPayment(
            currency="USD",
            total_amount=1000,
            invoice_payload="payload",
            telegram_payment_charge_id="charge_123"
        )
        assert refund.currency == "USD"
        assert refund.total_amount == 1000


class TestOrderInfo:
    """Tests for OrderInfo model."""

    def test_order_info_creation(self):
        """Test creating an OrderInfo."""
        order_info = payments.OrderInfo(
            name="John Doe",
            phone_number="+1234567890",
            email="john@example.com"
        )
        assert order_info.name == "John Doe"
        assert order_info.email == "john@example.com"

    def test_order_info_with_shipping(self):
        """Test creating an OrderInfo with shipping address."""
        order_info = payments.OrderInfo(
            name="Jane Doe",
            phone_number="+0987654321",
            email="jane@example.com",
            shipping_address=payments.ShippingAddress(
                country_code="UK",
                state="London",
                city="London",
                street_line1="456 High St",
                post_code="SW1A 1AA"
            )
        )
        assert order_info.shipping_address is not None
        assert order_info.shipping_address.city == "London"


# ============== GAMES MODULE TESTS ==============

class TestGame:
    """Tests for Game model."""

    def test_game_creation(self):
        """Test creating a Game."""
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
        assert game.title == "Test Game"
        assert game.description == "A test game"
        assert len(game.photo) == 1

    def test_game_with_animation(self):
        """Test creating a Game with animation."""
        game = games.Game(
            title="Animated Game",
            description="Game with animation",
            photo=[
                types.PhotoSize(
                    file_id="photo_1",
                    file_unique_id="unique_photo_1",
                    width=100,
                    height=100
                )
            ],
            animation=types.Animation(
                file_id="anim_1",
                file_unique_id="unique_anim_1",
                width=200,
                height=200,
                duration=10
            )
        )
        assert game.animation is not None
        assert game.animation.file_id == "anim_1"


class TestCallbackGame:
    """Tests for CallbackGame model."""

    def test_callback_game_creation(self):
        """Test creating a CallbackGame."""
        callback_game = games.CallbackGame()
        assert callback_game is not None


class TestGameHighScore:
    """Tests for GameHighScore model."""

    def test_game_high_score_creation(self):
        """Test creating a GameHighScore."""
        high_score = games.GameHighScore(
            position=1,
            user=types.User(id=123, is_bot=False, first_name="Player"),
            score=100
        )
        assert high_score.position == 1
        assert high_score.score == 100
        assert high_score.user.first_name == "Player"


# ============== INLINE MODE MODULE TESTS ==============

class TestInlineQuery:
    """Tests for InlineQuery model."""

    def test_inline_query_creation(self):
        """Test creating an InlineQuery."""
        inline_query = inline_mode.InlineQuery(
            id="inline_query_123",
            from_=types.User(id=123, is_bot=False, first_name="User"),
            query="test query",
            offset="0"
        )
        assert inline_query.id == "inline_query_123"
        assert inline_query.query == "test query"

    def test_inline_query_with_location(self):
        """Test creating an InlineQuery with user location."""
        inline_query = inline_mode.InlineQuery(
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


class TestChosenInlineResult:
    """Tests for ChosenInlineResult model."""

    def test_chosen_inline_result_creation(self):
        """Test creating a ChosenInlineResult."""
        chosen_result = inline_mode.ChosenInlineResult(
            result_id="result_123",
            from_=types.User(id=123, is_bot=False, first_name="User"),
            query="test query"
        )
        assert chosen_result.result_id == "result_123"

    def test_chosen_inline_result_with_location(self):
        """Test creating a ChosenInlineResult with location."""
        chosen_result = inline_mode.ChosenInlineResult(
            result_id="result_456",
            from_=types.User(id=123, is_bot=False, first_name="User"),
            query="location query",
            location=types.Location(
                latitude=40.7128,
                longitude=-74.0060
            )
        )
        assert chosen_result.location is not None


class TestInlineQueryResults:
    """Tests for InlineQuery result models."""

    def test_inline_query_result_article(self):
        """Test creating an InlineQueryResultArticle."""
        result = inline_mode.InlineQueryResultArticle(
            id="article_1",
            title="Test Article",
            input_message_content=inline_mode.InputTextMessageContent(
                message_text="Article content"
            )
        )
        assert result.type == "article"
        assert result.title == "Test Article"

    def test_inline_query_result_photo(self):
        """Test creating an InlineQueryResultPhoto."""
        result = inline_mode.InlineQueryResultPhoto(
            id="photo_1",
            photo_url="https://example.com/photo.jpg",
            thumbnail_url="https://example.com/thumb.jpg"
        )
        assert result.type == "photo"
        assert result.photo_url == "https://example.com/photo.jpg"

    def test_inline_query_result_video(self):
        """Test creating an InlineQueryResultVideo."""
        result = inline_mode.InlineQueryResultVideo(
            id="video_1",
            video_url="https://example.com/video.mp4",
            thumbnail_url="https://example.com/thumb.jpg",
            title="Test Video"
        )
        assert result.type == "video"
        assert result.title == "Test Video"

    def test_inline_query_result_audio(self):
        """Test creating an InlineQueryResultAudio."""
        result = inline_mode.InlineQueryResultAudio(
            id="audio_1",
            audio_url="https://example.com/audio.mp3",
            title="Test Audio"
        )
        assert result.type == "audio"
        assert result.title == "Test Audio"

    def test_inline_query_result_voice(self):
        """Test creating an InlineQueryResultVoice."""
        result = inline_mode.InlineQueryResultVoice(
            id="voice_1",
            voice_url="https://example.com/voice.ogg",
            title="Test Voice"
        )
        assert result.type == "voice"
        assert result.title == "Test Voice"

    def test_inline_query_result_document(self):
        """Test creating an InlineQueryResultDocument."""
        result = inline_mode.InlineQueryResultDocument(
            id="document_1",
            title="Test Document",
            document_url="https://example.com/document.pdf",
            mime_type="application/pdf"
        )
        assert result.type == "document"
        assert result.mime_type == "application/pdf"

    def test_inline_query_result_location(self):
        """Test creating an InlineQueryResultLocation."""
        result = inline_mode.InlineQueryResultLocation(
            id="location_1",
            title="Test Location",
            latitude=37.7749,
            longitude=-122.4194
        )
        assert result.type == "location"
        assert result.latitude == 37.7749

    def test_inline_query_result_venue(self):
        """Test creating an InlineQueryResultVenue."""
        result = inline_mode.InlineQueryResultVenue(
            id="venue_1",
            title="Test Venue",
            latitude=37.7749,
            longitude=-122.4194,
            address="123 Test St"
        )
        assert result.type == "venue"
        assert result.address == "123 Test St"

    def test_inline_query_result_contact(self):
        """Test creating an InlineQueryResultContact."""
        result = inline_mode.InlineQueryResultContact(
            id="contact_1",
            phone_number="+1234567890",
            first_name="John"
        )
        assert result.type == "contact"
        assert result.phone_number == "+1234567890"

    def test_inline_query_result_game(self):
        """Test creating an InlineQueryResultGame."""
        result = inline_mode.InlineQueryResultGame(
            id="game_1",
            game_short_name="test_game"
        )
        assert result.type == "game"
        assert result.game_short_name == "test_game"


class TestInputMessageContent:
    """Tests for InputMessageContent models."""

    def test_input_text_message_content(self):
        """Test creating an InputTextMessageContent."""
        content = inline_mode.InputTextMessageContent(
            message_text="Test message"
        )
        assert content.message_text == "Test message"

    def test_input_text_message_content_with_parse_mode(self):
        """Test creating an InputTextMessageContent with parse_mode."""
        content = inline_mode.InputTextMessageContent(
            message_text="*Bold* text",
            parse_mode="Markdown"
        )
        assert content.parse_mode == "Markdown"

    def test_input_location_message_content(self):
        """Test creating an InputLocationMessageContent."""
        content = inline_mode.InputLocationMessageContent(
            latitude=37.7749,
            longitude=-122.4194
        )
        assert abs(content.latitude - 37.7749) < 0.0001

    def test_input_venue_message_content(self):
        """Test creating an InputVenueMessageContent."""
        content = inline_mode.InputVenueMessageContent(
            latitude=37.7749,
            longitude=-122.4194,
            title="Test Venue",
            address="123 Test St"
        )
        assert content.title == "Test Venue"

    def test_input_contact_message_content(self):
        """Test creating an InputContactMessageContent."""
        content = inline_mode.InputContactMessageContent(
            phone_number="+1234567890",
            first_name="John"
        )
        assert content.phone_number == "+1234567890"

    def test_input_invoice_message_content(self):
        """Test creating an InputInvoiceMessageContent."""
        content = inline_mode.InputInvoiceMessageContent(
            title="Product",
            description="Product description",
            payload="payload",
            currency="USD",
            prices=[
                payments.LabeledPrice(label="Product", amount=1000)
            ]
        )
        assert content.title == "Product"
        assert content.currency == "USD"


# ============== PASSPORT MODULE TESTS ==============

class TestPassportData:
    """Tests for PassportData model."""

    def test_passport_data_creation(self):
        """Test creating PassportData."""
        passport_data = passport.PassportData(
            data=[
                passport.EncryptedPassportElement(
                    type="personal_details",
                    data="encrypted_data",
                    hash="element_hash"
                )
            ],
            credentials=passport.EncryptedCredentials(
                data="credentials_data",
                hash="credentials_hash",
                secret="secret"
            )
        )
        assert len(passport_data.data) == 1
        assert passport_data.credentials.hash == "credentials_hash"


class TestEncryptedPassportElement:
    """Tests for EncryptedPassportElement model."""

    def test_encrypted_passport_element_creation(self):
        """Test creating an EncryptedPassportElement."""
        element = passport.EncryptedPassportElement(
            type="personal_details",
            data="encrypted_data",
            hash="element_hash"
        )
        assert element.type == "personal_details"

    def test_encrypted_passport_element_with_files(self):
        """Test creating an EncryptedPassportElement with files."""
        element = passport.EncryptedPassportElement(
            type="utility_bill",
            files=[
                passport.PassportFile(
                    file_id="file_1",
                    file_unique_id="unique_file_1",
                    file_size=1024,
                    file_date=1234567890
                )
            ],
            hash="element_hash"
        )
        assert element.type == "utility_bill"
        assert len(element.files) == 1


class TestPassportFile:
    """Tests for PassportFile model."""

    def test_passport_file_creation(self):
        """Test creating a PassportFile."""
        passport_file = passport.PassportFile(
            file_id="file_1",
            file_unique_id="unique_file_1",
            file_size=1024,
            file_date=1234567890
        )
        assert passport_file.file_id == "file_1"
        assert passport_file.file_size == 1024


class TestEncryptedCredentials:
    """Tests for EncryptedCredentials model."""

    def test_encrypted_credentials_creation(self):
        """Test creating EncryptedCredentials."""
        credentials = passport.EncryptedCredentials(
            data="encrypted_data",
            hash="data_hash",
            secret="secret"
        )
        assert credentials.data == "encrypted_data"
        assert credentials.hash == "data_hash"


class TestPassportElementError:
    """Tests for PassportElementError models."""

    def test_passport_element_error_data_field(self):
        """Test creating a PassportElementErrorDataField."""
        error = passport.PassportElementErrorDataField(
            type="personal_details",
            field_name="first_name",
            data_hash="hash",
            message="Invalid field"
        )
        assert error.type == "data_field"
        assert error.field_name == "first_name"

    def test_passport_element_error_front_side(self):
        """Test creating a PassportElementErrorFrontSide."""
        error = passport.PassportElementErrorFrontSide(
            type="passport",
            file_hash="file_hash",
            message="Invalid front side"
        )
        assert error.type == "front_side"

    def test_passport_element_error_reverse_side(self):
        """Test creating a PassportElementErrorReverseSide."""
        error = passport.PassportElementErrorReverseSide(
            type="driver_license",
            file_hash="file_hash",
            message="Invalid reverse side"
        )
        assert error.type == "reverse_side"

    def test_passport_element_error_selfie(self):
        """Test creating a PassportElementErrorSelfie."""
        error = passport.PassportElementErrorSelfie(
            type="identity_card",
            file_hash="file_hash",
            message="Invalid selfie"
        )
        assert error.type == "selfie"

    def test_passport_element_error_file(self):
        """Test creating a PassportElementErrorFile."""
        error = passport.PassportElementErrorFile(
            type="utility_bill",
            file_hash="file_hash",
            message="Invalid file"
        )
        assert error.type == "file"

    def test_passport_element_error_files(self):
        """Test creating a PassportElementErrorFiles."""
        error = passport.PassportElementErrorFiles(
            type="bank_statement",
            file_hashes=["hash1", "hash2"],
            message="Invalid files"
        )
        assert error.type == "files"
        assert len(error.file_hashes) == 2

    def test_passport_element_error_translation_file(self):
        """Test creating a PassportElementErrorTranslationFile."""
        error = passport.PassportElementErrorTranslationFile(
            type="passport",
            file_hash="file_hash",
            message="Invalid translation"
        )
        assert error.type == "translation_file"

    def test_passport_element_error_translation_files(self):
        """Test creating a PassportElementErrorTranslationFiles."""
        error = passport.PassportElementErrorTranslationFiles(
            type="driver_license",
            file_hashes=["hash1", "hash2"],
            message="Invalid translations"
        )
        assert error.type == "translation_files"

    def test_passport_element_error_unspecified(self):
        """Test creating a PassportElementErrorUnspecified."""
        error = passport.PassportElementErrorUnspecified(
            type="passport",
            element_hash="element_hash",
            message="Unspecified error"
        )
        assert error.type == "unspecified"


# ============== UPDATING MESSAGES MODULE TESTS ==============

class TestEditMessageText:
    """Tests for editMessageText method."""

    def test_edit_message_text_with_chat_id(self):
        """Test editMessageText with chat_id."""
        edit = updating_messages.editMessageText(
            chat_id=123,
            message_id=456,
            text="Updated text"
        )
        assert edit.chat_id == 123
        assert edit.message_id == 456
        assert edit.text == "Updated text"

    def test_edit_message_text_with_inline_message_id(self):
        """Test editMessageText with inline_message_id."""
        edit = updating_messages.editMessageText(
            inline_message_id="inline_msg_123",
            text="Updated inline text"
        )
        assert edit.inline_message_id == "inline_msg_123"
        assert edit.text == "Updated inline text"

    def test_edit_message_text_with_parse_mode(self):
        """Test editMessageText with parse_mode."""
        edit = updating_messages.editMessageText(
            chat_id=123,
            message_id=456,
            text="*Bold* text",
            parse_mode="Markdown"
        )
        assert edit.parse_mode == "Markdown"


class TestEditMessageCaption:
    """Tests for editMessageCaption method."""

    def test_edit_message_caption_with_chat_id(self):
        """Test editMessageCaption with chat_id."""
        edit = updating_messages.editMessageCaption(
            chat_id=123,
            message_id=456,
            caption="New caption"
        )
        assert edit.chat_id == 123
        assert edit.caption == "New caption"

    def test_edit_message_caption_with_inline_message_id(self):
        """Test editMessageCaption with inline_message_id."""
        edit = updating_messages.editMessageCaption(
            inline_message_id="inline_msg_123",
            caption="New inline caption"
        )
        assert edit.inline_message_id == "inline_msg_123"


class TestEditMessageMedia:
    """Tests for editMessageMedia method."""

    def test_edit_message_media_with_chat_id(self):
        """Test editMessageMedia with chat_id."""
        edit = updating_messages.editMessageMedia(
            chat_id=123,
            message_id=456,
            media=types.InputMediaPhoto(
                media="https://example.com/new_photo.jpg"
            )
        )
        assert edit.chat_id == 123
        assert edit.media.type == "photo"

    def test_edit_message_media_with_inline_message_id(self):
        """Test editMessageMedia with inline_message_id."""
        edit = updating_messages.editMessageMedia(
            inline_message_id="inline_msg_123",
            media=types.InputMediaVideo(
                media="https://example.com/new_video.mp4"
            )
        )
        assert edit.inline_message_id == "inline_msg_123"
        assert edit.media.type == "video"


class TestEditMessageReplyMarkup:
    """Tests for editMessageReplyMarkup method."""

    def test_edit_message_reply_markup_with_chat_id(self):
        """Test editMessageReplyMarkup with chat_id."""
        edit = updating_messages.editMessageReplyMarkup(
            chat_id=123,
            message_id=456,
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton(text="Button", callback_data="data")]
                ]
            )
        )
        assert edit.chat_id == 123
        assert edit.reply_markup is not None

    def test_edit_message_reply_markup_with_inline_message_id(self):
        """Test editMessageReplyMarkup with inline_message_id."""
        edit = updating_messages.editMessageReplyMarkup(
            inline_message_id="inline_msg_123",
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton(text="Button", url="https://example.com")]
                ]
            )
        )
        assert edit.inline_message_id == "inline_msg_123"


class TestStopPoll:
    """Tests for stopPoll method."""

    def test_stop_poll_creation(self):
        """Test creating stopPoll."""
        stop = updating_messages.stopPoll(
            chat_id=123,
            message_id=456
        )
        assert stop.chat_id == 123
        assert stop.message_id == 456

    def test_stop_poll_with_reply_markup(self):
        """Test creating stopPoll with reply_markup."""
        stop = updating_messages.stopPoll(
            chat_id=123,
            message_id=456,
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton(text="Button", callback_data="data")]
                ]
            )
        )
        assert stop.reply_markup is not None


class TestDeleteMessage:
    """Tests for deleteMessage method."""

    def test_delete_message_creation(self):
        """Test creating deleteMessage."""
        delete = updating_messages.deleteMessage(
            chat_id=123,
            message_id=456
        )
        assert delete.chat_id == 123
        assert delete.message_id == 456


class TestDeleteMessages:
    """Tests for deleteMessages method."""

    def test_delete_messages_creation(self):
        """Test creating deleteMessages."""
        delete = updating_messages.deleteMessages(
            chat_id=123,
            message_ids=[1, 2, 3, 4, 5]
        )
        assert delete.chat_id == 123
        assert delete.message_ids == [1, 2, 3, 4, 5]


class TestCopyMessage:
    """Tests for copyMessage method."""

    def test_copy_message_required_fields(self):
        """Test copyMessage with required fields."""
        copy = updating_messages.copyMessage(
            chat_id=123,
            from_chat_id=456,
            message_id=789
        )
        assert copy.chat_id == 123
        assert copy.from_chat_id == 456
        assert copy.message_id == 789

    def test_copy_message_with_caption(self):
        """Test copyMessage with caption."""
        copy = updating_messages.copyMessage(
            chat_id=123,
            from_chat_id=456,
            message_id=789,
            caption="New caption"
        )
        assert copy.caption == "New caption"


class TestSendDice:
    """Tests for sendDice method."""

    def test_send_dice_default(self):
        """Test sendDice with default emoji."""
        dice = updating_messages.sendDice(
            chat_id=123
        )
        assert dice.chat_id == 123

    def test_send_dice_with_custom_emoji(self):
        """Test sendDice with custom emoji."""
        dice = updating_messages.sendDice(
            chat_id=123,
            emoji="🎯"
        )
        assert dice.emoji == "🎯"


class TestSendChatAction:
    """Tests for sendChatAction method."""

    def test_send_chat_action_typing(self):
        """Test sendChatAction with typing action."""
        action = updating_messages.sendChatAction(
            chat_id=123,
            action="typing"
        )
        assert action.action == "typing"

    def test_send_chat_action_upload_photo(self):
        """Test sendChatAction with upload_photo action."""
        action = updating_messages.sendChatAction(
            chat_id=123,
            action="upload_photo"
        )
        assert action.action == "upload_photo"

    def test_send_chat_action_record_video(self):
        """Test sendChatAction with record_video action."""
        action = updating_messages.sendChatAction(
            chat_id=123,
            action="record_video"
        )
        assert action.action == "record_video"

    def test_send_chat_action_record_voice(self):
        """Test sendChatAction with record_voice action."""
        action = updating_messages.sendChatAction(
            chat_id=123,
            action="record_voice"
        )
        assert action.action == "record_voice"

    def test_send_chat_action_upload_document(self):
        """Test sendChatAction with upload_document action."""
        action = updating_messages.sendChatAction(
            chat_id=123,
            action="upload_document"
        )
        assert action.action == "upload_document"

    def test_send_chat_action_choose_sticker(self):
        """Test sendChatAction with choose_sticker action."""
        action = updating_messages.sendChatAction(
            chat_id=123,
            action="choose_sticker"
        )
        assert action.action == "choose_sticker"

    def test_send_chat_action_find_location(self):
        """Test sendChatAction with find_location action."""
        action = updating_messages.sendChatAction(
            chat_id=123,
            action="find_location"
        )
        assert action.action == "find_location"

    def test_send_chat_action_record_video_note(self):
        """Test sendChatAction with record_video_note action."""
        action = updating_messages.sendChatAction(
            chat_id=123,
            action="record_video_note"
        )
        assert action.action == "record_video_note"
