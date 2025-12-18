# GitHub Copilot Instructions for YTScribe

## Skills System

This project uses a skills system located in `.claude/skills/`.

> **Important**: Use `@workspace` in Copilot Chat to give access to project files, then you can read the full skill definitions.

### Invoking Skills

When the user says `skill: {name}` or `run {name}`, look for a matching skill folder and follow the instructions in its `SKILL.md` file.

**Note**: Do NOT use `/` prefix for skills — that conflicts with Copilot's built-in commands like `/explain` and `/fix`.

### Available Skills

| Command | Skill Location | Purpose |
|---------|----------------|---------|
| `skill: extract-videos` | `.claude/skills/extract-videos/SKILL.md` | Extract videos from a YouTube channel |
| `skill: download-transcripts` | `.claude/skills/download-transcripts/SKILL.md` | Download transcripts for videos in a CSV |
| `skill: add-video-to-collection` | `.claude/skills/add-video-to-collection/SKILL.md` | Manually add a video URL to a collection |
| `skill: sync-all-channels` | `.claude/skills/sync-all-channels/SKILL.md` | Batch sync all enabled channels |
| `skill: download-all-transcripts` | `.claude/skills/download-all-transcripts/SKILL.md` | Batch download all pending transcripts |
| `skill: consolidate-transcripts` | `.claude/skills/consolidate-transcripts/SKILL.md` | Consolidate channel transcripts into single file |
| `skill: sync-agent-configs` | `.claude/skills/sync-agent-configs/SKILL.md` | Sync skill definitions to agent proxy files |

### How to Use Skills

When the user says `skill: {name}`, you should:

1. Read the corresponding `SKILL.md` file from `.claude/skills/{name}/SKILL.md`
2. Follow the instructions in that file
3. Execute the relevant commands or actions described

### Error Handling

If the user requests an unknown skill:
1. List the available skills from the table above
2. Suggest the closest matching skill if applicable
3. Ask for clarification

### Example

User: `skill: add-video-to-collection https://www.youtube.com/watch?v=xyz123 in library-of-minds`

Action: Read `.claude/skills/add-video-to-collection/SKILL.md` and follow the instructions to add the URL to `data/library-of-minds/videos.csv`.

## Quick Reference (If Unable to Read Skill Files)

Use these commands directly when skill files aren't accessible:

### extract-videos
```bash
transcript-extract <channel_url> --count <N> --append-csv data/<folder>/videos.csv
```

### download-transcripts
```bash
transcript-download --csv data/<folder>/videos.csv --output-dir data/<folder>/transcripts
```

### add-video-to-collection
1. Open `data/<collection>/videos.csv`
2. Add row: `https://www.youtube.com/watch?v=VIDEO_ID,,,,,,,`
3. Optionally run transcript download

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
Consolidates transcripts from a channel into a single file (newest first, up to 800K tokens).

### sync-agent-configs
This is a maintenance skill. When invoked:
1. Read all `SKILL.md` files from `.claude/skills/*/`
2. Update the Available Skills table in `.agent/workflows/skills.md`
3. Update the Available Skills table in `.github/copilot-instructions.md`
4. Update Quick Reference sections in both files
5. Update Collections table with any new data folders

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

## Collections

| Collection | Path |
|------------|------|
| OpenAI | `data/OpenAI/` |
| a16z | `data/a16z/` |
| aie-code-2025 | `data/aie-code-2025/` |
| aws-reinvent-2025 | `data/aws-reinvent-2025/` |
| dwarkesh-patel | `data/dwarkesh-patel/` |
| library-of-minds | `data/library-of-minds/` |
| random | `data/random/` |
| ryan-peterman | `data/ryan-peterman/` |
| the-diary-of-a-ceo | `data/the-diary-of-a-ceo/` |

## Agent Configuration Files

| File | Used By |
|------|---------|
| `.github/copilot-instructions.md` | GitHub Copilot (this file) |
| `.agent/workflows/skills.md` | Generic agents, Aider, custom tools |
| `.claude/skills/` | Claude Code (native skills system) |
