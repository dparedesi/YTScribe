"""Tests for data models."""

from __future__ import annotations

import pytest

from ytscriber.models import (
    BatchProgress,
    DownloadStatus,
    TranscriptResult,
    VideoMetadata,
)


class TestVideoMetadata:
    """Tests for VideoMetadata class."""

    def test_basic_creation(self):
        """Test creating VideoMetadata with required fields."""
        metadata = VideoMetadata(
            video_id="dQw4w9WgXcQ",
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        )
        assert metadata.video_id == "dQw4w9WgXcQ"
        assert metadata.url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    def test_full_creation(self):
        """Test creating VideoMetadata with all fields."""
        metadata = VideoMetadata(
            video_id="dQw4w9WgXcQ",
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            title="Test Video",
            author="Test Author",
            description="Test description",
            duration_seconds=180,
            duration_minutes=3.0,
            view_count=1000000,
            published_date="2024-01-15",
            keywords="test, video, keywords",
        )
        assert metadata.title == "Test Video"
        assert metadata.author == "Test Author"
        assert metadata.duration_seconds == 180

    def test_watch_url_property(self):
        """Test watch_url property."""
        metadata = VideoMetadata(
            video_id="dQw4w9WgXcQ",
            url="https://youtu.be/dQw4w9WgXcQ",
        )
        assert metadata.watch_url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    def test_to_dict(self):
        """Test conversion to dictionary."""
        metadata = VideoMetadata(
            video_id="dQw4w9WgXcQ",
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            title="Test Video",
        )
        d = metadata.to_dict()
        assert d["video_id"] == "dQw4w9WgXcQ"
        assert d["title"] == "Test Video"
        assert "url" in d

    def test_from_dict(self):
        """Test creation from dictionary."""
        data = {
            "video_id": "dQw4w9WgXcQ",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "title": "Test Video",
        }
        metadata = VideoMetadata.from_dict(data)
        assert metadata.video_id == "dQw4w9WgXcQ"
        assert metadata.title == "Test Video"


class TestTranscriptResult:
    """Tests for TranscriptResult class."""

    def test_success_result(self):
        """Test successful result."""
        result = TranscriptResult(
            video_id="dQw4w9WgXcQ",
            status=DownloadStatus.SUCCESS,
            transcript_text="Hello world",
        )
        assert result.success is True
        assert result.transcript_text == "Hello world"

    def test_error_result(self):
        """Test error result."""
        result = TranscriptResult(
            video_id="dQw4w9WgXcQ",
            status=DownloadStatus.ERROR,
            error_message="No transcript found",
        )
        assert result.success is False
        assert result.error_message == "No transcript found"

    def test_skipped_result(self):
        """Test skipped result."""
        result = TranscriptResult(
            video_id="dQw4w9WgXcQ",
            status=DownloadStatus.SKIPPED,
        )
        assert result.success is False


class TestBatchProgress:
    """Tests for BatchProgress class."""

    def test_initial_state(self):
        """Test initial progress state."""
        progress = BatchProgress(total=100)
        assert progress.total == 100
        assert progress.processed == 0
        assert progress.remaining == 100

    def test_remaining_calculation(self):
        """Test remaining count calculation."""
        progress = BatchProgress(total=100, processed=30)
        assert progress.remaining == 70

    def test_success_rate_zero_processed(self):
        """Test success rate when nothing processed."""
        progress = BatchProgress(total=100)
        assert progress.success_rate == 0.0

    def test_success_rate_calculation(self):
        """Test success rate calculation."""
        progress = BatchProgress(
            total=100,
            processed=50,
            success=40,
            errors=10,
        )
        assert progress.success_rate == 80.0

    def test_success_rate_all_successful(self):
        """Test 100% success rate."""
        progress = BatchProgress(
            total=10,
            processed=10,
            success=10,
        )
        assert progress.success_rate == 100.0


class TestDownloadStatus:
    """Tests for DownloadStatus enum."""

    def test_status_values(self):
        """Test status enum values."""
        assert DownloadStatus.PENDING.value == "pending"
        assert DownloadStatus.SUCCESS.value == "success"
        assert DownloadStatus.SKIPPED.value == "skipped"
        assert DownloadStatus.ERROR.value == "error"
        assert DownloadStatus.IP_BLOCKED.value == "ip_blocked"

    def test_status_is_string(self):
        """Test that status is a string enum."""
        assert isinstance(DownloadStatus.SUCCESS, str)
        assert DownloadStatus.SUCCESS == "success"
