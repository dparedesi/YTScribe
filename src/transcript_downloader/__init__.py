"""
Conference Transcript Downloader.

Download YouTube transcripts from conference channels and organize them
for analysis, summarization, and archival.
"""

__version__ = "1.0.0"
__author__ = "Daniel Paredes"

from transcript_downloader.downloader import TranscriptDownloader
from transcript_downloader.extractor import ChannelExtractor
from transcript_downloader.models import VideoMetadata, TranscriptResult

__all__ = [
    "TranscriptDownloader",
    "ChannelExtractor",
    "VideoMetadata",
    "TranscriptResult",
    "__version__",
]
