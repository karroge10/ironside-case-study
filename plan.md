# B3: South, one-week pilot

## Message to Marcus, proposed, not sent
Marcus, you said the recap needs to land in 10 to 15 minutes to be useful.
This week I'll help turn your existing notes into one checked recap in the client channel within an hour.
We'll aim to publish a checked recap in 15 minutes, using your notes if the bot is late.
Can you reserve 10 minutes after each call and name a backup for conflicts?
We'll review Friday against every call held, without counting unposted emails.

**Likely pushback:** another review step and duplicate messages while the bot is slow. Use one approved post, reuse the AM's existing notes, and stop the duplicate bot post when possible. **What sustains it:** a named primary and backup per call, a calendar review slot, a visible delivery receipt, and a weekly exception review owned by Marcus after the pilot. These are proposed responsibilities, not accepted commitments.

## Outcome and measurement

Proposed pilot: the first agreed Monday-to-Friday workweek, using the source snapshot through 24 September. Do not interpret the stale [NOW](brain/NOW.md) week as the actual execution week. Confirm calendar dates and the call roster with Marcus before starting.

Conditional Friday planning estimate: **8 of 10 calls (80%)**, assuming the illustrative coverage and capacity below are confirmed on Monday. This is not a data-derived prediction; the actual roster and reviewer effort are unavailable. The operational target remains at least 80% of all calls. Separately, aim to **publish a checked, usable recap within 15 minutes** as a stretch goal aligned with Marcus's feedback. Measure the share of all calls meeting each threshold; a draft does not count as a post. These are pilot goals, not achieved results or a claim that the historical 35% will become 80% cumulatively. Report actual counts, late/missing posts and content failures; phone calls and unresolved cases stay in the denominator. Baseline and rationale: [metrics](metrics.md), [calls](calls.csv), [lead feedback](slack-thread.txt).

**Capacity scenario, assumptions rather than commitments:** use 10 calls only as an illustration, not a forecast of call volume. Reserve 10 additional reviewer minutes per call: 100 minutes across the week, with a named primary and backup for each slot. This is a proposed allowance, not a measured service time; note preparation or correction may require more. The five-minute fallback must leave enough time to prepare, check and publish. Check overlapping calls and backup availability per slot, because weekly capacity alone cannot meet an hourly deadline.

| Friday scenario | Explicit assumption | Qualifying posts / all calls | Additional reviewer capacity |
|---|---|---|---|
| Planning case | Eight calls have covered slots, usable notes and a passing recap by 60 minutes; two miss | 8 / 10 = 80% | Reserve 100 minutes for all 10 calls, including failed attempts |
| Downside | Four calls miss because coverage, usable source material or quality checks fail | 6 / 10 = 60% | Same reserve; unused capacity cannot repair an expired deadline |

On Monday, replace 10 with the agreed call count N, assign actual dates and reviewers, and measure effort on the observed call. Required timely count is ceiling(0.8 * N). Reforecast from individually covered slots with usable input and sufficient review time; do not assume uncovered calls succeed. If capacity or source quality cannot support that count, report the lower forecast and request coverage rather than promise 80%. Track the 15-minute publication stretch separately.

**Acceptance checklist:** accurate summary of facts and confirmed decisions; action items with one supported owner and agreed due date each; missing owners or dates explicitly preserved as open questions rather than invented; required source/history/reference links; no restricted content. Follow [RESOLVER](brain/RESOLVER.md) and [SANITIZER](brain/SANITIZER.md). Check before posting. Count the timestamp of the first posted version that meets the checklist; an incomplete post does not qualify simply because it arrived early.

**Workload and evidence:** for every call, log call ID, call-end time, qualifying post time/receipt, checklist result and active manual preparation/review/correction minutes, including work on missed calls. Separate existing note-writing time from additional pilot work. Report median additional minutes per call and total additional minutes for the week. Agree a sustainable effort limit with Marcus on Monday, then compare actual effort on Friday; a delivery gain that depends on excessive manual effort needs redesign before handover.

| When | I do | Ask South | Ask engineering |
|---|---|---|---|
| Monday | Review the existing recap flow with Marcus; observe a call; audit recent emailed notes against the acceptance checklist. Build the all-call tracker and baseline note-writing effort. | Marcus agrees primary/backup reviewers, destination, review slots and sustainable additional effort. | Trace queue, transcript, generation and posting timestamps on recent late South calls; establish the actual bottleneck before choosing a fix. |
| Tuesday | Help reviewers check and publish within 15 minutes where feasible; record receipts, quality and manual effort. | Proposed checkpoint: at five minutes, use existing notes if no usable bot draft is ready, leaving time to check and publish. If the stretch goal is missed, continue toward 60 minutes without skipping safety checks. | Add visible job status and late-job alerts if feasible; confirm safe handling of duplicate/manual posts. Treat this as a request, not a shipped feature. |
| Wednesday | Review each miss and one successful recap; compare with transcript and approved commitments. | Primary or backup covers every call, including phone calls using confirmed notes; retain only the sanitized recap in the brain. | Report stage delays; test the smallest latency improvement if feasible. Manual coverage continues if engineering cannot ship this week. |
| Thursday | Have the pod run the process; help only with exceptions. Compare additional effort with the agreed limit. | Marcus checks exceptions and confirms unresolved commitments are explicitly flagged before approving the recap. | Confirm receipt/retry behavior and suppress duplicate delivery where supported. |
| Friday | Report both publication thresholds, audit content and summarize additional effort; document misses and hand over the checklist. | Marcus reviews usefulness and workload, owns the ongoing weekly review and confirms next week's coverage. | Agree the next measured latency/delivery milestone from the traces. |

**Failure rule:** if the pod cannot cover reviews, or source facts remain unresolved, report the miss honestly and resolve it with the lead. Do not trade safety for speed or claim success by redefining a recap. A fast, approved manual route is the first-week dependency; engineering acceleration is not assumed. West still needs a separate capture workstream to reach the company-wide 31 October target in [NOW](brain/NOW.md).
