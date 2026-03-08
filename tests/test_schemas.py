# tests/test_schemas.py
from pydantic import ValidationError
import pytest
from telegras.schemas import TgPhotoSize, TgMessage, TgChat

def test_photo_size_model():
    """Test TgPhotoSize model."""
    data = {
        "file_id": "abc123",
        "file_unique_id": "uniq123",
        "width": 800,
        "height": 600,
    }
    photo = TgPhotoSize(**data)
    assert photo.file_id == "abc123"
    assert photo.width == 800

def test_message_model():
    """Test TgMessage model."""
    data = {
        "message_id": 1,
        "chat": {"id": 123, "type": "private"},
        "date": 1234567890,
        "text": "Hello",
    }
    message = TgMessage(**data)
    assert message.message_id == 1
    assert message.text == "Hello"
