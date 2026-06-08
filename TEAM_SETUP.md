# Program Team Setup

This file explains how to package and distribute Mika for founders.

## Recommended Route: Public GitHub Marketplace

Use this when you want one link that can be forwarded by anyone.

Public repo:

```text
https://github.com/Leopold-26/mika-sommercamp
```

Founder install commands:

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

After installing, founders restart Codex, open a project folder, and write:

```text
Starte Mika.
```

This is the main route because it does not depend on local Mac paths or workspace plugin sharing.

## What To Send To Founders

Send:

1. GitHub repo link: `https://github.com/Leopold-26/mika-sommercamp`
2. Founder instructions: [INSTALL_FOR_FOUNDERS.md](INSTALL_FOR_FOUNDERS.md)
3. Optional one-pager PDF: `dist/mika-founder-one-pager.pdf`
4. Optional team PDF: `dist/mika-team-explainer.pdf`

Do not send local `codex://...marketplacePath=/Users/...` links. They only work on the creator's laptop.

## Repository Layout

This repo includes:

- `.agents/plugins/marketplace.json`
- `plugins/mika-sommercamp/.codex-plugin/plugin.json`
- `plugins/mika-sommercamp/skills/`
- `plugins/mika-sommercamp/references/`
- `plugins/mika-sommercamp/templates/project/`

Codex resolves the plugin path from `.agents/plugins/marketplace.json`.

## Updating Mika

1. Update the plugin files.
2. Run validation with the local plugin-creator validator when available:

   ```bash
   python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/mika-sommercamp
   ```

3. Commit and push to `main`.
4. Tell founders to run:

   ```bash
   codex plugin marketplace upgrade gruenderszene-sommercamp
   codex plugin add mika-sommercamp@gruenderszene-sommercamp
   ```

5. Founders restart Codex and start a new chat.

## Optional Fallback: Starter Repo

The repo also works as a full starter folder because it contains repo-level `AGENTS.md` and `.agents/skills/`.

If the plugin install fails for a founder:

1. They can clone or download this repo.
2. They open the folder in Codex.
3. They write `Starte Mika.`

The plugin route is still preferred because founders can use Mika inside their own project folders.
