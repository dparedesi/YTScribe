---
name: add-video-to-collection
description: Manually add individual YouTube URLs to a custom collection CSV. Use when adding one-off videos to folders like library-of-minds or random, not from a channel extraction.
---

# Add Video to Collection

## Overview

Add individual YouTube video URLs to a custom collection CSV file. Use this for curated collections like `library-of-minds` or `random`, where videos come from various sources rather than a single channel.

## Use Cases

- Adding videos to curated collections (e.g., `library-of-minds`, `random`)
- Adding one-off videos that aren't from a specific channel
- Building custom playlists of interesting videos

## Instructions

**ALWAYS use the `transcript-add` CLI command** to add videos. This ensures:
- Duplicate detection (skips if URL already exists)
- Proper CSV formatting (no newline issues)
- Canonical URL normalization

### Command

```bash
transcript-add <youtube-url> --csv data/<collection>/videos.csv
```

### Examples

```bash
# Add to random collection
transcript-add https://www.youtube.com/watch?v=VIDEO_ID --csv data/random/videos.csv

# Add to library-of-minds
transcript-add https://www.youtube.com/watch?v=abc123 --csv data/library-of-minds/videos.csv

# Verbose output
transcript-add https://www.youtube.com/watch?v=xyz789 --csv data/random/videos.csv -v
```

## Existing Collections

| Collection | CSV Path | Purpose |
|------------|----------|---------|
| library-of-minds | `data/library-of-minds/videos.csv` | Curated thought leaders & interviews |
| random | `data/random/videos.csv` | Miscellaneous interesting videos |

## Quick Add Example

User says: "Add this video to library-of-minds: https://www.youtube.com/watch?v=abc123"

Action:
```bash
transcript-add https://www.youtube.com/watch?v=abc123 --csv data/library-of-minds/videos.csv
```

Expected output:
- `✓ Added video abc123 to data/library-of-minds/videos.csv` (if new)
- `⊘ Video abc123 already exists in data/library-of-minds/videos.csv` (if duplicate)

## After Adding (Optional)

Once you are done, ask the user if they also want to download transcript for the newly added video. If so, run:
```bash
transcript-download --csv data/<collection>/videos.csv --output-dir data/<collection>/transcripts
```

## Notes

- **DO NOT manually edit CSV files** to add videos — always use `transcript-add`
- The CLI automatically handles duplicate checking
- URLs are normalized to canonical format: `https://www.youtube.com/watch?v=VIDEO_ID`
- The CSV will be created with proper headers if it doesn't exist
- Metadata (title, duration, etc.) will be populated during transcript download
