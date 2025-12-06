#!/bin/bash
# KubeCon conference video extraction and transcript download

set -e

CONFERENCE="kubecon-eu-2024"
CHANNEL_URL="https://www.youtube.com/@cncf/videos"
VIDEO_COUNT=75

echo "☸️  KubeCon EU 2024 Transcript Extraction"
echo "========================================"
echo ""

# Create directory structure
echo "Creating directory: data/${CONFERENCE}"
mkdir -p "data/${CONFERENCE}"

# Step 1: Extract video list
echo ""
echo "Step 1/2: Extracting ${VIDEO_COUNT} latest videos from channel..."
transcript-extract "${CHANNEL_URL}" \
  --count ${VIDEO_COUNT} \
  --append-csv "data/${CONFERENCE}/videos.csv"

# Step 2: Download transcripts
echo ""
echo "Step 2/2: Downloading transcripts (60s delay between requests)..."
echo "This may take a while. Press Ctrl+C to stop (progress is saved)."
transcript-download \
  --csv "data/${CONFERENCE}/videos.csv" \
  --output-dir "data/${CONFERENCE}/transcripts" \
  --delay 60

echo ""
echo "✅ Complete! Transcripts saved to data/${CONFERENCE}/transcripts/"
echo ""
echo "Next steps:"
echo "  - View transcripts: ls data/${CONFERENCE}/transcripts/"
echo "  - Search topics: grep -r 'security' data/${CONFERENCE}/transcripts/"
echo "  - Check status: cat data/${CONFERENCE}/videos.csv"
