"""CSV handling for batch processing."""

from __future__ import annotations

import csv
import os
from pathlib import Path
from typing import Optional

from ytscriber.exceptions import CSVError
from ytscriber.logging_config import get_logger
from ytscriber.models import VideoMetadata

logger = get_logger("csv")


# Standard column names
URL_COLUMN = "url"
TRANSCRIPT_STATUS_COLUMN = "transcript_downloaded"
SUMMARY_COLUMN = "summary_done"

# Metadata columns in desired order
METADATA_COLUMNS = [
    "title",
    "duration_minutes",
    "view_count",
    "published_date",
    "description",
]


def read_video_urls(csv_path: str) -> list[dict]:
    """
    Read video URLs and metadata from a CSV file.

    Args:
        csv_path: Path to CSV file

    Returns:
        List of row dictionaries

    Raises:
        CSVError: If file cannot be read or has no URLs
    """
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        raise CSVError(csv_path, "read", "File not found")
    except Exception as e:
        raise CSVError(csv_path, "read", str(e))

    if not rows:
        raise CSVError(csv_path, "read", "No rows found")

    # Verify URL column exists
    url_columns = ["url", "youtube_url", "URL", "YOUTUBE_URL"]
    has_url = any(col in rows[0] for col in url_columns)
    if not has_url:
        raise CSVError(
            csv_path,
            "read",
            f"No URL column found. Expected one of: {url_columns}",
        )

    return rows


def get_url_from_row(row: dict) -> Optional[str]:
    """
    Extract URL from a CSV row.

    Args:
        row: CSV row dictionary

    Returns:
        URL string or None if not found
    """
    url = (
        row.get("url")
        or row.get("youtube_url")
        or row.get("URL")
        or row.get("YOUTUBE_URL")
    )
    return url.strip() if url else None


def get_download_status(row: dict) -> Optional[str]:
    """
    Get download status from a CSV row.

    Args:
        row: CSV row dictionary

    Returns:
        Status string or None
    """
    return row.get(TRANSCRIPT_STATUS_COLUMN, "").strip() or None


def is_already_downloaded(row: dict) -> bool:
    """
    Check if a video has already been downloaded or has a permanent error.

    Args:
        row: CSV row dictionary

    Returns:
        True if already successfully downloaded or has a permanent error
    """
    status = get_download_status(row)
    if status in ["success", "success (already exists)"]:
        return True
    # Skip videos with disabled transcripts - this is a permanent error
    if status and "Transcripts disabled" in status:
        return True
    return False


def update_csv_status(
    csv_path: str,
    rows: list[dict],
    fieldnames: list[str],
) -> None:
    """
    Write updated rows back to CSV file.

    Args:
        csv_path: Path to CSV file
        rows: Updated row dictionaries
        fieldnames: Column names

    Raises:
        CSVError: If file cannot be written
    """
    try:
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        logger.debug(f"Updated CSV: {csv_path}")
    except Exception as e:
        raise CSVError(csv_path, "write", str(e))


def ensure_csv_columns(fieldnames: list[str]) -> list[str]:
    """
    Ensure CSV has all required columns.

    Args:
        fieldnames: Current column names

    Returns:
        Updated column names list
    """
    result = list(fieldnames) if fieldnames else [URL_COLUMN]

    # Add metadata columns if missing
    for col in METADATA_COLUMNS:
        if col not in result:
            # Insert before status columns
            if TRANSCRIPT_STATUS_COLUMN in result:
                idx = result.index(TRANSCRIPT_STATUS_COLUMN)
                result.insert(idx, col)
            else:
                result.append(col)

    # Add status columns if missing
    if TRANSCRIPT_STATUS_COLUMN not in result:
        result.append(TRANSCRIPT_STATUS_COLUMN)
    if SUMMARY_COLUMN not in result:
        result.append(SUMMARY_COLUMN)

    return result


def append_videos_to_csv(
    csv_path: str,
    videos: list[VideoMetadata],
) -> int:
    """
    Append new videos to a CSV file.

    Skips videos that already exist in the file.

    Args:
        csv_path: Path to CSV file
        videos: List of VideoMetadata to add

    Returns:
        Number of videos added
    """
    # Read existing URLs
    existing_urls: set[str] = set()
    rows: list[dict] = []
    fieldnames: list[str] = [URL_COLUMN]

    if os.path.exists(csv_path):
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                fieldnames = list(reader.fieldnames) if reader.fieldnames else [URL_COLUMN]
                for row in reader:
                    url = get_url_from_row(row)
                    if url:
                        existing_urls.add(url)
                        rows.append(row)
        except Exception as e:
            logger.warning(f"Could not read existing CSV: {e}")

    # Ensure all columns exist
    fieldnames = ensure_csv_columns(fieldnames)

    # Add new videos
    added_count = 0
    for video in videos:
        if video.url and video.url not in existing_urls:
            row = {col: "" for col in fieldnames}
            row[URL_COLUMN] = video.url

            # Add metadata
            if video.title:
                row["title"] = video.title.replace("\n", " ").replace("\r", " ")
            if video.duration_minutes is not None:
                row["duration_minutes"] = video.duration_minutes
            if video.view_count is not None:
                row["view_count"] = video.view_count
            if video.published_date:
                row["published_date"] = video.published_date
            if video.description:
                row["description"] = video.description.replace("\n", " ").replace("\r", " ")

            rows.append(row)
            existing_urls.add(video.url)
            added_count += 1

    # Write back
    try:
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    except Exception as e:
        raise CSVError(csv_path, "write", str(e))

    logger.info(f"Added {added_count} new videos to {csv_path}")
    logger.info(f"Total videos in CSV: {len(rows)}")

    return added_count
