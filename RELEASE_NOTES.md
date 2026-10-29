# Web Security Audit 1.2.1

Adds a dedicated PHP runtime assessment module and an official-source advisory snapshot checked on 2026-10-29. Covers CVE-2026-109618, CVE-2026-109619, the separate session advisory CVE-2026-115560, and Windows Brotli rebuilds for CVE-2026-111497. Requires deployed package and SAPI evidence, vendor-backport verification, and post-rollout checks; Composer and local CLI checks alone are insufficient.

Prepared on dev and promoted to main through a pull request. Includes five additional manual model-evaluation scenarios (not executed). No production website was scanned or changed.

Author: Voxiferum, for HumaitasTech, with support from Codex.

English release article: [ARTICLE-1.2.1.md](https://github.com/humanitastech/websecurityaudit/blob/main/ARTICLE-1.2.1.md).
