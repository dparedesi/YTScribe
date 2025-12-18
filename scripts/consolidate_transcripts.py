#!/usr/bin/env python3
"""
Consolidate transcripts from a channel into a single file.

Sorts transcripts by date (newest first) and combines them until
reaching the token limit (default: 800,000 tokens).

Uses tiktoken for accurate token counting to ensure consolidated files
fit within LLM context windows.

Usage:
    python scripts/consolidate_transcripts.py <channel_name> [--limit TOKENS]

Examples:
    python scripts/consolidate_transcripts.py library-of-minds
    python scripts/consolidate_transcripts.py aws-reinvent-2025 --limit 500000
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False


# Cache the encoder to avoid re-creating it for each file
_encoder = None


def get_encoder():
    """Get tiktoken encoder (cached)."""
    global _encoder
    if _encoder is None:
        if not TIKTOKEN_AVAILABLE:
            raise ImportError(
                "tiktoken is required for token counting. "
                "Install it with: pip install tiktoken"
            )
        # Use cl100k_base which is used by GPT-4 and similar to Claude's tokenizer
        _encoder = tiktoken.get_encoding("cl100k_base")
    return _encoder


def count_tokens(text: str) -> int:
    """Count tokens in text using tiktoken."""
    encoder = get_encoder()
    return len(encoder.encode(text))


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def extract_date_from_filename(filename: str) -> str:
    """Extract date from filename format: YYYY-MM-DD-{video_id}.md"""
    match = re.match(r"(\d{4}-\d{2}-\d{2})-", filename)
    if match:
        return match.group(1)
    return "0000-00-00"  # Files without date go last


def extract_title_from_frontmatter(content: str) -> str:
    """Extract title from YAML frontmatter."""
    match = re.search(r"^title:\s*(.+)$", content, re.MULTILINE)
    if match:
        return match.group(1).strip().strip('"\'')
    return "Unknown Title"


def extract_frontmatter_field(content: str, field: str) -> str:
    """Extract a field from YAML frontmatter."""
    match = re.search(rf"^{field}:\s*(.+)$", content, re.MULTILINE)
    if match:
        return match.group(1).strip().strip('"\'')
    return ""


def get_transcript_body(content: str) -> str:
    """Extract transcript body (everything after the YAML frontmatter)."""
    # Find the closing --- of frontmatter
    parts = content.split("---", 2)
    if len(parts) >= 3:
        return parts[2].strip()
    return content.strip()


def consolidate_transcripts(
    channel_name: str,
    token_limit: int = 800_000,
    data_dir: Path = None,
    output_dir: Path = None,
) -> dict:
    """
    Consolidate transcripts from a channel.

    Args:
        channel_name: Name of the channel folder in data/
        token_limit: Maximum tokens to include (default: 900,000)
        data_dir: Path to data directory (default: data/)
        output_dir: Path to output directory (default: consolidated/)

    Returns:
        dict with stats about the consolidation
    """
    # Set default paths
    repo_root = Path(__file__).parent.parent
    if data_dir is None:
        data_dir = repo_root / "data"
    if output_dir is None:
        output_dir = repo_root / "consolidated"

    transcripts_dir = data_dir / channel_name / "transcripts"

    # Validate channel exists
    if not transcripts_dir.exists():
        raise ValueError(f"Transcripts directory not found: {transcripts_dir}")

    # Find all transcript files
    transcript_files = list(transcripts_dir.glob("*.md"))
    if not transcript_files:
        raise ValueError(f"No transcript files found in: {transcripts_dir}")

    # Sort by date in filename (newest first)
    transcript_files.sort(key=lambda f: extract_date_from_filename(f.name), reverse=True)

    # Collect transcripts until token limit
    consolidated_parts = []
    included_files = []
    total_tokens = 0
    total_words = 0
    skipped_files = []

    for filepath in transcript_files:
        content = filepath.read_text(encoding="utf-8")
        body = get_transcript_body(content)
        token_count = count_tokens(body)
        word_count = count_words(body)

        # Check if adding this file would exceed limit
        if total_tokens + token_count > token_limit:
            skipped_files.append({
                "file": filepath.name,
                "tokens": token_count,
                "words": word_count,
                "reason": "token_limit_exceeded"
            })
            continue

        # Extract metadata
        title = extract_title_from_frontmatter(content)
        date = extract_date_from_filename(filepath.name)
        video_url = extract_frontmatter_field(content, "video_url")
        author = extract_frontmatter_field(content, "author")

        # Add separator and transcript
        separator = f"\n\n---\n\n## {title}\n\n"
        if date != "0000-00-00":
            separator += f"**Date:** {date}\n"
        if author:
            separator += f"**Author:** {author}\n"
        if video_url:
            separator += f"**Source:** {video_url}\n"
        separator += f"**Tokens:** {token_count:,} | **Words:** {word_count:,}\n\n"

        consolidated_parts.append(separator + body)
        included_files.append({
            "file": filepath.name,
            "title": title,
            "date": date,
            "tokens": token_count,
            "words": word_count
        })
        total_tokens += token_count
        total_words += word_count

    # Create output directory if needed
    output_dir.mkdir(parents=True, exist_ok=True)

    # Build consolidated file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"""# {channel_name} - Consolidated Transcripts

**Generated:** {timestamp}
**Total transcripts:** {len(included_files)}
**Total tokens:** {total_tokens:,}
**Total words:** {total_words:,}
**Token limit:** {token_limit:,}
**Skipped:** {len(skipped_files)} files (would exceed limit)

## Included Transcripts

| # | Date | Title | Tokens | Words |
|---|------|-------|--------|-------|
"""

    for i, f in enumerate(included_files, 1):
        title_truncated = f["title"][:45] + "..." if len(f["title"]) > 45 else f["title"]
        header += f"| {i} | {f['date']} | {title_truncated} | {f['tokens']:,} | {f['words']:,} |\n"

    header += "\n---\n"

    # Write consolidated file
    output_file = output_dir / f"{channel_name}-consolidated.md"
    output_content = header + "".join(consolidated_parts)
    output_file.write_text(output_content, encoding="utf-8")

    # Count tokens in final output (includes header and formatting)
    final_token_count = count_tokens(output_content)

    return {
        "channel": channel_name,
        "output_file": str(output_file),
        "included_count": len(included_files),
        "skipped_count": len(skipped_files),
        "total_tokens": total_tokens,
        "total_words": total_words,
        "final_tokens": final_token_count,
        "token_limit": token_limit,
        "included_files": included_files,
        "skipped_files": skipped_files
    }


def main():
    parser = argparse.ArgumentParser(
        description="Consolidate transcripts from a channel into a single file."
    )
    parser.add_argument(
        "channel",
        help="Channel name (folder name in data/)"
    )
    parser.add_argument(
        "--limit", "-l",
        type=int,
        default=800_000,
        help="Maximum tokens to include (default: 800000)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output"
    )

    args = parser.parse_args()

    try:
        result = consolidate_transcripts(args.channel, args.limit)

        print(f"\n✅ Consolidated {result['included_count']} transcripts")
        print(f"   Total tokens: {result['total_tokens']:,} (content)")
        print(f"   Final tokens: {result['final_tokens']:,} (with headers)")
        print(f"   Total words: {result['total_words']:,}")
        print(f"   Skipped: {result['skipped_count']} files (exceeded {result['token_limit']:,} token limit)")
        print(f"   Output: {result['output_file']}")

        if args.verbose and result['included_files']:
            print("\n📄 Included transcripts:")
            for f in result['included_files']:
                print(f"   - {f['date']} | {f['title'][:40]}... ({f['tokens']:,} tokens)")

        if args.verbose and result['skipped_files']:
            print("\n⏭️  Skipped transcripts:")
            for f in result['skipped_files']:
                print(f"   - {f['file']} ({f['tokens']:,} tokens)")

    except ImportError as e:
        print(f"❌ {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
