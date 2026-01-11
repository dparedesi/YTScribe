"""Batch operations for transcript downloads."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from ytscriber.csv_handler import (
    ensure_csv_columns,
    get_url_from_row,
    is_already_downloaded,
    read_video_urls,
    update_csv_status,
)
from ytscriber.downloader import TranscriptDownloader
from ytscriber.exceptions import CSVError, IPBlockedError, InvalidURLError
from ytscriber.logging_config import get_logger
from ytscriber.models import BatchProgress
from ytscriber.utils import extract_video_id

logger = get_logger("batch")


def find_video_csv_files(data_dir: Path) -> list[Path]:
    """Find all videos.csv files in the data directory."""
    if not data_dir.exists():
        return []
    return sorted(data_dir.rglob("videos.csv"))


def download_from_csv(
    csv_path: Path,
    output_dir: Path,
    languages: Optional[list[str]] = None,
    delay: float = 60.0,
) -> BatchProgress:
    """Download transcripts for a single CSV file."""
    try:
        rows = read_video_urls(str(csv_path))
    except CSVError as e:
        logger.error(str(e))
        return BatchProgress(total=0)

    fieldnames = list(rows[0].keys()) if rows else []
    fieldnames = ensure_csv_columns(fieldnames)

    progress = BatchProgress(total=len(rows))
    logger.info(f"Found {len(rows)} URLs in {csv_path}.")

    downloader = TranscriptDownloader(
        languages=languages,
        delay=delay,
        output_dir=str(output_dir),
    )

    for i, row in enumerate(rows, 1):
        url = get_url_from_row(row)

        if not url:
            if not row.get("transcript_downloaded"):
                row["transcript_downloaded"] = "skipped (no URL)"
                try:
                    update_csv_status(str(csv_path), rows, fieldnames)
                except CSVError as e:
                    logger.warning(f"Could not save CSV progress: {e}")
            progress.processed += 1
            continue

        if is_already_downloaded(row):
            logger.info(f"[{i}/{progress.total}] Skipping (already processed)")
            progress.processed += 1
            progress.skipped += 1
            continue

        try:
            video_id = extract_video_id(url)
        except InvalidURLError:
            logger.warning(f"[{i}/{progress.total}] Invalid URL: {url}")
            row["transcript_downloaded"] = "error: invalid URL"
            progress.processed += 1
            progress.errors += 1
            try:
                update_csv_status(str(csv_path), rows, fieldnames)
            except CSVError as e:
                logger.warning(f"Could not save CSV progress: {e}")
            continue

        output_dir.mkdir(parents=True, exist_ok=True)
        possible_files = list(output_dir.glob(f"*{video_id}.md"))
        if possible_files:
            logger.info(f"[{i}/{progress.total}] Skipping {video_id} (file exists)")
            row["transcript_downloaded"] = "success (already exists)"
            progress.processed += 1
            progress.success += 1
            try:
                update_csv_status(str(csv_path), rows, fieldnames)
            except CSVError as e:
                logger.warning(f"Could not save CSV progress: {e}")
            continue

        logger.info(f"[{i}/{progress.total}] Downloading: {video_id}")

        try:
            result = downloader.download(
                video_id=video_id,
                video_url=url,
                apply_delay=i > 1,
            )

            progress.processed += 1
            if result.success:
                row["transcript_downloaded"] = "success"
                if result.metadata:
                    if result.metadata.title:
                        row["title"] = result.metadata.title.replace("\n", " ").replace("\r", " ")
                    if result.metadata.duration_minutes is not None:
                        row["duration_minutes"] = str(result.metadata.duration_minutes)
                    if result.metadata.view_count is not None:
                        row["view_count"] = str(result.metadata.view_count)
                    if result.metadata.published_date:
                        row["published_date"] = result.metadata.published_date
                    if result.metadata.description:
                        row["description"] = result.metadata.description.replace("\n", " ").replace("\r", " ")
                progress.success += 1
            else:
                row["transcript_downloaded"] = f"error: {result.error_message or 'unknown'}"
                progress.errors += 1

            try:
                update_csv_status(str(csv_path), rows, fieldnames)
            except CSVError as e:
                logger.warning(f"Could not save CSV progress: {e}")

        except IPBlockedError:
            logger.error("IP blocked by YouTube. Saving progress and stopping.")
            row["transcript_downloaded"] = "error: IP blocked (stopped)"
            progress.processed += 1
            progress.errors += 1
            try:
                update_csv_status(str(csv_path), rows, fieldnames)
            except CSVError as e:
                logger.warning(f"Could not save CSV: {e}")
            raise

    try:
        update_csv_status(str(csv_path), rows, fieldnames)
        logger.info(f"Updated CSV file: {csv_path}")
    except CSVError as e:
        logger.warning(f"Could not update CSV: {e}")

    return progress


def download_all_transcripts(
    data_dir: Path,
    delay: float = 60.0,
    languages: Optional[list[str]] = None,
) -> BatchProgress:
    """Download transcripts for all folders with videos.csv."""
    csv_files = find_video_csv_files(data_dir)
    if not csv_files:
        raise FileNotFoundError(f"No videos.csv files found in {data_dir}")

    total_progress = BatchProgress(total=0)

    for csv_path in csv_files:
        output_dir = csv_path.parent / "transcripts"
        output_dir.mkdir(parents=True, exist_ok=True)

        progress = download_from_csv(
            csv_path=csv_path,
            output_dir=output_dir,
            languages=languages,
            delay=delay,
        )

        total_progress.total += progress.total
        total_progress.processed += progress.processed
        total_progress.success += progress.success
        total_progress.skipped += progress.skipped
        total_progress.errors += progress.errors

    return total_progress
