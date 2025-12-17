---
name: add-video-to-collection
description: Manually add individual YouTube URLs to a custom collection CSV. Use when adding one-off videos to folders like library-of-minds or random, not from a channel extraction.
---

# Add Video to Collection

Manually add individual YouTube video URLs to a custom collection CSV file.

## Use Cases

- Adding videos to curated collections (e.g., `library-of-minds`, `random`)
- Adding one-off videos that aren't from a specific channel
- Building custom playlists of interesting videos

## CSV Format

The CSV should have these columns:
```csv
url,title,duration_minutes,view_count,description,published_date,transcript_downloaded,summary_done
```

## Instructions

1. **Identify the target collection folder** in `data/`:
   - `data/library-of-minds/videos.csv`
   - `data/random/videos.csv`
   - Or create a new folder: `mkdir -p data/<collection-name>`

2. **Add the URL to the CSV**:
   - Open the CSV file
   - Add a new row with at minimum the `url` column filled
   - Other columns can be left empty or populated if known

3. **Example row to add**:
   ```csv
   https://www.youtube.com/watch?v=VIDEO_ID,Optional Title,,,,,
   ```

4. **After adding**, run transcript download:
   ```bash
   transcript-download \
     --csv data/<collection-name>/videos.csv \
     --output-dir data/<collection-name>/transcripts
   ```

## Existing Collections

| Collection | Path | Purpose |
|------------|------|---------|
| library-of-minds | `data/library-of-minds/videos.csv` | Curated thought leaders & interviews |
| random | `data/random/videos.csv` | Miscellaneous interesting videos |

## Quick Add Example

User says: "Add this video to library-of-minds: https://www.youtube.com/watch?v=abc123"

Action:
1. Open `data/library-of-minds/videos.csv`
2. Append row: `https://www.youtube.com/watch?v=abc123,,,,,,,`
3. Optionally run transcript download

## Notes

- Duplicate URLs should be avoided (check before adding)
- The `transcript_downloaded` column will be updated when transcripts are downloaded
- Metadata (title, duration, etc.) will be populated during transcript download
