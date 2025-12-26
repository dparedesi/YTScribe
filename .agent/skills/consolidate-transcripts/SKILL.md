---
name: consolidate-transcripts
description: Consolidate transcripts from a channel into a single file, sorted by date (newest first), up to 800K tokens. Use when preparing transcripts for LLM context or bulk analysis.
---

# Consolidate Transcripts

## Overview

Combine multiple transcripts from a channel into a single consolidated file. Transcripts are sorted by date (newest first) and included until reaching the token limit (default: 800,000 tokens). Output is saved directly in the channel folder (`data/<channel>/`).

Uses `tiktoken` for accurate token counting to ensure consolidated files fit within LLM context windows.

## Command

```bash
python scripts/consolidate_transcripts.py <channel_name> [--limit TOKENS] [--verbose]
```

## Parameters

| Option | Description | Default |
|--------|-------------|---------|
| `channel_name` | Folder name in `data/` | Required |
| `--limit, -l` | Maximum tokens to include | 800000 |
| `--verbose, -v` | Show detailed file list | False |

## Prerequisites

Install tiktoken (one-time setup):
```bash
pip install tiktoken
```

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
   data/<channel_name>/<channel_name>-consolidated.md
   ```

## Examples

```bash
# Consolidate library-of-minds (up to 800K tokens)
python scripts/consolidate_transcripts.py library-of-minds

# Consolidate with custom token limit
python scripts/consolidate_transcripts.py aws-reinvent-2025 --limit 500000

# Verbose output showing all included files
python scripts/consolidate_transcripts.py dwarkesh-patel --verbose
```

## Output Format

The consolidated file includes:

1. **Header** with generation metadata:
   - Total transcripts included
   - Total token and word count
   - Table of contents with dates, titles, tokens, and words

2. **Transcripts** separated by markdown headers:
   - Title, date, author, source URL
   - Token and word count per transcript
   - Full transcript text

## Use Cases

- **LLM Context**: Prepare transcripts for Claude/GPT analysis within context limits
- **Search/RAG**: Create a single searchable document per channel
- **Backup**: Consolidated archive of channel content
- **Analysis**: Bulk text analysis across multiple videos

## Notes

- Transcripts are sorted **newest first** (descending by date)
- Files without dates in filename are placed last
- Consolidated files (`*-consolidated.md`) are gitignored (not pushed to remote)
- Re-running overwrites the previous consolidated file for that channel
- Token counting uses `cl100k_base` encoding (GPT-4/Claude compatible)
- Default 800K token limit leaves ~200K tokens for prompts and responses
