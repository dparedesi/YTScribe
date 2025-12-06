"""Tests for CSV handler."""

from __future__ import annotations

import csv
import os
import tempfile
from pathlib import Path

import pytest

from transcript_downloader.csv_handler import (
    append_videos_to_csv,
    ensure_csv_columns,
    get_download_status,
    get_url_from_row,
    is_already_downloaded,
    read_video_urls,
)
from transcript_downloader.exceptions import CSVError
from transcript_downloader.models import VideoMetadata


class TestGetUrlFromRow:
    """Tests for get_url_from_row function."""

    def test_url_column(self):
        """Test getting URL from 'url' column."""
        row = {"url": "https://youtube.com/watch?v=abc123"}
        assert get_url_from_row(row) == "https://youtube.com/watch?v=abc123"

    def test_youtube_url_column(self):
        """Test getting URL from 'youtube_url' column."""
        row = {"youtube_url": "https://youtube.com/watch?v=abc123"}
        assert get_url_from_row(row) == "https://youtube.com/watch?v=abc123"

    def test_uppercase_column(self):
        """Test getting URL from uppercase column."""
        row = {"URL": "https://youtube.com/watch?v=abc123"}
        assert get_url_from_row(row) == "https://youtube.com/watch?v=abc123"

    def test_no_url(self):
        """Test row without URL."""
        row = {"title": "Test Video"}
        assert get_url_from_row(row) is None

    def test_strips_whitespace(self):
        """Test URL whitespace is stripped."""
        row = {"url": "  https://youtube.com/watch?v=abc123  "}
        assert get_url_from_row(row) == "https://youtube.com/watch?v=abc123"


class TestGetDownloadStatus:
    """Tests for get_download_status function."""

    def test_success_status(self):
        """Test getting success status."""
        row = {"transcript_downloaded": "success"}
        assert get_download_status(row) == "success"

    def test_empty_status(self):
        """Test empty status returns None."""
        row = {"transcript_downloaded": ""}
        assert get_download_status(row) is None

    def test_missing_column(self):
        """Test missing column returns None."""
        row = {"url": "test"}
        assert get_download_status(row) is None


class TestIsAlreadyDownloaded:
    """Tests for is_already_downloaded function."""

    def test_success_status(self):
        """Test success status returns True."""
        row = {"transcript_downloaded": "success"}
        assert is_already_downloaded(row) is True

    def test_already_exists_status(self):
        """Test 'success (already exists)' returns True."""
        row = {"transcript_downloaded": "success (already exists)"}
        assert is_already_downloaded(row) is True

    def test_error_status(self):
        """Test error status returns False."""
        row = {"transcript_downloaded": "error: not found"}
        assert is_already_downloaded(row) is False

    def test_empty_status(self):
        """Test empty status returns False."""
        row = {"transcript_downloaded": ""}
        assert is_already_downloaded(row) is False


class TestEnsureCsvColumns:
    """Tests for ensure_csv_columns function."""

    def test_adds_missing_columns(self):
        """Test adding missing metadata columns."""
        fieldnames = ["url"]
        result = ensure_csv_columns(fieldnames)
        assert "transcript_downloaded" in result
        assert "summary_done" in result
        assert "title" in result

    def test_preserves_existing_columns(self):
        """Test existing columns are preserved."""
        fieldnames = ["url", "custom_column"]
        result = ensure_csv_columns(fieldnames)
        assert "url" in result
        assert "custom_column" in result

    def test_empty_fieldnames(self):
        """Test empty fieldnames list."""
        result = ensure_csv_columns([])
        assert "url" in result


class TestReadVideoUrls:
    """Tests for read_video_urls function."""

    def test_read_valid_csv(self):
        """Test reading valid CSV file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("url,title\n")
            f.write("https://youtube.com/watch?v=abc123,Test Video\n")
            f.flush()

            try:
                rows = read_video_urls(f.name)
                assert len(rows) == 1
                assert rows[0]["url"] == "https://youtube.com/watch?v=abc123"
            finally:
                os.unlink(f.name)

    def test_file_not_found(self):
        """Test reading non-existent file raises error."""
        with pytest.raises(CSVError) as exc_info:
            read_video_urls("/nonexistent/file.csv")
        assert "not found" in str(exc_info.value).lower()

    def test_empty_csv(self):
        """Test reading empty CSV raises error."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("url,title\n")  # Headers only
            f.flush()

            try:
                with pytest.raises(CSVError):
                    read_video_urls(f.name)
            finally:
                os.unlink(f.name)


class TestAppendVideosToCsv:
    """Tests for append_videos_to_csv function."""

    def test_creates_new_csv(self):
        """Test creating new CSV file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = os.path.join(tmpdir, "videos.csv")
            videos = [
                VideoMetadata(
                    video_id="abc123",
                    url="https://youtube.com/watch?v=abc123",
                    title="Test Video",
                )
            ]

            added = append_videos_to_csv(csv_path, videos)

            assert added == 1
            assert os.path.exists(csv_path)

            with open(csv_path, "r") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                assert len(rows) == 1
                assert rows[0]["url"] == "https://youtube.com/watch?v=abc123"

    def test_skips_existing_urls(self):
        """Test that existing URLs are not duplicated."""
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = os.path.join(tmpdir, "videos.csv")

            # Create initial CSV
            videos1 = [
                VideoMetadata(
                    video_id="abc123",
                    url="https://youtube.com/watch?v=abc123",
                )
            ]
            append_videos_to_csv(csv_path, videos1)

            # Try to add same video again
            videos2 = [
                VideoMetadata(
                    video_id="abc123",
                    url="https://youtube.com/watch?v=abc123",
                )
            ]
            added = append_videos_to_csv(csv_path, videos2)

            assert added == 0

    def test_appends_new_videos(self):
        """Test appending new videos to existing CSV."""
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = os.path.join(tmpdir, "videos.csv")

            # Create initial CSV
            videos1 = [
                VideoMetadata(
                    video_id="abc123",
                    url="https://youtube.com/watch?v=abc123",
                )
            ]
            append_videos_to_csv(csv_path, videos1)

            # Add new video
            videos2 = [
                VideoMetadata(
                    video_id="xyz789",
                    url="https://youtube.com/watch?v=xyz789",
                )
            ]
            added = append_videos_to_csv(csv_path, videos2)

            assert added == 1

            with open(csv_path, "r") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                assert len(rows) == 2
