"""Initialization helpers for ytscriber."""

from __future__ import annotations

from ytscriber.config import default_config, load_config, normalize_config, read_config, save_config
from ytscriber.paths import ensure_data_structure


def ensure_initialized() -> dict:
    """Ensure directories and config exist, returning current config."""
    ensure_data_structure()

    config = read_config()
    if config is None:
        config = default_config()
        save_config(config)
        return config

    updated = check_for_updates()
    return updated if updated is not None else load_config()


def check_for_updates() -> dict | None:
    """Update config file if schema version has changed."""
    config = read_config()
    if config is None:
        return None

    version = config.get("version")
    if version != default_config().get("version"):
        updated = normalize_config(config)
        save_config(updated)
        return updated

    return None
