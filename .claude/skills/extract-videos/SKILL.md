---
name: extract-videos
description: Extract video metadata from a YouTube channel and save to CSV for tracking. This skill ONLY populates the CSV and does NOT download transcripts.
---

# Extract Videos from YouTube Channel

## Overview

Extract video metadata from a YouTube channel and save to a CSV file for tracking. This skill is strictly for generating the video list. It does not perform any transcript downloads.

## Command

```bash
transcript-extract <channel_url> --count <N> --append-csv <output.csv>
```

## Parameters

| Option | Description | Default |
|--------|-------------|---------|
| `--count, -n` | Number of latest videos to extract | 10 |
| `--append-csv` | Create or append to CSV file | - |
| `--output, -o` | Save video IDs to text file | - |
| `--verbose, -v` | Enable verbose output | False |

## Instructions

### Adding a New Channel (for recurring syncs)

When adding a channel that will be synced regularly:

1. Create the directory structure:
   ```bash
   mkdir -p data/<channel-name>
   ```

2. Add the channel to `data/channels.yaml`:
   ```yaml
   - folder: <channel-name>
     url: https://www.youtube.com/@ChannelName/videos
     count: 50  # Number of videos for FUTURE syncs
     enabled: true
   ```

3. Run the initial extraction (can use a different count than configured):
   ```bash
   transcript-extract https://www.youtube.com/@ChannelName/videos \
     --count 200 \
     --append-csv data/<channel-name>/videos.csv
   ```

**Important**: The `count` in `channels.yaml` is for future automated syncs. The initial extraction can use a larger count to backfill historical videos.

### One-time Extraction (no recurring sync)

For conferences or one-off extractions that won't be synced:

1. Create the directory:
   ```bash
   mkdir -p data/<conference-name>
   ```

2. Run the extract command:
   ```bash
   transcript-extract https://www.youtube.com/@ChannelName/videos \
     --count 100 \
     --append-csv data/<conference-name>/videos.csv
   ```

3. The CSV will be created with columns:
   - `url`, `title`, `duration_minutes`, `view_count`, `description`
   - `transcript_downloaded`, `summary_done` (for tracking)

## Examples

```bash
# New channel: Initial extraction of 200 videos, future syncs of 50
# 1. mkdir -p data/noduslabs
# 2. Add to channels.yaml with count: 50
# 3. Run initial extraction:
transcript-extract https://www.youtube.com/@noduslabs/videos \
  --count 200 \
  --append-csv data/noduslabs/videos.csv

# One-time conference extraction (no recurring sync)
transcript-extract https://www.youtube.com/@AWSEventsChannel/videos \
  --count 100 \
  --append-csv data/aws-reinvent-2025/videos.csv
```

## Notes

- Channel URL format: `https://www.youtube.com/@ChannelName/videos`
- CSV will be created if it doesn't exist, or appended to if it does
- Duplicate videos (by URL) are automatically skipped
- The `count` in `channels.yaml` controls future syncs via `sync-all-channels` skill
- Initial extraction count can differ from the configured sync count
