"""Tests for sync helpers."""

from __future__ import annotations

import yaml

from ytscriber.models import VideoMetadata
from ytscriber.sync import load_channels_config, sync_all_channels


def test_load_channels_config(tmp_path):
    channels_file = tmp_path / "channels.yaml"
    channels_file.write_text(
        yaml.safe_dump(
            {
                "channels": [
                    {"folder": "a16z", "url": "https://example.com", "count": 1}
                ]
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    channels = load_channels_config(channels_file)
    assert len(channels) == 1
    assert channels[0]["folder"] == "a16z"


def test_sync_all_channels(monkeypatch, tmp_path):
    channels_file = tmp_path / "channels.yaml"
    channels_file.write_text(
        yaml.safe_dump(
            {
                "channels": [
                    {"folder": "enabled", "url": "https://example.com", "count": 1},
                    {"folder": "disabled", "url": "https://example.com", "enabled": False},
                ]
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    class DummyExtractor:
        def extract_videos(self, channel_url, max_videos=None):
            return [
                VideoMetadata(
                    video_id="abc123xyz45",
                    url="https://www.youtube.com/watch?v=abc123xyz45",
                )
            ]

    calls = []

    def fake_append(csv_path, videos):
        calls.append((csv_path, videos))

    monkeypatch.setattr("ytscriber.sync.ChannelExtractor", DummyExtractor)
    monkeypatch.setattr("ytscriber.sync.append_videos_to_csv", fake_append)

    progress = sync_all_channels(
        channels_file=channels_file,
        data_dir=tmp_path,
        delay=0,
        quiet=True,
    )

    assert progress.success == 1
    assert progress.skipped == 1
    assert progress.errors == 0
    assert progress.processed == 2
    assert calls
