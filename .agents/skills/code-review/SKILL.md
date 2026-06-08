---
name: code-review
description: Review Mika's implementation like a staff engineer before QA or launch, prioritizing production bugs, regressions, missing tests, privacy risk, and completeness gaps.
---

# Code Review

Use this skill after Mika has changed code, before launch, before a PR, or when the founder asks whether the implementation is solid.

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

## Workflow

1. Inspect changed files and relevant surrounding code.
2. Identify tests/checks available in the repo.
3. List findings by severity with file references when possible.
4. Auto-fix small obvious issues if safe.
5. Ask before changing product behavior, schema, auth, payments, or data handling.
6. Update `docs/sommercamp/code-review.md`.

## Output

Use a code-review format:

- Findings first, ordered by severity.
- Then open questions.
- Then what was fixed, if anything.
- Then recommended next step: `$browser-qa`, `$build-sprint`, `$launch-readiness`, or `$ship-release`.
