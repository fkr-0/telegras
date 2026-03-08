from __future__ import annotations

import asyncio
import re
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, model_validator

from telegras.handler_registry import handler_executor
from telegras.parsers import ParseSpec, parser_service
from telegras.api.getting_updates import Update as TelegramUpdate
from telegras.matchers import (
    FieldName,
    MatchOp,
    RuleExpr,
    get_chat,
    get_message_text,
    get_payload,
    has_media,
    matches,
    media_type,
)

_TEMPLATE_RE = re.compile(r"\{\{\s*([a-zA-Z0-9_\.]+)\s*\}\}")


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
            if matches(item.when, update):
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
            parse_result = await parser_service.parse(attachment.parse, base_context, update)
            parse_info = parse_result.to_dict()
            if parse_result.status == "invalid" and attachment.parse_mode == ParseMode.STRICT:
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
            context["match"] = parse_result.match

            step_results: list[dict[str, Any]] = []
            steps = attachment.normalized_steps()

            async def run_step(step: HandlerStep) -> dict[str, Any]:
                rendered_args: list[Any] = []
                try:
                    rendered_args = [
                        render_template(arg, context) if isinstance(arg, str) else arg
                        for arg in step.handler_args
                    ]
                except Exception as exc:
                    return {
                        "handler": step.handler,
                        "rendered_args": rendered_args,
                        "ok": False,
                        "error": str(exc),
                    }
                execution = await handler_executor.execute(
                    step.handler, context, rendered_args
                )
                return execution.to_dict()

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


def build_message_context(update: TelegramUpdate) -> dict[str, Any]:
    payload = get_payload(update)
    text = get_message_text(update) or ""
    title = text.splitlines()[0] if text else ""
    full = text
    chat = get_chat(update)

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
            "has_media": has_media(update),
            "media_type": media_type(update),
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
