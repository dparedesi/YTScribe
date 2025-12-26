---
name: sync-all-channels
description: Extract videos from all enabled YouTube channels in channels.yaml. Use for batch updating video lists before downloading transcripts overnight.
---

# Sync All Channels

## Overview

Sequentially extract new videos from all enabled YouTube channels configured in `data/channels.yaml`. Run this before batch transcript downloads to ensure video lists are up-to-date.

## Command

```bash
./scripts/sync_all_channels.sh
```

## Prerequisites

- Install `yq` (YAML parser): `brew install yq`

## Configuration

Edit `data/channels.yaml` to manage channels:

```yaml
channels:
  - folder: aws-reinvent-2025
    url: https://www.youtube.com/@AWSEventsChannel/videos
    count: 100
    enabled: true   # Set to false to skip this channel

  - folder: OpenAI
    url: https://www.youtube.com/@OpenAI/videos
    count: 50
    enabled: false  # This channel will be skipped

collections:
  - library-of-minds  # Manual collections (not synced)
  - random
```

## Adding a New Channel

1. Add entry to `data/channels.yaml`:
   ```yaml
   - folder: new-channel-name
     url: https://www.youtube.com/@ChannelName/videos
     count: 50
     enabled: true
   ```

2. The script will create the folder automatically

## Disabling a Channel

Set `enabled: false` in the config - the channel will be skipped during sync.

## Rate Limiting

- 10 second delay between channels
- Runs sequentially (not parallel)

## Next Step

After syncing, run transcript download:
```bash
./scripts/download_all_transcripts.sh
```
