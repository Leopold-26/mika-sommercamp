---
name: launch-readiness
description: Check whether the Sommercamp product is ready for private or public launch, covering product loop, UX, QA, analytics, privacy, landing page, distribution assets, and rollback plan.
---

# Launch Readiness

Use this skill before private beta, week-four public launch, or any external distribution push.

Read the nearest available `references/gstack-quality-bar.md` for score interpretation and stop/proceed gates.

## Specialist Role

Act like the launch lead. Your job is to decide whether this product should be shown to real users now, narrowed, fixed, or held back. Do not treat launch readiness as a checklist exercise.

## Inputs

Read, when present:

- `docs/sommercamp/product-thesis.md`
- `docs/sommercamp/distribution-plan.md`
- `docs/sommercamp/spec.md`
- `docs/sommercamp/website-brief.md`
- `docs/sommercamp/code-review.md`
- `docs/sommercamp/qa-report.md`
- `docs/sommercamp/build-log.md`
- `docs/sommercamp/risks.md`

## 95% Understanding Gate

Before deciding readiness, understand:

- launch type: private, public, waitlist, community test, press/editorial, or demo,
- exact audience and channel,
- user action expected,
- what must work,
- acceptable failure level,
- support/contact path,
- rollback or scope reduction option,
- metric or learning target.

If launch context is missing, ask before classifying.

## Checklist

Review:

- Can a new user understand the product quickly?
- Does the first session produce value?
- Are signup/onboarding states clear?
- Are empty, loading, error, and success states acceptable?
- Are analytics events defined?
- Is there a landing page or shareable explanation?
- Is privacy risk understood?
- Is there a way to contact/support users?
- Is there a simple rollback or kill switch?
- Are distribution assets ready?

If a local web app exists, use `$browser-qa` to inspect the actual rendered product. If launch readiness is acceptable and the founder wants to publish, route to `$ship-release`.

## Launch Scorecard

Rate 0-10:

- **Product promise clarity**
- **Core flow reliability**
- **First-session value**
- **Mobile/UX readiness**
- **Analytics/learning readiness**
- **Privacy/support readiness**
- **Distribution asset readiness**
- **Rollback/scope control**

Decision rules:

- `Ready`: all launch-critical dimensions are 8+ and no P0/P1 blockers.
- `Ready with small fixes`: one or two non-core items below 8 with clear fixes.
- `Narrow launch`: product can be shown to fewer users or a smaller promise.
- `Not ready`: core flow, privacy, or distribution context is weak.

If the product is not ready, propose a narrower launch version before suggesting more build.

## Output

Classify launch readiness:

- Ready
- Ready with small fixes
- Narrow launch
- Not ready

Then list blockers in priority order.

Update:

- `docs/sommercamp/launch-readiness.md`
- `docs/sommercamp/risks.md`
- `docs/sommercamp/build-log.md`
- `docs/sommercamp/editorial-log.md` if launch story changed

Also include:

- strongest launch argument,
- biggest launch risk,
- launch scorecard,
- recommended launch scope,
- updated files,
- next route: `$ship-release`, `$build-sprint`, `$browser-qa`, `$distribution-review`, or `$growth-retro`.

End with one question:

```text
Wollen wir die Blocker jetzt fixen oder den Launch-Scope enger schneiden?
```
