# C1: what failed in the old recap

Compare the preserved [before](workers/output/bad-recap.md) with the [source transcript](workers/output/bad-recap-source.md), the [resolver](brain/RESOLVER.md), [sanitizer](brain/SANITIZER.md), [reference sheet](brain/knowledge/reference/accounts-sheet.csv) and [10 September meeting](brain/knowledge/meetings/2026-09-10-loop-athletic-weekly.md).

| Failure | Evidence | Required behavior |
|---|---|---|
| Private content leaked | The last sentence draws from a DM pasted after the client left, source 00:42 to 00:52. | Omit it completely; use a generic withheld-content flag. Do not turn it into an account-risk action. |
| Performance value copied and conflict hidden | The GMV sentence repeats the call value, which differs from the sheet's `loop-athletic` row. The call is month-to-date; the later sheet is trailing 30 days, so this does not establish that either value is wrong. | Link the sheet and flag reconciliation without reproducing the call figure in the brain. |
| Unsupported certainty | “Great call” is editorial; the format-performance claim is presented as fact rather than Theo's assessment at 00:14. | Remove praise and attribute the reported assessment. Do not infer causality from the GMV remark. |
| Missing action ownership and dates | October brief at 00:26 to 00:30 is Lena's commitment for Friday, 18 September. Size-chart issue at 00:33 to 00:37 has no specific assignee or date. | Table the supported brief commitment; put the size-chart follow-up in open questions. Do not assign Theo based on the older chart-delivery task. |
| Missing structure and provenance | No attendees/source metadata, Summary section, action table, Open questions or Flags for a person. | Follow the resolver template, including 3 to 6 summary bullets. |
| History omitted | The last four try-on videos were already agreed on 10 September. | Link the earlier meeting and identify delivery as follow-through. |

## C2: instruction change and evaluation

The [updated skill](workers/skills/skill-recap.md) replaces “include everything,” “include key numbers,” and “post it” with policy-first filtering, sheet links, evidence-backed commitments, unresolved questions, prior-meeting links and a pre-save check. See the preserved [before](workers/output/bad-recap.md) and isolated [after](workers/output/after-recap.md). Evaluation details and limits are in [validation.md](validation.md). One successful rerun demonstrates this case, not general reliability or faster posting.
