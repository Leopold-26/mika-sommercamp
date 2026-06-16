---
name: spec-builder
description: Turn a vague founder request, feature idea, website idea, or app change into a precise Mika spec before design, engineering, build, QA, or shipping work starts.
---

# Spec Builder

Use this skill when the founder asks for a feature, website, app, integration, AI flow, or product change and the request is not yet precise enough to build safely.

Read the nearest available `references/gstack-quality-bar.md` for the shared quality gate.

## Specialist Role

Act like a spec author preparing work for a senior builder. The spec should be executable by a future Codex chat without guessing.

## Five-Phase Spec Flow

1. **Why**: user, painful moment, product outcome, distribution/learning goal.
2. **Scope**: must-haves, non-goals, cuts, week-four relevance.
3. **System**: screens, data, integrations, state, failure modes, privacy.
4. **Acceptance**: observable behavior, test cases, success metric.
5. **File**: write the final spec to `docs/sommercamp/spec.md` and route next.

Do not skip phases. If a phase is unknown, ask or mark an explicit assumption.

## 95% Understanding Gate

Mika should not build from guesses. Before implementation, reach roughly 95% understanding of:

- target user and painful moment,
- desired outcome,
- exact user flow,
- must-have behavior,
- acceptance criteria,
- non-goals and cuts,
- data/content needed,
- distribution or learning goal,
- design references or tone when UI is involved,
- technical constraints and unknowns.

## Spec Quality Gate And Scorecard

Score the spec 0-10 before routing to build:

- `0-5`: not buildable; ask questions.
- `6`: buildable only with risky assumptions; ask or cut.
- `7`: buildable for a prototype; still needs named assumptions.
- `8`: build-ready for the next sprint.
- `9-10`: clear enough for implementation, review, QA, and launch checks.

Do not route to `$build-sprint` or `$website-builder` below 8 unless the founder explicitly accepts the assumptions and the work is low-risk.

If any of these are missing, say:

```text
Ich kann das bauen, aber ich will nicht raten. Dafür nutze ich jetzt den Spec-Builder: Er macht aus deiner Idee eine klare Bauanleitung. Damit ich bei 95% Verständnis bin, brauche ich noch diese Antworten:
```

Ask 5 to 8 focused questions. If the founder cannot answer, propose a default and mark it as an assumption.

## Output

Create or update `docs/sommercamp/spec.md` with:

- Goal
- User
- Problem Moment
- Why Now
- Scope
- Non-Goals
- User Flow
- Screens or Touchpoints
- Data and Integrations
- States: empty, loading, error, success
- Failure Modes
- Privacy and Trust Notes
- Acceptance Criteria
- Tests or Manual QA Checks
- Distribution or Learning Goal
- Open Questions
- Assumptions Mika Made
- Spec Score
- Decision State
- Recommended Next Skill

## Routing

After the spec:

- Use `$product-wedge-review` if the scope is still too broad.
- Use `$design-review` if UI, brand, screens, or interaction quality matter.
- Use `$engineering-plan-review` if architecture, state, backend, AI, auth, payments, or integrations matter.
- Use `$website-builder` for a landing page, website, demo, or first web-app MVP.
- Use `$build-sprint` only when the spec is clear enough to implement.

End with one decision question:

```text
Stimmt diese Spezifikation so, oder soll ich eine Annahme ändern, bevor ich den nächsten Review/Build-Schritt starte?
```
