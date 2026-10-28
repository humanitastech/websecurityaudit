# Profiles, checkpoints, and human inspection

Use the same record contract across all modules. JSON keys and enum values stay in English; narrative values and rendered reports follow the user's language. Consult `assets/audit-template.json` for the complete minimal shape and run `scripts/audit_records.py` to validate and render it. No external packages are needed.

## Select a profile

- `changes`: review a specified baseline/target diff and affected behavior; do not claim whole-site coverage.
- `component`: review named routes, files, or features and their relevant dependencies.
- `full`: inventory the entire declared site boundary, including documentary requirements. Full describes intended scope, not guaranteed completion.

Start with scope, commit, environment, working-tree state, evidence availability, and a compact threat model. Select modules using [modules/index.md](modules/index.md). Load only selected module instructions. Log excluded modules and reasons as well as selected ones. A module may contain checks that are not applicable. Select check scope by risk and explain omissions; module completion is not proof that all possible vulnerabilities were checked.

## Records and artifacts

Create an output directory chosen by the user, otherwise `audit-results/<audit-id>/` in the project. Never overwrite an existing audit silently. Keep:

- `audit.json`: machine-readable source of truth for scope, modules, checks, findings, evidence, sources, and append-only history.
- `report.md`: decision summary, coverage table, findings, review decisions, evidence dossier, normative mappings, and limitations, generated from the JSON. Renderer counts are coverage counts, never conformity percentages.
- `evidence/`: minimal sanitized supporting artifacts when necessary. Record paths and identifiers in JSON. Do not store credentials, live session material, or unnecessary personal data.

Populate the template with actual results; an empty template is only a starting point. Give each check a stable ID (for example `AUTH-01`) and each finding its own stable ID. Checks can cite multiple findings. Findings cite existing checks and evidence. Evidence must specify revision/environment, source location, method, observation, and limitations. Add file lines, symbols, test commands, and sanitized outputs in those strings where relevant.

Check statuses: `satisfied`, `partial`, `not_satisfied`, `not_verified`, `not_applicable`. Require evidence for verified outcomes and rationale for every status. Finding verdicts: `confirmed`, `unconfirmed`, `refuted`; confidence and severity are separate fields. Normative mappings belong to individual checks: include criterion, source, applicability rationale, and `verified` or `provisional` mapping status. Do not invent ENS/ISO identifiers.

## Human decisions and history

Each finding has a review object with status `pending`, `accepted`, `disputed`, or `retest_requested`. Acceptance means agreement with the finding, not acceptance of residual risk or closure. The agent leaves human decisions pending unless a human explicitly supplies a decision. Record reviewer identity, timestamp, rationale, and the referenced finding/version. Never invent approval. Keep a chronological event for every decision, correction, and retest; do not erase a disputed or refuted finding to improve the summary.

Remediation statuses: `open`, `in_progress`, `ready_for_retest`, `verified_fixed`. Only mark fixed when a recorded retest on the new revision demonstrates the acceptance criteria. A human dispute does not automatically change the technical verdict.

## Resume and invalidate

Checkpoint after each module and before interruption: save completed/partial/blocked state, remaining work, and record history. `complete` means the declared checks are recorded, not that they passed. Resuming the same revision still requires checking environment and uncommitted changes. Record dirty-tree changes with a content digest or a retained sanitized patch; never treat a commit hash alone as a snapshot of uncommitted code.

If code, configuration, dependencies, or environment changed, create a new audit ID with `previous_audit_id`, retain the old record, and record changed files and environment differences. Determine affected modules from evidence dependencies and callers, not file names alone. Start affected checks at `not_verified`; carry unaffected observations only with a written justification. Prior human acceptance does not approve a changed finding. If impact cannot be bounded, re-evaluate rather than marking old evidence current.

## Inspect and deliver

Run `python scripts/audit_records.py validate <audit.json>` and then `python scripts/audit_records.py render <audit.json> --output <report.md>`. Structural validation does not verify vulnerabilities, reviewer identity, or conformity. Inspect the rendered report for sensitive data and misleading conclusions. Include unresolved review decisions, unexecuted checks, and remaining work. No HTML viewer is required for this version.
