#!/bin/bash
# KubeCon conference video extraction and transcript download

set -e

CONFERENCE="kubecon-eu-2024"
CHANNEL_URL="https://www.youtube.com/@cncf/videos"
VIDEO_COUNT=75

echo "KubeCon EU 2024 Transcript Extraction"
echo "========================================"
echo ""

# Step 1: Extract video list
echo "Step 1/2: Extracting ${VIDEO_COUNT} latest videos from channel..."
ytscriber extract "${CHANNEL_URL}" \
  --count ${VIDEO_COUNT} \
  --folder "${CONFERENCE}" \
  --register-channel

# Step 2: Download transcripts
echo ""
echo "Step 2/2: Downloading transcripts (60s delay between requests)..."
echo "This may take a while. Press Ctrl+C to stop (progress is saved)."
ytscriber download \
  --folder "${CONFERENCE}" \
  --delay 60

echo ""
echo "Complete!"
echo "Next steps:"
echo "  - Check status: ytscriber status"
