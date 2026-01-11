"""Utility functions for transcript downloader."""

from __future__ import annotations

import json
import re
from typing import Optional
from urllib.parse import parse_qs, urlparse

from ytscriber.exceptions import InvalidURLError


def extract_video_id(url: str) -> str:
    """
    Extract video ID from a YouTube URL.

    Args:
        url: YouTube video URL

    Returns:
        YouTube video ID

    Raises:
        InvalidURLError: If URL is not a valid YouTube URL
    """
    parsed_url = urlparse(url)
    video_id: Optional[str] = None

    if parsed_url.hostname in ["www.youtube.com", "youtube.com", "m.youtube.com"]:
        if parsed_url.path == "/watch":
            video_id = parse_qs(parsed_url.query).get("v", [None])[0]
        elif parsed_url.path.startswith("/embed/"):
            video_id = parsed_url.path.split("/")[2]
        elif parsed_url.path.startswith("/v/"):
            video_id = parsed_url.path.split("/")[2]
    elif parsed_url.hostname == "youtu.be":
        video_id = parsed_url.path[1:]

    if not video_id:
        raise InvalidURLError(url)

    return video_id


def normalize_channel_url(url: str) -> str:
    """
    Normalize a YouTube channel URL.

    Ensures the URL ends with /videos for proper video listing.

    Args:
        url: YouTube channel URL

    Returns:
        Normalized channel URL
    """
    # Remove trailing /videos suffix if present (we'll add it back consistently)
    if url.endswith("/videos"):
        url = url[:-7]

    # Remove trailing slash
    url = url.rstrip("/")

    return url


def ensure_videos_endpoint(url: str) -> str:
    """
    Ensure channel URL points to the videos endpoint.

    Args:
        url: YouTube channel URL

    Returns:
        URL with /videos endpoint
    """
    normalized = normalize_channel_url(url)
    return f"{normalized}/videos"


def sanitize_filename(filename: str, max_length: int = 255) -> str:
    """
    Sanitize a string to be used as a filename.

    Args:
        filename: Original filename
        max_length: Maximum filename length

    Returns:
        Sanitized filename
    """
    # Remove or replace invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', "_", filename)
    # Remove control characters
    sanitized = re.sub(r"[\x00-\x1f\x7f]", "", sanitized)
    # Collapse multiple underscores
    sanitized = re.sub(r"_+", "_", sanitized)
    # Trim whitespace
    sanitized = sanitized.strip()
    # Truncate if too long
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    return sanitized


def format_duration(seconds: int) -> str:
    """
    Format duration in seconds to human-readable string.

    Args:
        seconds: Duration in seconds

    Returns:
        Formatted duration string (e.g., "1h 23m 45s")
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0 or hours > 0:
        parts.append(f"{minutes}m")
    parts.append(f"{secs}s")

    return " ".join(parts)


def truncate_text(text: str, max_length: int = 500, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length.

    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add when truncated

    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def escape_yaml_string(text: str) -> str:
    """
    Escape a string for safe YAML output.

    Args:
        text: String to escape

    Returns:
        Escaped string safe for YAML
    """
    # Replace problematic characters
    escaped = text.replace("\\", "\\\\")
    escaped = escaped.replace('"', '\\"')
    escaped = escaped.replace("\n", " ")
    escaped = escaped.replace("\r", "")
    return escaped


def is_valid_video_id(video_id: str) -> bool:
    """
    Check if a string is a valid YouTube video ID.

    YouTube video IDs are 11 characters long and contain
    alphanumeric characters, hyphens, and underscores.

    Args:
        video_id: String to check

    Returns:
        True if valid video ID
    """
    if len(video_id) != 11:
        return False
    # Video IDs contain alphanumeric, hyphen, and underscore
    return bool(re.match(r"^[a-zA-Z0-9_-]{11}$", video_id))


def parse_json_safely(text: str) -> Optional[dict]:
    """
    Safely parse JSON from text.

    Args:
        text: Text containing JSON

    Returns:
        Parsed JSON dict or None if parsing fails
    """
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None
