# Mika Sommercamp

Mika is the Gründerszene Sommercamp assistant for Codex. It helps founders onboard, audit existing work, sharpen the product idea, plan the 10 weeks, turn vague requests into specs, run GStack-style design/engineering/code reviews, build websites and web-app MVPs with Codex, QA in the browser, prepare launch, and turn progress into editorial updates.

## Founder Install

Founders should use the public GitHub route. They do not need the old local `codex://...` link.

Open Terminal and run these two commands:

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Then restart Codex.

Create or open a project folder in Codex. The folder can be empty. Start a new chat in that folder and write:

```text
Starte Mika.
```

Mika will create the Sommercamp workspace files if they are missing.

Full founder instructions: [INSTALL_FOR_FOUNDERS.md](INSTALL_FOR_FOUNDERS.md)

## What This Repo Contains

This repo is a Codex plugin marketplace. Codex reads:

- `.agents/plugins/marketplace.json`
- `plugins/mika-sommercamp/.codex-plugin/plugin.json`
- `plugins/mika-sommercamp/skills/`
- `plugins/mika-sommercamp/references/`
- `plugins/mika-sommercamp/templates/project/`

It also includes the ready-to-send delivery files:

- `dist/mika-founder-one-pager.pdf` - founder-facing setup PDF
- `dist/mika-team-explainer.pdf` - internal team explainer PDF
- `dist/mika-sommercamp-plugin.zip`
- `dist/mika-sommercamp-starter.zip`

The marketplace name is `gruenderszene-sommercamp`.

The plugin name is `mika-sommercamp`.

## How Founders Use Mika

1. Open `https://github.com/Leopold-26/mika-sommercamp`.
2. Copy the two install commands from [INSTALL_FOR_FOUNDERS.md](INSTALL_FOR_FOUNDERS.md) into Terminal.
3. Restart Codex.
4. Create or open a project folder in Codex.
5. Start a new chat in that folder.
6. Write `Starte Mika.`
7. Send existing materials in chat or place them in `docs/sommercamp/00_uploads/`.

Mika first inspects what already exists. Then it asks only for missing context. It should not start building until onboarding and product thesis are clear.

## What Mika Creates

Mika maintains these working documents in the founder's project folder:

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
- `docs/sommercamp/weekly-retros.md`
- `docs/sommercamp/editorial-log.md`

## Founder Promise

Mika is not only a coding assistant. Mika should:

- ask good questions,
- prevent duplicate work,
- push back when the plan is weak,
- explain technical choices simply,
- keep the founder focused on launch and distribution,
- explain which tool in Mika's arsenal fits the current phase,
- ask until the work is roughly 95% understood before building,
- ask concrete product and design questions before building websites,
- review code, test in browser, and prepare release only when the context is clear,
- help build the app when the plan is clear.

## Updating Mika

After pushing plugin changes to `main`, founders can update with:

```bash
codex plugin marketplace upgrade gruenderszene-sommercamp
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

They should restart Codex and start a new chat after updating.
