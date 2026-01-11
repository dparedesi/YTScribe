"""Sync channel videos from channels.yaml."""

from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from ytscriber.csv_handler import append_videos_to_csv
from ytscriber.exceptions import ChannelExtractionError
from ytscriber.extractor import ChannelExtractor
from ytscriber.logging_config import get_logger

logger = get_logger("sync")


@dataclass
class SyncProgress:
    """Progress tracking for channel sync."""

    total: int
    processed: int = 0
    success: int = 0
    skipped: int = 0
    errors: int = 0


def load_channels_config(channels_file: Path) -> list[dict[str, Any]]:
    """Load channels list from channels.yaml."""
    if not channels_file.exists():
        raise FileNotFoundError(f"Channels file not found: {channels_file}")

    data = yaml.safe_load(channels_file.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        channels = data.get("channels", [])
    elif isinstance(data, list):
        channels = data
    else:
        channels = []

    return [channel for channel in channels if isinstance(channel, dict)]


def sync_all_channels(
    channels_file: Path,
    data_dir: Path,
    delay: float = 10.0,
    quiet: bool = False,
) -> SyncProgress:
    """Sync all enabled channels from config."""
    channels = load_channels_config(channels_file)
    progress = SyncProgress(total=len(channels))
    extractor = ChannelExtractor()

    for index, channel in enumerate(channels, 1):
        enabled = channel.get("enabled", True)
        folder = channel.get("folder")
        url = channel.get("url")
        count = channel.get("count")

        if not enabled:
            progress.skipped += 1
            progress.processed += 1
            if not quiet:
                logger.info(f"[{index}/{progress.total}] Skipping (disabled): {folder}")
            continue

        if not folder or not url:
            progress.errors += 1
            progress.processed += 1
            logger.warning(f"[{index}/{progress.total}] Missing folder or URL")
            continue

        if not quiet:
            logger.info(f"[{index}/{progress.total}] Syncing: {folder}")

        target_dir = data_dir / folder
        target_dir.mkdir(parents=True, exist_ok=True)

        try:
            videos = extractor.extract_videos(url, max_videos=count)
            append_videos_to_csv(str(target_dir / "videos.csv"), videos)
            progress.success += 1
        except ChannelExtractionError as e:
            progress.errors += 1
            logger.warning(f"Failed to sync {folder}: {e}")
        except Exception as e:
            progress.errors += 1
            logger.warning(f"Unexpected error for {folder}: {e}")

        progress.processed += 1

        if delay > 0 and index < progress.total:
            time.sleep(delay)

    return progress
