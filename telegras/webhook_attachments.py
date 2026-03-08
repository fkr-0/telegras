from __future__ import annotations

import asyncio
import importlib
import inspect
import re
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, model_validator

from telegras.default_handlers import get_default_handlers
from telegras.api.getting_updates import Update as TelegramUpdate

_TEMPLATE_RE = re.compile(r"\{\{\s*([a-zA-Z0-9_\.]+)\s*\}\}")


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


class LeafRule(BaseModel):
    field: FieldName
    match: MatchOp
    value: Any = None


class RuleOp(str, Enum):
    ALL = "all"
    ANY = "any"
    NOT = "not"
    LEAF = "leaf"


class RuleExpr(BaseModel):
    op: RuleOp
    children: list["RuleExpr"] = Field(default_factory=list)
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


class ParseSpec(BaseModel):
    regex: dict[str, str] = Field(default_factory=dict)
    parser_ref: str | None = None
    allow_partial: bool = True


class HandlerStep(BaseModel):
    handler: str
    handler_args: list[str] = Field(default_factory=list)


class ParseMode(str, Enum):
    STRICT = "strict"
    WARN = "warn"
    IGNORE = "ignore"


class ExecutionMode(str, Enum):
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"


class Attachment(BaseModel):
    name: str
    handler: str | None = None
    handler_args: list[str] = Field(default_factory=list)
    handler_chain: list[HandlerStep] = Field(default_factory=list)
    execution_mode: ExecutionMode = ExecutionMode.SEQUENTIAL
    stop_on_error: bool = True
    enabled: bool = True
    priority: int = 100
    stop_on_match: bool = False
    when: RuleExpr
    parse: ParseSpec | None = None
    parse_mode: ParseMode = ParseMode.WARN

    @model_validator(mode="after")
    def _validate_handlers(self) -> "Attachment":
        has_primary = bool(self.handler)
        has_chain = len(self.handler_chain) > 0
        if not has_primary and not has_chain:
            raise ValueError("attachment requires handler or handler_chain")
        return self

    def normalized_steps(self) -> list[HandlerStep]:
        steps = list(self.handler_chain)
        if self.handler:
            steps.insert(0, HandlerStep(handler=self.handler, handler_args=self.handler_args))
        return steps


class WebhookAttachmentRegistry:
    def __init__(self) -> None:
        self._attachments: dict[str, Attachment] = {}

    def register(self, attachment: Attachment) -> Attachment:
        self._attachments[attachment.name] = attachment
        return attachment

    def unregister(self, name: str) -> bool:
        return self._attachments.pop(name, None) is not None

    def list_attachments(self) -> list[Attachment]:
        return sorted(
            self._attachments.values(),
            key=lambda item: (item.priority, item.name),
        )

    def match_attachments(self, update: TelegramUpdate) -> list[Attachment]:
        matched: list[Attachment] = []
        for item in self.list_attachments():
            if not item.enabled:
                continue
            if _matches(item.when, update):
                matched.append(item)
                if item.stop_on_match:
                    break
        return matched

    async def execute_matching_attachments(
        self, update: TelegramUpdate
    ) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []

        for attachment in self.match_attachments(update):
            base_context = build_message_context(update)
            parse_info = await apply_parser(attachment, update, base_context)
            if parse_info["status"] == "invalid" and attachment.parse_mode == ParseMode.STRICT:
                results.append(
                    {
                        "attachment": attachment.name,
                        "handler": attachment.handler or "",
                        "rendered_args": [],
                        "ok": False,
                        "error": "Parser invalid in strict mode",
                        "parse": parse_info,
                        "handler_executions": [],
                    }
                )
                continue

            context = dict(base_context)
            context["match"] = parse_info.get("match", {})

            step_results: list[dict[str, Any]] = []
            steps = attachment.normalized_steps()

            async def run_step(step: HandlerStep) -> dict[str, Any]:
                rendered_args = [
                    render_template(arg, context) if isinstance(arg, str) else arg
                    for arg in step.handler_args
                ]
                try:
                    handler = resolve_handler(step.handler)
                    value = handler(context, *rendered_args)
                    if inspect.isawaitable(value):
                        value = await value
                    return {
                        "handler": step.handler,
                        "rendered_args": rendered_args,
                        "ok": True,
                        "result": value,
                    }
                except Exception as exc:
                    return {
                        "handler": step.handler,
                        "rendered_args": rendered_args,
                        "ok": False,
                        "error": str(exc),
                    }

            if attachment.execution_mode == ExecutionMode.PARALLEL:
                step_results = await asyncio.gather(*(run_step(step) for step in steps))
            else:
                for step in steps:
                    row = await run_step(step)
                    step_results.append(row)
                    if not row["ok"] and attachment.stop_on_error:
                        break

            overall_ok = all(row.get("ok") for row in step_results) if step_results else False
            first = step_results[0] if step_results else {"handler": attachment.handler or "", "rendered_args": []}
            record = {
                "attachment": attachment.name,
                "handler": first.get("handler", ""),
                "rendered_args": first.get("rendered_args", []),
                "ok": overall_ok,
                "result": first.get("result"),
                "error": first.get("error"),
                "parse": parse_info,
                "handler_executions": step_results,
            }
            results.append(record)

        return results


def resolve_handler(handler_name: str):
    defaults = get_default_handlers()
    if handler_name in defaults:
        return defaults[handler_name]

    module_name, _, symbol = handler_name.partition(":")
    if not module_name or not symbol:
        raise ValueError(f"Invalid handler '{handler_name}'")
    module = importlib.import_module(module_name)
    handler = getattr(module, symbol, None)
    if handler is None:
        raise ValueError(f"Handler not found: {handler_name}")
    return handler


async def apply_parser(
    attachment: Attachment,
    update: TelegramUpdate,
    context: dict[str, Any],
) -> dict[str, Any]:
    result = {
        "status": "ok",
        "match": {},
        "warnings": [],
        "errors": [],
    }

    if attachment.parse is None:
        return result

    text = context.get("message", {}).get("full") or ""

    for key, pattern in attachment.parse.regex.items():
        matched = re.search(pattern, text)
        if not matched:
            result["warnings"].append(f"regex '{key}' did not match")
            if result["status"] == "ok":
                result["status"] = "partial"
            continue

        if matched.groupdict():
            result["match"].update(matched.groupdict())
        elif matched.groups():
            result["match"][key] = matched.group(1)
        else:
            result["match"][key] = matched.group(0)

    if attachment.parse.parser_ref:
        try:
            parser = resolve_handler(attachment.parse.parser_ref)
            parser_output = parser(context, update)
            if inspect.isawaitable(parser_output):
                parser_output = await parser_output
            if isinstance(parser_output, dict):
                result["match"].update(parser_output.get("match", {}))
                result["warnings"].extend(parser_output.get("warnings", []))
                result["errors"].extend(parser_output.get("errors", []))
                if parser_output.get("status") in {"ok", "partial", "invalid"}:
                    result["status"] = parser_output["status"]
        except Exception as exc:
            result["errors"].append(str(exc))
            result["status"] = "invalid"

    if result["errors"] and attachment.parse_mode == ParseMode.STRICT:
        result["status"] = "invalid"
    elif result["warnings"] and result["status"] == "ok":
        result["status"] = "partial"

    return result


def build_message_context(update: TelegramUpdate) -> dict[str, Any]:
    payload = _payload(update)
    text = _message_text(update) or ""
    title = text.splitlines()[0] if text else ""
    full = text
    chat = _chat(update)

    chat_info: dict[str, Any]
    if isinstance(chat, dict):
        chat_info = {
            "id": chat.get("id"),
            "type": chat.get("type"),
            "title": chat.get("title"),
        }
    elif chat is None:
        chat_info = {"id": None, "type": None, "title": None}
    else:
        chat_info = {
            "id": getattr(chat, "id", None),
            "type": getattr(chat, "type", None),
            "title": getattr(chat, "title", None),
        }

    kind = update.kind.value if update.kind else None
    return {
        "message": {
            "title": title,
            "full": full,
            "text": text,
            "has_media": _has_media(update),
            "media_type": _media_type(update),
        },
        "chat": chat_info,
        "update": {"update_id": update.update_id, "kind": kind},
        "update_obj": update,
        "payload": payload,
    }


def render_template(template: str, context: dict[str, Any]) -> str:
    def repl(match: re.Match[str]) -> str:
        path = match.group(1)
        value = lookup_context_value(context, path)
        if value is None:
            return ""
        return str(value)

    return _TEMPLATE_RE.sub(repl, template)


def lookup_context_value(context: dict[str, Any], dotted_path: str) -> Any:
    node: Any = context
    for part in dotted_path.split("."):
        if isinstance(node, dict):
            node = node.get(part)
        else:
            node = getattr(node, part, None)
        if node is None:
            return None
    return node


def _payload(update: TelegramUpdate) -> Any:
    return update.get_payload()


def _message_text(update: TelegramUpdate) -> str | None:
    payload = _payload(update)
    if payload is None:
        return None
    if isinstance(payload, dict):
        return payload.get("text") or payload.get("caption")
    return getattr(payload, "text", None) or getattr(payload, "caption", None)


def _chat(update: TelegramUpdate) -> Any:
    payload = _payload(update)
    if payload is None:
        return None
    if isinstance(payload, dict):
        return payload.get("chat")
    return getattr(payload, "chat", None)


def _sender(update: TelegramUpdate) -> Any:
    payload = _payload(update)
    if payload is None:
        return None
    if isinstance(payload, dict):
        return payload.get("from")
    return getattr(payload, "from_user", None) or getattr(payload, "from", None)


def _has_media(update: TelegramUpdate) -> bool:
    payload = _payload(update)
    if payload is None:
        return False

    media_keys = ["photo", "video", "animation", "document", "audio", "voice", "sticker"]
    if isinstance(payload, dict):
        return any(payload.get(k) is not None for k in media_keys)
    return any(getattr(payload, k, None) is not None for k in media_keys)


def _media_type(update: TelegramUpdate) -> str | None:
    payload = _payload(update)
    if payload is None:
        return None

    media_keys = ["video", "animation", "photo", "document", "audio", "voice", "sticker"]
    if isinstance(payload, dict):
        for k in media_keys:
            if payload.get(k) is not None:
                return k
        return None

    for k in media_keys:
        if getattr(payload, k, None) is not None:
            return k
    return None


def _resolve_field(field: FieldName, update: TelegramUpdate) -> Any:
    if field == FieldName.UPDATE_KIND:
        payload = _payload(update)
        if payload is None:
            return None
        return update.kind.value if update.kind else None

    if field == FieldName.MESSAGE_TEXT:
        return _message_text(update)

    if field == FieldName.MESSAGE_HAS_MEDIA:
        return _has_media(update)

    if field == FieldName.MESSAGE_MEDIA_TYPE:
        return _media_type(update)

    if field in {FieldName.CHAT_ID, FieldName.CHAT_TYPE, FieldName.CHAT_TITLE}:
        chat = _chat(update)
        if chat is None:
            return None
        if isinstance(chat, dict):
            key = field.value.split(".", 1)[1]
            return chat.get(key)
        key = field.value.split(".", 1)[1]
        return getattr(chat, key, None)

    if field == FieldName.SENDER_ID:
        sender = _sender(update)
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


def _matches(expr: RuleExpr, update: TelegramUpdate) -> bool:
    if expr.op == RuleOp.LEAF and expr.leaf is not None:
        return _eval_leaf(expr.leaf, update)

    if expr.op == RuleOp.ALL:
        return all(_matches(child, update) for child in expr.children)

    if expr.op == RuleOp.ANY:
        return any(_matches(child, update) for child in expr.children)

    if expr.op == RuleOp.NOT:
        return not _matches(expr.children[0], update)

    return False
