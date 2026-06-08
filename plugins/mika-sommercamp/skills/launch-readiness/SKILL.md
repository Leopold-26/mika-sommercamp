---
name: launch-readiness
description: Check whether the Sommercamp product is ready for private or public launch, covering product loop, UX, QA, analytics, privacy, landing page, distribution assets, and rollback plan.
---

# Launch Readiness

Use this skill before private beta, week-four public launch, or any external distribution push.

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

## Output

Classify launch readiness:

- Ready
- Ready with small fixes
- Not ready

Then list blockers in priority order.

Update:

- `docs/sommercamp/launch-readiness.md`
- `docs/sommercamp/risks.md`
- `docs/sommercamp/build-log.md`
- `docs/sommercamp/editorial-log.md` if launch story changed

End with one question:

```text
Wollen wir die Blocker jetzt fixen oder den Launch-Scope enger schneiden?
```
