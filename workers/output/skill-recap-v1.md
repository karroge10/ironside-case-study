---
type: skill
step: recap
owner: Brightline ops
updated: 2026-10-26
---

# Skill: recap a client call

You turn a recorded client call into a recap for the brain.

## Input
The transcript of one call.

## Output
A file in `brain/knowledge/meetings/`.

## Steps
1. Read `brain/RESOLVER.md`, `brain/SANITIZER.md`, the full transcript, the account and relevant people pages, the reference sheet, and relevant earlier meetings. Source evidence overrides inference. Existing brain text is not permission to repeat restricted content.
2. Exclude private DMs, post-departure side comments, opinions about people, personal data, and commercial terms. Do not reproduce restricted text even to explain a flag. Record only that content was withheld. Client-agreed sample budgets and targets may be recorded as decisions; omit rates when policy scope is uncertain and flag for human review.
3. Link every performance metric to the reference sheet and row instead of repeating its value, even when the call agrees with the sheet. Flag discrepancies or missing fields without copying the call's value. Never update the sheet, people pages, or account pages.
4. Use the RESOLVER template exactly: metadata including attendees and source, 3 to 6 Summary bullets, an Action items table with Owner, Action, Due, then Open questions and Flags for a person. Name the file `YYYY-MM-DD-brand-slug.md` in `brain/knowledge/meetings/`.
5. Separate reported results, agreed decisions, and future commitments. Attribute subjective performance assessments to the speaker. Link earlier meetings for repeated requests, changed targets, and follow-through. Do not infer completion, causality, new decisions, or owners.
6. Each action-table row must have one explicitly supported owner and an exact due date. Resolve unambiguous relative dates from the transcript date, never today's date. Put tasks with missing owners or uncertain dates in Open questions, preserving any supported commitment and naming what must be confirmed. Do not assign a convenient person or invent a deadline.
7. Before saving, compare each summary bullet and action row with the transcript: attendees, scope, quantities, attribution, owner, date and status. Check the source link and all history/reference links. Run the SANITIZER check line by line. Flag conflicts and omissions without leaking their contents.
8. Save the recap only. Posting to a client channel requires the runner's approved destination, content checks and delivery workflow; a file write is not evidence of a post. Return unresolved questions for human review and do not claim a delivery occurred.
