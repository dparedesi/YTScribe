"""Tests for utility functions."""

from __future__ import annotations

import pytest

from ytscriber.exceptions import InvalidURLError
from ytscriber.utils import (
    escape_yaml_string,
    extract_video_id,
    format_duration,
    is_valid_video_id,
    normalize_channel_url,
    sanitize_filename,
    truncate_text,
)


class TestExtractVideoId:
    """Tests for extract_video_id function."""

    def test_standard_watch_url(self):
        """Test extracting ID from standard watch URL."""
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        assert extract_video_id(url) == "dQw4w9WgXcQ"

    def test_watch_url_with_extra_params(self):
        """Test extracting ID from URL with additional parameters."""
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf"
        assert extract_video_id(url) == "dQw4w9WgXcQ"

    def test_short_url(self):
        """Test extracting ID from short youtu.be URL."""
        url = "https://youtu.be/dQw4w9WgXcQ"
        assert extract_video_id(url) == "dQw4w9WgXcQ"

    def test_embed_url(self):
        """Test extracting ID from embed URL."""
        url = "https://www.youtube.com/embed/dQw4w9WgXcQ"
        assert extract_video_id(url) == "dQw4w9WgXcQ"

    def test_invalid_url_raises_error(self):
        """Test that invalid URL raises InvalidURLError."""
        with pytest.raises(InvalidURLError):
            extract_video_id("https://example.com/video")

    def test_non_youtube_url_raises_error(self):
        """Test that non-YouTube URL raises InvalidURLError."""
        with pytest.raises(InvalidURLError):
            extract_video_id("https://vimeo.com/12345678")

    def test_youtube_url_without_video_id(self):
        """Test URL without video ID raises error."""
        with pytest.raises(InvalidURLError):
            extract_video_id("https://www.youtube.com/")


class TestNormalizeChannelUrl:
    """Tests for normalize_channel_url function."""

    def test_removes_videos_suffix(self):
        """Test removing /videos suffix."""
        url = "https://www.youtube.com/@AWSEventsChannel/videos"
        assert normalize_channel_url(url) == "https://www.youtube.com/@AWSEventsChannel"

    def test_removes_trailing_slash(self):
        """Test removing trailing slash."""
        url = "https://www.youtube.com/@AWSEventsChannel/"
        assert normalize_channel_url(url) == "https://www.youtube.com/@AWSEventsChannel"

    def test_already_normalized(self):
        """Test URL that's already normalized."""
        url = "https://www.youtube.com/@AWSEventsChannel"
        assert normalize_channel_url(url) == "https://www.youtube.com/@AWSEventsChannel"


class TestIsValidVideoId:
    """Tests for is_valid_video_id function."""

    def test_valid_id(self):
        """Test valid 11-character video ID."""
        assert is_valid_video_id("dQw4w9WgXcQ") is True

    def test_valid_id_with_hyphen(self):
        """Test valid ID containing hyphen."""
        assert is_valid_video_id("abc-123_XYZ") is True

    def test_too_short(self):
        """Test ID that's too short."""
        assert is_valid_video_id("abc123") is False

    def test_too_long(self):
        """Test ID that's too long."""
        assert is_valid_video_id("dQw4w9WgXcQx") is False

    def test_invalid_characters(self):
        """Test ID with invalid characters."""
        assert is_valid_video_id("dQw4w9Wg!cQ") is False


class TestFormatDuration:
    """Tests for format_duration function."""

    def test_seconds_only(self):
        """Test duration less than a minute."""
        assert format_duration(45) == "45s"

    def test_minutes_and_seconds(self):
        """Test duration in minutes and seconds."""
        assert format_duration(125) == "2m 5s"

    def test_hours_minutes_seconds(self):
        """Test duration in hours, minutes, and seconds."""
        assert format_duration(3725) == "1h 2m 5s"

    def test_zero_seconds(self):
        """Test zero duration."""
        assert format_duration(0) == "0s"

    def test_exact_hour(self):
        """Test exactly one hour."""
        assert format_duration(3600) == "1h 0m 0s"


class TestTruncateText:
    """Tests for truncate_text function."""

    def test_short_text_unchanged(self):
        """Test that short text is not modified."""
        text = "Hello, world!"
        assert truncate_text(text, max_length=50) == text

    def test_truncation_with_default_suffix(self):
        """Test truncation with default suffix."""
        text = "A" * 100
        result = truncate_text(text, max_length=50)
        assert len(result) == 50
        assert result.endswith("...")

    def test_custom_suffix(self):
        """Test truncation with custom suffix."""
        text = "A" * 100
        result = truncate_text(text, max_length=50, suffix="[...]")
        assert result.endswith("[...]")

    def test_exact_length(self):
        """Test text at exact max length."""
        text = "A" * 50
        assert truncate_text(text, max_length=50) == text


class TestSanitizeFilename:
    """Tests for sanitize_filename function."""

    def test_valid_filename_unchanged(self):
        """Test that valid filename is unchanged."""
        assert sanitize_filename("my_video.md") == "my_video.md"

    def test_removes_invalid_characters(self):
        """Test removal of invalid characters."""
        # Invalid chars replaced with _, then consecutive _ collapsed
        assert sanitize_filename('file<>name.md') == "file_name.md"
        assert sanitize_filename('file:name.md') == "file_name.md"

    def test_collapses_underscores(self):
        """Test collapsing multiple underscores."""
        assert sanitize_filename("file___name.md") == "file_name.md"
        # Multiple invalid chars in a row collapse to single underscore
        assert sanitize_filename('file<>:name.md') == "file_name.md"

    def test_truncates_long_filename(self):
        """Test truncation of long filename."""
        long_name = "a" * 300
        result = sanitize_filename(long_name, max_length=255)
        assert len(result) == 255


class TestEscapeYamlString:
    """Tests for escape_yaml_string function."""

    def test_simple_string_unchanged(self):
        """Test that simple string is unchanged."""
        assert escape_yaml_string("Hello world") == "Hello world"

    def test_escapes_quotes(self):
        """Test escaping double quotes."""
        assert escape_yaml_string('Say "hello"') == 'Say \\"hello\\"'

    def test_escapes_backslash(self):
        """Test escaping backslashes."""
        assert escape_yaml_string("path\\to\\file") == "path\\\\to\\\\file"

    def test_replaces_newlines(self):
        """Test replacing newlines with spaces."""
        assert escape_yaml_string("line1\nline2") == "line1 line2"

    def test_removes_carriage_return(self):
        """Test removing carriage returns."""
        assert escape_yaml_string("line1\r\nline2") == "line1 line2"
