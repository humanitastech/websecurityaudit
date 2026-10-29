"""Record integrity tests; these do not evaluate the AI's security conclusions."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('records', ROOT / 'scripts/audit_records.py')
records = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(records)


def sample():
    data = json.loads((ROOT / 'assets/audit-template.json').read_text())
    data['modules'] = [dict(id='identity', status='complete', reason='Accounts present', remaining_work='None')]
    data['evidence'] = [dict(id='E1', revision='abc', environment='local', location='policy.py:4',
                             method='Code trace', observation='Ownership check absent', limitations='No deployment access')]
    data['checks'] = [dict(id='AUTH-01', module='identity', title='Object authorization',
                          status='not_satisfied', rationale='Cross-user access path', evidence_ids=['E1'], mappings=[])]
    data['findings'] = [dict(id='F1', title='Cross-user access', severity='high', verdict='confirmed',
                            impact='Other user data', likelihood='Authenticated attacker', confidence='high',
                            reproduction='Local synthetic users', recommendation='Enforce ownership',
                            acceptance_criteria='Other user receives denial', check_ids=['AUTH-01'],
                            evidence_ids=['E1'], review=dict(status='pending'), remediation='open')]
    return data


class RecordTests(unittest.TestCase):
    def test_valid_record_renders_evidence_and_pending_review(self):
        text = records.render(records.validate(sample()))
        self.assertIn('policy.py:4', text)
        self.assertIn('pending', text)

    def test_broken_evidence_link_is_rejected(self):
        data = sample()
        data['checks'][0]['evidence_ids'] = ['missing']
        with self.assertRaises(ValueError):
            records.validate(data)

    def test_unattributed_human_acceptance_is_rejected(self):
        data = sample()
        data['findings'][0]['review']['status'] = 'accepted'
        with self.assertRaises(ValueError):
            records.validate(data)

    def test_fix_without_retest_is_rejected(self):
        data = sample()
        data['findings'][0]['remediation'] = 'verified_fixed'
        with self.assertRaises(ValueError):
            records.validate(data)

    def test_dirty_tree_requires_snapshot(self):
        data = sample()
        data['working_tree'] = 'dirty'
        with self.assertRaises(ValueError):
            records.validate(data)

    def test_unverified_check_is_not_rendered_as_pass(self):
        data = sample()
        data['checks'][0].update(status='not_verified', evidence_ids=[], rationale='Missing code')
        self.assertIn('not_verified', records.render(records.validate(data)))


if __name__ == '__main__':
    unittest.main()
