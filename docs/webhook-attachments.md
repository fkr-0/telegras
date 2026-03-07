# Webhook Matchers and Handlers

`telegras` uses **webhook attachments** to decide what to do with each incoming Telegram update.

An attachment combines:

- `when`: match criteria expression
- `parse` (optional): parse/extract structured values from message text
- handler binding: `handler` or `handler_chain` + `handler_args`
- execution controls: priority, enabled flag, execution mode

## Mental model

1. Update arrives.
2. Attachment matcher (`when`) is evaluated.
3. If matched, optional parser runs and emits `match.*` values.
4. Bound handler(s) execute with rendered args.
5. Execution result is persisted and visible via introspection endpoints.

## Match expression (`when`)

Use composable boolean expressions:

- `leaf`: one condition
- `all`: logical AND over children
- `any`: logical OR over children
- `not`: negation over one child

Example:

```json
{
  "op": "all",
  "children": [
    {"op": "leaf", "leaf": {"field": "chat.type", "match": "eq", "value": "group"}},
    {"op": "leaf", "leaf": {"field": "message.text", "match": "contains", "value": "urgent"}}
  ]
}
```

## Handlers

Single handler:

```json
{
  "handler": "handlers.shell:sh",
  "handler_args": ["echo {{ message.title }}"]
}
```

Grouped handler chain:

```json
{
  "handler_chain": [
    {"handler": "handlers.python:eval", "handler_args": ["title='{{ message.title }}'"]},
    {"handler": "handlers.shell:ls", "handler_args": ["/tmp"]}
  ],
  "execution_mode": "sequential",
  "stop_on_error": true
}
```

## Parser output and templates

Attachment parsers can enrich context with extracted fields available as `{{ match.<name> }}`.

Example parser:

```json
{
  "parse": {
    "regex": {
      "title": "^(?P<title>[^\\n]+)",
      "tag": "#(?P<tag>[a-z0-9_-]+)"
    },
    "allow_partial": true
  },
  "parse_mode": "warn"
}
```

Then use:

- `{{ match.title }}`
- `{{ match.tag }}`

Built-in template values also include `message.*`, `chat.*`, and `update.*`.

## Minimal full attachment example

```json
{
  "name": "ops-alert",
  "handler": "handlers.python:eval",
  "handler_args": ["result='{{ match.title }}'"],
  "enabled": true,
  "priority": 20,
  "when": {
    "op": "all",
    "children": [
      {"op": "leaf", "leaf": {"field": "chat.type", "match": "eq", "value": "group"}},
      {"op": "leaf", "leaf": {"field": "message.text", "match": "regex", "value": "#ops"}}
    ]
  },
  "parse": {"regex": {"title": "^(?P<title>[^\\n]+)"}},
  "parse_mode": "warn"
}
```

## APIs

- Public attachment APIs:
  - `GET /v1/webhook-attachments`
  - `POST /v1/webhook-attachments`
  - `DELETE /v1/webhook-attachments/{name}`
  - `POST /v1/webhook-attachments/match`
  - `POST /v1/webhook-attachments/execute`
- Introspection helper:
  - `GET /internal/introspection/match-criteria`
