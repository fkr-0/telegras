"""Telegram message parsing utilities - extracts media and text from updates."""

from __future__ import annotations

import mimetypes
from dataclasses import dataclass

from .schemas import TgMessage, TgPhotoSize, TgVideo, TgAnimation, TgDocument
from .api.getting_updates import Update


@dataclass
class TelegramMedia:
    """Lightweight descriptor for supported Telegram media attachments."""
    file_id: str
    media_type: str
    file_name: str | None = None
    mime_type: str | None = None


def find_photo_with_max_size(msg: TgMessage) -> TgPhotoSize | None:
    """
    From a TgMessage, pick the largest photo variant if present.

    Telegram sends multiple sizes of the same photo in msg.photo.
    """
    if not msg.photo:
        return None
    return max(msg.photo, key=lambda p: p.width * p.height)


def _add_media(
    media: list[TelegramMedia],
    seen_ids: set,
    *,
    file_id: str | None,
    media_type: str,
    file_name: str | None = None,
    mime_type: str | None = None,
) -> None:
    """Add media to list if not already seen."""
    if not file_id or file_id in seen_ids:
        return
    seen_ids.add(file_id)
    media.append(
        TelegramMedia(
            file_id=file_id,
            media_type=media_type,
            file_name=file_name,
            mime_type=mime_type,
        )
    )


def _infer_filename(
    *,
    file_id: str,
    media_type: str,
    file_name: str | None,
    mime_type: str | None,
) -> str:
    """Return a stable filename with extension when Telegram omits file_name."""
    if file_name:
        return file_name

    ext = mimetypes.guess_extension(mime_type or "")
    if not ext:
        fallback_ext = {
            "photo": ".jpg",
            "video": ".mp4",
            "animation": ".gif",
            "document": ".bin",
        }
        ext = fallback_ext.get(media_type, ".bin")
    return f"{file_id}{ext}"


def collect_supported_media(msg: TgMessage) -> list[TelegramMedia]:
    """Return a list of supported media descriptors for the message."""
    media: list[TelegramMedia] = []
    seen_ids: set = set()

    photo = find_photo_with_max_size(msg)
    if photo:
        _add_media(
            media,
            seen_ids,
            file_id=photo.file_id,
            media_type="photo",
            file_name=f"{photo.file_id}.jpg",
            mime_type="image/jpeg",
        )

    if isinstance(msg.video, TgVideo):
        inferred_name = _infer_filename(
            file_id=msg.video.file_id,
            media_type="video",
            file_name=msg.video.file_name,
            mime_type=msg.video.mime_type,
        )
        _add_media(
            media,
            seen_ids,
            file_id=msg.video.file_id,
            media_type="video",
            file_name=inferred_name,
            mime_type=msg.video.mime_type,
        )

    if isinstance(msg.animation, TgAnimation):
        inferred_name = _infer_filename(
            file_id=msg.animation.file_id,
            media_type="animation",
            file_name=msg.animation.file_name,
            mime_type=msg.animation.mime_type,
        )
        _add_media(
            media,
            seen_ids,
            file_id=msg.animation.file_id,
            media_type="animation",
            file_name=inferred_name,
            mime_type=msg.animation.mime_type,
        )

    if isinstance(msg.document, TgDocument):
        inferred_name = _infer_filename(
            file_id=msg.document.file_id,
            media_type="document",
            file_name=msg.document.file_name,
            mime_type=msg.document.mime_type,
        )
        _add_media(
            media,
            seen_ids,
            file_id=msg.document.file_id,
            media_type="document",
            file_name=inferred_name,
            mime_type=msg.document.mime_type,
        )

    return media


def extract_message_entity(update: Update) -> TgMessage | None:
    """
    Return the effective TgMessage from a Telegram update.

    This helper prefers channel_post over message when both are present.
    """
    # Check for channel_post first
    if hasattr(update, 'channel_post') and update.channel_post is not None:
        return update.channel_post

    # Fall back to message
    if hasattr(update, 'message') and update.message is not None:
        return update.message

    # Check for edited variants
    if hasattr(update, 'edited_channel_post') and update.edited_channel_post is not None:
        return update.edited_channel_post

    if hasattr(update, 'edited_message') and update.edited_message is not None:
        return update.edited_message

    return None


def extract_message_text(update: Update) -> str | None:
    """
    Extract text from an update, preferring message/channel_post.text
    and falling back to .caption.
    """
    msg = extract_message_entity(update)
    if not msg:
        return None

    return msg.text or msg.caption
