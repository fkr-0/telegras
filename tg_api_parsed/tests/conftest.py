"""Pytest configuration and shared fixtures for telegram_api tests."""

import pytest

# Import all modules and set up models before any tests run
from telegram_api import types, methods, getting_updates
from telegram_api import stickers, payments, games, inline_mode, passport, updating_messages


def setup_models():
    """Set up models by injecting types and rebuilding."""
    # Collect all type classes from all modules
    all_types = {}
    for module in [types, methods, getting_updates, stickers, payments, games, inline_mode, passport, updating_messages]:
        for attr_name in dir(module):
            if attr_name[0].isupper():  # Types start with uppercase
                attr = getattr(module, attr_name)
                try:
                    if isinstance(attr, type) and issubclass(attr, object):
                        all_types[attr_name] = attr
                except TypeError:
                    pass

    # Inject all types into each module's namespace
    for module in [types, methods, getting_updates, stickers, payments, games, inline_mode, passport, updating_messages]:
        for type_name, type_class in all_types.items():
            if not hasattr(module, type_name):
                setattr(module, type_name, type_class)

    # Rebuild all models that have forward references
    for module in [types, methods, getting_updates, stickers, payments, games, inline_mode, passport, updating_messages]:
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            try:
                if hasattr(attr, 'model_rebuild'):
                    attr.model_rebuild(_types_namespace={**all_types, **vars(module)})
            except Exception:
                pass  # Skip if rebuild fails


# Run setup at module import time
setup_models()


@pytest.fixture
def sample_user():
    """Create a sample User for testing."""
    return types.User(
        id=123456789,
        is_bot=False,
        first_name="Test",
        username="test_user"
    )


@pytest.fixture
def sample_bot():
    """Create a sample Bot user for testing."""
    return types.User(
        id=987654321,
        is_bot=True,
        first_name="TestBot",
        username="test_bot"
    )


@pytest.fixture
def sample_chat():
    """Create a sample Chat for testing."""
    return types.Chat(
        id=-100123456789,
        type="supergroup",
        title="Test Group"
    )


@pytest.fixture
def sample_private_chat():
    """Create a sample private Chat for testing."""
    return types.Chat(
        id=123456789,
        type="private"
    )


@pytest.fixture
def sample_message():
    """Create a sample Message for testing."""
    return types.Message(
        message_id=1,
        date=1234567890,
        chat=types.Chat(id=123, type="private"),
        text="Hello, World!"
    )


@pytest.fixture
def sample_update():
    """Create a sample Update for testing."""
    return getting_updates.Update(
        update_id=12345,
        message=types.Message(
            message_id=1,
            date=1234567890,
            chat=types.Chat(id=123, type="private"),
            text="Test message"
        )
    )


@pytest.fixture
def sample_callback_query():
    """Create a sample CallbackQuery for testing."""
    return types.CallbackQuery(
        id="callback123",
        from_=types.User(id=123, is_bot=False, first_name="User"),
        message=types.Message(
            message_id=1,
            date=1234567890,
            chat=types.Chat(id=123, type="private")
        ),
        data="callback_data"
    )


@pytest.fixture
def sample_inline_query():
    """Create a sample InlineQuery for testing."""
    return inline_mode.InlineQuery(
        id="inline_query_123",
        from_=types.User(id=123, is_bot=False, first_name="User"),
        query="test query",
        offset="0"
    )


@pytest.fixture
def sample_shipping_query():
    """Create a sample ShippingQuery for testing."""
    return payments.ShippingQuery(
        id="shipping_123",
        from_=types.User(id=123, is_bot=False, first_name="User"),
        shipping_address=payments.ShippingAddress(
            country_code="US",
            state="CA",
            city="San Francisco",
            street_line1="123 Main St",
            post_code="94102"
        )
    )


@pytest.fixture
def sample_pre_checkout_query():
    """Create a sample PreCheckoutQuery for testing."""
    return payments.PreCheckoutQuery(
        id="precheckout_123",
        from_=types.User(id=123, is_bot=False, first_name="User"),
        currency="USD",
        total_amount=1000,
        invoice_payload="invoice_payload"
    )


@pytest.fixture
def sample_successful_payment():
    """Create a sample SuccessfulPayment for testing."""
    return payments.SuccessfulPayment(
        currency="USD",
        total_amount=1000,
        invoice_payload="invoice_payload",
        telegram_payment_charge_id="charge_123",
        provider_payment_charge_id="provider_charge_123"
    )


@pytest.fixture
def sample_game():
    """Create a sample Game for testing."""
    return games.Game(
        title="Test Game",
        description="A test game",
        photo=[
            types.PhotoSize(
                file_id="photo_123",
                file_unique_id="unique_photo_123",
                width=100,
                height=100
            )
        ]
    )


@pytest.fixture
def sample_sticker():
    """Create a sample Sticker for testing."""
    return stickers.Sticker(
        file_id="sticker_123",
        file_unique_id="unique_sticker_123",
        type="regular",
        width=512,
        height=512,
        is_animated=False,
        is_video=False
    )


@pytest.fixture
def sample_webhook_info():
    """Create a sample WebhookInfo for testing."""
    return getting_updates.WebhookInfo(
        url="https://example.com/webhook",
        has_custom_certificate=False,
        pending_update_count=0
    )
