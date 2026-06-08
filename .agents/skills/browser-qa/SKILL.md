---
name: browser-qa
description: Test a local or deployed Sommercamp website or app in a real browser flow, find user-visible bugs, fix safe issues, capture QA notes, and route to launch or release.
---

# Browser QA

Use this skill when a local or deployed website/app exists and the founder wants to test it, launch it, verify fixes, or understand whether users can complete the core flow.

## Founder Framing

```text
Wir sind jetzt nicht mehr im Ideenmodus, sondern im Nutzer-Test. Dafür habe ich Browser-QA im Arsenal: Ich öffne die App wie ein echter Nutzer, gehe die wichtigsten Flows durch und suche nach Dingen, die im Code allein nicht auffallen.
```

## 95% Understanding Gate

Before QA, understand:

- target URL or local start command,
- core user flow,
- primary CTA,
- device priority: mobile, desktop, or both,
- expected success state,
- known risks or areas the founder worries about.

If unclear, ask. Do not wander randomly through the app and call it QA.

## Workflow

1. Read `docs/sommercamp/spec.md`, `website-brief.md`, `engineering-plan.md`, `launch-readiness.md`, and `build-log.md` if present.
2. Start the dev server if needed and practical.
3. Use browser QA when available to test:
   - first screen,
   - core action,
   - navigation,
   - mobile layout,
   - empty/loading/error/success states,
   - console errors,
   - obvious accessibility and contrast issues.
4. Save findings to `docs/sommercamp/qa-report.md`.
5. Fix safe layout/copy/state bugs directly.
6. Re-test fixed flows.

## Output

End with:

- QA status: `Pass`, `Pass with fixes`, or `Blocked`.
- Tested flows.
- Bugs found.
- Fixes made.
- Remaining risks.
- Recommended next step: `$launch-readiness`, `$code-review`, `$build-sprint`, or `$ship-release`.
