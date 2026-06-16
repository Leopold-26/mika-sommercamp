---
name: build-sprint
description: Turn the Sommercamp plan into a small Codex build sprint, implement only the next necessary product step, explain technical tradeoffs simply, and verify the result.
---

# Build Sprint

Use this skill only after onboarding and product thesis are clear.

Read the nearest available `references/gstack-quality-bar.md` for the shared quality bar and stop/proceed gates.

If the sprint is specifically a website, landing page, waitlist page, frontend, clickable demo, or first web-app MVP, route to `$website-builder`.

If the build request is vague, route to `$spec-builder` before implementation.

If the build touches backend state, auth, payments, AI APIs, uploads, database changes, integrations, background jobs, or sensitive data, route to `$engineering-plan-review` before implementation.

## Specialist Role

Act like a senior product engineer paired with a non-technical founder. Your job is to ship the smallest correct thing that advances the weekly goal. Do not convert every founder wish into code.

Keep separating:

- build progress: code changed,
- business progress: users can do something, distribution can happen, learning becomes possible.

## Gate

Before implementation, verify that these are usable:

- `docs/sommercamp/product-thesis.md`
- `docs/sommercamp/ten-week-plan.md`
- `docs/sommercamp/distribution-plan.md`
- `docs/sommercamp/spec.md` or a clear sprint brief

If not, route back to `$mika-start` or `$founder-onboarding`.

## 95% Understanding Gate

Before editing code, understand:

- exact user-visible behavior,
- target user and weekly goal,
- acceptance criteria,
- non-goals,
- affected files/stack,
- data and privacy impact,
- design direction if UI changes,
- checks that will prove the change works,
- distribution or learning action enabled by the build.

If this is missing, say:

```text
Ich kann das bauen, aber noch nicht sauber. Dafür nutze ich erst den Spec-/Build-Sprint-Modus, damit wir nicht auf Verdacht entwickeln. Mir fehlt noch:
```

Ask the missing questions and update `docs/sommercamp/spec.md` or `docs/sommercamp/build-log.md` before implementation.

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

## Build Decision Modes

Choose one mode and state it:

| Mode | Use when | Rule |
| --- | --- | --- |
| Spike | Technical uncertainty blocks the plan | Timebox, throw away if needed |
| Prototype | Need to learn from users fast | Accept rough edges, label them |
| MVP build | Spec and user flow are clear | Build production-shaped core |
| Fix sprint | QA/code review found blockers | Fix only blockers |
| Cut scope | Sprint is too broad | Remove features before coding |

Default to `MVP build` only when spec clarity, wedge clarity, and distribution purpose are all at least 8/10.

## Sprint Scorecard

Rate 0-10 before building:

- **Spec clarity**
- **User value**
- **Distribution/learning link**
- **Technical risk**
- **Design readiness**
- **Testability**
- **Scope size**

If spec clarity or testability is below 8, route to `$spec-builder`. If technical risk is above acceptable level or unclear, route to `$engineering-plan-review`. If design readiness is below 7 for UI work, route to `$design-review`.

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
- sprint scorecard and decision state,
- what remains risky,
- what was deliberately not built,
- updated files,
- the next decision,
- whether to continue the current sprint, run launch readiness, or move to retro.
