---
name: download-transcripts
description: Download YouTube transcripts for videos tracked in a CSV file. Use when you need to download transcripts in bulk with progress tracking.
---

# Download Transcripts from CSV

## Overview

Download YouTube transcripts for videos tracked in a CSV file. Use after running `extract-videos` to build your video list, or with manually curated collections.

## Command

```bash
transcript-download --csv <input.csv> --output-dir <directory>
```

## Parameters

| Option | Description | Default |
|--------|-------------|---------|
| `--csv` | Input CSV file with video URLs | - |
| `--output-dir` | Directory for transcript files | outputs |
| `--delay` | Seconds between requests | 60 |
| `--languages, -l` | Language codes to try | en en-US en-GB |
| `--verbose, -v` | Enable verbose output | False |

## Instructions

1. Ensure you have a CSV file with video URLs (use `extract-videos` skill first)

2. Run the download command:
   ```bash
   transcript-download \
     --csv data/<conference-name>/videos.csv \
     --output-dir data/<conference-name>/transcripts
   ```

3. The command will:
   - Download transcripts as markdown with YAML frontmatter
   - Update the CSV `transcript_downloaded` column with status
   - Skip already-downloaded videos on re-run

## Examples

```bash
# Download transcripts for AWS re:Invent
transcript-download \
  --csv data/aws-reinvent-2025/videos.csv \
  --output-dir data/aws-reinvent-2025/transcripts

# Faster processing (shorter delay)
transcript-download \
  --csv data/pycon-2024/videos.csv \
  --output-dir data/pycon-2024/transcripts \
  --delay 30

# Single video mode
transcript-download https://www.youtube.com/watch?v=VIDEO_ID --output transcript.md
```

## Output Format

Transcripts are saved as markdown with YAML frontmatter:

```markdown
---
video_id: abc123xyz
video_url: https://www.youtube.com/watch?v=abc123xyz
title: Conference Talk Title
author: Speaker Name
published_date: 2025-01-15
length_minutes: 45.5
views: 1234
---

Full transcript text here...
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No transcript found" | Try `--languages en en-US auto` |
| IP blocked | Wait 30-60 min, increase delay to 120 |
| Script interrupted | Re-run same command; skips completed |
