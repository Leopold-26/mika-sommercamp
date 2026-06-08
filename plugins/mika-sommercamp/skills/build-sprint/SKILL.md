---
name: build-sprint
description: Turn the Sommercamp plan into a small Codex build sprint, implement only the next necessary product step, explain technical tradeoffs simply, and verify the result.
---

# Build Sprint

Use this skill only after onboarding and product thesis are clear.

If the sprint is specifically a website, landing page, waitlist page, frontend, clickable demo, or first web-app MVP, route to `$website-builder`.

If the build request is vague, route to `$spec-builder` before implementation.

If the build touches backend state, auth, payments, AI APIs, uploads, database changes, integrations, background jobs, or sensitive data, route to `$engineering-plan-review` before implementation.

## Gate

Before implementation, verify that these are usable:

- `docs/sommercamp/product-thesis.md`
- `docs/sommercamp/ten-week-plan.md`
- `docs/sommercamp/distribution-plan.md`

If not, route back to `$mika-start` or `$founder-onboarding`.

## Sprint Shape

1. State the weekly goal.
2. Pick the smallest build task that advances the goal.
3. Explain the implementation plan in plain language.
4. Name what will not be built.
5. Implement.
6. Run relevant checks if available.
7. For meaningful code changes, route to `$code-review`.
8. If a local website/app exists, route to `$browser-qa`.
9. Update `docs/sommercamp/build-log.md`.
10. Ask what the founder wants to change or clarify.
11. If the sprint is complete, route to `$growth-retro` before choosing the next sprint.

## Founder-Friendly Explanations

For non-technical founders, explain tradeoffs as:

- fastest now,
- cleanest later,
- cheapest,
- most flexible,
- riskiest.

Do not overbuild infrastructure before the first launch.

## Output

End with:

- what changed,
- how it was checked,
- what remains risky,
- the next decision,
- whether to continue the current sprint, run launch readiness, or move to retro.
