"""Validate audit records and render a human-readable dossier (stdlib only)."""
import argparse
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(data):
    for key in ('schema_version', 'audit_id', 'profile', 'scope', 'revision',
                'environment', 'working_tree', 'summary', 'threat_model'):
        require(isinstance(data.get(key), str) and data[key].strip(), f'Missing string: {key}')
    require(data['schema_version'] == '1.0', 'Unsupported schema version')
    require(data['profile'] in ('changes', 'component', 'full'), 'Invalid profile')
    require(data['working_tree'] in ('clean', 'dirty', 'unknown'), 'Invalid working tree')
    if data['profile'] == 'changes':
        require(bool(data.get('baseline_revision')), 'Changes profile needs baseline_revision')
    if data['working_tree'] == 'dirty':
        require(bool(data.get('working_tree_evidence')), 'Dirty tree needs snapshot evidence')
    for key in ('limitations', 'sources', 'modules', 'evidence', 'checks', 'findings', 'history'):
        require(isinstance(data.get(key), list), f'Missing array: {key}')
    indexes = {}
    for group in ('modules', 'evidence', 'checks', 'findings'):
        rows = data[group]
        require(all(isinstance(row, dict) and isinstance(row.get('id'), str)
                    and row['id'].strip() for row in rows), f'Invalid ID in {group}')
        indexes[group] = {row['id']: row for row in rows}
        require(len(indexes[group]) == len(rows), f'Duplicate ID in {group}')
    def fields(row, keys):
        for key in keys:
            require(isinstance(row.get(key), str) and row[key].strip(), f'{row["id"]}: missing {key}')
    for row in data['modules']:
        fields(row, ('reason', 'remaining_work'))
        require(row.get('status') in ('pending', 'partial', 'complete', 'blocked', 'excluded'), 'Invalid module status')
    for row in data['evidence']:
        fields(row, ('revision', 'environment', 'location', 'method', 'observation', 'limitations'))
    for row in data['checks']:
        fields(row, ('title', 'rationale'))
        require(row.get('module') in indexes['modules'], 'Unknown check module')
        require(indexes['modules'][row['module']]['status'] != 'excluded', 'Check in excluded module')
        require(row.get('status') in ('satisfied', 'partial', 'not_satisfied', 'not_verified', 'not_applicable'), 'Invalid check status')
        require(isinstance(row.get('evidence_ids'), list), 'Missing check evidence_ids')
        require(all(e in indexes['evidence'] for e in row['evidence_ids']), 'Unknown check evidence')
        if row['status'] in ('satisfied', 'partial', 'not_satisfied'):
            require(bool(row['evidence_ids']), 'Verified check needs evidence')
        require(isinstance(row.get('mappings'), list), 'Missing mappings')
        for mapping in row['mappings']:
            require(all(mapping.get(k) for k in ('criterion', 'source', 'rationale')), 'Incomplete mapping')
            require(mapping.get('status') in ('verified', 'provisional'), 'Invalid mapping status')
    for row in data['findings']:
        fields(row, ('title', 'impact', 'likelihood', 'confidence', 'reproduction', 'recommendation', 'acceptance_criteria'))
        require(row.get('severity') in ('critical', 'high', 'medium', 'low', 'informational'), 'Invalid severity')
        require(row.get('verdict') in ('confirmed', 'unconfirmed', 'refuted'), 'Invalid verdict')
        for key, group in (('check_ids', 'checks'), ('evidence_ids', 'evidence')):
            require(isinstance(row.get(key), list) and row[key], f'Missing {key}')
            require(all(i in indexes[group] for i in row[key]), f'Unknown {key}')
        review = row.get('review', {})
        require(review.get('status') in ('pending', 'accepted', 'disputed', 'retest_requested'), 'Invalid human review')
        if review['status'] != 'pending':
            require(all(review.get(k) for k in ('reviewer', 'at', 'rationale')), 'Decision needs attribution')
            require(any(e.get('subject') == row['id'] and e.get('type') == 'human_review' for e in data['history']), 'Decision needs history')
        require(row.get('remediation') in ('open', 'in_progress', 'ready_for_retest', 'verified_fixed'), 'Invalid remediation')
        if row['remediation'] == 'verified_fixed':
            require(any(e.get('subject') == row['id'] and e.get('type') == 'retest_passed'
                        and e.get('revision') and e.get('evidence_ids')
                        and all(i in indexes['evidence'] for i in e['evidence_ids'])
                        for e in data['history']), 'Fixed finding needs retest evidence')
    for event in data['history']:
        require(isinstance(event, dict) and all(event.get(k) for k in ('at', 'actor', 'type', 'subject', 'detail')), 'Incomplete history event')
    return data


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def render(data):
    # Labels are structural; record narratives retain the user's language.
    lines = [f'# Audit {data["audit_id"]}', '', data['summary'], '',
             f'Profile: {data["profile"]} | Revision: {data["revision"]}',
             f'Environment: {data["environment"]} | Working tree: {data["working_tree"]}',
             '', '## Scope', '', data['scope'], '', '## Threat model', '', data['threat_model'],
             '', '## Limitations', ''] + [f'- {x}' for x in data['limitations']]
    for title, group, columns in (
        ('Modules and remaining work', 'modules', ('id', 'status', 'reason', 'remaining_work')),
        ('Coverage', 'checks', ('id', 'module', 'title', 'status', 'rationale', 'evidence_ids'))):
        lines += ['', f'## {title}', '', '| ' + ' | '.join(columns) + ' |',
                  '| ' + ' | '.join('---' for _ in columns) + ' |']
        lines += ['| ' + ' | '.join(cell(row.get(c, '')) for c in columns) + ' |' for row in data[group]]
    for title, group in (('Findings and human decisions', 'findings'), ('Evidence dossier', 'evidence'),
                        ('Normative mappings', 'checks'), ('History', 'history'), ('Sources', 'sources')):
        lines += ['', f'## {title}', '']
        for row in data[group]:
            if group == 'checks':
                row = {'check_id': row['id'], 'mappings': row['mappings']}
            lines += ['```json', json.dumps(row, ensure_ascii=False, indent=2), '```', '']
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('validate', 'render'))
    parser.add_argument('record', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        data = validate(json.loads(args.record.read_text(encoding='utf-8-sig')))
        if args.command == 'render':
            require(args.output is not None, 'Render needs --output')
            require(not args.output.exists(), 'Output exists; choose a new path')
            args.output.write_text(render(data), encoding='utf-8')
        print('Valid audit record (structure only).')
    except (ValueError, OSError, TypeError, KeyError, AttributeError) as error:
        parser.exit(1, f'{error}\n')


if __name__ == '__main__':
    main()
