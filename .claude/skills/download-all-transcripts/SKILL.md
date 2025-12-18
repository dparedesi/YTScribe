---
name: download-all-transcripts
description: Download transcripts for all data folders sequentially. Use for overnight batch processing or when you need to download pending transcripts across all channels and collections.
---

# Download All Transcripts

## Overview

Sequentially download transcripts for ALL data folders (both channels and manual collections). This is a batch operation designed for overnight runs.

## Command

Run this single command — the script handles all logic internally:

```bash
./scripts/download_all_transcripts.sh
```

> **Note**: This is a self-contained script. No need to inspect or reconstruct its logic — just execute it.

## What It Does

1. Finds all folders in `data/` that have a `videos.csv`
2. For each folder, downloads pending transcripts to `transcripts/` subfolder
3. Updates CSV with download status
4. Runs with 60s delay between videos to avoid rate limiting

## Output

Transcripts are saved as markdown with YAML frontmatter:

```
data/<folder-name>/
├── videos.csv
└── transcripts/
    ├── 2024-01-15-abc123.md
    ├── 2024-01-20-def456.md
    └── ...
```

## Resumable

If interrupted, just run again — it skips already-downloaded videos based on the `transcript_downloaded` column in the CSV.
