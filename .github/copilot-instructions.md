# GitHub Copilot Instructions for YTScribe

## Skills System

This project uses a skills system located in `.claude/skills/`. When the user types a command starting with `/`, look for a matching skill folder and follow the instructions in its `SKILL.md` file.

### Available Skills

| Command | Skill Location | Purpose |
|---------|----------------|---------|
| `/extract-videos` | `.claude/skills/extract-videos/SKILL.md` | Extract videos from a YouTube channel |
| `/download-transcripts` | `.claude/skills/download-transcripts/SKILL.md` | Download transcripts for videos in a CSV |
| `/add-video-to-collection` | `.claude/skills/add-video-to-collection/SKILL.md` | Manually add a video URL to a collection |
| `/sync-all-channels` | `.claude/skills/sync-all-channels/SKILL.md` | Batch sync all enabled channels |
| `/download-all-transcripts` | `.claude/skills/download-all-transcripts/SKILL.md` | Batch download all pending transcripts |

### How to Use Skills

When the user types `/{skill-name}`, you should:

1. Read the corresponding `SKILL.md` file from `.claude/skills/{skill-name}/SKILL.md`
2. Follow the instructions in that file
3. Execute the relevant commands or actions described

### Example

User: `/add-video-to-collection https://www.youtube.com/watch?v=xyz123 in library-of-minds`

Action: Read `.claude/skills/add-video-to-collection/SKILL.md` and follow the instructions to add the URL to `data/library-of-minds/videos.csv`.

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
- `.claude/skills/` - Skill definitions for AI assistants

## Configuration

- `data/channels.yaml` - Channel configuration for batch operations
- `pyproject.toml` - Python project configuration
