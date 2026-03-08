from __future__ import annotations

import importlib
from pathlib import Path

from fastapi.testclient import TestClient

from telegras.update_model import TelegramUpdate
from telegras.handler_registry import handler_registry
from telegras.webhook_attachments import (
    Attachment,
    FieldName,
    MatchOp,
    RuleExpr,
    WebhookAttachmentRegistry,
)


def _build_app(monkeypatch, tmp_path: Path):
    db_path = tmp_path / "telegras_webhook_attachments.db"
    monkeypatch.setenv("TELEGRAS_DATABASE_URL", f"sqlite+aiosqlite:///{db_path}")

    db_module = importlib.import_module("telegras.persistence.db")
    app_module = importlib.import_module("telegras.app")
    importlib.reload(db_module)
    app_module = importlib.reload(app_module)
    app_module._db_initialized = False

    return app_module.create_app()


def _text_regex_rule(pattern: str) -> RuleExpr:
    return RuleExpr.make_leaf(
        field=FieldName.MESSAGE_TEXT,
        match=MatchOp.REGEX,
        value=pattern,
    )


def test_registry_register_list_unregister() -> None:
    registry = WebhookAttachmentRegistry()
    attachment = Attachment(
        name="blog-channel",
        handler="handlers.wordpress:publish_post",
        when=RuleExpr.all_of(
            [
                RuleExpr.make_leaf(
                    field=FieldName.CHAT_TYPE,
                    match=MatchOp.EQ,
                    value="channel",
                ),
                _text_regex_rule(r"#blog\\b"),
            ]
        ),
    )

    registry.register(attachment)
    listed = registry.list_attachments()

    assert len(listed) == 1
    assert listed[0].name == "blog-channel"
    assert listed[0].handler == "handlers.wordpress:publish_post"

    removed = registry.unregister("blog-channel")
    assert removed is True
    assert registry.list_attachments() == []


def test_registry_match_attachments_composable_rules() -> None:
    registry = WebhookAttachmentRegistry()
    registry.register(
        Attachment(
            name="video-channel",
            handler="handlers.wordpress:publish_video",
            when=RuleExpr.all_of(
                [
                    RuleExpr.make_leaf(
                        field=FieldName.CHAT_TYPE,
                        match=MatchOp.EQ,
                        value="channel",
                    ),
                    RuleExpr.make_leaf(
                        field=FieldName.MESSAGE_HAS_MEDIA,
                        match=MatchOp.EQ,
                        value=True,
                    ),
                    RuleExpr.make_leaf(
                        field=FieldName.MESSAGE_MEDIA_TYPE,
                        match=MatchOp.IN,
                        value=["video", "animation"],
                    ),
                ]
            ),
        )
    )

    update = TelegramUpdate(
        update_id=77,
        channel_post={
            "message_id": 1,
            "date": 1700000000,
            "chat": {"id": 123, "type": "channel"},
            "caption": "new clip",
            "video": {
                "file_id": "abc",
                "file_unique_id": "unique-abc",
                "width": 1280,
                "height": 720,
                "duration": 60,
            },
        },
    )

    matched = registry.match_attachments(update)

    assert [item.name for item in matched] == ["video-channel"]


def test_api_register_list_unregister_and_match(monkeypatch, tmp_path: Path) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    payload = {
        "name": "group-alert",
        "handler": "handlers.alerts:send",
        "when": {
            "op": "all",
            "children": [
                {
                    "op": "leaf",
                    "leaf": {
                        "field": "chat.type",
                        "match": "eq",
                        "value": "group",
                    },
                },
                {
                    "op": "leaf",
                    "leaf": {
                        "field": "message.text",
                        "match": "contains",
                        "value": "urgent",
                    },
                },
            ],
        },
    }

    register_resp = client.post("/v1/webhook-attachments", json=payload)
    assert register_resp.status_code == 200

    list_resp = client.get("/v1/webhook-attachments")
    assert list_resp.status_code == 200
    listed = list_resp.json()
    row = next(item for item in listed if item["name"] == "group-alert")
    assert row["handler"] == "handlers.alerts:send"

    match_resp = client.post(
        "/v1/webhook-attachments/match",
        json={
            "update": {
                "update_id": 999,
                "message": {
                    "message_id": 11,
                    "date": 1700000000,
                    "chat": {"id": 999, "type": "group"},
                    "text": "urgent: please check",
                },
            }
        },
    )
    assert match_resp.status_code == 200
    assert "group-alert" in match_resp.json()

    del_resp = client.delete("/v1/webhook-attachments/group-alert")
    assert del_resp.status_code == 200
    assert del_resp.json() == {"removed": True}


def test_api_register_supports_handler_args(monkeypatch, tmp_path: Path) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    payload = {
        "name": "list-temp",
        "handler": "handlers.shell:ls",
        "handler_args": ["/tmp"],
        "when": {
            "op": "leaf",
            "leaf": {
                "field": "chat.type",
                "match": "eq",
                "value": "group",
            },
        },
    }

    register_resp = client.post("/v1/webhook-attachments", json=payload)
    assert register_resp.status_code == 200
    assert register_resp.json()["handler_args"] == ["/tmp"]


def test_api_execute_runs_default_handler_with_templated_args(
    monkeypatch, tmp_path: Path
) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    register_resp = client.post(
        "/v1/webhook-attachments",
        json={
            "name": "python-eval",
            "handler": "handlers.python:eval",
            "handler_args": ["result = '{{ message.title }}'"],
            "when": {
                "op": "leaf",
                "leaf": {
                    "field": "chat.type",
                    "match": "eq",
                    "value": "group",
                },
            },
        },
    )
    assert register_resp.status_code == 200

    execute_resp = client.post(
        "/v1/webhook-attachments/execute",
        json={
            "update": {
                "update_id": 10001,
                "message": {
                    "message_id": 33,
                    "date": 1700000000,
                    "chat": {"id": 444, "type": "group", "title": "Ops"},
                    "text": "Status report\nEverything looks green.",
                },
            }
        },
    )

    assert execute_resp.status_code == 200
    payload = execute_resp.json()
    row = next(item for item in payload if item["attachment"] == "python-eval")
    assert row["handler"] == "handlers.python:eval"
    assert row["rendered_args"] == ["result = 'Status report'"]
    assert row["result"]["locals"]["result"] == "Status report"


def test_api_execute_runs_shell_sh_handler(monkeypatch, tmp_path: Path) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    register_resp = client.post(
        "/v1/webhook-attachments",
        json={
            "name": "shell-sh",
            "handler": "handlers.shell:sh",
            "handler_args": ["echo telegras-ok"],
            "when": {
                "op": "leaf",
                "leaf": {
                    "field": "chat.type",
                    "match": "eq",
                    "value": "group",
                },
            },
        },
    )
    assert register_resp.status_code == 200

    execute_resp = client.post(
        "/v1/webhook-attachments/execute",
        json={
            "update": {
                "update_id": 10002,
                "message": {
                    "message_id": 34,
                    "date": 1700000000,
                    "chat": {"id": 555, "type": "group"},
                    "text": "run",
                },
            }
        },
    )
    assert execute_resp.status_code == 200
    payload = execute_resp.json()
    row = next(item for item in payload if item["attachment"] == "shell-sh")
    assert row["handler"] == "handlers.shell:sh"
    assert row["ok"] is True
    assert row["result"]["returncode"] == 0
    assert row["result"]["stdout"].strip() == "telegras-ok"


def test_parse_mode_strict_blocks_when_parser_invalid(
    monkeypatch, tmp_path: Path
) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    parser_name = "tests.test_webhook_attachments:failing_parser"

    def failing_parser(context, update):
        raise RuntimeError("parse failure")

    handler_registry.register_parser(parser_name, failing_parser)

    register_resp = client.post(
        "/v1/webhook-attachments",
        json={
            "name": "strict-parser",
            "handler": "handlers.shell:sh",
            "handler_args": ["echo hi"],
            "parse": {"parser_ref": parser_name},
            "parse_mode": "strict",
            "when": {
                "op": "leaf",
                "leaf": {
                    "field": "chat.type",
                    "match": "eq",
                    "value": "group",
                },
            },
        },
    )
    assert register_resp.status_code == 200

    execute_resp = client.post(
        "/v1/webhook-attachments/execute",
        json={
            "update": {
                "update_id": 10003,
                "message": {
                    "message_id": 99,
                    "date": 1700000000,
                    "chat": {"id": 999, "type": "group"},
                    "text": "test",
                },
            }
        },
    )
    assert execute_resp.status_code == 200
    payload = execute_resp.json()
    row = next(item for item in payload if item["attachment"] == "strict-parser")
    assert row["ok"] is False
    assert row["error"] == "Parser invalid in strict mode"
    assert row["handler_executions"] == []

    handler_registry._parsers.pop(parser_name, None)


def test_parser_ref_plugins_merge_match(monkeypatch, tmp_path: Path) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    parser_name = "tests.test_webhook_attachments:match_parser"

    def match_parser(context, update):
        return {"status": "ok", "match": {"parsed": "value"}}

    handler_registry.register_parser(parser_name, match_parser)

    register_resp = client.post(
        "/v1/webhook-attachments",
        json={
            "name": "parser-match",
            "handler": "handlers.python:eval",
            "handler_args": ["result = '{{ match.parsed }}'"],
            "parse": {"parser_ref": parser_name},
            "when": {
                "op": "leaf",
                "leaf": {
                    "field": "chat.type",
                    "match": "eq",
                    "value": "group",
                },
            },
        },
    )
    assert register_resp.status_code == 200

    execute_resp = client.post(
        "/v1/webhook-attachments/execute",
        json={
            "update": {
                "update_id": 10004,
                "message": {
                    "message_id": 106,
                    "date": 1700000000,
                    "chat": {"id": 888, "type": "group"},
                    "text": "test",
                },
            }
        },
    )
    assert execute_resp.status_code == 200
    payload = execute_resp.json()
    row = next(item for item in payload if item["attachment"] == "parser-match")
    assert row["ok"] is True
    assert row["handler_executions"][0]["result"]["locals"]["result"] == "value"

    handler_registry._parsers.pop(parser_name, None)



def test_handler_registry_register_plugin_invalidates_default_cache() -> None:
    handler_registry.get_handler("handlers.shell:ls")

    def plugin_echo(context, *args):
        return {"echo": list(args), "chat_type": context.get("chat", {}).get("type")}

    handler_registry.register_plugin(lambda: {"tests.plugins:echo": plugin_echo})

    resolved = handler_registry.get_handler("tests.plugins:echo")
    assert resolved is plugin_echo

    handler_registry._handlers.pop("tests.plugins:echo", None)


def test_default_parser_plugin_populates_match_context(
    monkeypatch,
    tmp_path: Path,
) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    register_resp = client.post(
        "/v1/webhook-attachments",
        json={
            "name": "default-parser",
            "handler": "handlers.python:eval",
            "handler_args": [
                "result = {'title': '{{ match.title }}', 'body': '{{ match.body }}'}"
            ],
            "parse": {"parser_ref": "parsers.message:text_parts"},
            "when": {
                "op": "leaf",
                "leaf": {
                    "field": "chat.type",
                    "match": "eq",
                    "value": "group",
                },
            },
        },
    )
    assert register_resp.status_code == 200

    execute_resp = client.post(
        "/v1/webhook-attachments/execute",
        json={
            "update": {
                "update_id": 10005,
                "message": {
                    "message_id": 107,
                    "date": 1700000000,
                    "chat": {"id": 889, "type": "group"},
                    "text": "Release note\nAll systems nominal.",
                },
            }
        },
    )
    assert execute_resp.status_code == 200
    payload = execute_resp.json()
    row = next(item for item in payload if item["attachment"] == "default-parser")
    assert row["ok"] is True
    assert row["parse"]["match"]["title"] == "Release note"
    assert row["parse"]["match"]["body"] == "All systems nominal."
    assert row["handler_executions"][0]["result"]["locals"]["result"] == {
        "title": "Release note",
        "body": "All systems nominal.",
    }


def test_parser_service_merges_regex_and_registered_parser_match(
    monkeypatch,
    tmp_path: Path,
) -> None:
    app = _build_app(monkeypatch, tmp_path)
    client = TestClient(app)

    parser_name = "tests.test_webhook_attachments:registered_parser"

    def registered_parser(context, update):
        return {"status": "ok", "match": {"suffix": "done"}}

    handler_registry.register_parser(parser_name, registered_parser)

    register_resp = client.post(
        "/v1/webhook-attachments",
        json={
            "name": "parser-merge",
            "handler": "handlers.python:eval",
            "handler_args": [
                "result = '{{ match.title }} {{ match.suffix }}'"
            ],
            "parse": {
                "regex": {"title": "^(?P<title>[^\n]+)"},
                "parser_ref": parser_name,
            },
            "when": {
                "op": "leaf",
                "leaf": {
                    "field": "chat.type",
                    "match": "eq",
                    "value": "group",
                },
            },
        },
    )
    assert register_resp.status_code == 200

    execute_resp = client.post(
        "/v1/webhook-attachments/execute",
        json={
            "update": {
                "update_id": 10006,
                "message": {
                    "message_id": 108,
                    "date": 1700000000,
                    "chat": {"id": 890, "type": "group"},
                    "text": "Ship it\nthat is all",
                },
            }
        },
    )
    assert execute_resp.status_code == 200
    payload = execute_resp.json()
    row = next(item for item in payload if item["attachment"] == "parser-merge")
    assert row["parse"]["match"] == {"title": "Ship it", "suffix": "done"}
    assert row["handler_executions"][0]["result"]["locals"]["result"] == "Ship it done"

    handler_registry._parsers.pop(parser_name, None)
