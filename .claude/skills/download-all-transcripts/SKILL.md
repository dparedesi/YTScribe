---
name: download-all-transcripts
description: Download transcripts for all data folders sequentially.
---

# Download All Transcripts

Sequentially download transcripts for ALL data folders (both channels and manual collections).

## ⚠️ IMPORTANT: What to Do

**JUST RUN THE COMMAND BELOW. DO NOT:**
- Read or inspect the script file
- Read the Python CLI or project files
- Try to validate or understand the implementation
- Manually reconstruct the logic yourself
- Run the Python module directly

**Simply execute this single command in background mode (the script is already executable):**

```bash
./scripts/download_all_transcripts.sh
```

That's it. The script handles everything. No need to monitor it closely because it takes a long time to run (due to the 60 seconds delay between videos)

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
