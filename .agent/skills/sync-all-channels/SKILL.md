---
name: sync-all-channels
description: Extract videos from all enabled YouTube channels in channels.yaml. Use for batch updating video lists before downloading transcripts overnight, when the user mentions "sync channels", "update video lists", "refresh channels", or before running download-all-transcripts.
---

# Sync All Channels

**Why?** Manually running extract-videos on each channel is tedious and error-prone. This skill automates batch extraction with rate limiting to respect YouTube's API.

## Quick Start

```bash
# Run the unified CLI command
ytscriber sync-all
```

> [!TIP]
> Run this before `ytscriber download-all` to ensure video lists are current.

---

## Workflow

### 1. Review Channel Configuration

Check `~/Documents/YTScriber/channels.yaml` and verify:
- All desired channels have `enabled: true`
- Video counts are appropriate (20-100 typical)
- URLs point to channel video pages

```yaml
channels:
  - folder: OpenAI
    url: https://www.youtube.com/@OpenAI/videos
    count: 50
    enabled: true

collections:
  - library-of-minds
  - random
```

> [!CAUTION]
> Setting `count` above 200 significantly increases sync time and may trigger rate limiting.

### 2. Execute the Sync

```bash
ytscriber sync-all
```

The command will:
1. Parse `channels.yaml`
2. Skip channels with `enabled: false`
3. Extract videos for each enabled channel
4. Wait between channels (rate limiting)
5. Report completion and next steps

### 3. Verify Results

After completion, check:
- Each channel folder exists
- Each folder contains `videos.csv` with entries
- No persistent errors in output

```bash
# Quick verification
ls -la ~/Documents/YTScriber/*/videos.csv | head -10
```

---

## Configuration

### Adding a New Channel

1. Add entry to `channels.yaml`:
   ```yaml
   - folder: new-channel-name
     url: https://www.youtube.com/@ChannelName/videos
     count: 50
     enabled: true
   ```

2. Run sync - folder is created automatically

Or use the extract command with `--register-channel`:
```bash
ytscriber extract https://www.youtube.com/@ChannelName/videos \
  --count 50 \
  --folder new-channel-name \
  --register-channel
```

> [!WARNING]
> Folder names should use lowercase with hyphens (e.g., `my-channel`). Avoid spaces or special characters.

### Disabling a Channel

Set `enabled: false` - the channel will be skipped during sync but data is preserved.

### Recommended Video Counts

| Channel Type | Recommended Count |
|-------------|-------------------|
| Infrequent posters (1-2/month) | 20 |
| Regular posters (weekly) | 50 |
| High-volume (daily) | 100 |
| Conference channels | 100-200 |

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| `Config file not found` | Running from wrong directory or channels.yaml missing | Ensure `~/Documents/YTScriber/channels.yaml` exists |
| `Failed to sync [channel]` | Network issue or invalid URL | Check URL is accessible in browser, retry |
| Sync takes forever | Too many channels or high counts | Reduce counts or disable some channels |
| Empty videos.csv | Channel has no public videos or URL is wrong | Verify URL ends in `/videos` |
| Rate limit errors | Too many requests | Wait 1 hour and retry; reduce counts |

---

## Common Mistakes

1. **Wrong URL format** - Use `https://www.youtube.com/@ChannelName/videos` not `/channel/` or `/c/` URLs
2. **Forgetting to enable** - New channels default to `enabled: false` in templates
3. **Excessive counts** - Starting with `count: 500` causes long waits; start with 50

---

## Next Steps

After syncing channels:

```bash
# Download transcripts for all synced videos
ytscriber download-all
```

---

## Quality Checklist

Before running sync:
- [ ] `channels.yaml` exists and is valid YAML
- [ ] At least one channel has `enabled: true`

After sync completes:
- [ ] No persistent errors in output (warnings OK)
- [ ] Each enabled channel has `videos.csv`
- [ ] CSV files contain video entries

---

## Rate Limiting Details

- **Sequential processing** - one channel at a time
- **Graceful failure** - if one channel fails, others continue

> [!TIP]
> For overnight batch operations, run sync first, then download-all. This sequence ensures video lists are current before downloading.
