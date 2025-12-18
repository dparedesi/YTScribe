---
name: consolidate-transcripts
description: Consolidate transcripts from a channel into a single file, sorted by date (newest first), up to 550K words. Use when preparing transcripts for LLM context or bulk analysis.
---

# Consolidate Transcripts

## Overview

Combine multiple transcripts from a channel into a single consolidated file. Transcripts are sorted by date (newest first) and included until reaching the word limit (default: 550,000 words). Output is saved to the `consolidated/` folder.

## Command

```bash
python scripts/consolidate_transcripts.py <channel_name> [--limit WORDS] [--verbose]
```

## Parameters

| Option | Description | Default |
|--------|-------------|---------|
| `channel_name` | Folder name in `data/` | Required |
| `--limit, -l` | Maximum words to include | 550000 |
| `--verbose, -v` | Show detailed file list | False |

## Instructions

1. Identify the channel name (folder in `data/`):
   ```bash
   ls data/
   ```

2. Run the consolidation:
   ```bash
   python scripts/consolidate_transcripts.py <channel_name>
   ```

3. Output will be saved to:
   ```
   consolidated/<channel_name>-consolidated.md
   ```

## Examples

```bash
# Consolidate library-of-minds (up to 550K words)
python scripts/consolidate_transcripts.py library-of-minds

# Consolidate with custom word limit
python scripts/consolidate_transcripts.py aws-reinvent-2025 --limit 500000

# Verbose output showing all included files
python scripts/consolidate_transcripts.py dwarkesh-patel --verbose
```

## Output Format

The consolidated file includes:

1. **Header** with generation metadata:
   - Total transcripts included
   - Total word count
   - Table of contents with dates and titles

2. **Transcripts** separated by markdown headers:
   - Title, date, author, source URL
   - Word count per transcript
   - Full transcript text

## Use Cases

- **LLM Context**: Prepare transcripts for Claude/GPT analysis with ~550K word context window
- **Search/RAG**: Create a single searchable document per channel
- **Backup**: Consolidated archive of channel content
- **Analysis**: Bulk text analysis across multiple videos

## Notes

- Transcripts are sorted **newest first** (descending by date)
- Files without dates in filename are placed last
- The `consolidated/` folder is gitignored (not pushed to remote)
- Re-running overwrites the previous consolidated file for that channel
- Word limit prevents exceeding LLM context windows
