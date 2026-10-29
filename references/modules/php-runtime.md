# PHP runtime and native dependencies

Load for any site served by PHP, including WordPress, Laravel, other CMS/frameworks, and PHP embedded in vendor products. Composer checks alone do not cover PHP or its native libraries. Read the [dated advisory snapshot](../php-advisories.md) and refresh official sources during every assessment. Do not infer that a clean application-code review makes the runtime safe.

## Checks to record

- **PHP-01 — Deployed inventory:** identify each web-serving runtime, SAPI, OS, package vendor/revision or image digest, loaded configuration, and enabled extensions. Separate CLI, FPM pools, Apache modules, containers, and replicas. `php -v` on the developer machine is not production evidence. Use authorized operator output or hosting attestations; never publish a diagnostic `phpinfo()` page.
- **PHP-02 — Advisory applicability:** compare each runtime/package with current upstream and vendor advisories, recording CVE, source, consultation date, affected/fixed branch, and proof of any backported fix. A Composer PHP constraint is not an installed version. Do not compare branches as a single numeric threshold. Unsupported branches need vendor-specific patch evidence and a lifecycle plan; a limited source backport does not restore upstream support.
- **PHP-03 — Configuration-dependent paths:** assess SAPI and effective pre-request settings, session behavior, and relevant application calls for advisory-specific conditions. Distinguish confirmed affected package, unverified prerequisites, and proven non-applicability. Do not lower vendor urgency simply because an application-specific exploit has not been reproduced.
- **PHP-04 — Native package dependencies:** assess cURL, compression libraries, and Windows package rebuilds where relevant. Record native-library versions and package metadata; a PHP version string may remain unchanged after a dependency rebuild. An upstream library release does not prove the hosting package incorporates it.
- **PHP-05 — Remediation evidence:** recommend supported patched packages and compatibility validation. If changes are authorized, verify all serving workers/replicas load the fixed build after the operator's rollout, then check legitimate forms, sessions, uploads, and integrations. Capture sanitized post-update evidence. A package download or CLI upgrade alone does not close the finding.

## Decision and safety boundaries

Prioritize exposed affected runtimes. Lack of production access is `not_verified` with required evidence, not a pass. A vulnerable runtime is distinct from confirmed exploitation or compromise; neither infer nor conceal an incident. If compromise evidence exists, recommend the owner's incident process in addition to patching.

Do not execute public exploit PoCs, exhaust memory, change memory limits, restart services, upgrade packages, or isolate production merely to audit. Propose operator actions within existing authorization. WAF rules, proxy limits, application authentication, or a configuration workaround must not be called a complete fix unless the specific official advisory supports that conclusion. Keep a workaround's residual risk and expiry/recheck condition visible.

Attach each check to the audit record under module `php-runtime`; map ENS/ISO criteria separately and only after verification. Keep advisory applicability, technical verdict, human review, and remediation state independent.
