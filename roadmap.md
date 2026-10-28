# Next improvements

The assessment demonstrates the workflow on the supplied cases, not production reliability. These are proposed follow-ups, ordered by the uncertainty they would resolve; none is implemented or scheduled.

| Priority | Improvement | Why it matters | Evidence of completion |
|---|---|---|---|
| 1 | Evaluate the revised recap skill on unseen transcripts in fresh sessions, including a changed sanitizer policy. Keep synthetic fixtures separate from the company brain. | The current [C2 evaluation](validation.md) covers one business case. Checker tests do not establish model generalization. | Preserve inputs, policy versions, outputs and permitted-file read records. Review against an answer key prepared before generation, covering private provenance, performance figures, owner/date ambiguity and prior-meeting links. Report failures as well as passes. |
| 2 | Replace the illustrative Friday scenario with a roster-based forecast. | The [pilot plan](plan.md) has no confirmed call roster, reviewer availability or measured review effort. | Confirm dated primary/backup coverage, observe preparation and review time, and estimate timely posts call by call. Publish expected numerator/denominator, a downside case and additional workload; revise when coverage changes. |
| 3 | Add source-aware review before approved posting. | The [checker](extra/README.md) detects structural problems and selected keywords; unmarked private content can pass. | Test unsupported commitments and private-source statements against labeled synthetic cases. Measure missed violations and false alarms. Keep human approval and distinguish a clean structural check from a policy clearance. |
| 4 | Implement delivery tracing, then choose the smallest operational fix. | South's delay is observed, but its slow processing stage is unknown. West also has a separate capture gap. | Deliver the bounded [event-trail ticket](fde-ticket.md), then use observed failures to prioritize latency or delivery work. Separately validate a consent-aware capture or confirmed-note route with West before committing to an integration. |

Keep this lightweight: establish evidence on new cases and real coverage before adding integrations or making reliability claims. Preserve source files and propose canonical knowledge changes for approval throughout.
