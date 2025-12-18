---
name: extract-videos
description: Extract video metadata from a YouTube channel and save to CSV for tracking. Use when you need to build a list of videos from a YouTube channel.
---

# Extract Videos from YouTube Channel

## Overview

Extract video metadata from a YouTube channel and save to a CSV file for tracking. This is typically the first step in the transcript download workflow.

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
