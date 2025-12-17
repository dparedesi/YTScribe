#!/bin/bash
# download_all_transcripts.sh
#
# Sequentially download transcripts for ALL data folders.
# Includes both channel folders and manual collections.
#
# Usage: ./scripts/download_all_transcripts.sh
#
# Note: Runs sequentially with 60s delay between videos to avoid rate limiting.
# This script is designed to run overnight.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$REPO_ROOT/data"
DELAY=60  # seconds between video downloads

echo "📝 YTScribe - Download All Transcripts"
echo "======================================="
echo "Started at: $(date)"
echo "Delay between videos: ${DELAY}s"
echo ""

# Find all folders with a videos.csv file
FOLDERS=$(find "$DATA_DIR" -name "videos.csv" -type f | sort)

if [ -z "$FOLDERS" ]; then
    echo "❌ No videos.csv files found in $DATA_DIR"
    exit 1
fi

FOLDER_COUNT=$(echo "$FOLDERS" | wc -l | tr -d ' ')
echo "Found $FOLDER_COUNT folders with videos.csv"
echo ""

CURRENT=1
for CSV_FILE in $FOLDERS; do
    FOLDER_PATH=$(dirname "$CSV_FILE")
    FOLDER_NAME=$(basename "$FOLDER_PATH")
    TRANSCRIPTS_DIR="$FOLDER_PATH/transcripts"
    
    echo "────────────────────────────────────────"
    echo "[$CURRENT/$FOLDER_COUNT] Processing: $FOLDER_NAME"
    echo "  CSV: $CSV_FILE"
    echo "  Output: $TRANSCRIPTS_DIR"
    echo ""
    
    # Create transcripts directory if it doesn't exist
    mkdir -p "$TRANSCRIPTS_DIR"
    
    # Download transcripts
    transcript-download \
        --csv "$CSV_FILE" \
        --output-dir "$TRANSCRIPTS_DIR" \
        --delay "$DELAY" \
        || echo "⚠️  Warning: Some errors in $FOLDER_NAME, continuing..."
    
    echo ""
    echo "✅ Completed: $FOLDER_NAME"
    echo ""
    
    CURRENT=$((CURRENT + 1))
done

echo "════════════════════════════════════════"
echo "✅ All transcripts downloaded!"
echo "Finished at: $(date)"
echo ""
echo "Summary of folders processed:"
for CSV_FILE in $FOLDERS; do
    FOLDER_NAME=$(basename "$(dirname "$CSV_FILE")")
    TRANSCRIPT_COUNT=$(find "$(dirname "$CSV_FILE")/transcripts" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
    echo "  - $FOLDER_NAME: $TRANSCRIPT_COUNT transcripts"
done
