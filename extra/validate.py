import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(path):
    text = path.read_text(encoding='utf-8-sig')
    errors = []
    warnings = []
    sections = ['Summary', 'Action items', 'Open questions', 'Flags for a person']
    positions = [text.find('## ' + s) for s in sections]
    if min(positions) < 0 or positions != sorted(positions):
        errors.append('Required sections missing or out of order')
    front = re.match(r'\A---\n(.*?)\n---', text, re.S)
    metadata = front.group(1) if front else ''
    for field in ['type', 'date', 'account', 'attendees', 'source']:
        if not re.search(rf'^{field}:\s*\S', metadata, re.M):
            errors.append(f'Missing metadata: {field}')
    meeting_date = re.search(r'^date:\s*(.+)$', metadata, re.M)
    if meeting_date:
        try:
            date.fromisoformat(meeting_date.group(1).strip())
        except ValueError:
            errors.append('Meeting date needs exact ISO date')
    source = re.search(r'^source:\s*(.+)$', metadata, re.M)
    if source and not (ROOT / source.group(1).strip()).is_file():
        errors.append('Source path does not resolve from workspace root')
    if min(positions) >= 0:
        summary = text[positions[0]:positions[1]]
        if not 3 <= len(re.findall(r'^- ', summary, re.M)) <= 6:
            errors.append('Summary requires 3 to 6 bullets')
        table = text[positions[1]:positions[2]]
        if '| Owner | Action | Due |' not in table:
            errors.append('Missing action table header')
        for line in table.splitlines():
            if not line.startswith('|') or 'Owner' in line or re.fullmatch(r'[|\s:-]+', line):
                continue
            cells = [c.strip() for c in line.strip('|').split('|')]
            if len(cells) != 3 or not all(cells):
                errors.append('Incomplete action row: ' + line)
                continue
            try:
                date.fromisoformat(cells[2])
            except ValueError:
                errors.append('Action needs exact ISO date: ' + cells[2])
            if re.search(r'\b(TBD|unknown|unassigned)\b|/| & ', cells[0], re.I):
                errors.append('Action needs one confirmed owner: ' + cells[0])
    for label, target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text):
        if '://' not in target and not (path.parent / target.split('#')[0]).exists():
            errors.append('Broken link: ' + target)
    for number, line in enumerate(text.splitlines(), 1):
        if re.search(r'\b(GMV|ad spend|retention|active affiliates)\b', line, re.I) and re.search(r'\$[\d,]+|\b\d+(?:\.\d+)?\s*%|\b\d+[Kk]\b', line):
            warnings.append(f'Review possible copied performance metric at line {number}')
        if re.search(r'\b(flaky|difficult|checked out|between us|agency fees|margin|commission|DMed|home address|phone number)\b', line, re.I):
            warnings.append(f'Review possible restricted content at line {number}')
    return errors, warnings


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Recap structure and policy triage; human source review is required.')
    parser.add_argument('paths', nargs='+')
    args = parser.parse_args()
    failed = False
    for name in args.paths:
        path = ROOT / name
        errors, warnings = check(path)
        print(f'{name}: {len(errors)} errors, {len(warnings)} review warnings')
        for message in errors:
            print('ERROR:', message)
        for message in warnings:
            print('REVIEW:', message)
        failed |= bool(errors)
    raise SystemExit(1 if failed else 0)
