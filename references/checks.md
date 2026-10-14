# Evidence-driven checks

This list guides technical inspection; it is neither the complete ENS measures catalog nor an official ISO crosswalk. Verify each normative relationship individually.

| Surface | Inspect | Useful evidence |
| --- | --- | --- |
| Authentication and sessions | Account recovery, relevant MFA, expiration, revocation, cookies, session fixation, and attempt limits | Login flow and local session lifecycle tests |
| Authorization | Role and object access, isolation between users/organizations, administrative endpoints | Permission matrix and negative tests between synthetic identities |
| Inputs and outputs | Injection, XSS, CSRF, SSRF, uploads, path traversal, validation, and contextual encoding | Input-to-use data path and minimal local reproduction |
| Transport and browser | TLS, redirects, cookies, CORS, CSP, framing, and sensitive information caching | Actual configuration and observed responses; assess headers according to their purpose |
| Secrets and data | Exposed credentials, key management, privileges, retention, logging, and backup access | Sanitized configuration, data flow, policy, and execution evidence |
| Dependencies and delivery | Vulnerable versions, vulnerability reachability, lockfiles, updates, CI/CD, and deployment permissions | Official advisory, installed version, and exploitability analysis |
| Infrastructure | Environment separation, network, exposed services, hardening, and provider responsibilities | Configuration and operational evidence, avoiding assumptions based on website appearance |
| Operations | Logs, alerts, incidents, recovery, availability, and changes | Sanitized logs, procedures, and restoration tests |
| Organization | Policy, responsible parties, assets, risk, applicability, suppliers, and training | Approved documents and dated records |

Retain minimal evidence, removing tokens, credentials, and personal data. Mark each test as executed, not executed, or inconclusive. Record frontend, backend, API, infrastructure, and governance coverage separately. A static site may not need its own session controls; still inspect its pipeline, hosting, and existing integrations.
