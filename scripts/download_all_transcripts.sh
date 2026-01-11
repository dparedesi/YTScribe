#!/bin/bash
# download_all_transcripts.sh
#
# Wrapper for the ytscriber download-all command.
#
# Usage: ./scripts/download_all_transcripts.sh [args]

set -e

echo "YTScriber - Download All Transcripts"

ytscriber download-all "$@"
