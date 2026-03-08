# telegras handler and parser plugin flow

## Describe `handler_registry.handler_registry`

The module `telegras.handler_registry` exports a singleton registry instance named `handler_registry`.
That object keeps four layers of state:

1. module-level plugin declarations collected by decorators like `@handler_plugin(...)` and `@parser_plugin(...)`
2. default maps materialized from those declarations the first time the registry is asked for a handler or parser
3. per-process runtime registrations added with `handler_registry.register_handler(...)` or `handler_registry.register_parser(...)`
4. merged lookup maps used by execution

The cache is revision-based, not just a one-shot boolean anymore.
Whenever a plugin is registered, the global plugin revision increments.
On the next lookup, the singleton rebuilds its default handler/parser maps and then overlays any runtime registrations.
That fixes the old trap where `register_plugin()` could append a plugin but the already-cached default handler map never refreshed.

### `HandlerExecutor.execute`

Inputs:

- `handler_name`: registry key like `handlers.python:eval` or a fallback `module:symbol`
- `context`: the rendered webhook context, including `message`, `chat`, `update`, and `match`
- `rendered_args`: already-templated positional arguments

Output structure:

- `handler`: the resolved handler name
- `rendered_args`: the concrete argument list handed to the handler
- `ok`: boolean success flag
- `result`: handler return value on success
- `error`: stringified exception on failure

### plugin registration hooks

- `handler_registry.register_plugin(...)` registers a legacy plugin factory that returns `{name: callable}`
- `@handler_plugin("name")` registers a concrete handler function directly
- `@handler_plugin` without arguments still supports the legacy plugin-factory style

That gives telegras both compatibility and a decorator-first extension style.

## Explain ParserService

`ParserService.parse(spec, context, update)` accepts:

- an optional `ParseSpec`
- the base webhook context
- the current Telegram update object

It returns `ParserResult(status, match, warnings, errors)`.

### `ParseMode` semantics

`ParseMode` is enforced in webhook attachment execution:

- `warn`: parsing problems are reported in `parse.warnings` or `parse.errors`, but handlers still run
- `ignore`: parsing metadata is still computed, but callers should treat parser failures as non-blocking
- `strict`: an `invalid` parser result aborts execution before any handler is called

In strict mode the execution record comes back with `ok = false`, an empty `handler_executions` list, and the error `Parser invalid in strict mode`.

### parser plugins

Parser plugins are registered through the same singleton registry, but through parser-specific entry points:

- `handler_registry.register_parser(name, func)` for runtime registration
- `@parser_plugin("name")` for module-level decorator registration

`ParserService` resolves `spec.parser_ref` through `handler_registry.get_parser(...)`, not through the handler map.
That separation makes parser signatures explicit and avoids the old “parsers are secretly handlers” confusion.

## Link default handler/plugin flow

Default handlers live in `telegras.default_handlers` and are registered with `@handler_plugin(...)`.
Default parsers in the same module use `@parser_plugin(...)`.

On first access, `HandlerRegistry` bootstraps `telegras.default_handlers`, which executes those decorators and fills the global plugin declarations.
The registry then builds a single merged handler/parser map, so every attachment lookup resolves against the same canonical registry state.

Additional plugins should follow the same pattern:

    from telegras.handler_registry import handler_plugin, parser_plugin

    @parser_plugin("parsers.example:suffix")
    def parse_suffix(context, update):
        return {"status": "ok", "match": {"suffix": "done"}}

    @handler_plugin("handlers.example:echo")
    def echo(context, *args):
        return {"args": list(args), "match": context.get("match", {})}

That is the clean path now: decorators for default/static plugins, runtime registration for tests or dynamic modules, and one registry responsible for merging both.
