---
name: download-all-transcripts
description: Download transcripts for all data folders sequentially. Use for overnight batch processing of all pending transcripts.
---

# Download All Transcripts

Sequentially download transcripts for ALL data folders (both channels and manual collections).

## Command

```bash
./scripts/download_all_transcripts.sh
```

## What It Does

1. Finds all folders in `data/` that have a `videos.csv`
2. For each folder, downloads pending transcripts to `transcripts/` subfolder
3. Updates CSV with download status
4. Runs sequentially with 60s delay between videos

## Overnight Usage

This script is designed to run overnight:

```bash
# Run in background with output logging
nohup ./scripts/download_all_transcripts.sh > download.log 2>&1 &

# Or combine with sync first
./scripts/sync_all_channels.sh && ./scripts/download_all_transcripts.sh
```

## Rate Limiting

- 60 second delay between videos (configurable in script)
- Processes one folder at a time
- Skips already-downloaded videos

## Output

Transcripts are saved as markdown with YAML frontmatter:

```
data/<folder-name>/
├── videos.csv
└── transcripts/
    ├── abc123.md
    ├── def456.md
    └── ...
```

## Resumable

If interrupted, just run again - it will skip already-downloaded videos based on the `transcript_downloaded` column in the CSV.

## Monitoring Progress

```bash
# Check how many transcripts downloaded
find data/*/transcripts -name "*.md" | wc -l

# Watch the log
tail -f download.log
```
