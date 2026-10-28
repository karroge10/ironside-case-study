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
            value = meeting_date.group(1).strip()
            if not re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', value):
                raise ValueError
            date.fromisoformat(value)
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
        for number, line in enumerate(table.splitlines(), text[:positions[1]].count('\n') + 1):
            if not line.startswith('|') or line.strip() == '| Owner | Action | Due |' or re.fullmatch(r'[|\s:-]+', line):
                continue
            cells = [c.strip() for c in line.strip('|').split('|')]
            if len(cells) != 3 or not all(cells):
                errors.append(f'Incomplete action row at line {number}')
                continue
            try:
                if not re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', cells[2]):
                    raise ValueError
                date.fromisoformat(cells[2])
            except ValueError:
                errors.append(f'Action needs exact ISO date at line {number}')
            if re.search(r'\b(TBD|unknown|unassigned|and)\b|/|&|;|,', cells[0], re.I):
                errors.append(f'Action needs one confirmed owner at line {number}')
    for number, line in enumerate(text.splitlines(), 1):
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', line):
            if '://' not in target and not (path.parent / target.split('#')[0]).exists():
                errors.append(f'Broken link at line {number}')
    for number, line in enumerate(text.splitlines(), 1):
        if re.search(r'\b(GMV|ad spend|retention|active affiliates)\b', line, re.I) and re.search(r'\b\d[\d,]*(?:\.\d+)?[Kk]?\b', re.sub(r'\b\d+[- ]day\b', '', line, flags=re.I)):
            warnings.append(f'Review possible copied performance metric at line {number}')
        if re.search(r'\b(flaky|difficult|checked out|between us|agency fees|margin|commission|DMed|home address|phone number)\b', line, re.I):
            warnings.append(f'Review possible restricted content at line {number}')
    return errors, warnings


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Recap structure and policy triage; human source review is required.')
    parser.add_argument('paths', nargs='+')
    args = parser.parse_args()
    failed = False
    for input_number, name in enumerate(args.paths, 1):
        path = ROOT / name
        errors, warnings = check(path)
        print(f'Input {input_number}: {len(errors)} errors, {len(warnings)} review warnings')
        for message in errors:
            print('ERROR:', message)
        for message in warnings:
            print('REVIEW:', message)
        failed |= bool(errors)
    raise SystemExit(1 if failed else 0)
