"""Pytest fixtures for transcript downloader tests."""

from __future__ import annotations

import csv
import os
import tempfile
from pathlib import Path
from typing import Generator

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_csv(temp_dir: Path) -> Path:
    """Create a sample CSV file with video URLs."""
    csv_path = temp_dir / "videos.csv"
    
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["url", "title", "transcript_downloaded"],
        )
        writer.writeheader()
        writer.writerows([
            {
                "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "title": "Test Video 1",
                "transcript_downloaded": "",
            },
            {
                "url": "https://www.youtube.com/watch?v=abc123xyz45",
                "title": "Test Video 2",
                "transcript_downloaded": "success",
            },
            {
                "url": "https://www.youtube.com/watch?v=xyz789abc12",
                "title": "Test Video 3",
                "transcript_downloaded": "error: not found",
            },
        ])
    
    return csv_path


@pytest.fixture
def sample_video_ids() -> list[str]:
    """Sample valid YouTube video IDs."""
    return [
        "dQw4w9WgXcQ",
        "abc123xyz45",
        "xyz789-_abc",
    ]


@pytest.fixture
def sample_urls() -> list[str]:
    """Sample valid YouTube URLs."""
    return [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://youtu.be/abc123xyz45",
        "https://www.youtube.com/embed/xyz789-_abc",
    ]


@pytest.fixture
def invalid_urls() -> list[str]:
    """Sample invalid URLs."""
    return [
        "https://example.com/video",
        "https://vimeo.com/123456789",
        "not-a-url",
        "",
    ]
