---
name: download-all-transcripts
description: Download transcripts for all data folders sequentially. Use for overnight batch processing or when you need to download pending transcripts across all channels and collections.
---

# Download All Transcripts

**Why?** Manually downloading transcripts folder-by-folder is tedious and error-prone. This skill automates overnight batch processing across all channels and collections with built-in rate limiting and resumability.

## Quick Start

```bash
# Run the unified CLI command
ytscriber download-all
```

That's it. The command finds all folders with `videos.csv`, downloads pending transcripts, and resumes safely if interrupted.

---

## Workflow

### 1. Verify Prerequisites

Before running, ensure:
- You have at least one folder with a `videos.csv` file
- The `ytscriber` CLI is installed (`pip install -e .`)

```bash
# Check for valid data folders
ls ~/Documents/YTScriber/*/videos.csv
```

> [!TIP]
> If no `videos.csv` files exist, first run `extract-videos` or `sync-all-channels` to populate them.

### 2. Execute Batch Download

```bash
ytscriber download-all
```

The command will:
1. Find all folders containing `videos.csv`
2. Process each folder sequentially
3. Download transcripts to `<folder>/transcripts/`
4. Wait 60 seconds between videos to avoid YouTube rate limiting
5. Update CSV with download status

> [!CAUTION]
> This is a long-running operation. For a channel with 500 videos, expect 8+ hours. Run overnight or in a `tmux`/`screen` session.

### 3. Monitor Progress

The command outputs real-time progress:

```
YTScriber - Download All Transcripts
=======================================
Started at: Thu Dec 26 09:00:00 PST 2024
Delay between videos: 60s

Found 12 folders with videos.csv

────────────────────────────────────────
[1/12] Processing: lex-fridman
  CSV: ~/Documents/YTScriber/lex-fridman/videos.csv
  Output: ~/Documents/YTScriber/lex-fridman/transcripts
```

### 4. Handle Completion or Interruption

**On successful completion:**
```
All transcripts downloaded!
Finished at: Thu Dec 26 17:30:00 PST 2024

Summary of folders processed:
  - lex-fridman: 342 transcripts
  - huberman-lab: 156 transcripts
  ...
```

**On interruption or IP block:**
Simply run the command again. It automatically skips videos where `transcript_downloaded=success` in the CSV.

---

## Output Structure

Transcripts are saved as markdown with YAML frontmatter:

```
~/Documents/YTScriber/huberman-lab/
├── videos.csv
└── transcripts/
    ├── 2024-01-15-abc123XYZ00.md
    ├── 2024-01-20-def456ABC11.md
    └── ...
```

Each transcript file contains:
```markdown
---
video_id: abc123XYZ00
video_url: https://www.youtube.com/watch?v=abc123XYZ00
title: "Sleep Optimization Toolkit"
author: Huberman Lab
published_date: 2024-01-15
length_minutes: 135.5
views: 1234567
description: "..."
is_generated: True
---

[Transcript text as continuous paragraph]
```

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| IP blocked message | YouTube detected automated requests | Switch VPN server, wait 1-2 hours, then resume |
| `No videos.csv files found` | Empty or missing data folders | Run `ytscriber extract` or `ytscriber sync-all` first |
| Command exits immediately | No pending transcripts | Check CSVs - all may already be downloaded |
| `ytscriber: command not found` | CLI not installed | Run `pip install -e .` from repo root |
| Partial download (some videos skipped) | Videos without transcripts/captions | Check YouTube - video may have no captions available |

---

## Common Mistakes

1. **Running without checking disk space** - Transcripts are small (~50KB each), but 10,000 videos = ~500MB. Verify space before overnight runs.

2. **Interrupting during a download** - Safe to Ctrl+C between videos. If you interrupt mid-download, that video's transcript may be incomplete. The CSV won't mark it as downloaded, so it will retry.

3. **Running multiple instances** - Don't run the command twice simultaneously. The 60s delay assumes single-threaded operation to respect rate limits.

4. **Expecting instant results** - The 60s delay is intentional. Faster rates trigger IP blocks. Plan for overnight runs.

---

## Quality Checklist

Before considering batch download complete:

- [ ] All folders show transcript counts in summary output
- [ ] No IP blocked errors (or resolved by VPN switch)
- [ ] Spot-check 2-3 random `.md` files have valid content
- [ ] CSV `transcript_downloaded` column reflects actual downloads

---

## When to Use This vs. download-transcripts

| Scenario | Use |
|----------|-----|
| Download ALL pending transcripts across all channels | `ytscriber download-all` (this skill) |
| Download transcripts for a single specific folder | `ytscriber download --folder <name>` |

---

## Technical Details

- **Rate limiting**: 60 second delay between videos
- **Resumability**: Based on `transcript_downloaded` column in each CSV
- **Dependencies**: Requires `ytscriber` CLI (`pip install -e .`)
