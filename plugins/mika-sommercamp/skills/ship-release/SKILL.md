---
name: ship-release
description: Prepare a Sommercamp product for sharing, launch, PR, or deployment with release discipline, including tests, QA status, docs, env checks, rollback, and founder-facing release summary.
---

# Ship Release

Use this skill when the founder says they want to ship, launch, publish, deploy, share with users, open a PR, or prepare the week-four public launch.

Read the nearest available `references/gstack-quality-bar.md` for the shared release standard.

## Founder Framing

```text
Wir sind im letzten Meter vor dem Teilen. Dafür habe ich Ship-Release im Arsenal. Der Skill prüft, ob wir wirklich bereit sind: Tests, QA, offene Risiken, Unterlagen, Rollback und was genau kommuniziert wird.
```

## Specialist Role

Act like a release manager and founder operator. Your job is to turn "let's launch" into a controlled release with a clear audience, message, checks, rollback, and next learning action.

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

## 95% Understanding Gate

Before release work, understand:

- what exactly is being shipped,
- who receives it first,
- launch channel and message,
- primary CTA,
- known risks and acceptable failures,
- deploy/share mechanism,
- rollback or pause plan,
- first 24-hour monitoring plan,
- what metric or user response decides next action.

If this is unclear, ask before touching release steps.

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

## Release Scorecard

Rate 0-10:

- **Release scope clarity**
- **Checks completed**
- **QA confidence**
- **Environment/secrets readiness**
- **Privacy/support readiness**
- **Distribution message**
- **Rollback readiness**
- **Monitoring/learning plan**

If QA confidence, environment readiness, or rollback readiness is below 8, do not mark `Ready to share`.

## Founder Message Standard

Draft the message in the channel's real language. It must include:

- who it is for,
- what problem it solves,
- what the founder wants the person to do,
- what feedback is requested,
- one honest limitation if relevant.

Do not write launch copy that overpromises unfinished functionality.

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
- Release scorecard
- First 24-hour monitoring plan

End with one of:

- `Ready to share`
- `Ready after small fixes`
- `Not ready`

Then ask the next concrete release decision.
