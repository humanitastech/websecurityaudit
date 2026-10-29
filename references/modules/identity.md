# Identity and authorization

Trace account creation, login, recovery, session rotation/revocation, and privileged actions. Separate authentication, role checks, object ownership, and tenant isolation. For each sensitive operation inspect the real middleware/policy/service path and denied cases. Do not assume random IDs enforce access control.

Choose checks for credential recovery, session lifecycle, sensitive-action authorization, and cross-user isolation. Prefer synthetic identities and local tests. Record who can reach the operation, its object, the enforced rule, and evidence of both denied and legitimate access. Missing test infrastructure is a limitation, not an automatic vulnerability. Assess MFA by the actual risk and applicable criteria.
