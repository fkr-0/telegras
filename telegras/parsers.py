from __future__ import annotations

import inspect
import re
from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel, Field as PydanticField

from telegras.api.getting_updates import Update as TelegramUpdate
from telegras.handler_registry import HandlerRegistry, handler_registry


class ParseSpec(BaseModel):
    regex: dict[str, str] = PydanticField(default_factory=dict)
    parser_ref: str | None = None
    allow_partial: bool = True


@dataclass
class ParserResult:
    """Normalized parser output consumed by attachment execution.

    Fields:
        status: ``ok``, ``partial`` or ``invalid``.
        match: extracted values merged into ``context['match']``.
        warnings: non-fatal parse notes.
        errors: fatal parse notes.
    """

    status: str
    match: dict[str, Any]
    warnings: list[str]
    errors: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "match": self.match,
            "warnings": self.warnings,
            "errors": self.errors,
        }


class ParserService:
    def __init__(self, registry: HandlerRegistry) -> None:
        self._registry = registry

    async def parse(
        self,
        spec: ParseSpec | None,
        context: dict[str, Any],
        update: TelegramUpdate,
    ) -> ParserResult:
        """Parse one Telegram update with optional regex and parser plugin steps.

        Args:
            spec: Optional ``ParseSpec``. ``None`` yields an empty successful result.
            context: Base execution context built from the Telegram update.
            update: The raw update model.
        """
        result = ParserResult(status="ok", match={}, warnings=[], errors=[])
        if spec is None:
            return result

        text = context.get("message", {}).get("full") or ""
        for key, pattern in spec.regex.items():
            matched = re.search(pattern, text)
            if not matched:
                result.warnings.append(f"regex '{key}' did not match")
                if result.status == "ok":
                    result.status = "partial"
                continue

            if matched.groupdict():
                result.match.update(matched.groupdict())
            elif matched.groups():
                result.match[key] = matched.group(1)
            else:
                result.match[key] = matched.group(0)

        if spec.parser_ref:
            try:
                parser = self._registry.get_parser(spec.parser_ref)
                parser_output = parser(context, update)
                if inspect.isawaitable(parser_output):
                    parser_output = await parser_output
                self._merge_parser_output(result, parser_output)
            except Exception as exc:
                result.errors.append(str(exc))
                result.status = "invalid"

        if result.warnings and result.status == "ok":
            result.status = "partial"
        return result

    @staticmethod
    def _merge_parser_output(result: ParserResult, parser_output: Any) -> None:
        if parser_output is None:
            return

        if isinstance(parser_output, ParserResult):
            output = parser_output.to_dict()
        elif isinstance(parser_output, dict):
            output = parser_output
        else:
            raise TypeError("parser output must be a dict or ParserResult")

        match_values = output.get("match", output if "status" not in output else {})
        if isinstance(match_values, dict):
            result.match.update(match_values)

        warnings = output.get("warnings", [])
        if isinstance(warnings, list):
            result.warnings.extend(str(item) for item in warnings)

        errors = output.get("errors", [])
        if isinstance(errors, list):
            result.errors.extend(str(item) for item in errors)

        status = output.get("status")
        if status in {"ok", "partial", "invalid"}:
            result.status = status


parser_service = ParserService(handler_registry)
