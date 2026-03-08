"""Tests for message parser module."""

from __future__ import annotations

import pytest
from telegras.message_parser import (
    TelegramMedia,
    find_photo_with_max_size,
    collect_supported_media,
    extract_message_entity,
    extract_message_text,
)
from telegras.schemas import (
    TgMessage,
    TgPhotoSize,
    TgChat,
    TgVideo,
    TgAnimation,
    TgDocument,
)
from telegras.api.getting_updates import Update


def test_find_photo_with_max_size():
    """Test finding largest photo."""
    small = TgPhotoSize(file_id="small", file_unique_id="s", width=100, height=100)
    large = TgPhotoSize(file_id="large", file_unique_id="l", width=800, height=600)

    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
        photo=[small, large],
    )

    result = find_photo_with_max_size(msg)
    assert result == large


def test_find_photo_with_max_size_no_photo():
    """Test finding largest photo when no photo present."""
    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
    )

    result = find_photo_with_max_size(msg)
    assert result is None


def test_collect_supported_media_video():
    """Test collecting video media from message."""
    video = TgVideo(
        file_id="vid123",
        file_unique_id="v123",
        width=1280,
        height=720,
        duration=30,
        file_name="video.mp4",
        mime_type="video/mp4",
    )

    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
        video=video,
    )

    media = collect_supported_media(msg)
    assert len(media) == 1
    assert media[0].file_id == "vid123"
    assert media[0].media_type == "video"


def test_collect_supported_media_photo():
    """Test collecting photo media from message."""
    small = TgPhotoSize(file_id="small", file_unique_id="s", width=100, height=100)
    large = TgPhotoSize(file_id="large", file_unique_id="l", width=800, height=600)

    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
        photo=[small, large],
    )

    media = collect_supported_media(msg)
    assert len(media) == 1
    assert media[0].file_id == "large"
    assert media[0].media_type == "photo"
    assert media[0].file_name == "large.jpg"
    assert media[0].mime_type == "image/jpeg"


def test_collect_supported_media_animation():
    """Test collecting animation media from message."""
    animation = TgAnimation(
        file_id="anim123",
        file_unique_id="a123",
        width=640,
        height=480,
        duration=5,
        file_name="animation.gif",
        mime_type="image/gif",
    )

    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
        animation=animation,
    )

    media = collect_supported_media(msg)
    assert len(media) == 1
    assert media[0].file_id == "anim123"
    assert media[0].media_type == "animation"


def test_collect_supported_media_document():
    """Test collecting document media from message."""
    document = TgDocument(
        file_id="doc123",
        file_unique_id="d123",
        file_name="report.pdf",
        mime_type="application/pdf",
    )

    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
        document=document,
    )

    media = collect_supported_media(msg)
    assert len(media) == 1
    assert media[0].file_id == "doc123"
    assert media[0].media_type == "document"


def test_collect_supported_media_multiple():
    """Test collecting multiple media types from message."""
    photo = TgPhotoSize(file_id="photo", file_unique_id="p", width=800, height=600)
    video = TgVideo(
        file_id="vid123",
        file_unique_id="v123",
        width=1280,
        height=720,
        duration=30,
    )

    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
        photo=[photo],
        video=video,
    )

    media = collect_supported_media(msg)
    assert len(media) == 2
    assert media[0].file_id == "photo"
    assert media[0].media_type == "photo"
    assert media[1].file_id == "vid123"
    assert media[1].media_type == "video"


def test_collect_supported_media_empty():
    """Test collecting media when none present."""
    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
    )

    media = collect_supported_media(msg)
    assert len(media) == 0


def test_extract_message_entity_from_message():
    """Test extracting message entity from update.message."""
    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
    )
    update = Update(update_id=1, message=msg)

    result = extract_message_entity(update)
    assert result == msg


def test_extract_message_entity_from_channel_post():
    """Test extracting message entity from update.channel_post."""
    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="channel"),
        date=1234567890,
    )
    update = Update(update_id=1, channel_post=msg)

    result = extract_message_entity(update)
    assert result == msg


def test_extract_message_entity_prefers_channel_post():
    """Test that channel_post is preferred over message."""
    channel_msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="channel"),
        date=1234567890,
    )
    regular_msg = TgMessage(
        message_id=2,
        chat=TgChat(id=456, type="private"),
        date=1234567891,
    )
    update = Update(update_id=1, message=regular_msg, channel_post=channel_msg)

    result = extract_message_entity(update)
    assert result == channel_msg


def test_extract_message_entity_from_edited_message():
    """Test extracting message entity from update.edited_message."""
    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
    )
    update = Update(update_id=1, edited_message=msg)

    result = extract_message_entity(update)
    assert result == msg


def test_extract_message_entity_from_edited_channel_post():
    """Test extracting message entity from update.edited_channel_post."""
    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="channel"),
        date=1234567890,
    )
    update = Update(update_id=1, edited_channel_post=msg)

    result = extract_message_entity(update)
    assert result == msg


def test_extract_message_entity_none():
    """Test extracting message entity when none present."""
    update = Update(update_id=1)

    result = extract_message_entity(update)
    assert result is None


def test_extract_message_text_from_text():
    """Test extracting text from message."""
    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
        text="Hello, world!",
    )
    update = Update(update_id=1, message=msg)

    result = extract_message_text(update)
    assert result == "Hello, world!"


def test_extract_message_text_from_caption():
    """Test extracting text from caption."""
    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
        caption="This is a caption",
    )
    update = Update(update_id=1, message=msg)

    result = extract_message_text(update)
    assert result == "This is a caption"


def test_extract_message_text_prefers_text_over_caption():
    """Test that text is preferred over caption."""
    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
        text="Text message",
        caption="Caption",
    )
    update = Update(update_id=1, message=msg)

    result = extract_message_text(update)
    assert result == "Text message"


def test_extract_message_text_none():
    """Test extracting text when none present."""
    msg = TgMessage(
        message_id=1,
        chat=TgChat(id=123, type="private"),
        date=1234567890,
    )
    update = Update(update_id=1, message=msg)

    result = extract_message_text(update)
    assert result is None


def test_extract_message_text_no_message():
    """Test extracting text when no message entity."""
    update = Update(update_id=1)

    result = extract_message_text(update)
    assert result is None
