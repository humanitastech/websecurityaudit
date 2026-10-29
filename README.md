# HT Web Security Audit — ENS

An evidence-driven AI skill for auditing websites and web applications against Spain's **Esquema Nacional de Seguridad (ENS)**, with relevant ISO standards as complementary guidance.

**Author:** Voxiferum, for HumaitasTech, with support from Codex.

GitHub home: [humanitastech](https://github.com/humanitastech).

## What it does

- Reviews source code, configuration, dependencies, infrastructure evidence, and organizational documentation.
- Uses applicable ENS requirements as the baseline and ISO/IEC 27001, 27002, 27005, and 27034 where relevant.
- Distinguishes confirmed vulnerabilities, provisional hypotheses, and missing evidence.
- Produces a traceable findings report, requirements matrix, and prioritized remediation plan.
- Responds and writes reports in the user's language. The skill itself is maintained in English.
- Covers static sites, CMS sites, server-rendered applications, SPAs, and their APIs, selecting checks for the features actually present.
- Models realistic threats, verifies candidate findings, reviews security-sensitive changes, and validates authorized fixes.

The [bibliography](references/bibliography.md) credits methodological references from OpenAI and Trail of Bits and separates them from ENS/ISO normative sources. These references do not require installing additional skills.

This is an assessment workflow, not an automated scanner or certification service. It does not establish ENS or ISO conformity by itself. Normative versions and applicability must be verified for each assessment. It does not include copyrighted ISO standard texts.

## Files

```text
SKILL.md                  Main skill instructions
references/standards.md    Official sources and standard selection
references/checks.md       Technical inspection and evidence guidance
references/web-review.md   Website assessment and development review workflow
references/bibliography.md Methodological and normative bibliography
VERSION                    Release version
```

## Use with Codex

Download or clone this repository, then place its contents in a folder named `ht-web-security-audit-ens` in your Codex skills directory. Keep `SKILL.md` and `references/` together. In installations using a personal `~/.codex/skills` directory, the entry point is:

```text
~/.codex/skills/ht-web-security-audit-ens/SKILL.md
```

Start a new session if needed for discovery, open the project you own or are authorized to assess, and invoke:

```text
Use $ht-web-security-audit-ens to audit this project.
Start with a non-destructive local review. Produce a Markdown report
with evidence, ENS applicability gaps, and prioritized remediation.
Respond in English.
```

Replace the final language instruction or omit it to use your conversation language. Give the agent the system boundaries, environment, ENS category and statement of applicability if known, and relevant documentation. Unknown categorization is treated as provisional.

## Use with ChatGPT

For a portable, manual workflow, attach or paste `SKILL.md` and the Markdown files in `references/` into a conversation that supports the required inputs. Ask:

```text
Use the attached HT Web Security Audit — ENS instructions as the
workflow for this assessment. Read the relevant reference documents.
Review only the files and evidence I provide. Identify anything
you cannot verify. Respond in my language.
```

Then provide sanitized source files, configuration, and documentation within the product's supported limits. A chat cannot inspect your local filesystem or execute tests without suitable tools and access. Pasting instructions or sharing a GitHub URL does not install a native skill. Native skill/plugin support depends on the product and workspace; follow its current installation documentation when available.

Official background: [OpenAI skill concepts](https://developers.openai.com/plugins/concepts/skills).

## Use with other AI assistants

The instructions are plain Markdown and can be supplied as context to another assistant. Include the reference files and explicitly ask it to follow the workflow. For agents that support `SKILL.md`, follow that agent's own installation and discovery documentation; folder locations, invocation syntax, tools, and permission behavior differ. Compatibility has not been independently tested across other products.

An assistant without browsing must report that it cannot verify current normative versions. An assistant without execution or repository access must limit conclusions to supplied evidence. Do not claim tests ran when they did not.

## Scope and authorization

Use only on systems you own or are authorized to assess. Define targets, environment, permitted methods, and limits before active remote testing. Remove credentials and personal data from shared evidence. An audit request does not itself authorize fixes or publication. The skill preserves these boundaries and requires evidence for findings.

## Branches and versioning

- `main`: initial public baseline and documentation.
- `dev`: development branch carrying version `1.2.1`.
- Tag `v1.1.0`: snapshot of the website-focused update on `dev` at publication.
- Tag `v1.0.0`: preserved initial release.

The GitHub release targets `dev`; it does not merge `dev` into `main`. Branches may advance after the tag is created. See [CHANGELOG.md](CHANGELOG.md) for release details.

## Credits and rights

Created by **Voxiferum**, for **HumaitasTech**, with support from **Codex**. ENS, ISO, and OpenAI names identify external standards or products; no endorsement is claimed.

No open-source license has been selected for this release. Public visibility does not by itself grant a general license to redistribute or modify the original material. Ask the author about reuse terms. Referenced standards retain their respective rights.

## Modular audits and human inspection

Choose changes, component, or full scope. The skill loads only relevant modules and saves a revision-bound audit.json plus a Markdown dossier. Human acceptance is separate from technical confirmation; missing evidence and pending checks remain visible. See [record workflow](references/audit-records.md) and [module catalog](references/modules/index.md).

Start from assets/audit-template.json. Validate with Python: python scripts/audit_records.py validate audit.json. Generate a new report with: python scripts/audit_records.py render audit.json --output report.md. No third-party packages are required. Structural checks do not establish security or conformity. Run integrity tests with python -m unittest discover -s tests. Manual AI evaluation scenarios are in tests/behavioral-cases.md.

## PHP runtime advisories

PHP sites also load the runtime module, covering deployed versions, vendor backports, native dependencies, and rollout evidence. See [dated PHP advisory snapshot](references/php-advisories.md) and [PHP runtime checks](references/modules/php-runtime.md). Official guidance is refreshed per audit; a clean source-code review or Composer audit does not establish runtime safety.
