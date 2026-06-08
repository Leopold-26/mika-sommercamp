---
name: ship-release
description: Prepare a Sommercamp product for sharing, launch, PR, or deployment with release discipline, including tests, QA status, docs, env checks, rollback, and founder-facing release summary.
---

# Ship Release

Use this skill when the founder says they want to ship, launch, publish, deploy, share with users, open a PR, or prepare the week-four public launch.

## Founder Framing

```text
Wir sind im letzten Meter vor dem Teilen. Dafür habe ich Ship-Release im Arsenal. Der Skill prüft, ob wir wirklich bereit sind: Tests, QA, offene Risiken, Unterlagen, Rollback und was genau kommuniziert wird.
```

## Gate

Before shipping, inspect:

- `docs/sommercamp/spec.md`
- `docs/sommercamp/product-thesis.md`
- `docs/sommercamp/distribution-plan.md`
- `docs/sommercamp/launch-readiness.md`
- `docs/sommercamp/qa-report.md`
- `docs/sommercamp/code-review.md`
- `docs/sommercamp/build-log.md`
- repo status and available test commands

If QA or code review is missing for meaningful app changes, route to `$code-review` or `$browser-qa` first.

## Release Checklist

Check:

- branch/worktree state,
- tests and lint/build commands,
- environment variables and secrets,
- analytics and user feedback path,
- privacy/support/contact basics,
- rollback or kill switch,
- launch copy and primary CTA,
- known risks,
- what the founder will send to first users.

Do not push, deploy, merge, or publish unless the founder explicitly asked for that action and the repo is ready.

## Output

Create or update `docs/sommercamp/release-log.md` with:

- Release goal
- What changed
- Checks run
- QA status
- Known risks
- Rollback
- Distribution action
- Founder message draft

End with one of:

- `Ready to share`
- `Ready after small fixes`
- `Not ready`

Then ask the next concrete release decision.
