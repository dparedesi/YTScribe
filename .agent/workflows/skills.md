# YTScribe Project Rules

## Skills System

This project uses a skills system. When the user requests a skill using `skill: {name}` or `run {name}`, look for a matching skill in `.claude/skills/` and follow the instructions.

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

### How to Handle Skill Commands

When user says `skill: {name}` or `run {name}` with optional arguments:

1. Read `.claude/skills/{name}/SKILL.md`
2. Follow the instructions in that file
3. Parse any arguments provided by the user
4. Execute the actions described in the skill

### Error Handling

If the user requests an unknown skill:
1. List the available skills from the table above
2. Suggest the closest matching skill if applicable
3. Ask for clarification

### Example

```
User: skill: add-video-to-collection https://www.youtube.com/watch?v=xyz123 in library-of-minds
```

Action:
1. Read `.claude/skills/add-video-to-collection/SKILL.md`
2. Add URL to `data/library-of-minds/videos.csv`
3. Confirm the addition

## Quick Reference (Inline Commands)

If unable to read skill files, use these commands directly:

| Skill | Command |
|-------|---------|
| extract-videos | `transcript-extract <url> --count N --append-csv data/<folder>/videos.csv` |
| download-transcripts | `transcript-download --csv data/<folder>/videos.csv --output-dir data/<folder>/transcripts` |
| add-video-to-collection | Edit `data/<collection>/videos.csv` and add URL row |
| sync-all-channels | `./scripts/sync_all_channels.sh` |
| download-all-transcripts | `./scripts/download_all_transcripts.sh` |
| consolidate-transcripts | `python scripts/consolidate_transcripts.py <channel_name> [--limit TOKENS]` |
| sync-agent-configs | Read all skills, update `.agent/workflows/skills.md` and `.github/copilot-instructions.md` |

## Project Structure

```
YTScribe/
├── src/transcript_downloader/   # Core Python package
├── data/                        # Downloaded data by source
│   ├── channels.yaml           # Channel configuration
│   └── {folder}/videos.csv     # Video tracking per folder
├── scripts/                     # Automation scripts
├── .claude/skills/             # Skill definitions
└── .github/                    # GitHub config
```

## Key Files

- `data/channels.yaml` - Configure which channels to sync (set `enabled: false` to skip)
- `scripts/sync_all_channels.sh` - Batch sync all channels
- `scripts/download_all_transcripts.sh` - Batch download all transcripts

## Agent Configuration Files

| File | Used By |
|------|---------|
| `.github/copilot-instructions.md` | GitHub Copilot |
| `.agent/workflows/skills.md` | Generic agents, Aider, custom tools |
| `.claude/skills/` | Claude Code (native skills system) |
| `.cursorrules` | Cursor (not configured) |
| `CLAUDE.md` | Claude Code project instructions (not configured) |
