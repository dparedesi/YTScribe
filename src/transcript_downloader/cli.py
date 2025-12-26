"""Command-line interface for transcript downloader."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

from transcript_downloader import __version__
from transcript_downloader.csv_handler import (
    append_videos_to_csv,
    ensure_csv_columns,
    get_download_status,
    get_url_from_row,
    is_already_downloaded,
    read_video_urls,
    update_csv_status,
)
from transcript_downloader.downloader import TranscriptDownloader
from transcript_downloader.exceptions import (
    CSVError,
    ChannelExtractionError,
    IPBlockedError,
    InvalidURLError,
)
from transcript_downloader.extractor import ChannelExtractor
from transcript_downloader.logging_config import get_logger, setup_logging
from transcript_downloader.models import BatchProgress, DownloadStatus
from transcript_downloader.utils import extract_video_id

logger = get_logger("cli")


def download_main() -> None:
    """Main entry point for transcript downloading."""
    parser = argparse.ArgumentParser(
        prog="transcript-download",
        description="Download YouTube video transcripts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single video
  transcript-download https://www.youtube.com/watch?v=VIDEO_ID
  transcript-download https://www.youtube.com/watch?v=VIDEO_ID --output transcript.md
  
  # Batch processing from CSV
  transcript-download --csv list-of-videos.csv
  transcript-download --csv list-of-videos.csv --output-dir my_outputs --delay 30
        """,
    )
    parser.add_argument("url", nargs="?", help="YouTube video URL")
    parser.add_argument(
        "--csv",
        metavar="FILE",
        help="CSV file containing YouTube URLs (column: url)",
    )
    parser.add_argument(
        "--output",
        "-o",
        metavar="FILE",
        help="Output file path (single video mode only)",
    )
    parser.add_argument(
        "--output-dir",
        metavar="DIR",
        default="outputs",
        help="Output directory for batch processing (default: outputs)",
    )
    parser.add_argument(
        "--languages",
        "-l",
        nargs="+",
        metavar="LANG",
        default=["en", "en-US", "en-GB"],
        help="Language codes to try (default: en en-US en-GB)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=60.0,
        metavar="SECONDS",
        help="Delay between requests (default: 60)",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    args = parser.parse_args()

    # Setup logging
    setup_logging(level=logging.DEBUG if args.verbose else logging.INFO)

    # Batch mode
    if args.csv:
        _run_batch_download(args)
        return

    # Single video mode
    if not args.url:
        parser.error("Either provide a URL or use --csv for batch processing")

    _run_single_download(args)


def _run_single_download(args: argparse.Namespace) -> None:
    """Run single video download."""
    try:
        video_id = extract_video_id(args.url)
    except InvalidURLError:
        logger.error(f"Invalid YouTube URL: {args.url}")
        sys.exit(1)

    downloader = TranscriptDownloader(
        languages=args.languages,
        delay=0,  # No delay for single requests
        output_dir=args.output_dir,
    )

    try:
        result = downloader.download(
            video_id=video_id,
            video_url=args.url,
            output_file=args.output,
        )

        if not result.success:
            sys.exit(1)

    except IPBlockedError as e:
        logger.error(f"IP blocked by YouTube: {e}")
        logger.error("Please wait before retrying or use a different network.")
        sys.exit(1)


def _run_batch_download(args: argparse.Namespace) -> None:
    """Run batch download from CSV."""
    try:
        rows = read_video_urls(args.csv)
    except CSVError as e:
        logger.error(str(e))
        sys.exit(1)

    # Get fieldnames from first row
    fieldnames = list(rows[0].keys()) if rows else []
    fieldnames = ensure_csv_columns(fieldnames)

    # Initialize progress tracking
    progress = BatchProgress(total=len(rows))
    logger.info(f"Found {len(rows)} URLs in CSV file. Starting batch download...\n")

    downloader = TranscriptDownloader(
        languages=args.languages,
        delay=args.delay,
        output_dir=args.output_dir,
    )

    for i, row in enumerate(rows, 1):
        url = get_url_from_row(row)

        if not url:
            if "transcript_downloaded" not in row or not row.get("transcript_downloaded"):
                row["transcript_downloaded"] = "skipped (no URL)"
                # Save progress for skipped URLs
                try:
                    update_csv_status(args.csv, rows, fieldnames)
                except CSVError as e:
                    logger.warning(f"Could not save CSV progress: {e}")
            progress.processed += 1
            continue

        # Check if already downloaded
        if is_already_downloaded(row):
            logger.info(f"[{i}/{progress.total}] ⊘ Skipping (already processed)")
            progress.processed += 1
            progress.skipped += 1
            continue

        try:
            video_id = extract_video_id(url)
        except InvalidURLError:
            logger.warning(f"[{i}/{progress.total}] ✗ Invalid URL: {url}")
            row["transcript_downloaded"] = "error: invalid URL"
            progress.processed += 1
            progress.errors += 1
            # Save progress for invalid URLs
            try:
                update_csv_status(args.csv, rows, fieldnames)
            except CSVError as e:
                logger.warning(f"Could not save CSV progress: {e}")
            continue

        # Check if file already exists (with or without date prefix)
        # Files are saved as YYYY-MM-DD-{video_id}.md or {video_id}.md
        output_dir = Path(args.output_dir)
        possible_files = list(output_dir.glob(f"*{video_id}.md"))
        if possible_files:
            logger.info(f"[{i}/{progress.total}] ⊘ Skipping {video_id} (file exists)")
            row["transcript_downloaded"] = "success (already exists)"
            progress.processed += 1
            progress.success += 1
            # Save progress for files that already exist
            try:
                update_csv_status(args.csv, rows, fieldnames)
            except CSVError as e:
                logger.warning(f"Could not save CSV progress: {e}")
            continue

        logger.info(f"[{i}/{progress.total}] Downloading: {video_id}")

        try:
            result = downloader.download(
                video_id=video_id,
                video_url=url,
                apply_delay=i > 1,  # No delay for first request
            )

            progress.processed += 1
            if result.success:
                row["transcript_downloaded"] = "success"
                # Update metadata from download result
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
            
            # Save progress after each video
            try:
                update_csv_status(args.csv, rows, fieldnames)
            except CSVError as e:
                logger.warning(f"Could not save CSV progress: {e}")

        except IPBlockedError:
            logger.error("\n⚠️  STOPPING: IP blocked by YouTube. Saving progress...")
            row["transcript_downloaded"] = "error: IP blocked (stopped)"
            progress.processed += 1
            progress.errors += 1

            # Save progress and exit
            try:
                update_csv_status(args.csv, rows, fieldnames)
            except CSVError as e:
                logger.warning(f"Could not save CSV: {e}")

            _print_summary(progress, interrupted=True)
            sys.exit(2)  # Exit code 2 = IP blocked

    # Save final CSV
    try:
        update_csv_status(args.csv, rows, fieldnames)
        logger.info(f"\n✓ Updated CSV file: {args.csv}")
    except CSVError as e:
        logger.warning(f"Could not update CSV: {e}")

    _print_summary(progress)


def _print_summary(progress: BatchProgress, interrupted: bool = False) -> None:
    """Print batch processing summary."""
    status = "STOPPED" if interrupted else "Complete"
    print(f"\n{'=' * 60}")
    print(f"Batch processing {status}!")
    print(f"  Success: {progress.success}")
    print(f"  Skipped: {progress.skipped}")
    print(f"  Errors: {progress.errors}")
    print(f"  Total: {progress.total}")
    print(f"{'=' * 60}")

    if interrupted:
        print("\n⚠️  Please wait before retrying. Consider:")
        print("   - Waiting 30-60 minutes before retrying")
        print("   - Using a different network/IP address")
        print("   - Increasing delay between requests")


def extract_main() -> None:
    """Main entry point for channel video extraction."""
    parser = argparse.ArgumentParser(
        prog="transcript-extract",
        description="Extract video IDs from a YouTube channel",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract 10 latest videos
  transcript-extract https://www.youtube.com/@AWSEventsChannel/videos --count 10
  
  # Save to CSV file
  transcript-extract https://www.youtube.com/@AWSEventsChannel/videos --count 100 --append-csv videos.csv
        """,
    )
    parser.add_argument("channel_url", help="YouTube channel URL")
    parser.add_argument(
        "--count",
        "-n",
        type=int,
        default=10,
        metavar="N",
        help="Number of videos to extract (default: 10)",
    )
    parser.add_argument(
        "--output",
        "-o",
        metavar="FILE",
        help="Output file for video IDs (one per line)",
    )
    parser.add_argument(
        "--append-csv",
        metavar="FILE",
        help="Append video URLs to CSV file",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    args = parser.parse_args()

    # Setup logging
    setup_logging(level=logging.DEBUG if args.verbose else logging.INFO)

    logger.info(f"Extracting {args.count} latest videos from channel...")

    extractor = ChannelExtractor()

    try:
        videos = extractor.extract_videos(args.channel_url, max_videos=args.count)
    except ChannelExtractionError as e:
        logger.error(str(e))
        sys.exit(1)

    if not videos:
        logger.error("No videos found.")
        sys.exit(1)

    logger.info(f"Found {len(videos)} videos")

    # Output results
    if args.append_csv:
        try:
            append_videos_to_csv(args.append_csv, videos)
        except CSVError as e:
            logger.error(str(e))
            sys.exit(1)
    elif args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                for video in videos:
                    f.write(f"{video.video_id}\n")
            logger.info(f"✓ Video IDs saved to: {args.output}")
        except Exception as e:
            logger.error(f"Error writing to file: {e}")
            sys.exit(1)
    else:
        # Print video IDs to stdout
        for video in videos:
            print(video.video_id)


def add_main() -> None:
    """Main entry point for adding videos to a collection CSV."""
    parser = argparse.ArgumentParser(
        prog="transcript-add",
        description="Add a YouTube video URL to a collection CSV",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Add a video to the random collection
  transcript-add https://www.youtube.com/watch?v=VIDEO_ID --csv data/random/videos.csv
  
  # Add a video to library-of-minds
  transcript-add https://www.youtube.com/watch?v=VIDEO_ID --csv data/library-of-minds/videos.csv
        """,
    )
    parser.add_argument("url", help="YouTube video URL to add")
    parser.add_argument(
        "--csv",
        required=True,
        metavar="FILE",
        help="CSV file to add the video to",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    args = parser.parse_args()

    # Setup logging
    setup_logging(level=logging.DEBUG if args.verbose else logging.INFO)

    # Validate URL and extract video ID
    try:
        video_id = extract_video_id(args.url)
    except InvalidURLError:
        logger.error(f"Invalid YouTube URL: {args.url}")
        sys.exit(1)

    # Create VideoMetadata with canonical URL
    from transcript_downloader.models import VideoMetadata

    video = VideoMetadata(
        video_id=video_id,
        url=f"https://www.youtube.com/watch?v={video_id}",
    )

    # Ensure CSV directory exists
    csv_path = Path(args.csv)
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    # Create CSV with header if it doesn't exist
    if not csv_path.exists():
        fieldnames = ensure_csv_columns([])
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            import csv

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
        logger.info(f"Created new CSV file: {args.csv}")

    # Add video to CSV
    try:
        added = append_videos_to_csv(args.csv, [video])
        if added > 0:
            logger.info(f"✓ Added video {video_id} to {args.csv}")
        else:
            logger.info(f"⊘ Video {video_id} already exists in {args.csv}")
    except CSVError as e:
        logger.error(str(e))
        sys.exit(1)


if __name__ == "__main__":
    download_main()
