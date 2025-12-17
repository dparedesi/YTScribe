#!/usr/bin/env python3
"""Rename transcript files to include publication date prefix.

This script renames transcript files from `{video_id}.md` to `YYYY-MM-DD-{video_id}.md`
by extracting the `published_date` from the YAML frontmatter in each file.
"""

import os
import re
from pathlib import Path
from typing import Optional, Tuple


def extract_published_date(file_path: Path) -> Optional[str]:
    """Extract published_date from YAML frontmatter in a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(1000)  # Read first 1000 chars for frontmatter
            
            # Check if file starts with frontmatter
            if not content.startswith('---'):
                return None
            
            # Find published_date field
            match = re.search(r'^published_date:\s*(\d{4}-\d{2}-\d{2})', content, re.MULTILINE)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"  Error reading {file_path}: {e}")
    
    return None


def rename_transcripts_in_folder(folder_path: Path, dry_run: bool = True) -> Tuple[int, int]:
    """Rename all transcript files in a folder.
    
    Returns:
        Tuple of (renamed_count, skipped_count)
    """
    renamed = 0
    skipped = 0
    
    for file_path in folder_path.glob('*.md'):
        filename = file_path.name
        
        # Skip files that already have date prefix (YYYY-MM-DD format)
        if re.match(r'^\d{4}-\d{2}-\d{2}-', filename):
            print(f"  Skipping (already has date): {filename}")
            skipped += 1
            continue
        
        # Extract video_id from filename (without .md extension)
        video_id = file_path.stem
        
        # Get published date from frontmatter
        published_date = extract_published_date(file_path)
        
        if not published_date:
            print(f"  Skipping (no published_date found): {filename}")
            skipped += 1
            continue
        
        # Create new filename
        new_filename = f"{published_date}-{video_id}.md"
        new_path = file_path.parent / new_filename
        
        if dry_run:
            print(f"  Would rename: {filename} -> {new_filename}")
        else:
            file_path.rename(new_path)
            print(f"  Renamed: {filename} -> {new_filename}")
        
        renamed += 1
    
    return renamed, skipped


def main():
    """Main function to rename all transcript files."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Rename transcript files to include publication date prefix'
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Actually perform the rename (default is dry-run)'
    )
    parser.add_argument(
        '--data-dir',
        type=str,
        default='data',
        help='Path to the data directory (default: data)'
    )
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    # Find the data directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    data_dir = project_root / args.data_dir
    
    if not data_dir.exists():
        print(f"Error: Data directory not found: {data_dir}")
        return
    
    print(f"{'DRY RUN - ' if dry_run else ''}Renaming transcript files...")
    print(f"Data directory: {data_dir}")
    print()
    
    total_renamed = 0
    total_skipped = 0
    
    # Find all transcript folders
    for folder in data_dir.iterdir():
        if not folder.is_dir():
            continue
        
        transcripts_dir = folder / 'transcripts'
        if not transcripts_dir.exists():
            continue
        
        print(f"Processing: {folder.name}/transcripts/")
        renamed, skipped = rename_transcripts_in_folder(transcripts_dir, dry_run)
        total_renamed += renamed
        total_skipped += skipped
        print()
    
    print("=" * 50)
    print(f"Total files to rename: {total_renamed}")
    print(f"Total files skipped: {total_skipped}")
    
    if dry_run:
        print()
        print("This was a dry run. Use --execute to actually rename the files.")


if __name__ == '__main__':
    main()
