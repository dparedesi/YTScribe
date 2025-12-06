"""Tests for exception classes."""

from __future__ import annotations

import pytest

from transcript_downloader.exceptions import (
    ChannelExtractionError,
    CSVError,
    IPBlockedError,
    InvalidURLError,
    TranscriptDownloaderError,
    TranscriptNotFoundError,
    TranscriptsDisabledError,
    VideoNotFoundError,
)


class TestTranscriptDownloaderError:
    """Tests for base exception class."""

    def test_base_exception(self):
        """Test base exception can be raised."""
        with pytest.raises(TranscriptDownloaderError):
            raise TranscriptDownloaderError("Test error")


class TestIPBlockedError:
    """Tests for IPBlockedError."""

    def test_default_message(self):
        """Test default error message."""
        error = IPBlockedError()
        assert "IP blocked" in str(error)

    def test_custom_message(self):
        """Test custom error message."""
        error = IPBlockedError("Custom block message")
        assert error.message == "Custom block message"


class TestVideoNotFoundError:
    """Tests for VideoNotFoundError."""

    def test_error_message(self):
        """Test error message includes video ID."""
        error = VideoNotFoundError("dQw4w9WgXcQ")
        assert "dQw4w9WgXcQ" in str(error)
        assert error.video_id == "dQw4w9WgXcQ"


class TestTranscriptNotFoundError:
    """Tests for TranscriptNotFoundError."""

    def test_error_with_languages(self):
        """Test error message includes languages."""
        error = TranscriptNotFoundError("abc123", ["en", "en-US"])
        assert "abc123" in str(error)
        assert "en" in str(error)
        assert error.languages == ["en", "en-US"]

    def test_error_without_languages(self):
        """Test error message without languages."""
        error = TranscriptNotFoundError("abc123")
        assert "abc123" in str(error)
        assert "any language" in str(error)


class TestTranscriptsDisabledError:
    """Tests for TranscriptsDisabledError."""

    def test_error_message(self):
        """Test error message includes video ID."""
        error = TranscriptsDisabledError("dQw4w9WgXcQ")
        assert "disabled" in str(error).lower()
        assert "dQw4w9WgXcQ" in str(error)


class TestInvalidURLError:
    """Tests for InvalidURLError."""

    def test_error_message(self):
        """Test error message includes URL."""
        url = "https://example.com/video"
        error = InvalidURLError(url)
        assert url in str(error)
        assert error.url == url


class TestChannelExtractionError:
    """Tests for ChannelExtractionError."""

    def test_error_with_reason(self):
        """Test error with reason."""
        url = "https://youtube.com/@channel"
        error = ChannelExtractionError(url, "Connection timeout")
        assert url in str(error)
        assert "Connection timeout" in str(error)

    def test_error_without_reason(self):
        """Test error without reason."""
        url = "https://youtube.com/@channel"
        error = ChannelExtractionError(url)
        assert url in str(error)


class TestCSVError:
    """Tests for CSVError."""

    def test_read_error(self):
        """Test CSV read error."""
        error = CSVError("videos.csv", "read", "File not found")
        assert "videos.csv" in str(error)
        assert "read" in str(error)
        assert "File not found" in str(error)

    def test_write_error(self):
        """Test CSV write error."""
        error = CSVError("output.csv", "write", "Permission denied")
        assert "output.csv" in str(error)
        assert "write" in str(error)

    def test_error_without_reason(self):
        """Test error without reason."""
        error = CSVError("file.csv", "read")
        assert "file.csv" in str(error)
