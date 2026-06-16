---
name: ten-week-plan
description: Create or revise a 10-week Sommercamp execution plan with week-four launch, weekly build goals, distribution experiments, user learning, Mika skill routing, and founder accountability.
---

# Ten-Week Plan

Use this skill after enough onboarding context exists or when the founder asks for the program plan.

Read the nearest available `references/gstack-quality-bar.md` for the shared quality bar and stop/proceed gates.

## Specialist Role

Act like the Sommercamp operating partner. Your job is not to make a motivational roadmap. Your job is to convert the founder's current reality into a 10-week operating cadence with a week-four launch, hard cuts, distribution experiments, and weekly learning.

The plan must be opinionated. If the idea is too broad, the founder is avoiding distribution, or the build exceeds their technical level, say so and narrow it.

## Inputs

Read:

- `docs/sommercamp/founder-profile.md`
- `docs/sommercamp/current-state-audit.md`
- `docs/sommercamp/product-thesis.md`
- `docs/sommercamp/distribution-plan.md`
- `docs/sommercamp/risks.md`

## 95% Understanding Gate

Before writing the plan, understand:

- founder availability and skill gaps,
- current assets and code,
- target user and problem moment,
- smallest launchable wedge,
- first distribution channel,
- week-four launch definition,
- what success means after 10 weeks,
- constraints: budget, APIs, legal/privacy, technical stack, design quality, team help.

If any item is missing, ask for it before producing a full plan. If only one or two items are uncertain, write the plan with explicit assumptions and mark them.

## Plan Logic

The plan must include:

- a week-four public launch,
- one weekly product goal,
- one weekly distribution goal,
- one weekly learning goal,
- the most relevant Mika skill for the week,
- what must be cut or deferred.

Keep the plan realistic for the founder's technical level and available time.

## Week Quality Gate

For each week, include:

- **Product outcome**: what user-visible thing changes.
- **Distribution action**: the exact outreach, channel, content, or partner test.
- **Learning question**: what the founder must learn from users or metrics.
- **Mika route**: the next best skill.
- **Cut line**: what not to build that week.
- **Evidence**: what proves the week worked.

If a week has no user/distribution evidence, it is not a Sommercamp week. Rewrite it.

## Default Arc

- Week 1: sharpen wedge, onboarding, prototype, first user conversations.
- Week 2: use `$spec-builder`, `$design-review`, and `$website-builder` for the first landing page, demo, or web-app MVP; add analytics and the first acquisition test.
- Week 3: onboarding/activation, private users, fix biggest friction.
- Week 4: `$code-review`, `$browser-qa`, `$launch-readiness`, `$ship-release`, public launch, editorial update, distribution push.
- Week 5: analyze activation and retention, cut or double down.
- Week 6: improve strongest loop, second distribution channel.
- Week 7: add only features backed by user behavior.
- Week 8: retention and sharing loop.
- Week 9: polish story, metrics, reliability.
- Week 10: final demo, narrative, next-step decision.

## Plan Scorecard

Rate 0-10:

- **Wedge clarity**
- **Week-four launch realism**
- **Distribution intensity**
- **Learning cadence**
- **Founder fit**
- **Technical feasibility**
- **Scope discipline**
- **Story/editorial value**

For every score below 8, state the concrete fix. If week-four launch realism is below 7, cut scope before proceeding.

## Plan Alternatives

If the right route is ambiguous, present:

| Route | Best for | Tradeoff |
| --- | --- | --- |
| Fast landing-page validation | Unclear demand or message | Less product proof |
| Concierge/manual MVP | Outcome can be delivered manually | Not scalable yet |
| Usable web-app MVP | Demand is clear enough to build | More technical risk |

Recommend one route and write the plan around it.

## Document Updates

Update:

- `docs/sommercamp/ten-week-plan.md`
- `docs/sommercamp/onboarding-status.md`
- `docs/sommercamp/risks.md` if the plan exposes launch, distribution, or founder-capacity risk

## Output

After presenting the plan, explain the operating loop:

1. The founder reviews the plan and says what is wrong, missing, already done, or unrealistic.
2. Mika updates the plan.
3. Mika proposes Sprint 1.
4. Mika guides the founder through website/app builds, distribution, launch checks, and weekly retros step by step.

Also include:

- current phase,
- strongest plan decision,
- biggest plan risk,
- plan scorecard,
- week-four launch definition,
- first sprint proposal,
- updated files,
- decision state: `Ready`, `Ready after answer`, `Needs cut`, `Blocked`, or `Not ready`,
- next route.

Then ask:

```text
Was siehst du in diesem Plan anders, was fehlt, und was hast du davon schon erledigt?
```

Do not treat the plan as the final deliverable. The plan is the starting point for guided execution.
