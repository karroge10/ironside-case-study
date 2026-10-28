import argparse
import html
import json
import re
from metrics import ROOT, calculate

parser = argparse.ArgumentParser()
parser.add_argument('--folder-url', default='https://github.com/karroge10/ironside-case-study')
parser.add_argument('--source-base-url', default='https://github.com/karroge10/ironside-case-study/blob/main/')
args = parser.parse_args()
rows = calculate()
held = sum(row['calls'] for row in rows)
timely = sum(row['timely'] for row in rows)
overall = 100 * timely / held
south = next(row for row in rows if row['pod'] == 'South')
folder_url = html.escape(args.folder_url, quote=True)
chart_data = json.dumps({'items': [{'name': row['pod'], 'value': row['rate']} for row in rows], 'unit': '%', 'max': 100})
coverage_data = json.dumps({'items': [{'name': row['pod'], 'value': round(row['capture_rate'], 1)} for row in rows], 'unit': '%', 'max': 100})
table = ''.join(f'<tr><td class="txt">{row["pod"]}</td><td>{row["timely"]}/{row["calls"]}</td><td>{row["rate"]:.0f}%</td><td>{row["recorded"]}/{row["calls"]}</td></tr>' for row in rows)
body = f"""<header>
<div><h1>Brightline: recap delivery</h1><p class="lede">Where delivery breaks down, what to change first, and how to verify progress.</p></div>
<div class="meta"><b>Source snapshot</b><br>1 to 24 September 2026<br>Proposed pilot, not executed</div>
</header>
<div class="tldr"><p>Start with South: most calls are recorded, but recaps arrive after the team has already sent its notes. Reuse those notes, check commitments and publish one approved recap, aiming for 15 minutes while retaining the official one-hour measure. West needs a separate call-capture or confirmed-note path.</p></div>
<div class="kpis">
<div class="kpi"><div class="l">Overall timely-post rate</div><div class="v">{overall:.1f}%</div><div class="d">{timely} of {held} client calls</div></div>
<div class="kpi"><div class="l">Official target, every pod</div><div class="v">80%</div><div class="d">Within one hour, by 31 October</div></div>
</div>
<section><h2>Delivery and recording coverage</h2><p class="sec-lede">The official result uses all calls held. Recording coverage is a diagnostic, with no separate target.</p>
<div class="grid2">
<div><figure class="chart"><figcaption>Recaps posted within one hour</figcaption><div class="sub">Percentage of all calls held; official target is 80%</div><div data-bars="delivery-data"></div></figure></div>
<div><figure class="chart"><figcaption>Calls recorded</figcaption><div class="sub">Percentage of all calls held; explains whether calls can reach the agent</div><div data-bars="coverage-data"></div></figure></div>
</div>
<script type="application/json" id="delivery-data">{chart_data}</script>
<script type="application/json" id="coverage-data">{coverage_data}</script>
<div class="tbl-wrap"><table><thead><tr><th class="txt">Pod</th><th>Timely / held</th><th>Official result</th><th>Recorded</th></tr></thead><tbody>{table}</tbody></table></div>
<p class="note">East's correct result is 70%. The dashboard's 75% matches division by recorded calls; its original formula is not supplied. Timestamp-based results still require a content audit. <a href="metrics.md">Analysis and evidence</a>.</p></section>
<section><h2>A one-week South pilot</h2>
<p class="sec-lede">South has {south['late']} late posts and a {south['median_post_minutes']:.0f}-minute median delay across {sum(south['posted_by'].values())} posts. Marcus wants recaps posted in 10 to 15 minutes. The first-week process should work without an engineering release.</p>
<div class="tbl-wrap"><table><thead><tr><th class="txt">Timing</th><th class="txt">Proposed routine</th></tr></thead><tbody>
<tr><td class="txt">Before calls</td><td class="txt">Agree reviewer and backup coverage, a destination and a sustainable manual-effort limit.</td></tr>
<tr><td class="txt">At five minutes</td><td class="txt">Use existing AM notes if no usable bot draft is ready. Check accuracy, decisions, actions and confidentiality.</td></tr>
<tr><td class="txt">By 15 minutes</td><td class="txt">Stretch goal: publish a complete, approved recap. An unpublished draft does not count.</td></tr>
<tr><td class="txt">By Friday</td><td class="txt">Conditional planning case: 8/10 calls within 60 minutes, assuming confirmed coverage and capacity; downside 6/10. Replace illustrative counts with Monday's roster. Report both publication thresholds, misses and manual minutes.</td></tr>
</tbody></table></div>
<p>Count the first posted version that meets the checklist, supported by a delivery receipt. Keep phone calls and failures in the denominator. Engineering should trace delays before choosing a fix and test safe retries and manual takeover. <a href="plan.md">Full pilot plan</a> and <a href="fde-ticket.md">engineering request</a>.</p></section>
<section><h2>Other decisions to keep visible</h2>
<p>West has 26 unrecorded calls out of 30. Scope capture or confirmed notes with Lena; counting unposted emails would change the metric. For Kettle &amp; Crumb, confirm creator-approval ownership, sampling eligibility beyond the top-10 offer, the sample-list date and posting baseline. Reconcile the reported account GMV before changing reference data. <a href="answer.md">Affiliate briefing</a> and <a href="proposed-changes.md">updates for approval</a>.</p></section>
<section><h2>What to automate next</h2>
<p>Automate call-to-post tracking so every held call has a visible delivery status and late-call alert. Add source-aware recap checks before posting to catch unsupported commitments and restricted content. Build a consent-aware capture or confirmed-note path for WhatsApp calls so West can improve without changing the denominator.</p></section>
<section><h2>Sources and method</h2>
<ul class="method"><li><a href="calls.csv">Per-call log</a> and <a href="adoption.csv">dashboard</a>, recomputed with <a href="extra/metrics.py">Python</a>; late means more than 60 minutes after call end. Blank timestamps are not evidenced timely posts.</li><li><a href="slack-thread.txt">Pod-lead feedback</a> and <a href="brain/NOW.md">operating notes</a> support the bottleneck diagnosis. Proposed interventions are recommendations, not agreed or achieved outcomes.</li></ul></section>
<footer class="report"><p><a href="{folder_url}">Open working folder</a> | <a href="README.md">Submission guide</a> | <a href="diagnosis.md">Before and after</a> | <a href="validation.md">Validation</a> | <a href="log.md">Activity log</a> | <a href="extra/README.md">Runnable checks</a></p><p>Calculations, recap structure and checker tests verified. Business execution and future performance are not verified. The activity log distinguishes timing evidence from estimates.</p></footer>"""
if args.source_base_url:
    base = args.source_base_url.rstrip('/') + '/'
    body = re.sub(r'href="([^"]+)"', lambda match: match.group(0) if re.match(r'^(?:https?://|#|mailto:)', match.group(1)) else 'href="' + html.escape(base + match.group(1), quote=True) + '"', body)
template = (ROOT / 'extra/report-template.html').read_text(encoding='utf-8')
page = template.replace('{{REPORT_BODY}}', body)
(ROOT / 'summary.html').write_bytes(page.encode('utf-8'))
(ROOT / 'index.html').write_bytes(page.encode('utf-8'))
print(ROOT / 'summary.html')
