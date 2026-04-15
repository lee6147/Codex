# Workspace Guidance

This workspace is a Git repository and may use `git worktree` for parallel work.

## Git / Worktree Rules

- Assume `C:\Users\user\Desktop\Codex` is the primary worktree on `main` unless the repo state shows otherwise.
- Prefer creating a separate worktree for substantial parallel work, risky edits, or branch-isolated experiments.
- Use a different branch per worktree.
- Do not assume a secondary worktree already exists; check first.
- Keep user-facing analysis artifacts inside the main workspace unless the user explicitly asks to place them elsewhere.

## YouTube Transcript Team

- The `youtube-transcript-team` folder stores transcript analysis prompts, templates, and saved analyses.
- When analyzing a new video, save results under `youtube-transcript-team/analyses/`.
- If the raw transcript is too long for a single note, split it into a `transcript/` subfolder with ordered parts.
