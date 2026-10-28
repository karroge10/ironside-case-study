# Ironside assessment: working folder

Start with [summary.html](summary.html), the client-facing brief. All conclusions use the provided September 2026 snapshot, not live business data. No people, account or reference-sheet updates have been applied.

| Task | Output | Status |
|---|---|---|
| A1 | [22 September recap](brain/knowledge/meetings/2026-09-22-kettle-and-crumb.md) | Complete, unresolved shipment owner flagged |
| A2 | [24 September recap](brain/knowledge/meetings/2026-09-24-kettle-and-crumb.md), [proposals](proposed-changes.md) | Complete, GMV and date clarification pending |
| A3 | [Dana briefing](answer.md) | Complete |
| B1, B2 | [Metrics and prioritization](metrics.md) | Complete |
| B3 | [One-week plan](plan.md) | Complete proposal, not executed |
| C1 | [Diagnosis](diagnosis.md) | Complete |
| C2 | [Skill](workers/skills/skill-recap.md), [before](workers/output/bad-recap.md), [isolated after](workers/output/after-recap.md) | Complete, one-case evaluation |
| C3 | [Engineering ticket](fde-ticket.md) | Complete |
| Extra | [Runnable tools](extra/README.md) | Complete |

No assessment question was skipped. See [actual usage log](log.md) and [validation](validation.md).

## Reproduce and change quickly

From this folder, with Python 3 and no third-party packages:

```
python extra/metrics.py
python extra/validate.py brain/knowledge/meetings/2026-09-22-kettle-and-crumb.md brain/knowledge/meetings/2026-09-24-kettle-and-crumb.md workers/output/after-recap.md
python -m unittest discover -s extra -p test_validate.py -v
python extra/build_summary.py
```

Edit Markdown outputs directly. Edit `extra/build_summary.py` and rebuild to change the summary, or update the CSV only in a separate live-exercise copy and recalculate. The static narrative in `metrics.md`, `plan.md` and the summary must also be reviewed if data changes. The original bad recap is expected to fail validation.

To repeat C2 independently, open a new AI session with no inherited conversation and give it only `workers/skills/skill-recap.md`, `brain/` and `workers/output/bad-recap-source.md`. Ask it to follow the skill and save a new evaluation recap in `workers/output/`; do not show it the before, after or diagnosis. Check the new file against the source and policy. The current after file is retained outside the brain to keep the evaluation separate; its relative links match that location.

## Share the working folder

The private working repository is [ironside-case-study](https://github.com/karroge10/ironside-case-study). Use the [block-c submission branch](https://github.com/karroge10/ironside-case-study/tree/block-c) for the assembled work; `main` retains the original assessment until a final merge is explicitly approved. Grant the assessor repository access before sending the link. Keep raw transcripts and the original bad recap in the restricted assessment folder; share the sanitized summary with the intended assessment audience.

Rebuild with `python extra/build_summary.py --folder-url "https://github.com/karroge10/ironside-case-study/tree/block-c"`. The local HTML opens from a downloaded working folder; its supporting document links are relative. GitHub's normal file viewer does not render HTML as a web page. Publishing a separate artifact is still pending: use an appropriate restricted host and preserve the supporting paths or adapt the links, then test artifact and folder access as a recipient. 

## Three sentences for the submission

Automate call-to-post tracking so every held call has a visible delivery status and late-call alert. Add source-aware recap checks before posting to catch unsupported commitments and restricted content. Build a consent-aware capture or confirmed-note path for WhatsApp calls so West can improve without changing the denominator.
