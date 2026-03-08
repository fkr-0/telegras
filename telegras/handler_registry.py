from __future__ import annotations

import importlib
import inspect
import logging
from dataclasses import dataclass
from typing import Any, Callable, Sequence

log = logging.getLogger("telegras.handler_registry")


@dataclass
class RegisteredHandler:
    name: str
    handler: Callable[..., Any]
    matcher: Any | None = None
    parser: Any | None = None
    description: str | None = None


@dataclass
class RegisteredParser:
    name: str
    parser: Callable[..., Any]
    description: str | None = None


@dataclass
class HandlerExecutionResult:
    """Normalized execution record returned by :class:`HandlerExecutor`.

    Inputs are the resolved execution context and the already rendered argument list.
    The output mirrors the JSON payload emitted by the webhook execution endpoint.
    """

    handler: str
    rendered_args: list[Any]
    ok: bool
    result: Any | None = None
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "handler": self.handler,
            "rendered_args": self.rendered_args,
            "ok": self.ok,
            "result": self.result,
            "error": self.error,
        }


_handler_plugins: list[Callable[[], dict[str, Callable[..., Any]]]] = []
_direct_handler_plugins: dict[str, RegisteredHandler] = {}
_direct_parser_plugins: dict[str, RegisteredParser] = {}
_plugin_revision = 0
_defaults_bootstrapped = False


def _bump_plugin_revision() -> None:
    global _plugin_revision
    _plugin_revision += 1


def _bootstrap_default_plugins() -> None:
    global _defaults_bootstrapped
    if _defaults_bootstrapped:
        return
    importlib.import_module("telegras.default_handlers")
    _defaults_bootstrapped = True


def register_handler_plugin(
    plugin: Callable[[], dict[str, Callable[..., Any]]],
) -> Callable[[], dict[str, Callable[..., Any]]]:
    _handler_plugins.append(plugin)
    _bump_plugin_revision()
    return plugin


def register_handler_definition(
    name: str,
    handler: Callable[..., Any],
    *,
    matcher: Any | None = None,
    parser: Any | None = None,
    description: str | None = None,
) -> Callable[..., Any]:
    _direct_handler_plugins[name] = RegisteredHandler(
        name=name,
        handler=handler,
        matcher=matcher,
        parser=parser,
        description=description,
    )
    _bump_plugin_revision()
    return handler


def register_parser_definition(
    name: str,
    parser: Callable[..., Any],
    *,
    description: str | None = None,
) -> Callable[..., Any]:
    _direct_parser_plugins[name] = RegisteredParser(
        name=name,
        parser=parser,
        description=description,
    )
    _bump_plugin_revision()
    return parser


def handler_plugin(
    func_or_name: Callable[[], dict[str, Callable[..., Any]]] | str | None = None,
    *,
    matcher: Any | None = None,
    parser: Any | None = None,
    description: str | None = None,
):
    """Register either a legacy handler map plugin or a direct decorated handler.

    Legacy usage::

        @handler_plugin
        def plugin() -> dict[str, Callable[..., Any]]:
            return {"handlers.foo:bar": bar}

    Decorator usage::

        @handler_plugin("handlers.foo:bar", parser="parsers.foo:extract")
        def bar(context, *args):
            ...
    """

    if callable(func_or_name) and matcher is None and parser is None and description is None:
        return register_handler_plugin(func_or_name)

    explicit_name = func_or_name if isinstance(func_or_name, str) else None

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        name = explicit_name or f"{func.__module__}:{func.__name__}"
        register_handler_definition(
            name,
            func,
            matcher=matcher,
            parser=parser,
            description=description,
        )
        return func

    return decorator


def parser_plugin(
    func_or_name: Callable[..., Any] | str | None = None,
    *,
    description: str | None = None,
):
    """Register a decorated parser plugin."""

    if callable(func_or_name) and description is None:
        name = f"{func_or_name.__module__}:{func_or_name.__name__}"
        register_parser_definition(name, func_or_name)
        return func_or_name

    explicit_name = func_or_name if isinstance(func_or_name, str) else None

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        name = explicit_name or f"{func.__module__}:{func.__name__}"
        register_parser_definition(name, func, description=description)
        return func

    return decorator


class HandlerRegistry:
    def __init__(self) -> None:
        self._default_handlers: dict[str, Callable[..., Any]] = {}
        self._default_handler_defs: dict[str, RegisteredHandler] = {}
        self._default_parsers: dict[str, Callable[..., Any]] = {}
        self._default_parser_defs: dict[str, RegisteredParser] = {}
        self._custom_handlers: dict[str, Callable[..., Any]] = {}
        self._custom_handler_defs: dict[str, RegisteredHandler] = {}
        self._custom_parsers: dict[str, Callable[..., Any]] = {}
        self._custom_parser_defs: dict[str, RegisteredParser] = {}
        self._handlers: dict[str, Callable[..., Any]] = {}
        self._handler_defs: dict[str, RegisteredHandler] = {}
        self._parsers: dict[str, Callable[..., Any]] = {}
        self._parser_defs: dict[str, RegisteredParser] = {}
        self._loaded_revision = -1

    def _refresh_maps(self) -> None:
        self._handlers = {**self._default_handlers, **self._custom_handlers}
        self._handler_defs = {**self._default_handler_defs, **self._custom_handler_defs}
        self._parsers = {**self._default_parsers, **self._custom_parsers}
        self._parser_defs = {**self._default_parser_defs, **self._custom_parser_defs}

    def _rebuild_defaults(self) -> None:
        self._default_handlers = {}
        self._default_handler_defs = {}
        self._default_parsers = {}
        self._default_parser_defs = {}

        for plugin in _handler_plugins:
            try:
                for name, handler in plugin().items():
                    self._default_handlers[name] = handler
                    self._default_handler_defs[name] = RegisteredHandler(
                        name=name,
                        handler=handler,
                    )
            except Exception:
                log.exception("Handler plugin failed, skipping")

        for entry in _direct_handler_plugins.values():
            self._default_handlers[entry.name] = entry.handler
            self._default_handler_defs[entry.name] = entry

        for entry in _direct_parser_plugins.values():
            self._default_parsers[entry.name] = entry.parser
            self._default_parser_defs[entry.name] = entry

        self._loaded_revision = _plugin_revision
        self._refresh_maps()

    def _ensure_defaults(self) -> None:
        _bootstrap_default_plugins()
        if self._loaded_revision != _plugin_revision:
            self._rebuild_defaults()

    def register_handler(
        self,
        name: str,
        handler: Callable[..., Any],
        *,
        matcher: Any | None = None,
        parser: Any | None = None,
        description: str | None = None,
    ) -> None:
        self._ensure_defaults()
        self._custom_handlers[name] = handler
        self._custom_handler_defs[name] = RegisteredHandler(
            name=name,
            handler=handler,
            matcher=matcher,
            parser=parser,
            description=description,
        )
        self._refresh_maps()

    def register_parser(
        self,
        name: str,
        parser: Callable[..., Any],
        *,
        description: str | None = None,
    ) -> None:
        self._ensure_defaults()
        self._custom_parsers[name] = parser
        self._custom_parser_defs[name] = RegisteredParser(
            name=name,
            parser=parser,
            description=description,
        )
        self._refresh_maps()

    def register_plugin(
        self, plugin: Callable[[], dict[str, Callable[..., Any]]]
    ) -> Callable[[], dict[str, Callable[..., Any]]]:
        register_handler_plugin(plugin)
        self._loaded_revision = -1
        return plugin

    def get_handler_definition(self, handler_name: str) -> RegisteredHandler:
        self._ensure_defaults()
        entry = self._handler_defs.get(handler_name)
        if entry is not None:
            return entry
        handler = self.get_handler(handler_name)
        return RegisteredHandler(name=handler_name, handler=handler)

    def get_handler(self, handler_name: str) -> Callable[..., Any]:
        self._ensure_defaults()
        handler = self._handlers.get(handler_name)
        if handler is not None:
            return handler

        module_name, _, symbol = handler_name.partition(":")
        if not module_name or not symbol:
            raise ValueError(f"Invalid handler '{handler_name}'")

        module = importlib.import_module(module_name)
        handler = getattr(module, symbol, None)
        if handler is None:
            raise ValueError(f"Handler not found: {handler_name}")
        return handler

    def get_parser(self, parser_name: str) -> Callable[..., Any]:
        self._ensure_defaults()
        parser = self._parsers.get(parser_name)
        if parser is not None:
            return parser

        module_name, _, symbol = parser_name.partition(":")
        if not module_name or not symbol:
            raise ValueError(f"Invalid parser '{parser_name}'")

        module = importlib.import_module(module_name)
        parser = getattr(module, symbol, None)
        if parser is None:
            raise ValueError(f"Parser not found: {parser_name}")
        return parser


class HandlerExecutor:
    def __init__(self, registry: HandlerRegistry) -> None:
        self._registry = registry

    async def execute(
        self,
        handler_name: str,
        context: dict[str, Any],
        rendered_args: Sequence[Any],
    ) -> HandlerExecutionResult:
        """Execute one handler with a prepared context and rendered argument list.

        Args:
            handler_name: Registry key or ``module:symbol`` reference.
            context: Execution context assembled from the Telegram update.
            rendered_args: Positional arguments after template rendering.

        Returns:
            HandlerExecutionResult: normalized output with ``ok/result/error`` fields.
        """
        try:
            handler = self._registry.get_handler(handler_name)
            result = handler(context, *rendered_args)
            if inspect.isawaitable(result):
                result = await result
            return HandlerExecutionResult(
                handler=handler_name,
                rendered_args=list(rendered_args),
                ok=True,
                result=result,
                error=None,
            )
        except Exception as exc:  # pragma: no cover - executor should not explode the API surface
            return HandlerExecutionResult(
                handler=handler_name,
                rendered_args=list(rendered_args),
                ok=False,
                result=None,
                error=str(exc),
            )


handler_registry = HandlerRegistry()
handler_executor = HandlerExecutor(handler_registry)


def resolve_handler(handler_name: str) -> Callable[..., Any]:
    return handler_registry.get_handler(handler_name)
