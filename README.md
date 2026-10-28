# Ironside assessment: working folder

Start with the [rendered summary](https://karroge10.github.io/ironside-case-study/) or open [summary.html](summary.html) locally. All conclusions use the provided September 2026 snapshot, not live business data. No people, account or reference-sheet updates have been applied.

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

All nine assessment questions and the optional extra credit are completed. See [usage and approximate time](log.md), [validation evidence and limitations](validation.md), and the [prioritized improvement roadmap](roadmap.md).

## Reproduce results

From this folder, with Python 3 and no third-party packages:

```
python extra/metrics.py
python extra/validate.py brain/knowledge/meetings/2026-09-22-kettle-and-crumb.md brain/knowledge/meetings/2026-09-24-kettle-and-crumb.md workers/output/after-recap.md
python -m unittest discover -s extra -p test_validate.py -v
python extra/build_summary.py
```

Edit Markdown outputs directly. Edit `extra/build_summary.py` and rebuild to change the summary; its portable layout and embedded fonts are in `extra/report-template.html`. To explore different input data, use a separate copy and recalculate. The static narrative in `metrics.md`, `plan.md` and the summary must also be reviewed if data changes. The original bad recap is expected to fail validation.

To repeat C2 independently, open a new AI session with no inherited conversation and give it only `workers/skills/skill-recap.md`, `brain/` and `workers/output/bad-recap-source.md`. Ask it to follow the skill and save a new evaluation recap in `workers/output/`; do not show it the before, after or diagnosis. Check the new file against the source and policy. The current after file is retained outside the brain to keep the evaluation separate; its relative links match that location.

## Repository and report

The public working repository is [ironside-case-study](https://github.com/karroge10/ironside-case-study). The assembled submission is on `main`; the block branches preserve the review stages. The [original baseline](https://github.com/karroge10/ironside-case-study/tree/e09d80872fdbd0c8bc8958a3abc732f2bebc7b4c) remains available in history. The supplied fictional source materials remain preserved.

GitHub Pages serves the rendered report from `main` at [the artifact URL](https://karroge10.github.io/ironside-case-study/), while the repository provides the working files. Rebuild with `python extra/build_summary.py`; it produces identical `summary.html` and `index.html`, with supporting links pointing to readable GitHub documents on `main`. For relative links in an offline working-folder copy, use `python extra/build_summary.py --source-base-url=`. Push an approved report update to `main` to trigger a Pages rebuild.

The archived `workers/output/skill-recap-v1.md` and `after-recap-v1.md` preserve the first C2 test before the policy-reference revision. They are intentional evaluation evidence, not temporary files. Embedded fonts make the report portable; Python caches and local test copies are excluded.

## Next automation

Automate call-to-post tracking so every held call has a visible delivery status and late-call alert. Add source-aware recap checks before posting to catch unsupported commitments and restricted content. Build a consent-aware capture or confirmed-note path for WhatsApp calls so West can improve without changing the denominator.
