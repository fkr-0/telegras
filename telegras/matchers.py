from __future__ import annotations

import re
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field as PydanticField, model_validator

from telegras.api.getting_updates import Update as TelegramUpdate


class FieldName(str, Enum):
    UPDATE_KIND = "update.kind"
    CHAT_TYPE = "chat.type"
    CHAT_ID = "chat.id"
    CHAT_TITLE = "chat.title"
    SENDER_ID = "sender.id"
    MESSAGE_TEXT = "message.text"
    MESSAGE_HAS_MEDIA = "message.has_media"
    MESSAGE_MEDIA_TYPE = "message.media_type"


class MatchOp(str, Enum):
    EQ = "eq"
    IN = "in"
    REGEX = "regex"
    CONTAINS = "contains"
    STARTS_WITH = "starts_with"
    EXISTS = "exists"


class RuleOp(str, Enum):
    ALL = "all"
    ANY = "any"
    NOT = "not"
    LEAF = "leaf"


class LeafRule(BaseModel):
    field: FieldName
    match: MatchOp
    value: Any = None


class RuleExpr(BaseModel):
    op: RuleOp
    children: list["RuleExpr"] = PydanticField(default_factory=list)
    leaf: LeafRule | None = None

    @model_validator(mode="after")
    def _validate_shape(self) -> "RuleExpr":
        if self.op == RuleOp.LEAF:
            if self.leaf is None:
                raise ValueError("leaf must be provided for op=leaf")
            return self

        if self.leaf is not None:
            raise ValueError("leaf must be omitted for non-leaf ops")

        if self.op == RuleOp.NOT and len(self.children) != 1:
            raise ValueError("not requires exactly one child")

        if self.op in {RuleOp.ALL, RuleOp.ANY} and not self.children:
            raise ValueError("all/any require at least one child")

        return self

    @staticmethod
    def make_leaf(field: FieldName, match: MatchOp, value: Any = None) -> "RuleExpr":
        return RuleExpr(op=RuleOp.LEAF, leaf=LeafRule(field=field, match=match, value=value))

    @staticmethod
    def all_of(children: list["RuleExpr"]) -> "RuleExpr":
        return RuleExpr(op=RuleOp.ALL, children=children)

    @staticmethod
    def any_of(children: list["RuleExpr"]) -> "RuleExpr":
        return RuleExpr(op=RuleOp.ANY, children=children)

    @staticmethod
    def not_(child: "RuleExpr") -> "RuleExpr":
        return RuleExpr(op=RuleOp.NOT, children=[child])


def get_payload(update: TelegramUpdate) -> Any:
    return update.get_payload()


def get_message_text(update: TelegramUpdate) -> str | None:
    payload = get_payload(update)
    if payload is None:
        return None
    if isinstance(payload, dict):
        return payload.get("text") or payload.get("caption")
    return getattr(payload, "text", None) or getattr(payload, "caption", None)


def get_chat(update: TelegramUpdate) -> Any:
    payload = get_payload(update)
    if payload is None:
        return None
    if isinstance(payload, dict):
        return payload.get("chat")
    return getattr(payload, "chat", None)


def get_sender(update: TelegramUpdate) -> Any:
    payload = get_payload(update)
    if payload is None:
        return None
    if isinstance(payload, dict):
        return payload.get("from")
    return getattr(payload, "from_user", None) or getattr(payload, "from", None)


def has_media(update: TelegramUpdate) -> bool:
    payload = get_payload(update)
    if payload is None:
        return False

    media_keys = ["photo", "video", "animation", "document", "audio", "voice", "sticker"]
    if isinstance(payload, dict):
        return any(payload.get(k) is not None for k in media_keys)
    return any(getattr(payload, k, None) is not None for k in media_keys)


def media_type(update: TelegramUpdate) -> str | None:
    payload = get_payload(update)
    if payload is None:
        return None

    media_keys = ["video", "animation", "photo", "document", "audio", "voice", "sticker"]
    if isinstance(payload, dict):
        for key in media_keys:
            if payload.get(key) is not None:
                return key
        return None

    for key in media_keys:
        if getattr(payload, key, None) is not None:
            return key
    return None


def _resolve_field(field: FieldName, update: TelegramUpdate) -> Any:
    if field == FieldName.UPDATE_KIND:
        payload = get_payload(update)
        if payload is None:
            return None
        return update.kind.value if update.kind else None

    if field == FieldName.MESSAGE_TEXT:
        return get_message_text(update)

    if field == FieldName.MESSAGE_HAS_MEDIA:
        return has_media(update)

    if field == FieldName.MESSAGE_MEDIA_TYPE:
        return media_type(update)

    if field in {FieldName.CHAT_ID, FieldName.CHAT_TYPE, FieldName.CHAT_TITLE}:
        chat = get_chat(update)
        if chat is None:
            return None
        key = field.value.split(".", 1)[1]
        if isinstance(chat, dict):
            return chat.get(key)
        return getattr(chat, key, None)

    if field == FieldName.SENDER_ID:
        sender = get_sender(update)
        if sender is None:
            return None
        if isinstance(sender, dict):
            return sender.get("id")
        return getattr(sender, "id", None)

    return None


def _eval_leaf(leaf: LeafRule, update: TelegramUpdate) -> bool:
    actual = _resolve_field(leaf.field, update)

    if leaf.match == MatchOp.EXISTS:
        return actual is not None

    if leaf.match == MatchOp.EQ:
        return actual == leaf.value

    if leaf.match == MatchOp.IN:
        if not isinstance(leaf.value, list):
            return False
        return actual in leaf.value

    if leaf.match == MatchOp.CONTAINS:
        if actual is None:
            return False
        return str(leaf.value) in str(actual)

    if leaf.match == MatchOp.STARTS_WITH:
        if actual is None:
            return False
        return str(actual).startswith(str(leaf.value))

    if leaf.match == MatchOp.REGEX:
        if actual is None:
            return False
        return re.search(str(leaf.value), str(actual)) is not None

    return False


def matches(expr: RuleExpr, update: TelegramUpdate) -> bool:
    if expr.op == RuleOp.LEAF and expr.leaf is not None:
        return _eval_leaf(expr.leaf, update)

    if expr.op == RuleOp.ALL:
        return all(matches(child, update) for child in expr.children)

    if expr.op == RuleOp.ANY:
        return any(matches(child, update) for child in expr.children)

    if expr.op == RuleOp.NOT:
        return not matches(expr.children[0], update)

    return False
