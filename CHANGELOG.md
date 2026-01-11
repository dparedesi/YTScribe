# Changelog

All notable changes to YTScriber will be documented in this file.

## [1.2.1] - 2025-01-11

### Fixed
- Version mismatch between pyproject.toml and __init__.py

## [1.2.0] - 2025-01-11

### Added
- **PyPI package**: Published as `ytscriber` on PyPI (`pip install ytscriber`).
- **Unified CLI**: Single `ytscriber <subcommand>` pattern replaces `transcript-*` commands.
- **Cross-platform paths**: Data/config directories via `platformdirs` (`~/Documents/YTScriber` on macOS/Windows, `~/ytscriber` on Linux).
- **New commands**: `sync-all`, `download-all`, `config`, and `status` subcommands.
- **Auto-initialization**: Creates config/data folders automatically on first run.
- **Improved --help**: All arguments now have help text, examples, and defaults shown.
- **Edge case handling**: Helpful errors for video URL to extract, missing folders, missing API key.
- **Rate limiting guidance**: VPN recommendations and overnight batch suggestions in warnings.

### Changed
- **CLI commands**: `transcript-extract` → `ytscriber extract`, `transcript-download` → `ytscriber download`, etc.
- **--folder shorthand**: Use `--folder name` instead of explicit CSV paths.
- **Configuration**: User settings stored in `~/.config/ytscriber/config.yaml`.
- **Documentation**: Comprehensive README and CLAUDE.md for new workflows.

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
