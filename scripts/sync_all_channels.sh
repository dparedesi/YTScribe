#!/bin/bash
# sync_all_channels.sh
#
# Wrapper for the ytscriber sync-all command.
#
# Usage: ./scripts/sync_all_channels.sh [args]

set -e

echo "YTScriber - Sync All Channels"

ytscriber sync-all "$@"
