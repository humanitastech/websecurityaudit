---
name: ht-web-security-audit-ens
description: Audit websites and web applications with evidence, using Spain's ENS as the baseline and relevant ISO standards as complementary guidance. Use for security audits, compliance assessments, or ENS security reviews, not routine website changes.
---

# HT Web Security Audit — ENS

Produce a traceable technical and documentary assessment. ENS refers to Spain's Esquema Nacional de Seguridad. The result is a gap assessment within the examined scope, not ENS or ISO certification.

## Language

Respond in the language used by the user, including questions, progress updates, findings, reports, and remediation plans. Follow an explicitly requested output language instead when provided. If the conversation changes language, follow the latest clear preference. Preserve official standard names, control identifiers, code, paths, and quoted evidence; explain their meaning in the user's language. These skill instructions remain in English regardless of the response language.

## Scope and criteria

1. Identify the repository, URLs, environment, ownership, system boundaries, external services, processed data, and assessment purpose. Start with available local inspection; ask only for information that blocks specific decisions or tests.
2. Determine whether ENS applies by law or contract, or is voluntarily adopted as a reference. Do not assume every private website is subject to ENS. Distinguish the web application from the complete system, including infrastructure, people, processes, and suppliers.
3. Read [normative references](references/standards.md) and verify current versions through official sources for each audit. Record the date, edition, and source. If access is unavailable, disclose the limitation and avoid definitive normative conclusions.
4. Request the existing ENS category and statement of applicability. Without documentation, develop a provisional categorization of availability, authenticity, integrity, confidentiality, and traceability according to Annex I; do not assume BÁSICA because a website is small. Distinguish the system category from dimension levels. Record assumptions and who must validate the category.
5. Derive controls, enhancements, and required evidence from the category, dimension levels, risk analysis, and any approved specific compliance profile. Meanwhile, perform technical checks independent of the category and leave normative applicability pending.

## ENS and ISO compatibility

Applicable ENS requirements are the mandatory baseline for this assessment. ISO complements management, risk, and application security without replacing ENS requirements. Technical similarity between controls does not establish normative equivalence or full compliance.

For each mapping, record the confirmed ENS identifier, verified ISO reference, rationale, differences, and required evidence. Do not invent clause numbers, mappings, or content from paid standards. If only a public summary is available, mark the ISO mapping as provisional and its clause as unverified.

If criteria appear to conflict, explain both requirements and propose a solution satisfying both; do not discard an ENS requirement for convenience. Compensating measures require documented justification, evidence of equivalent or stronger protection, and handling under the current ENS rules. An audit recommendation does not approve an exception. Other applicable legal or contractual duties still require their own analysis.

## Execution

Read [checks and evidence](references/checks.md). Prioritize surfaces actually present in the project. Inspect code, configuration, dependencies, and documentation; connect behavior to data flows and privileges. Record the commit, environment, tools, relevant commands, and coverage.

An audit request authorizes assessment, not fixes, publication, or account changes. Non-destructive local tests may proceed within the authorized scope. Before active scanning, fuzzing, exploitation, or authenticated testing of remote systems, establish authorization covering the target, method, environment, and limits; use existing session authorization when sufficient. Links or integrations do not imply permission to test third-party services. Prefer local reproduction with synthetic data; stop tests that affect availability or data outside the scope. Do not copy secrets or personal data into reports or external services.

Assign each result a status: satisfied within the verified scope, partially satisfied, not satisfied, not verified, or not applicable with justification. Missing documentation is an evidence gap, not automatic proof of a vulnerability; no findings does not prove security. Tool results require triage and context. Evaluate tools and unfamiliar scripts before installing or executing them.

## Deliverables

Save a Markdown report in the project or requested location, in the user's language, including:

- Scope, date, normative versions, validated or provisional category, assumptions, and limitations.
- Main risks and actual coverage, without a compliance percentage based only on technical checks.
- Matrix: ENS requirement and applicable enhancement; ISO complement; evidence; status; gap; action. Include applicable organizational requirements, marking them not verified when documents are missing.
- Findings: ID, severity justified by impact and likelihood, confidence, file/line or endpoint, sanitized evidence, safe reproduction, consequence, related requirement, and recommended fix. Separate confirmed vulnerabilities, hypotheses, and documentary gaps. Use CVSS only with a justified version and vector.
- Prioritized remediation plan, suggested owners, dependencies, and verifiable acceptance criteria. Distinguish technical urgency from normative gaps.
- Outstanding evidence and the need for an independent formal assessment where relevant.

If the user also requests fixes, implement authorized changes, test affected flows, and update the report with before/after results. Do not claim remediation solely because code changed.
