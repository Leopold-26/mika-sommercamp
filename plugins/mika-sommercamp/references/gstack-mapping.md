# GStack-Inspired Mika Mapping

Mika borrows the useful workflow shape from GStack: think, plan, build, review, QA, ship, retro. The language and gates are adapted for non-technical Sommercamp founders.

## Mapping

| GStack-style function | Mika skill | Purpose |
| --- | --- | --- |
| Office hours | `founder-onboarding` | Understand founder, idea, assets, constraints, and gaps. |
| Spec | `spec-builder` | Turn vague founder intent into a precise build spec and ask until Mika is not guessing. |
| CEO review | `product-wedge-review` | Challenge strategy, scope, user, and wedge. |
| Engineering review | `engineering-plan-review` | Pressure-test architecture, data flow, state, edge cases, tests, and privacy before implementation. |
| Implementation | `build-sprint` | Convert the approved plan into the smallest build task. |
| Website/App builder | `website-builder` | Ask founder-friendly product and design questions, then build the first landing page, website, demo, or web-app MVP. |
| Design review | `design-review` | Review first screen, CTA, states, mobile behavior, visual direction, and AI-slop risk. |
| Code review | `code-review` | Find implementation bugs, regressions, missing tests, privacy risks, and completeness gaps. |
| QA | `browser-qa` | Test local/staging product behavior through user flows and record QA findings. |
| Ship | `ship-release` | Prepare release checks, distribution action, docs, rollback, and founder-facing release summary. |
| Retro | `growth-retro` | Review user learning, metrics, founder blockers, and next decision. |
| Learn/memory | `founder-profile`, `spec`, `engineering-plan`, `design-review`, `weekly-retros`, `build-log`, `qa-report`, `release-log` | Keep durable context inside the repo. |

## Parity Gap We Intentionally Close

GStack quality comes from more than skill names. Mika must include the same depth pattern:

- specialist role per phase,
- uncomfortable premise challenge,
- concrete alternatives,
- 0-10 scorecards,
- stop/proceed gates,
- persistent artifacts,
- evidence-based QA and launch checks,
- retros that convert usage into the next decision.

See `references/gstack-quality-bar.md` for the common standard every Mika skill should follow.

## Important Difference

GStack is primarily an engineering operating system. Mika is a founder operating system. The main quality bar is not just code quality. It is whether the founder is moving toward launch, users, distribution, and learning.

## Mika 95% Understanding Rule

Mika should explain the relevant tool before using it, then ask enough questions to reach roughly 95% understanding. If Mika does not know the target user, painful moment, outcome, scope, non-goals, success criteria, design direction, technical constraints, and distribution goal, Mika must ask before building.
