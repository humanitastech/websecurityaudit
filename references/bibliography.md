# Bibliography

## PHP runtime security sources (consulted 2026-10-29)

- **PHP Security Team.** [October 2026 announcements and follow-up notices](https://www.php.net/archive/2026.php).
- **PHP project.** [GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) and [GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp).
- **CERT-EU.** [Security advisory 2026-018](https://cert.europa.eu/publications/security-advisories/2026-018/).
- **Google Brotli maintainers.** [Brotli 1.2.1 security release](https://github.com/google/brotli/releases/tag/v1.2.1).

These are technical advisories, not new ENS/ISO requirements. See [PHP snapshot](php-advisories.md) for dated applicability guidance; revalidate during each audit.

Consulted: 2026-10-14. Upstream `main` links are living references and may change. Recheck content, versions, licenses, and applicability before reusing upstream material. Inclusion does not imply endorsement or compliance validation.

## Methodological references

1. **OpenAI.** [security-threat-model](https://github.com/openai/skills/tree/main/skills/.curated/security-threat-model). Agent skill. Reference for repository-backed threat models, attacker capabilities, trust boundaries, and abuse paths. Upstream skill includes an Apache-2.0 license file.
2. **Trail of Bits.** [audit-context-building](https://github.com/trailofbits/skills/tree/main/plugins/audit-context-building). Agent skill/plugin. Reference for understanding code assumptions and inter-function dependencies before judging security.
3. **Trail of Bits.** [fp-check](https://github.com/trailofbits/skills/tree/main/plugins/fp-check). Agent skill/plugin. Reference for challenging suspected vulnerabilities and tracing controls before accepting findings. This skill retains an explicit unconfirmed outcome when evidence is incomplete.
4. **Trail of Bits.** [differential-review](https://github.com/trailofbits/skills/tree/main/plugins/differential-review). Agent skill/plugin. Reference for security review of changes, historical context, and affected code. Its workflow is evaluated selectively; test absence alone does not determine vulnerability severity here.
5. **OpenAI.** [security-best-practices](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices). Agent skill. Reference for selecting language/framework-specific material. Its declared language scope is Python, JavaScript/TypeScript, and Go; it does not establish PHP, Laravel, or WordPress coverage. Upstream skill includes an Apache-2.0 license file.
6. **Trail of Bits; Spencer Michaels (original author), Eric Quintero (current design, as credited upstream).** [supply-chain-risk-auditor](https://github.com/trailofbits/skills/tree/main/plugins/supply-chain-risk-auditor). Agent skill/plugin. Reference for separating measured dependency evidence from interpretation and recording assessment coverage.

Trail of Bits publishes its [skills repository](https://github.com/trailofbits/skills) under CC-BY-SA-4.0. Consult the applicable files before copying or adapting upstream text or code. The bibliography attributes conceptual references; this update does not vendor upstream skill files, scripts, or templates. Existing project rights are unchanged, and references do not grant rights to third-party material.

## Normative references

- **Spain.** [Royal Decree 311/2022 — consolidated ENS text, BOE](https://www.boe.es/eli/es/rd/2022/05/03/311/con).
- **Centro Criptológico Nacional.** [ENS conformity portal](https://ens.ccn.cni.es/es/conformidad) and relevant current CCN-STIC guidance.
- **ISO/IEC.** [27001:2022](https://www.iso.org/standard/27001), [27002:2022](https://www.iso.org/standard/75652.html), [27005:2022](https://www.iso.org/standard/80585.html), and [27034-1:2011](https://www.iso.org/standard/44378.html), subject to edition and amendment checks.

See [standards.md](standards.md) for selection rules and limits on clause verification. Methodological references are not normative requirements. Framework documentation should be selected and cited for the actual project version during each audit.
