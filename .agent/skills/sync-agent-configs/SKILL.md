---
name: sync-agent-configs
description: Sync skill definitions to agent proxy files (.agent/workflows/skills.md and .github/copilot-instructions.md). Use after adding, removing, or modifying skills.
---

# Sync Agent Configurations

## Overview

Synchronize skill definitions from `.claude/skills/` to the agent proxy configuration files. Run this after any changes to skills to keep all agent configurations in sync.

## Target Files

| File | Purpose |
|------|---------|
| `.agent/workflows/skills.md` | Generic agents, Aider, custom tools |
| `.github/copilot-instructions.md` | GitHub Copilot |

## Instructions

### Step 1: Scan All Skills

Read all `SKILL.md` files from `.claude/skills/*/SKILL.md` and extract:
- `name` from frontmatter
- `description` from frontmatter
- Key command from the `## Command` section (if present)

### Step 2: Update Available Skills Table

In both proxy files, update the "Available Skills" table with format:

```markdown
| Command | Skill Location | Purpose |
|---------|----------------|---------|
| `skill: {name}` | `.claude/skills/{name}/SKILL.md` | {description (truncated to ~60 chars)} |
```

### Step 3: Update Quick Reference Section

In `.agent/workflows/skills.md`, update the "Quick Reference (Inline Commands)" table:

```markdown
| Skill | Command |
|-------|---------|
| {name} | `{primary command from skill}` |
```

In `.github/copilot-instructions.md`, update the "Quick Reference (If Unable to Read Skill Files)" section with individual headings and bash blocks for each skill.

### Step 4: Verify Collections

Check `data/` for folders with `videos.csv` and update the Collections table in `.github/copilot-instructions.md` if new collections exist.

### Step 5: Report Changes

Summarize what was updated:
- Skills added
- Skills removed
- Skills modified
- Collections updated

## Example Output

```
Synced agent configurations:

Skills (5):
  ✓ extract-videos
  ✓ download-transcripts
  ✓ add-video-to-collection
  ✓ sync-all-channels
  ✓ download-all-transcripts

Updated files:
  ✓ .agent/workflows/skills.md
  ✓ .github/copilot-instructions.md

Collections detected: library-of-minds, random, aws-reinvent-2025
```

## Notes

- This skill is self-referential — it maintains the system that enables skills
- Run after any skill changes to keep proxy files accurate
- The proxy files contain inline commands as fallback for agents that can't read files dynamically
