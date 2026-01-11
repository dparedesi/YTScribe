"""Data models for transcript downloader."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class DownloadStatus(str, Enum):
    """Status of a transcript download."""

    PENDING = "pending"
    SUCCESS = "success"
    SKIPPED = "skipped"
    ERROR = "error"
    IP_BLOCKED = "ip_blocked"


@dataclass
class VideoMetadata:
    """Metadata for a YouTube video."""

    video_id: str
    url: str
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    duration_seconds: Optional[int] = None
    duration_minutes: Optional[float] = None
    view_count: Optional[int] = None
    published_date: Optional[str] = None
    keywords: Optional[str] = None

    @property
    def watch_url(self) -> str:
        """Get the YouTube watch URL."""
        return f"https://www.youtube.com/watch?v={self.video_id}"

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "video_id": self.video_id,
            "url": self.url,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "duration_seconds": self.duration_seconds,
            "duration_minutes": self.duration_minutes,
            "view_count": self.view_count,
            "published_date": self.published_date,
            "keywords": self.keywords,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "VideoMetadata":
        """Create from dictionary."""
        return cls(
            video_id=data.get("video_id", ""),
            url=data.get("url", ""),
            title=data.get("title"),
            author=data.get("author"),
            description=data.get("description"),
            duration_seconds=data.get("duration_seconds"),
            duration_minutes=data.get("duration_minutes"),
            view_count=data.get("view_count"),
            published_date=data.get("published_date"),
            keywords=data.get("keywords"),
        )


@dataclass
class TranscriptMetadata:
    """Metadata about a downloaded transcript."""

    video_id: str
    video_url: str
    is_generated: Optional[bool] = None
    is_translatable: Optional[bool] = None
    language: Optional[str] = None


@dataclass
class TranscriptResult:
    """Result of a transcript download attempt."""

    video_id: str
    status: DownloadStatus
    transcript_text: Optional[str] = None
    error_message: Optional[str] = None
    metadata: Optional[VideoMetadata] = None
    transcript_metadata: Optional[TranscriptMetadata] = None
    output_path: Optional[str] = None

    @property
    def success(self) -> bool:
        """Check if download was successful."""
        return self.status == DownloadStatus.SUCCESS


@dataclass
class BatchProgress:
    """Progress tracking for batch downloads."""

    total: int
    processed: int = 0
    success: int = 0
    skipped: int = 0
    errors: int = 0

    @property
    def remaining(self) -> int:
        """Get remaining items to process."""
        return self.total - self.processed

    @property
    def success_rate(self) -> float:
        """Get success rate as percentage."""
        if self.processed == 0:
            return 0.0
        return (self.success / self.processed) * 100
