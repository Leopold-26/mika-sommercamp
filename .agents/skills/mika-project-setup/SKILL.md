---
name: mika-project-setup
description: Set up Mika's Sommercamp project workspace in the current folder by creating AGENTS.md guidance, docs/sommercamp working documents, the upload folder, and the founder start prompt when the plugin is installed without the starter repo.
---

# Mika Project Setup

Use this skill when Mika is installed as a plugin and the current project does not yet contain the Sommercamp starter files.

## Goal

Create the minimum durable project context so future Codex chats remember how to work with the founder.

Mika's skills live in the installed plugin. Do not tell the founder they need to copy or manage skill files. The project folder stores the founder-specific working files, audits, plans, and logs.

## Files To Create If Missing

- `AGENTS.md`
- `FOUNDER_START_PROMPT.md`
- `START_HERE.md`
- `docs/sommercamp/00_uploads/README.md`
- `docs/sommercamp/founder-profile.md`
- `docs/sommercamp/current-state-audit.md`
- `docs/sommercamp/product-thesis.md`
- `docs/sommercamp/distribution-plan.md`
- `docs/sommercamp/spec.md`
- `docs/sommercamp/engineering-plan.md`
- `docs/sommercamp/design-review.md`
- `docs/sommercamp/website-brief.md`
- `docs/sommercamp/code-review.md`
- `docs/sommercamp/qa-report.md`
- `docs/sommercamp/launch-readiness.md`
- `docs/sommercamp/release-log.md`
- `docs/sommercamp/ten-week-plan.md`
- `docs/sommercamp/risks.md`
- `docs/sommercamp/onboarding-status.md`
- `docs/sommercamp/weekly-retros.md`
- `docs/sommercamp/editorial-log.md`
- `docs/sommercamp/build-log.md`
- `docs/sommercamp/archive/.gitkeep`

If this repository already contains any of these files, do not overwrite them. Read and preserve the existing content.

## Setup Behavior

1. Tell the founder you are creating the Mika workspace files.
2. If the installed plugin contains templates, resolve them from the skill folder at `../../templates/project/`. If this is the starter repo, use `templates/project/` when present or the root project files as examples.
3. Create only missing files and folders.
4. If there is already an `AGENTS.md`, append a concise Mika section instead of replacing the file.
5. After setup, ask the founder to add current materials to `docs/sommercamp/00_uploads/` or point you to existing files.
6. Continue with `$current-state-audit` or `$founder-onboarding`.

## Output

End with:

```text
Der Mika-Workspace ist vorbereitet. Hast du schon Unterlagen, Links, Screenshots, Pitch Decks, Prototypen oder Code, die ich zuerst prüfen soll?
```
