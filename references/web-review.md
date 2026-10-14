# Website security review workflow

Use the sections relevant to the request. These are original operational instructions informed by the methodological bibliography, not an official ENS/ISO mapping. They do not require installing another skill.

## Establish the site context

Identify site type, languages, framework/CMS versions, rendering model, hosting, reverse proxy/CDN, database, forms, accounts, uploads, and external scripts. Separate deployed code from examples, tests, and build tooling. Follow critical calls across middleware and services; names such as `validateUser` do not establish that a check works. Record assumptions that code relies on but available evidence does not establish.

For a static site, examine forms and embedded services, hosting configuration, deployment access, and browser scripts. For CMS sites, include plugin/theme versions, administrative roles, update paths, and supported extension APIs. For dynamic sites, examine server routes, APIs, background jobs, and access to stored data. Use official documentation for the detected version, especially for PHP/Laravel and WordPress; guidance for another framework is not interchangeable.

## Model realistic threats

Make a compact inventory of valuable assets and reachable entry points. Describe where requests cross trust or privilege boundaries: browser to server, anonymous to authenticated routes, one user to another user's objects, app to database, build to deployment, and site to provider.

For important flows, record an attacker goal, capabilities and prerequisites, entry point, affected asset, existing protection, possible abuse path, and evidence location. A public form, compromised editor account, and privileged deployment account are different attacker models. Mark assumptions instead of inventing integrations. Model proposed features as proposed, not observed. Continue independent review while asking only questions that materially affect conclusions.

## Verify candidate findings

Before reporting a vulnerability as confirmed:

1. State the exact claim, trigger, and security consequence.
2. Trace attacker-controlled input to the sensitive operation, including middleware, validation, escaping, permissions, and platform behavior.
3. Attempt to disprove the claim using existing controls and deployment conditions. Record what remains unknown.
4. Prefer a safe local reproduction or focused regression test when feasible and authorized. Code evidence may establish a flaw without executing an exploit; label that validation method accurately.
5. Classify as confirmed, unconfirmed, or refuted, with reasons. Keep unconfirmed leads separate from confirmed findings; do not turn missing evidence into a clean verdict.

Separate likelihood, impact, and confidence. A missing test does not by itself prove a vulnerability or justify higher severity. Unguessable resource IDs do not replace object authorization. Distinguish an application behind a TLS-terminating proxy from a publicly unencrypted deployment; check production evidence before concluding transport is insecure.

## Review changes and fixes

For a PR, commit range, or follow-up audit, record baseline and target revisions. Inspect changed security behavior and affected callers, routes, templates, policies, and configuration. Identify new exposure, removed checks, and reintroduced weaknesses. Classify findings as introduced, pre-existing, or unresolved. A reviewed diff is not a full-site audit.

When fixes are authorized, test the original failure and legitimate flows, including denied access and cross-user isolation where relevant. Inspect sibling code for the same root cause and document any remaining risk. Do not bundle unrelated redesigns into a security correction. Record tests actually run, results, and deployment checks still needed.

## Assess dependencies without executing them

Read manifests and lockfiles to identify resolved direct and transitive versions. Match advisories to versions and assess whether the affected feature is reachable. Separately report abandoned components, installation scripts, and uncertain provenance as supply-chain concerns. Missing registry information is unknown, not proof of compromise. State unsupported lockfile formats and private/vendored package limitations; never substitute the latest version for the installed one. Do not install dependencies merely to inventory them.
