#!/usr/bin/env python3
"""
Script to count words in the summary field of YAML frontmatter
in markdown files in transcript directories.

Usage:
    # Default: searches in data/aws-reinvent-2025/transcripts/
    python summary_word_count.py
    
    # Specify a different conference
    python summary_word_count.py --conference pycon-2024
    
    # Or specify a custom directory
    python summary_word_count.py --dir outputs
"""

import argparse
import os
import csv
import re
from pathlib import Path

def extract_yaml_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    # Match YAML frontmatter between --- markers
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def extract_summary(yaml_content):
    """Extract summary field from YAML content."""
    if not yaml_content:
        return None
    
    # Look for summary field in YAML
    # Handle both single-line and multi-line summaries (with | or >)
    
    # First check if it's a multi-line block (starts with | or >)
    match = re.search(r'^summary:\s*[|>]\s*\n((?:(?:[ ]{2,}.*|)\n)*)', yaml_content, re.MULTILINE)
    if match:
        # Extract all indented content (including blank lines within the block)
        summary_block = match.group(1)
        # Remove the indentation from each line and join, preserving paragraph breaks
        lines = []
        for line in summary_block.split('\n'):
            stripped = line.strip()
            if stripped or lines:  # Include line if it has content or if we've started collecting
                lines.append(stripped)
        # Remove trailing empty lines
        while lines and not lines[-1]:
            lines.pop()
        summary = '\n'.join(lines)
        return summary if summary else None
    
    # Otherwise try single-line format
    match = re.search(r'^summary:\s*(.+?)(?=\n\w+:|$)', yaml_content, re.MULTILINE | re.DOTALL)
    if match:
        summary = match.group(1).strip()
        # Remove quotes if present
        summary = summary.strip('"\'')
        return summary
    
    return None

def count_words(text):
    """Count words in text."""
    if not text:
        return 0
    # Split by whitespace and count
    return len(text.split())

def main():
    parser = argparse.ArgumentParser(
        description='Count words in summaries from transcript markdown files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Default: use data/aws-reinvent-2025/transcripts/
  python summary_word_count.py
  
  # Specify a different conference
  python summary_word_count.py --conference pycon-2024
  
  # Use a custom directory
  python summary_word_count.py --dir outputs
        """
    )
    parser.add_argument('--conference', '-c', default='aws-reinvent-2025',
                       help='Conference name (looks in data/<conference>/transcripts/)')
    parser.add_argument('--dir', '-d', help='Custom directory path (overrides --conference)')
    parser.add_argument('--output', '-o', help='Output CSV file (default: summary_word_counts.csv)')
    
    args = parser.parse_args()
    
    # Determine the directory to scan
    if args.dir:
        transcripts_dir = Path(args.dir)
    else:
        transcripts_dir = Path(__file__).parent / "data" / args.conference / "transcripts"
    
    if not transcripts_dir.exists():
        print(f"Error: Directory not found: {transcripts_dir}")
        print(f"\nTip: Use --conference <name> or --dir <path> to specify the location")
        return 1
    
    print(f"Scanning directory: {transcripts_dir}")
    
    # List to store results
    results = []
    
    # Process all .md files in the directory
    md_files = sorted(transcripts_dir.glob("*.md"))
    
    if not md_files:
        print(f"No markdown files found in {transcripts_dir}")
        return 1
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract YAML frontmatter
            yaml_content = extract_yaml_frontmatter(content)
            
            # Extract summary
            summary = extract_summary(yaml_content)
            
            # Count words
            word_count = count_words(summary)
            
            # Only add to results if there's a summary
            if summary:
                results.append({
                    'filename': md_file.name,
                    'word_count': word_count,
                    'summary': summary
                })
        
        except Exception as e:
            print(f"Error processing {md_file.name}: {e}")
    
    # Write results to CSV
    output_csv = Path(args.output) if args.output else Path(__file__).parent / "summary_word_counts.csv"
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['filename', 'word_count', 'summary'])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"\nProcessed {len(md_files)} markdown files")
    print(f"Found {len(results)} files with summaries")
    print(f"Results saved to: {output_csv}")
    
    # Print some statistics
    if results:
        word_counts = [r['word_count'] for r in results]
        print(f"\nSummary statistics:")
        print(f"  Total files with summaries: {len(results)}")
        print(f"  Average word count: {sum(word_counts) / len(word_counts):.1f}")
        print(f"  Min word count: {min(word_counts)}")
        print(f"  Max word count: {max(word_counts)}")
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
