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

1. If the folder doesn't exist, create the directory structure first:
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
# Extract 100 videos from AWS re:Invent
transcript-extract https://www.youtube.com/@AWSEventsChannel/videos \
  --count 100 \
  --append-csv data/aws-reinvent-2025/videos.csv

# Extract 50 videos from PyCon
transcript-extract https://www.youtube.com/@PyConUS \
  --count 50 \
  --append-csv data/pycon-2024/videos.csv
```

## Notes

- Channel URL format: `https://www.youtube.com/@ChannelName/videos`
- CSV will be created if it doesn't exist, or appended to if it does
- Duplicate videos (by URL) are automatically skipped
