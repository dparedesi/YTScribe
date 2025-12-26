# Changelog

All notable changes to YTScribe will be documented in this file.

## [1.1.0] - 2025-12-26

### Added
- **AI Summarization**: New `transcript-summarize` command to generate AI summaries for transcripts using OpenRouter.
- **Agent Skill**: `summarize-transcripts` skill to automate the summarization workflow securely.
- **Template**: Added `.env.example` for environment configuration.
- **Security**: Enhanced API key checks in documentation to prevent secret leakage in logs.
- New dependencies: `requests`, `python-dotenv`.

### Changed
- **Documentation**: Updated `README.md` and `AGENTS.md` to reflect new summarization capabilities.
- **Skills**: Updated all existing agent skills (`download`, `extract`, `consolidate`, `add-video`) for consistency and prompts.
- **Project Structure**: Refactored `.gitignore` to better handle data and environment files.

### Removed
- **Skill**: Removed `sync-agent-configs` skill as it is no longer required.
- **Prompts**: Removed standalone `prompts/` directory; moved prompt logic into `summarizer.py` and skills.

## [1.0.0] - 2025-12-25

### Added
- `transcript-extract` command to extract video metadata from YouTube channels
- `transcript-download` command to download transcripts with YAML frontmatter
- `transcript-add` command to manually add videos to collections
- Batch processing with resume capability via CSV tracking
- Rate limiting with automatic IP block detection
- Support for multiple extraction backends (yt-dlp, pytube)
- Consolidation script to merge transcripts for LLM analysis
- Comprehensive test suite
