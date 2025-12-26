# AI Agent Instructions for YTScribe

## Project Overview

YTScribe is a YouTube transcript downloader that:

- Extracts video metadata from YouTube channels
- Downloads transcripts as markdown files with YAML frontmatter
- Tracks progress in CSV files
- Supports both channel-based extraction and manual collections

## Key Directories

- `src/transcript_downloader/` - Core Python package
- `data/` - Downloaded data organized by source
- `scripts/` - Automation scripts for batch operations
- `prompts/` - AI prompts for transcript analysis
- `.agent/skills/` - Skill definitions for Agents (create .claude symlink if needed)

## Configuration

- `data/channels.yaml` - Channel configuration for batch operations
- `pyproject.toml` - Python project configuration

## Available Skills Index
_This index is for IDEs that don't natively support skills (e.g., Gemini CLI, Kiro). Skip if your IDE reads SKILL.md directly._

- **Name:** `add-video-to-collection`
  - **Trigger:** Manually add individual YouTube URLs to a custom collection CSV. Use when adding one-off videos to folders like library-of-minds or random, not from a channel extraction.
  - **Path:** `.agent/skills/add-video-to-collection/SKILL.md`

- **Name:** `consolidate-transcripts`
  - **Trigger:** Consolidate transcripts from a channel into a single file, sorted by date (newest first), up to 800K tokens. Use when preparing transcripts for LLM context or bulk analysis.
  - **Path:** `.agent/skills/consolidate-transcripts/SKILL.md`

- **Name:** `download-all-transcripts`
  - **Trigger:** Download transcripts for all data folders sequentially. Use for overnight batch processing or when you need to download pending transcripts across all channels and collections.
  - **Path:** `.agent/skills/download-all-transcripts/SKILL.md`

- **Name:** `download-transcripts`
  - **Trigger:** Download YouTube transcripts for videos tracked in a CSV file. Use when you need to download transcripts in bulk with progress tracking, fetching transcripts overnight, processing video libraries, or when the user mentions "get transcripts", "download captions", or "bulk transcript download".
  - **Path:** `.agent/skills/download-transcripts/SKILL.md`

- **Name:** `extract-videos`
  - **Trigger:** Extract video metadata from a YouTube channel and save to CSV for tracking. Use when adding a new channel, extracting conference videos, populating video lists, or when the user mentions "extract videos", "get videos from channel", "add channel", or "video metadata".
  - **Path:** `.agent/skills/extract-videos/SKILL.md`

- **Name:** `summarize-transcripts`
  - **Trigger:** Generate AI summaries for downloaded YouTube transcripts. Use when you want to add summaries to existing transcript files, batch process transcripts for summarization, summarize a channel's videos, generate frontmatter summaries, or when the user mentions summarize, AI summaries, OpenRouter, or transcript metadata.
  - **Path:** `.agent/skills/summarize-transcripts/SKILL.md`

- **Name:** `sync-all-channels`
  - **Trigger:** Extract videos from all enabled YouTube channels in channels.yaml. Use for batch updating video lists before downloading transcripts overnight, when the user mentions "sync channels", "update video lists", "refresh channels", or before running download-all-transcripts.
  - **Path:** `.agent/skills/sync-all-channels/SKILL.md`

---

## Quick Reference

Use these commands directly:

### extract-videos

```bash
transcript-extract <channel_url> --count <N> --append-csv data/<folder>/videos.csv
```

### download-transcripts

```bash
transcript-download --csv data/<folder>/videos.csv --output-dir data/<folder>/transcripts
```

### summarize-transcripts

```bash
transcript-summarize <folder-name>
# or
transcript-summarize --all
```

### add-video-to-collection

```bash
transcript-add <youtube_url> --csv data/<collection>/videos.csv
```

### sync-all-channels

```bash
./scripts/sync_all_channels.sh
```

Requires `yq` installed (`brew install yq`)

### download-all-transcripts

```bash
./scripts/download_all_transcripts.sh
```

### consolidate-transcripts

```bash
python scripts/consolidate_transcripts.py <channel_name> [--limit TOKENS] [--verbose]
```

Consolidates transcripts into a single file (newest first, up to 800K tokens by default).
