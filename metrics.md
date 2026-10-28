# B1 and B2: recap delivery

**Definition:** calls with a posted recap within 60 minutes of call end / all client calls held. Include agent and AM posts. Blank posting timestamps count as no evidenced timely post, not as proof no summary was written. Calculations use [calls.csv](calls.csv), 1 to 24 September 2026, checked against the counts in [adoption.csv](adoption.csv); reproduce with `python extra/metrics.py`.

| Rank | Pod | Timely / all calls | Correct rate | Recorded / all | Late posts | No post timestamp |
|---|---|---|---|---|---|---|
| 1 | North | 36 / 40 | 90% | 38 / 40 | 2 | 2 |
| 2 | East | 21 / 30 | 70% | 28 / 30 | 7 | 2 |
| 3 | South | 14 / 40 | 35% | 36 / 40 | 20 | 6 |
| 4 | West | 3 / 30 | 10% | 4 / 30 | 1 | 26 |

**Dashboard correction:** East's displayed 75% equals 21 / 28 recorded calls, consistent with using the recorded-call denominator; the original dashboard formula is not provided. The required denominator is 30 held calls, giving 70%. All four dashboard counts reconcile to the call log. Overall: 74 / 140 = 52.9%, weighted by calls, not an average of pod rates. At the existing call volumes, East, South and West need respectively 3, 18 and 21 additional timely posts to reach 80%; these are gap illustrations, not next month's forecasts.

**B1 additional metric: recording coverage.** Recorded calls / all calls held shows whether calls can reach the agent, which runs on recorded Meet calls. This is a diagnostic, not the official recap-delivery metric or a separate 80% target.

| Pod | Recorded / all calls | Recording coverage | Unrecorded calls and platform |
|---|---|---|---|
| North | 38 / 40 | 95.0% | 2 phone calls |
| East | 28 / 30 | 93.3% | 2 phone calls |
| South | 36 / 40 | 90.0% | 4 phone calls |
| West | 4 / 30 | 13.3% | 26 WhatsApp calls |

Source: [per-call log](calls.csv). [NOW](brain/NOW.md) explains that West clients prefer WhatsApp and those calls are not recorded or passed to the agent. The other pods' missing recordings are all phone calls, but the materials do not establish why phone was chosen or whether capture was attempted. Investigate rather than invent the reason. Recording is a dependency of this agent, not a requirement for a human to write and post a complete recap.

**Further B2 diagnostic:** timely posts per recorded call are North 94.7%, East 75.0%, South 38.9%, West 75.0%. South's high recording coverage but low timely delivery points to a downstream problem; West's conditional rate covers only four recordings. Conditional rates must not replace the headline metric.

**Work on South first.** It has 20 late posts, versus four unrecorded calls and two recorded calls without posting timestamps (`c117`, `c140`). Its 34 observed posts are all agent posts, with median delay 74 minutes. The [18 September thread](slack-thread.txt) supplies the behavioral explanation: Marcus and Tomas say they send their own summaries before the bot arrives; Marcus would use it at 10 to 15 minutes. The log measures latency and delivery, not whether those emailed summaries contain action owners and dates. The [current operating note](brain/NOW.md) says the agent usually takes 45 to 90 minutes, consistent with a speed problem, not evidence of a specific infrastructure fault.

**Why South before West:** South offers a bounded delivery pilot on existing recordings, with a willing lead's explicit speed threshold. West has the worst rate and a separate capture dependency: 26 unrecorded WhatsApp calls, consistent with [NOW](brain/NOW.md) and [Lena's page](brain/knowledge/people/lena-varga.md). Ask Lena and engineering to scope a consent-aware capture or structured-note path in parallel; do not mandate a platform switch without clients' agreement. North's 33 AM posts out of 38 posts suggest a manual routine worth observing, but do not prove that its routine caused its performance.

**Keep the metric honest.** Priya's suggestion in the thread would count unposted emailed summaries. That changes the stated metric and lacks timestamp/content evidence. Offer to post the existing summary, after checking it includes actions with owners and dates, and count it only when a timely post is verified. The CSV alone cannot establish that any posted content meets the recap definition; sample content and delivery evidence before operational reporting.
