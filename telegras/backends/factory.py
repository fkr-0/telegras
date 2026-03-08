from __future__ import annotations

from importlib import import_module
import os

from telegras.contracts import PublishBackend

AVAILABLE_BACKENDS: dict[str, str | type[PublishBackend]] = {}


def _load_backend_class(entry: str | type[PublishBackend]) -> type[PublishBackend]:
    if isinstance(entry, type):
        return entry

    module_path, _, symbol = entry.partition(":")
    if not module_path or not symbol:
        raise ValueError(f"Invalid backend entry '{entry}'")

    module = import_module(module_path)
    backend_cls = getattr(module, symbol)
    if not isinstance(backend_cls, type):
        raise TypeError(f"Backend '{entry}' did not resolve to a class")
    return backend_cls


def parse_backend_names(config_value: str | None) -> list[str]:
    raw = (
        config_value
        if config_value is not None
        else os.getenv("TELEGRAS_BACKENDS", "")
    )
    names = [item.strip() for item in raw.split(",") if item.strip()]
    return names


def build_backends(config_value: str | None = None) -> list[PublishBackend]:
    names = parse_backend_names(config_value)
    backends: list[PublishBackend] = []
    for name in names:
        backend_entry = AVAILABLE_BACKENDS.get(name)
        if backend_entry is None:
            known = ", ".join(sorted(AVAILABLE_BACKENDS))
            raise ValueError(f"Unknown backend '{name}'. Available: {known}")
        backend_cls = _load_backend_class(backend_entry)
        backends.append(backend_cls())
    return backends
