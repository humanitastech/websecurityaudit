# Web Security Audit 1.2.1: bringing PHP runtime checks into website security reviews

Web Security Audit is an AI skill for evidence-based website security reviews. Created by **Voxiferum**, for **HumaitasTech**, with support from **Codex**, it helps developers examine application code, hosting evidence, and organizational requirements using Spain's Esquema Nacional de Seguridad (ENS) as a baseline, with relevant ISO guidance as a complement.

Its instructions are maintained in English, while questions and reports follow the user's language. Assessments identify gaps within the reviewed scope; they do not provide ENS or ISO certification.

## How the workflow works

The user selects a review of changes, a component, or a complete declared site boundary. The skill loads relevant modules and records checks, findings, evidence, and limitations. A JSON record connects the results to the inspected revision, and a Python utility generates a Markdown dossier for human inspection.

Technical conclusions and human decisions remain separate. A reviewer can accept or dispute a finding, request a retest, and retain the decision history. These modular records were introduced in version 1.2.0.

## What changes in version 1.2.1

This release adds a dedicated PHP runtime review:

- Inventory of the deployed web-serving PHP version, server interface, package revision, and enabled extensions.
- Verification of vendor backports rather than relying only on the displayed version number.
- Checks for native libraries and Windows package rebuilds.
- Evidence requirements for confirming that updated workers and replicas are serving the corrected build.
- A dated advisory reference and additional manual evaluation scenarios.

## Why application review is not enough

The new module addresses the distinction between application flaws and vulnerabilities in the PHP runtime itself. A clean code review or Composer dependency audit does not establish that the interpreter serving production requests is patched. A developer's local command-line PHP installation may also differ from the hosting environment.

The advisory snapshot, checked on 29 October 2026, references the PHP2Shell advisories CVE-2026-109618 and CVE-2026-109619, the separate session issue CVE-2026-115560, and Windows Brotli rebuilds associated with CVE-2026-111497. Audits must refresh official guidance rather than treat this snapshot as a permanent list of safe versions. See the [PHP security announcements](https://www.php.net/archive/2026.php) and the project's [advisory reference](references/php-advisories.md).

## Requirements and validation

- An AI assistant capable of reading the skill and relevant project evidence.
- Python 3 to use the record validator and report generator; no third-party Python packages are required by those utilities.
- Authorized access or operator-supplied evidence for production runtime checks. Missing evidence remains unverified.

The skill validator and six record-integrity tests passed during preparation. The additional PHP model-evaluation scenarios are documented but have not been executed as independent AI evaluations. This release did not scan or modify a production website.

## Availability

The source, instructions, bibliography, and usage examples are available in [humanitastech/websecurityaudit](https://github.com/humanitastech/websecurityaudit). Release files and notes are available on the [version 1.2.1 release page](https://github.com/humanitastech/websecurityaudit/releases/tag/v1.2.1).
