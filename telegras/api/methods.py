from __future__ import annotations

from pydantic import BaseModel, Field


class SendMessageRequest(BaseModel):
    chat_id: int | str
    text: str = Field(min_length=1)


class TelegramUser(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    username: str | None = None


class GetMeResponse(BaseModel):
    ok: bool
    result: TelegramUser
