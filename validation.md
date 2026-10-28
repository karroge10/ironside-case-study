# Validation evidence and limitations

Checks below were performed with AI and local scripts. They do not establish client approval or business execution.

## Source checks

| Output | Evidence | Result |
|---|---|---|
| [A1 recap](brain/knowledge/meetings/2026-09-22-kettle-and-crumb.md) | [Call 1](inbox/call-1.md), 00:29 to 01:36, and linked prior meetings | Five supported action rows; relative dates resolve to 22, 23 and 25 September. Shipment ownership remains open. Private content and copied performance figures excluded. |
| [A2 recap](brain/knowledge/meetings/2026-09-24-kettle-and-crumb.md) | [Call 2](inbox/call-2.md), 00:05 to 01:13, and reference sheet | Marcus's plan is due 29 September. Sample-list Thursday and GMV comparability remain unresolved. The candidate GMV update appears only in the approval proposal. |
| [C2 result](workers/output/after-recap.md) | [Source](workers/output/bad-recap-source.md), 00:08 to 00:37, and 10 September meeting | Four summary bullets; Lena's brief due 18 September; size-chart investigation and October delivery details remain open. Prior decisions linked and private content excluded. |

Client sample budgets, targets and creator commissions are treated as client-agreed decisions under RESOLVER. SANITIZER's prohibition on our fees, margins and rates is interpreted as Brightline's commercial terms. The briefing dates the creator-rate agreement rather than claiming later reconfirmation. The later GMV claims and reference figures have different or unclear reporting periods, so a numerical difference does not establish like-for-like growth.

## C2 fresh-session evaluation

Two independent conversations were launched with no inherited conversation (`fork_turns: none`). Each was instructed to read only the skill, brain and source transcript. The first [skill version](workers/output/skill-recap-v1.md) and [result](workers/output/after-recap-v1.md) are preserved. After simplifying the skill to reference authoritative policies, the second session generated the current [after recap](workers/output/after-recap.md), which has not been manually edited.

Both sessions reported reading:

```
workers/skills/skill-recap.md
workers/output/bad-recap-source.md
brain/RESOLVER.md
brain/SANITIZER.md
brain/knowledge/accounts/loop-athletic.md
brain/knowledge/people/lena-varga.md
brain/knowledge/reference/accounts-sheet.csv
brain/knowledge/meetings/2026-09-10-loop-athletic-weekly.md
```

They also listed brain filenames and reread their generated output. The old recap, diagnosis and previous results were not supplied. The conversations shared a filesystem, so the read restrictions were instructional, not sandbox-enforced. The final output was compared with the transcript, policies and earlier meeting, then checked programmatically. One source case demonstrates this improvement, not broad reliability; the creator-rate interpretation was not separately exercised by this transcript.

## Reproducible checks

- `python extra/metrics.py`: 140 distinct calls; all dashboard counts reconcile; timely rates are 90%, 70%, 35% and 10%. Independent datetime-based recounting confirmed the results. East's displayed 75% is inconsistent with the all-call denominator.
- `python extra/validate.py brain/knowledge/meetings/2026-09-22-kettle-and-crumb.md brain/knowledge/meetings/2026-09-24-kettle-and-crumb.md workers/output/after-recap.md`: zero errors and warnings for all three. The supplied bad recap returns three structural errors and two review warnings.
- `python -m unittest discover -s extra -p test_validate.py -v`: eleven tests passed, including synthetic error-path disclosure probes, multiple-owner checks, strict YYYY-MM-DD date validation and plain-integer performance warnings. An unmarked private-content probe deliberately demonstrates the checker cannot establish confidentiality. Diagnostics report categories and line numbers, not input values. Keyword checks cannot prove factual accuracy or correct ownership.
- Calendar dates, the conditional 70-box budget illustration and relative document links were checked. The engineering ticket remains under 150 words. The extra-credit README is five lines; the activity log is ten.
- The report rebuilds byte-for-byte. Unauthenticated live browser checks at 390 and 1280 pixels confirmed HTTP 200, eight correctly valued bars, embedded fonts, full-width text, no horizontal page overflow and no JavaScript errors. The report makes no third-party resource requests. Four document links initially hit bulk-request throttling; normal browser retests returned 200.
- All 46 tracked paths and published branch history were audited for temporary files and common credential patterns. No tracked caches, dependency folders, databases, environment files or media dumps were found. All 21 original files other than the required skill revision remain byte-for-byte unchanged; the original 22-file baseline is preserved in history.

## Limits

The pilot is proposed, not executed. Unknown owners, dates, definitions and completion status remain explicitly flagged. The skill evaluation and checker do not establish performance on unseen calls. Time figures in [log.md](log.md) are approximate: completed AI-turn metadata supports the AI estimate, and the human estimate was confirmed by the candidate rather than treated as a measurement from discussion gaps.
