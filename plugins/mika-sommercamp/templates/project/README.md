# Mika Sommercamp Starter

Mika is the Gründerszene Sommercamp assistant for Codex. It helps founders onboard, audit existing work, sharpen the product idea, plan the 10 weeks, turn vague requests into specs, run GStack-style design/engineering/code reviews, build websites and web-app MVPs with Codex, QA in the browser, prepare launch, and turn progress into editorial updates.

## Fastest Start

### Option A: Codex Plugin

Install Mika from the public GitHub marketplace:

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Then restart Codex.

Then open your project folder in Codex and write:

```text
Starte Mika.
```

Mika will create the Sommercamp workspace files if they are missing.

### Option B: GitHub Template / ZIP Fallback

1. Download or fork this repo.
2. Open this folder in Codex.
3. Put any existing materials into:

   ```text
   docs/sommercamp/00_uploads/
   ```

   Examples: pitch deck, notes, screenshots, prototype links, docs, Figma exports, user research, landing page copy, code, product ideas.

4. Start a new Codex chat in this folder and write:

   ```text
   Starte Mika.
   ```

Mika will first inspect what already exists. Then it will ask only for missing context. It should not start building until the onboarding and product thesis are clear.

## What Mika Creates

Mika maintains these working documents:

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

## If You Already Have Work

Do not rewrite everything manually. Upload or place your existing materials in `docs/sommercamp/00_uploads/` and ask:

```text
Mika, prüfe bitte meinen aktuellen Stand und sag mir, was noch fehlt.
```

Mika will audit the documents and create a current-state summary before asking follow-up questions.

## For The Program Team

This repo works immediately as a Codex starter repo because skills live under `.agents/skills/`.

It also contains a packaged plugin under `plugins/mika-sommercamp/`. Use the GitHub marketplace route when you want founders to install Mika into any project folder. Use the GitHub Template route when you want every founder to start with a complete project folder.
