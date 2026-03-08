"""Pydantic models for Telegram API responses."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class TgPhotoSize(BaseModel):
    """Telegram photo size model.

    Attributes:
        file_id: Identifier for this file, can be used to download or reuse
        file_unique_id: Unique identifier for this file
        width: Photo width in pixels
        height: Photo height in pixels
        file_size: File size in bytes, if available
    """
    model_config = ConfigDict(extra="allow")

    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: int | None = None


class TgVideo(BaseModel):
    """Telegram video model.

    Attributes:
        file_id: Identifier for this file, can be used to download or reuse
        file_unique_id: Unique identifier for this file
        width: Video width in pixels
        height: Video height in pixels
        duration: Video duration in seconds
        thumb: Video thumbnail, if available
        file_name: Original filename, if available
        mime_type: MIME type of the file, if available
    """
    model_config = ConfigDict(extra="allow")

    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: TgPhotoSize | None = None
    file_name: str | None = None
    mime_type: str | None = None


class TgAnimation(BaseModel):
    """Telegram animation model.

    Attributes:
        file_id: Identifier for this file, can be used to download or reuse
        file_unique_id: Unique identifier for this file
        width: Animation width in pixels
        height: Animation height in pixels
        duration: Animation duration in seconds
        thumb: Animation thumbnail, if available
        file_name: Original filename, if available
        mime_type: MIME type of the file, if available
    """
    model_config = ConfigDict(extra="allow")

    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: TgPhotoSize | None = None
    file_name: str | None = None
    mime_type: str | None = None


class TgDocument(BaseModel):
    """Telegram document model.

    Attributes:
        file_id: Identifier for this file, can be used to download or reuse
        file_unique_id: Unique identifier for this file
        file_name: Original filename, if available
        mime_type: MIME type of the file, if available
        thumb: Document thumbnail, if available
    """
    model_config = ConfigDict(extra="allow")

    file_id: str
    file_unique_id: str
    file_name: str | None = None
    mime_type: str | None = None
    thumb: TgPhotoSize | None = None


class TgChat(BaseModel):
    """Telegram chat model.

    Attributes:
        id: Unique identifier for this chat
        type: Type of chat (private, group, supergroup, channel)
        title: Chat title, for groups/supergroups/channels
        username: Username, for private chats and public channels/chats
    """
    model_config = ConfigDict(extra="allow")

    id: int
    type: str
    title: str | None = None
    username: str | None = None


class TgMessage(BaseModel):
    """Telegram message model.

    Attributes:
        message_id: Unique message identifier inside this chat
        chat: Chat the message belongs to
        date: Date the message was sent in Unix time
        text: Text of the message, for text messages
        caption: Caption for media content, if present
        photo: Photo content as array of sizes
        video: Video content, if present
        animation: Animation content, if present
        document: General file content, if present
        edit_date: Date the message was last edited in Unix time
        media_group_id: Unique identifier of a media message group
    """
    model_config = ConfigDict(extra="allow")

    message_id: int
    chat: TgChat
    date: int
    text: str | None = None
    caption: str | None = None
    photo: list[TgPhotoSize] | None = None
    video: TgVideo | None = None
    animation: TgAnimation | None = None
    document: TgDocument | None = None
    edit_date: int | None = None
    media_group_id: str | None = None
