"""Custom exceptions for transcript downloader."""

from __future__ import annotations


class TranscriptDownloaderError(Exception):
    """Base exception for transcript downloader."""

    pass


class IPBlockedError(TranscriptDownloaderError):
    """Raised when YouTube blocks the IP address."""

    def __init__(self, message: str = "IP blocked by YouTube"):
        self.message = message
        super().__init__(self.message)


class VideoNotFoundError(TranscriptDownloaderError):
    """Raised when a video cannot be found."""

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.message = f"Video not found: {video_id}"
        super().__init__(self.message)


class TranscriptNotFoundError(TranscriptDownloaderError):
    """Raised when no transcript is available for a video."""

    def __init__(self, video_id: str, languages: list[str] | None = None):
        self.video_id = video_id
        self.languages = languages or []
        lang_str = ", ".join(self.languages) if self.languages else "any language"
        self.message = f"No transcript found for video {video_id} in {lang_str}"
        super().__init__(self.message)


class TranscriptsDisabledError(TranscriptDownloaderError):
    """Raised when transcripts are disabled for a video."""

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.message = f"Transcripts are disabled for video {video_id}"
        super().__init__(self.message)


class InvalidURLError(TranscriptDownloaderError):
    """Raised when a URL is not a valid YouTube URL."""

    def __init__(self, url: str):
        self.url = url
        self.message = f"Invalid YouTube URL: {url}"
        super().__init__(self.message)


class ChannelExtractionError(TranscriptDownloaderError):
    """Raised when video extraction from a channel fails."""

    def __init__(self, channel_url: str, reason: str = ""):
        self.channel_url = channel_url
        self.reason = reason
        self.message = f"Failed to extract videos from channel {channel_url}"
        if reason:
            self.message += f": {reason}"
        super().__init__(self.message)


class CSVError(TranscriptDownloaderError):
    """Raised when there's an error reading or writing CSV files."""

    def __init__(self, filepath: str, operation: str, reason: str = ""):
        self.filepath = filepath
        self.operation = operation
        self.reason = reason
        self.message = f"CSV {operation} error for {filepath}"
        if reason:
            self.message += f": {reason}"
        super().__init__(self.message)
