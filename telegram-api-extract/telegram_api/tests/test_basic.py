"""Basic tests for telegram_api package."""

from telegram_api import types, methods, getting_updates

# Rebuild models that have forward references
methods.sendMessage.model_rebuild()


def test_user_model():
    """Test User model creation and validation."""
    user = types.User(
        id=123456789,
        is_bot=False,
        first_name="Test"
    )
    assert user.id == 123456789
    assert user.first_name == "Test"
    assert user.last_name is None  # Optional field


def test_sendmessage_model():
    """Test sendMessage method model."""
    msg = methods.sendMessage(
        chat_id=123456789,
        text="Hello, World!"
    )
    assert msg.chat_id == 123456789
    assert msg.text == "Hello, World!"


def test_update_model():
    """Test Update model."""
    update = getting_updates.Update(update_id=1)
    assert update.update_id == 1


def test_json_serialization():
    """Test JSON serialization."""
    user = types.User(id=123, is_bot=True, first_name="Bot")
    json_str = user.model_dump_json()
    assert "123" in json_str
    assert "Bot" in json_str
