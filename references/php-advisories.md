# PHP advisory snapshot — checked 2026-10-29

This is a dated starting point, not a complete vulnerability feed or a permanent minimum-version policy. Recheck official advisories, later releases, supported branches, and hosting vendor package notices at audit time. Record changed guidance in the audit's sources and history.

## October 2026 critical runtime advisories

| Advisory | Issue | Upstream fixed releases by branch |
| --- | --- | --- |
| [CVE-2026-109618 / GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) | Out-of-memory handling corrupts request state; potential unauthenticated RCE | 8.2.35, 8.3.36, 8.4.27, 8.5.12 |
| [CVE-2026-109619 / GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp) | Freed request memory remains reachable through worker state; potential unauthenticated RCE | 8.2.35, 8.3.36, 8.4.27, 8.5.12 |

These fixes were announced on 21 October. Scope includes web-serving PHP, not just a particular CMS. `mod_php` can be attacked before application code runs. Treat FPM, CGI, FrankenPHP, and LiteSpeed as needing assessment too. Do not interpret lack of a demonstrated exploit for one setup as immunity. Read the individual advisories for precise susceptibility and current updates.

[PHP's announcement](https://www.php.net/archive/2026.php) calls for upgrading; temporary measures are not a complete substitute. Distribution/LTS backports require package-specific confirmation. Do not classify an old numeric version as unpatched if a verified vendor backport fixes the CVE, nor assume a backport exists without evidence.

## Follow-up session issue

The 23 October [PHP informational notice](https://www.php.net/archive/2026.php) identifies **CVE-2026-115560** under an unusual combination: configured `php_binary` or `php_serialize`, changed to `php` with `ini_set()` before `session_start()`, with upload progress enabled. The notice recommends `session.upload_progress.enabled=0` pending the regular fix. Recheck whether that fix has shipped; do not label the four releases above as fixing this separate issue. Verify effective configuration and worker rollout before recording a workaround as applied.

## Windows native dependency rebuild

The 26 October [PHP Windows notice](https://www.php.net/archive/2026.php) lists **8.2.35-1, 8.3.36-1, 8.4.27-1, and 8.5.12-1** with Brotli **1.2.1** for **CVE-2026-111497**. The PHP runtime version stays unchanged. Assess the installed package build and whether cURL response decompression is enabled. See [Google Brotli 1.2.1 release](https://github.com/google/brotli/releases/tag/v1.2.1) for the native-library fix. Do not generalize these Windows rebuild labels to Linux vendor packages.

## Operational reference

[CERT-EU advisory 2026-018](https://cert.europa.eu/publications/security-advisories/2026-018/) provides operational guidance and follow-up context. Use it to cross-check patch planning and temporary controls; use upstream/vendor sources to establish actual package status. Do not implement high-impact tuning or service isolation without operator authorization.
