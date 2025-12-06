# YTScribe: Conference Transcript Downloader

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Download YouTube transcripts from conference channels and organize them for analysis, summarization, and archival.

## Features

- 📹 **Extract videos** from any YouTube channel
- 📝 **Download transcripts** with metadata (title, author, duration, etc.)
- 📄 **Save as markdown** files with YAML frontmatter for easy processing
- 🔄 **Track progress** in CSV files to resume interrupted downloads
- 🛡️ **Rate limiting** with automatic IP block detection
- 🎯 **Type-safe** with full type hints and mypy support

## Installation

### From source (recommended)

```bash
git clone https://github.com/danielparedes/conference-transcript-downloader.git
cd conference-transcript-downloader
pip install -e .
```

### Development installation

```bash
pip install -e ".[dev]"
```

## Quick Start

```bash
# Extract videos from a conference channel
transcript-extract https://www.youtube.com/@AWSEventsChannel/videos \
  --count 100 \
  --append-csv data/aws-reinvent-2025/videos.csv

# Download transcripts
transcript-download \
  --csv data/aws-reinvent-2025/videos.csv \
  --output-dir data/aws-reinvent-2025/transcripts
```

Or use the legacy scripts directly:

```bash
python extract_channel_videos.py https://www.youtube.com/@AWSEventsChannel/videos \
  --count 100 \
  --append-csv data/aws-reinvent-2025/videos.csv

python download_youtube_transcript.py \
  --csv data/aws-reinvent-2025/videos.csv \
  --output-dir data/aws-reinvent-2025/transcripts
```

## Usage

### Extract videos from a channel

```bash
transcript-extract <channel_url> --count <number> --append-csv <output.csv>
```

**Examples:**

```bash
# AWS re:Invent 2025
transcript-extract https://www.youtube.com/@AWSEventsChannel/videos \
  --count 100 \
  --append-csv data/aws-reinvent-2025/videos.csv

# PyCon US
transcript-extract https://www.youtube.com/@PyConUS \
  --count 50 \
  --append-csv data/pycon-2024/videos.csv

# KubeCon
transcript-extract https://www.youtube.com/@cncf/videos \
  --count 75 \
  --append-csv data/kubecon-2024/videos.csv
```

**Options:**

| Option | Description | Default |
|--------|-------------|---------|
| `--count, -n` | Number of latest videos to extract | 10 |
| `--append-csv` | Create or append to CSV file | - |
| `--output, -o` | Save video IDs to text file | - |
| `--verbose, -v` | Enable verbose output | False |

### Download transcripts

```bash
transcript-download --csv <input.csv> --output-dir <directory>
```

**Examples:**

```bash
# Download transcripts for AWS re:Invent
transcript-download \
  --csv data/aws-reinvent-2025/videos.csv \
  --output-dir data/aws-reinvent-2025/transcripts

# With faster processing (shorter delay)
transcript-download \
  --csv data/pycon-2024/videos.csv \
  --output-dir data/pycon-2024/transcripts \
  --delay 30
```

**Options:**

| Option | Description | Default |
|--------|-------------|---------|
| `--csv` | Input CSV file with video URLs | - |
| `--output-dir` | Directory for transcript files | outputs |
| `--delay` | Seconds between requests | 60 |
| `--languages, -l` | Language codes to try | en en-US en-GB |
| `--verbose, -v` | Enable verbose output | False |

**Single video mode:**

```bash
transcript-download https://www.youtube.com/watch?v=VIDEO_ID --output transcript.md
```

## Output Format

### Transcript files (Markdown with YAML frontmatter)

```markdown
---
video_id: abc123xyz
video_url: https://www.youtube.com/watch?v=abc123xyz
title: Conference Talk Title
author: Speaker Name
published_date: 2025-01-15
length_minutes: 45.5
views: 1234
description: "Talk description..."
keywords: cloud, kubernetes, devops
is_generated: False
is_translatable: True
---

Full transcript text here...
```

### CSV tracking format

```csv
url,title,duration_minutes,view_count,description,transcript_downloaded,summary_done
https://youtube.com/watch?v=...,Talk Title,45.5,1234,Description...,success,
```

| Column | Description |
|--------|-------------|
| `transcript_downloaded` | Status: `success`, `error: <reason>`, or empty |
| `summary_done` | Track if you've processed the transcript |

## Project Structure

```
conference-transcript-downloader/
├── src/
│   └── transcript_downloader/
│       ├── __init__.py          # Package exports
│       ├── cli.py               # Command-line interface
│       ├── downloader.py        # Transcript downloading
│       ├── extractor.py         # Channel video extraction
│       ├── csv_handler.py       # CSV operations
│       ├── metadata.py          # Video metadata extraction
│       ├── models.py            # Data models
│       ├── exceptions.py        # Custom exceptions
│       ├── logging_config.py    # Logging setup
│       └── utils.py             # Utility functions
├── tests/                       # Unit tests
├── data/                        # Downloaded data
├── examples/                    # Example scripts
├── pyproject.toml              # Project configuration
└── README.md
```

## Data Organization

Organize your data however makes sense for your workflow:

```
data/
├── aws-reinvent-2025/
│   ├── videos.csv
│   └── transcripts/
│       ├── video1.md
│       └── video2.md
├── pycon-2024/
│   ├── videos.csv
│   └── transcripts/
└── kubecon-eu-2024/
    ├── videos.csv
    └── transcripts/
```

## Rate Limiting & Best Practices

YouTube may rate limit or block your IP if you make too many requests:

1. **Use reasonable delays**: Default 60 seconds between requests is safe
2. **Resume capability**: Script tracks progress in CSV, can resume after interruption
3. **Start small**: Test with 10-20 videos before large batches
4. **Respect limits**: If you get blocked, wait 30-60 minutes before retrying

## Development

### Setup

```bash
# Clone repository
git clone https://github.com/danielparedes/conference-transcript-downloader.git
cd conference-transcript-downloader

# Install with development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks (optional)
pre-commit install
```

### Running tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=transcript_downloader

# Run specific test file
pytest tests/test_utils.py
```

### Code quality

```bash
# Format code
black src tests

# Lint code
ruff check src tests

# Type checking
mypy src
```

## Programmatic Usage

```python
from transcript_downloader import TranscriptDownloader, ChannelExtractor

# Extract videos from a channel
extractor = ChannelExtractor()
videos = extractor.extract_videos(
    "https://www.youtube.com/@AWSEventsChannel/videos",
    max_videos=10
)

# Download transcripts
downloader = TranscriptDownloader(
    languages=["en", "en-US"],
    delay=30,
    output_dir="transcripts"
)

for video in videos:
    result = downloader.download(video.video_id, video.url)
    if result.success:
        print(f"Downloaded: {video.title}")
    else:
        print(f"Failed: {result.error_message}")
```

## Troubleshooting

### "No transcript found"

- Video may not have captions/transcripts available
- Try with different language codes: `--languages en en-US auto`

### "IP blocked" or rate limiting

- Wait 30-60 minutes before retrying
- Increase delay: `--delay 120`
- Use different network/IP if persistent

### "Could not extract metadata"

- Transcript will still download, just without extra metadata
- Check if video is accessible and not private

### Script interrupted

- Just run the same command again - it will skip already downloaded videos
- Progress is saved to CSV after each video

## Requirements

- Python 3.9+
- youtube-transcript-api
- yt-dlp
- pytube (optional, for enhanced metadata)

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests and linting (`pytest && ruff check .`)
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request
