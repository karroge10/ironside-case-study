import tempfile
import unittest
from pathlib import Path
from validate import ROOT, check


class RecapChecks(unittest.TestCase):
    def setUp(self):
        self.clean = (ROOT / 'workers/output/after-recap.md').read_text(encoding='utf-8-sig')

    def evaluate(self, text):
        with tempfile.TemporaryDirectory(dir=ROOT / 'workers/output') as directory:
            path = Path(directory) / 'recap.md'
            path.write_text(text.replace('../../brain/', '../../../brain/'), encoding='utf-8')
            return check(path)

    def test_known_good(self):
        self.assertEqual(check(ROOT / 'workers/output/after-recap.md'), ([], []))

    def test_known_bad(self):
        errors, warnings = check(ROOT / 'workers/output/bad-recap.md')
        self.assertEqual(len(errors), 3)
        self.assertEqual(len(warnings), 2)
        self.assertTrue(all(' at line ' in w for w in warnings))

    def test_missing_owner(self):
        errors, _ = self.evaluate(self.clean.replace('| Lena Varga |', '| TBD |'))
        self.assertTrue(any('one confirmed owner' in e for e in errors))

    def test_invalid_action_date(self):
        errors, _ = self.evaluate(self.clean.replace('| 2026-09-18 |', '| 2026-02-30 |'))
        self.assertTrue(any('exact ISO date' in e for e in errors))

    def test_broken_link(self):
        errors, _ = self.evaluate(self.clean.replace('accounts-sheet.csv)', 'missing.csv)'))
        self.assertTrue(any('Broken link' in e for e in errors))

    def test_invalid_meeting_date(self):
        errors, _ = self.evaluate(self.clean.replace('date: 2026-09-15', 'date: tomorrow'))
        self.assertTrue(any('Meeting date needs' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
