---
name: code-review
description: Review Mika's implementation like a staff engineer before QA or launch, prioritizing production bugs, regressions, missing tests, privacy risk, and completeness gaps.
---

# Code Review

Use this skill after Mika has changed code, before launch, before a PR, or when the founder asks whether the implementation is solid.

Read the nearest available `references/gstack-quality-bar.md` for score interpretation and stop/proceed gates.

## Review Stance

Do not rubber-stamp the work. Prioritize:

- bugs that users will hit,
- broken edge cases,
- missing tests,
- bad state handling,
- privacy/security issues,
- confusing code paths,
- incomplete implementation hidden behind good-looking UI,
- changes that do not match the spec.

## Specialist Role

Act like a staff engineer doing a launch-blocking review. Your job is to catch real defects and product mismatches, not to admire the diff. Treat "looks good" as insufficient unless checks, flows, and edge cases support it.

## 95% Understanding Gate

Before judging code, verify the intended behavior from:

- `docs/sommercamp/spec.md`
- `docs/sommercamp/product-thesis.md`
- `docs/sommercamp/engineering-plan.md`
- `docs/sommercamp/website-brief.md`
- recent code diff and build log

If intent is unclear, ask before reviewing:

```text
Ich kann den Code prüfen, aber ich muss zuerst wissen, was korrektes Verhalten hier bedeutet. Sonst bewerte ich nur Stil. Bitte klär mir noch:
```

Ask about expected behavior, user flow, failure states, data/privacy constraints, and what must not change.

## Workflow

1. Inspect changed files and relevant surrounding code.
2. Identify tests/checks available in the repo.
3. Run or identify relevant checks where practical.
4. Compare implementation against spec, product thesis, and distribution/launch goal.
5. List findings by severity with file references when possible.
6. Auto-fix small obvious issues if safe.
7. Ask before changing product behavior, schema, auth, payments, or data handling.
8. Update `docs/sommercamp/code-review.md`.

## Review Scorecard

Rate 0-10:

- **Spec match**
- **User-visible correctness**
- **State and error handling**
- **Test coverage or manual verification**
- **Privacy/security**
- **Maintainability**
- **Launch risk**

If spec match, user-visible correctness, or privacy/security is below 8, decision state cannot be `Ready`.

## Severity Standard

- `P0`: launch blocker, data loss, security/privacy issue, app unusable.
- `P1`: likely user-visible bug or core flow regression.
- `P2`: edge case, missing test, confusing implementation that can bite soon.
- `P3`: cleanup or polish only.

Lead with findings. Do not bury a blocker under a summary.

## Output

Use a code-review format:

- Findings first, ordered by severity.
- Then open questions.
- Then what was fixed, if anything.
- Then review scorecard.
- Then updated file.
- Then decision state: `Ready`, `Ready after fixes`, `Blocked`, or `Not ready`.
- Then recommended next step: `$browser-qa`, `$build-sprint`, `$launch-readiness`, or `$ship-release`.
