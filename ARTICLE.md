# HT Web Security Audit 1.2.1 adds PHP runtime checks

HT Web Security Audit is an AI skill for reviewing websites and web applications against applicable requirements of Spain’s Esquema Nacional de Seguridad (ENS), with relevant ISO guidance. Voxiferum created it for HumanitasTech with Codex support.

## How the review works

Define the site boundary or change set and provide authorized access to the relevant code, configuration, and hosting evidence. The skill records verified findings, evidence gaps, and prioritized remediation. Its JSON records tie findings to the reviewed revision and can be turned into a Markdown dossier. Questions and reports follow the user’s language.

## What changes in version 1.2.1

- Identify the PHP build, server interface, and extensions that serve web requests.
- Check whether the vendor backported a fix and whether native libraries or Windows package rebuilds affect the installation.
- Verify that the updated build is serving traffic across workers and replicas.

A local command-line PHP version or a Composer audit covers a different layer from the PHP runtime serving the site. The runtime review uses current vendor guidance and evidence from the deployment. The assessment reports findings within its declared scope.

## Requirements

The development branch also includes a credit integrity review in version 1.4.0. It gives reviewers a reproducible protocol for exercising concurrent debits, retries after lost responses, and competing refunds. The checks apply to sites with usage credits or wallet features.

Use an AI assistant with access to the skill instructions and authorized evidence. The optional record validator and report generator require Python 3.

## Availability

HumanitasTech hosts the source and release notes on GitHub. [Repository](https://github.com/humanitastech/websecurityaudit) · [Version 1.2.1](https://github.com/humanitastech/websecurityaudit/releases/tag/v1.2.1)
