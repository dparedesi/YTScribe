#!/bin/bash
# sync_all_channels.sh
# 
# Sequentially extract videos from all configured YouTube channels.
# Run this to update your video lists before downloading transcripts.
#
# Usage: ./scripts/sync_all_channels.sh
#
# Note: Runs sequentially to avoid rate limiting.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$REPO_ROOT/data/channels.yaml"

echo "📹 YTScribe - Sync All Channels"
echo "================================"
echo "Started at: $(date)"
echo ""

# Check if yq is installed (for parsing YAML)
if ! command -v yq &> /dev/null; then
    echo "❌ Error: 'yq' is required but not installed."
    echo "   Install with: brew install yq"
    exit 1
fi

# Check if config file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ Error: Config file not found: $CONFIG_FILE"
    exit 1
fi

# Get channel count
CHANNEL_COUNT=$(yq '.channels | length' "$CONFIG_FILE")
echo "Found $CHANNEL_COUNT channels to sync"
echo ""

# Process each channel sequentially
PROCESSED=0
for i in $(seq 0 $((CHANNEL_COUNT - 1))); do
    FOLDER=$(yq ".channels[$i].folder" "$CONFIG_FILE")
    URL=$(yq ".channels[$i].url" "$CONFIG_FILE")
    COUNT=$(yq ".channels[$i].count" "$CONFIG_FILE")
    ENABLED=$(yq ".channels[$i].enabled // true" "$CONFIG_FILE")
    
    echo "────────────────────────────────────────"
    
    # Skip disabled channels
    if [ "$ENABLED" != "true" ]; then
        echo "[$((i + 1))/$CHANNEL_COUNT] Skipping (disabled): $FOLDER"
        echo ""
        continue
    fi
    
    echo "[$((i + 1))/$CHANNEL_COUNT] Syncing: $FOLDER"
    echo "  URL: $URL"
    echo "  Count: $COUNT videos"
    echo ""
    
    # Create directory if it doesn't exist
    mkdir -p "$REPO_ROOT/data/$FOLDER"
    
    # Extract videos
    transcript-extract "$URL" \
        --count "$COUNT" \
        --append-csv "$REPO_ROOT/data/$FOLDER/videos.csv" \
        || echo "⚠️  Warning: Failed to sync $FOLDER, continuing..."
    
    echo ""
    echo "✅ Completed: $FOLDER"
    echo ""
    
    PROCESSED=$((PROCESSED + 1))
    
    # Small delay between channels to be respectful
    if [ $i -lt $((CHANNEL_COUNT - 1)) ]; then
        echo "⏳ Waiting 10 seconds before next channel..."
        sleep 10
    fi
done

echo "════════════════════════════════════════"
echo "✅ All channels synced!"
echo "Finished at: $(date)"
echo ""
echo "Next step: Run ./scripts/download_all_transcripts.sh"
