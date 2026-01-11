"""Path helpers for ytscriber data and config locations."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml
from platformdirs import user_config_dir, user_documents_path

APP_NAME = "ytscriber"
DOCUMENTS_DATA_DIR = "YTScriber"
LINUX_DATA_DIR = "ytscriber"
DEFAULT_COLLECTION = "ad-hoc-downloads"


def get_data_dir() -> Path:
    """Return the cross-platform data directory."""
    if sys.platform.startswith("linux"):
        return Path.home() / LINUX_DATA_DIR
    return user_documents_path() / DOCUMENTS_DATA_DIR


def get_config_dir() -> Path:
    """Return the cross-platform config directory."""
    return Path(user_config_dir(APP_NAME))


def get_channels_file() -> Path:
    """Return the channels configuration file path."""
    return get_data_dir() / "channels.yaml"


def get_default_collection_dir() -> Path:
    """Return the default collection directory for ad-hoc downloads."""
    return get_data_dir() / DEFAULT_COLLECTION


def ensure_data_structure() -> None:
    """Ensure base data/config directories and channels.yaml exist."""
    data_dir = get_data_dir()
    config_dir = get_config_dir()

    data_dir.mkdir(parents=True, exist_ok=True)
    config_dir.mkdir(parents=True, exist_ok=True)
    default_collection_dir = get_default_collection_dir()
    default_collection_dir.mkdir(parents=True, exist_ok=True)
    (default_collection_dir / "transcripts").mkdir(parents=True, exist_ok=True)

    channels_file = get_channels_file()
    if not channels_file.exists():
        default_channels = {
            "channels": [],
            "collections": [],
        }
        channels_file.write_text(
            yaml.safe_dump(default_channels, sort_keys=False),
            encoding="utf-8",
        )
