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
            path.write_text(text.replace('../../brain/', '../../../brain/').replace('(bad-recap-source.md)', '(../bad-recap-source.md)'), encoding='utf-8')
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

    def test_strict_date_format(self):
        for value in ['20260918', '2026-W38-5', '2026-9-18']:
            with self.subTest(value=value):
                errors, _ = self.evaluate(self.clean.replace('| 2026-09-18 |', f'| {value} |'))
                self.assertTrue(any('Action needs exact ISO date' in e for e in errors))
                errors, _ = self.evaluate(self.clean.replace('date: 2026-09-15', f'date: {value}'))
                self.assertTrue(any('Meeting date needs exact ISO date' in e for e in errors))

    def test_broken_link(self):
        errors, _ = self.evaluate(self.clean.replace('accounts-sheet.csv)', 'missing.csv)'))
        self.assertTrue(any('Broken link' in e for e in errors))

    def test_invalid_meeting_date(self):
        errors, _ = self.evaluate(self.clean.replace('date: 2026-09-15', 'date: tomorrow'))
        self.assertTrue(any('Meeting date needs' in e for e in errors))

    def test_multiple_owners(self):
        for owner in ['Lena and Theo', 'Lena & Theo', 'Lena/Theo', 'Lena, Theo']:
            with self.subTest(owner=owner):
                errors, _ = self.evaluate(self.clean.replace('| Lena Varga |', f'| {owner} |'))
                self.assertTrue(any('one confirmed owner' in e for e in errors))

    def test_integer_performance_warning(self):
        _, warnings = self.evaluate(self.clean + '\nGMV was 95000.\n')
        self.assertTrue(any('performance metric' in w for w in warnings))

    def test_diagnostics_do_not_echo_input(self):
        marker = 'SYNTHETIC_TEST_VALUE'
        cases = [
            self.clean.replace('| Lena Varga |', f'| TBD {marker} |'),
            self.clean.replace('| 2026-09-18 |', f'| {marker} |'),
            self.clean.replace('| Lena Varga |', f'| {marker} | |'),
            self.clean + f'\n[link]({marker})\n',
        ]
        for text in cases:
            with self.subTest(text=text):
                errors, warnings = self.evaluate(text)
                self.assertTrue(errors)
                self.assertNotIn(marker, '\n'.join(errors + warnings))

    def test_unmarked_private_content_is_not_detected(self):
        self.assertEqual(self.evaluate(self.clean + '\nSYNTHETIC_UNMARKED_PRIVATE_VALUE\n'), ([], []))


if __name__ == '__main__':
    unittest.main()
