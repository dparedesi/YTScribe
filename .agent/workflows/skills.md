# YTScribe Project Rules

## Skills System

This project uses a skills system. When the user types a command starting with `/`, look for a matching skill in `.claude/skills/` and follow the instructions.

### Skill Locations

- `/extract-videos` → `.claude/skills/extract-videos/SKILL.md`
- `/download-transcripts` → `.claude/skills/download-transcripts/SKILL.md`
- `/add-video-to-collection` → `.claude/skills/add-video-to-collection/SKILL.md`
- `/sync-all-channels` → `.claude/skills/sync-all-channels/SKILL.md`
- `/download-all-transcripts` → `.claude/skills/download-all-transcripts/SKILL.md`

### How to Handle Skill Commands

When user types `/{skill-name} [arguments]`:

1. Read `.claude/skills/{skill-name}/SKILL.md`
2. Follow the instructions in that file
3. Parse any arguments provided by the user
4. Execute the actions described in the skill

### Example

```
User: /add-video-to-collection https://www.youtube.com/watch?v=xyz123 in library-of-minds
```

Action:
1. Read `.claude/skills/add-video-to-collection/SKILL.md`
2. Add URL to `data/library-of-minds/videos.csv`
3. Confirm the addition

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

## CLI Commands

```bash
# Extract videos from a channel
transcript-extract <channel_url> --count <N> --append-csv <output.csv>

# Download transcripts
transcript-download --csv <input.csv> --output-dir <directory>
```
