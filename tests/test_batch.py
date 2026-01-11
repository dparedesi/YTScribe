"""Tests for batch downloads."""

from __future__ import annotations

import csv

from ytscriber.batch import download_from_csv, find_video_csv_files
from ytscriber.models import DownloadStatus, TranscriptResult, VideoMetadata


def test_find_video_csv_files(tmp_path):
    (tmp_path / "a").mkdir()
    (tmp_path / "b").mkdir()
    (tmp_path / "a" / "videos.csv").write_text("url\n", encoding="utf-8")
    (tmp_path / "b" / "videos.csv").write_text("url\n", encoding="utf-8")

    csv_files = find_video_csv_files(tmp_path)
    assert len(csv_files) == 2
    assert csv_files[0].name == "videos.csv"


def test_download_from_csv(monkeypatch, tmp_path):
    csv_path = tmp_path / "videos.csv"
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["url", "transcript_downloaded"])
        writer.writeheader()
        writer.writerow({"url": "https://www.youtube.com/watch?v=abc123xyz45"})
        writer.writerow({"url": ""})

    output_dir = tmp_path / "transcripts"

    class DummyDownloader:
        def __init__(self, languages=None, delay=0.0, output_dir=None):
            self.languages = languages
            self.delay = delay
            self.output_dir = output_dir

        def download(self, video_id, video_url=None, output_file=None, apply_delay=False):
            metadata = VideoMetadata(
                video_id=video_id,
                url=video_url or f"https://www.youtube.com/watch?v={video_id}",
                title="Test Video",
                duration_minutes=1.5,
                view_count=100,
                published_date="2025-01-01",
                description="Test description",
            )
            return TranscriptResult(
                video_id=video_id,
                status=DownloadStatus.SUCCESS,
                metadata=metadata,
            )

    monkeypatch.setattr("ytscriber.batch.TranscriptDownloader", DummyDownloader)

    progress = download_from_csv(
        csv_path=csv_path,
        output_dir=output_dir,
        languages=["en"],
        delay=0,
    )

    assert progress.total == 2
    assert progress.processed == 2
    assert progress.success == 1
    assert progress.errors == 0
