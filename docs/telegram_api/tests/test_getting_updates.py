"""Comprehensive tests for telegram_api.getting_updates module."""

import pytest
import json
from pydantic import ValidationError
from telegram_api import types, getting_updates


class TestUpdate:
    """Tests for Update model."""

    def test_update_with_message(self, sample_update):
        """Test creating an Update with a message."""
        assert sample_update.update_id == 12345
        assert sample_update.message is not None
        assert sample_update.message.text == "Test message"

    def test_update_with_callback_query(self):
        """Test creating an Update with a callback query."""
        update = getting_updates.Update(
            update_id=12346,
            callback_query=types.CallbackQuery(
                id="callback123",
                from_=types.User(id=1, is_bot=False, first_name="User"),
                data="callback_data"
            )
        )
        assert update.callback_query is not None
        assert update.callback_query.id == "callback123"

    def test_update_with_inline_query(self):
        """Test creating an Update with an inline query."""
        update = getting_updates.Update(
            update_id=12347,
            inline_query=types.InlineQuery(
                id="inline123",
                from_=types.User(id=1, is_bot=False, first_name="User"),
                query="test query",
                offset="0"
            )
        )
        assert update.inline_query is not None
        assert update.inline_query.query == "test query"

    def test_update_with_chosen_inline_result(self):
        """Test creating an Update with a chosen inline result."""
        update = getting_updates.Update(
            update_id=12348,
            chosen_inline_result=types.ChosenInlineResult(
                result_id="result123",
                from_=types.User(id=1, is_bot=False, first_name="User"),
                query="test query"
            )
        )
        assert update.chosen_inline_result is not None

    def test_update_with_shipping_query(self):
        """Test creating an Update with a shipping query."""
        update = getting_updates.Update(
            update_id=12349,
            shipping_query=types.ShippingQuery(
                id="shipping123",
                from_=types.User(id=1, is_bot=False, first_name="User"),
                shipping_address=types.ShippingAddress(
                    country_code="US",
                    state="CA",
                    city="San Francisco",
                    street_line1="123 Main St",
                    post_code="94102"
                )
            )
        )
        assert update.shipping_query is not None
        assert update.shipping_query.id == "shipping123"

    def test_update_with_pre_checkout_query(self):
        """Test creating an Update with a pre-checkout query."""
        update = getting_updates.Update(
            update_id=12350,
            pre_checkout_query=types.PreCheckoutQuery(
                id="precheckout123",
                from_=types.User(id=1, is_bot=False, first_name="User"),
                currency="USD",
                total_amount=1000,
                invoice_payload="payload"
            )
        )
        assert update.pre_checkout_query is not None

    def test_update_with_poll(self):
        """Test creating an Update with a poll."""
        update = getting_updates.Update(
            update_id=12351,
            poll=types.Poll(
                id="poll123",
                question="What is your favorite color?",
                options=[
                    types.PollOption(text="Red", voter_count=5),
                    types.PollOption(text="Blue", voter_count=10)
                ],
                total_voter_count=15,
                is_closed=False,
                type="regular"
            )
        )
        assert update.poll is not None
        assert update.poll.question == "What is your favorite color?"

    def test_update_with_poll_answer(self):
        """Test creating an Update with a poll answer."""
        update = getting_updates.Update(
            update_id=12352,
            poll_answer=types.PollAnswer(
                poll_id="poll123",
                user=types.User(id=1, is_bot=False, first_name="User"),
                option_ids=[0, 1]
            )
        )
        assert update.poll_answer is not None
        assert update.poll_answer.option_ids == [0, 1]

    def test_update_with_my_chat_member(self):
        """Test creating an Update with my_chat_member."""
        update = getting_updates.Update(
            update_id=12353,
            my_chat_member=types.ChatMemberUpdated(
                chat=types.Chat(id=-100123, type="supergroup"),
                from_=types.User(id=1, is_bot=False, first_name="User"),
                date=1234567890,
                old_chat_member=types.ChatMember(
                    status="left",
                    user=types.User(id=2, is_bot=True, first_name="Bot")
                ),
                new_chat_member=types.ChatMember(
                    status="administrator",
                    user=types.User(id=2, is_bot=True, first_name="Bot")
                )
            )
        )
        assert update.my_chat_member is not None
        assert update.my_chat_member.new_chat_member.status == "administrator"

    def test_update_with_chat_member(self):
        """Test creating an Update with chat_member."""
        update = getting_updates.Update(
            update_id=12354,
            chat_member=types.ChatMemberUpdated(
                chat=types.Chat(id=-100123, type="supergroup"),
                from_=types.User(id=1, is_bot=False, first_name="User"),
                date=1234567890,
                old_chat_member=types.ChatMember(
                    status="left",
                    user=types.User(id=2, is_bot=False, first_name="User2")
                ),
                new_chat_member=types.ChatMember(
                    status="member",
                    user=types.User(id=2, is_bot=False, first_name="User2")
                )
            )
        )
        assert update.chat_member is not None

    def test_update_with_chat_join_request(self):
        """Test creating an Update with chat_join_request."""
        update = getting_updates.Update(
            update_id=12355,
            chat_join_request=types.ChatJoinRequest(
                chat=types.Chat(id=-100123, type="supergroup"),
                from_=types.User(id=1, is_bot=False, first_name="User"),
                date=1234567890,
                user_chat_id=123456
            )
        )
        assert update.chat_join_request is not None

    def test_update_with_chat_boost(self):
        """Test creating an Update with chat_boost."""
        update = getting_updates.Update(
            update_id=12356,
            chat_boost=types.ChatBoostUpdated(
                chat=types.Chat(id=-100123, type="supergroup"),
                boost=types.ChatBoost(
                    boost_id="boost123",
                    add_date=1234567890,
                    expiration_date=1234567890,
                    source=types.ChatBoostSourcePremium(user=types.User(id=1, is_bot=False, first_name="User"))
                )
            )
        )
        assert update.chat_boost is not None

    def test_update_with_removed_chat_boost(self):
        """Test creating an Update with removed_chat_boost."""
        update = getting_updates.Update(
            update_id=12357,
            removed_chat_boost=types.ChatBoostRemoved(
                chat=types.Chat(id=-100123, type="supergroup"),
                boost_id="boost123",
                remove_date=1234567890,
                source=types.ChatBoostSourcePremium(user=types.User(id=1, is_bot=False, first_name="User"))
            )
        )
        assert update.removed_chat_boost is not None


class TestWebhookInfo:
    """Tests for WebhookInfo model."""

    def test_webhook_info_basic(self):
        """Test creating a basic WebhookInfo."""
        webhook = getting_updates.WebhookInfo(
            url="https://example.com/webhook",
            has_custom_certificate=False,
            pending_update_count=0
        )
        assert webhook.url == "https://example.com/webhook"
        assert webhook.pending_update_count == 0

    def test_webhook_info_with_all_fields(self):
        """Test creating WebhookInfo with all fields."""
        webhook = getting_updates.WebhookInfo(
            url="https://example.com/webhook",
            has_custom_certificate=True,
            pending_update_count=5,
            last_error_date=1234567890,
            last_error_message="Connection timeout",
            max_connections=40,
            allowed_updates=["message", "callback_query", "inline_query"]
        )
        assert webhook.has_custom_certificate is True
        assert webhook.pending_update_count == 5
        assert "message" in webhook.allowed_updates

    def test_webhook_info_empty_url(self):
        """Test WebhookInfo with empty URL (webhook not set)."""
        webhook = getting_updates.WebhookInfo(
            url="",
            has_custom_certificate=False,
            pending_update_count=0
        )
        assert webhook.url == ""


class TestUpdateSerialization:
    """Tests for Update serialization and deserialization."""

    def test_update_json_roundtrip(self, sample_update):
        """Test Update JSON serialization and deserialization."""
        json_str = sample_update.model_dump_json()
        data = json.loads(json_str)
        assert data["update_id"] == 12345
        assert "message" in data

    def test_update_with_all_fields_serialization(self):
        """Test Update with multiple fields serialization."""
        update = getting_updates.Update(
            update_id=123,
            message=types.Message(
                message_id=1,
                date=1234567890,
                chat=types.Chat(id=123, type="private"),
                text="Test"
            ),
            edited_message=types.Message(
                message_id=2,
                edit_date=1234567891,
                date=1234567890,
                chat=types.Chat(id=123, type="private"),
                text="Edited"
            ),
            channel_post=types.Message(
                message_id=3,
                date=1234567890,
                chat=types.Chat(id=-100123, type="channel"),
                text="Channel post"
            )
        )
        json_str = update.model_dump_json()
        data = json.loads(json_str)
        assert data["update_id"] == 123
        assert "message" in data
        assert "edited_message" in data
        assert "channel_post" in data


class TestUpdateEdgeCases:
    """Tests for Update edge cases."""

    def test_update_with_minimal_data(self):
        """Test Update with minimal required data."""
        update = getting_updates.Update(update_id=1)
        assert update.update_id == 1
        assert update.message is None
        assert update.callback_query is None

    def test_update_with_large_id(self):
        """Test Update with very large update_id."""
        update = getting_updates.Update(update_id=999999999999)
        assert update.update_id == 999999999999

    def test_update_with_multiple_optional_fields(self):
        """Test Update with many optional fields set."""
        update = getting_updates.Update(
            update_id=123,
            message=types.Message(
                message_id=1,
                date=1234567890,
                chat=types.Chat(id=123, type="private"),
                text="Message"
            ),
            edited_message=types.Message(
                message_id=2,
                edit_date=1234567891,
                date=1234567890,
                chat=types.Chat(id=123, type="private"),
                text="Edited"
            ),
            channel_post=types.Message(
                message_id=3,
                date=1234567890,
                chat=types.Chat(id=-100123, type="channel"),
                text="Post"
            ),
            edited_channel_post=types.Message(
                message_id=4,
                edit_date=1234567891,
                date=1234567890,
                chat=types.Chat(id=-100123, type="channel"),
                text="Edited post"
            )
        )
        assert update.message is not None
        assert update.edited_message is not None
        assert update.channel_post is not None
        assert update.edited_channel_post is not None
