# Changelog

All notable changes to YTScribe will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-26

### Added
- Initial public release
- `transcript-extract` command to extract video metadata from YouTube channels
- `transcript-download` command to download transcripts with YAML frontmatter
- `transcript-add` command to manually add videos to collections
- Batch processing with resume capability via CSV tracking
- Rate limiting with automatic IP block detection
- Support for multiple extraction backends (yt-dlp, pytube)
- Consolidation script to merge transcripts for LLM analysis
- Pre-commit hooks for code quality (black, ruff, mypy)
- Comprehensive test suite
