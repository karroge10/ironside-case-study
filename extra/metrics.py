import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]


def calculate():
    with (ROOT / 'calls.csv').open(encoding='utf-8-sig', newline='') as f:
        calls = list(csv.DictReader(f))
    with (ROOT / 'adoption.csv').open(encoding='utf-8-sig', newline='') as f:
        dashboard = {r['pod']: r for r in csv.DictReader(f)}
    assert len({r['call_id'] for r in calls}) == len(calls)
    result = []
    for pod in dashboard:
        rows = [r for r in calls if r['pod'] == pod]
        posted = [r for r in rows if r['recap_posted_at']]
        delays = [(datetime.fromisoformat(r['recap_posted_at']) - datetime.fromisoformat(r['call_end'])).total_seconds() / 60 for r in posted]
        assert all(d >= 0 for d in delays)
        timely = sum(d <= 60 for d in delays)
        recorded = sum(r['recorded'] == 'yes' for r in rows)
        d = dashboard[pod]
        assert (len(rows), recorded, timely) == (int(d['client_calls_held']), int(d['calls_recorded']), int(d['recaps_posted_within_1hr']))
        result.append(dict(pod=pod, calls=len(rows), recorded=recorded, timely=timely, late=len(delays)-timely, missing=len(rows)-len(delays), rate=100*timely/len(rows), capture_rate=100*recorded/len(rows), timely_of_recorded=100*timely/recorded, median_post_minutes=median(delays), dashboard_rate=d['share_of_calls_with_recap_within_1hr'], posted_by=dict(Counter(r['posted_by'] for r in posted)), gap_to_80=max(0, int(0.8*len(rows)+0.999999)-timely)))
    return sorted(result, key=lambda r: r['rate'], reverse=True)


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
