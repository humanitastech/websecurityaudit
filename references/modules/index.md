# Module selection

Read only modules applicable to the site and requested profile. These identifiers are local audit identifiers, not ENS control numbers. Individual checks are created from the real scope and linked to verified normative criteria separately.

| ID | Load when | Instructions |
| --- | --- | --- |
| identity | Accounts, sessions, restricted data, or administrative routes exist | [identity.md](identity.md) |
| inputs | Forms, uploads, user-controlled URLs, APIs, or webhooks exist | [inputs.md](inputs.md) |
| browser | The site delivers browser content or integrates scripts | [browser.md](browser.md) |
| cms | A CMS, plugin, or theme is involved | [cms.md](cms.md) |
| dependencies | Manifests, lockfiles, external packages, or builds exist | [dependencies.md](dependencies.md) |
| operations | Hosting, deployment, secrets, logs, or availability is in scope | [operations.md](operations.md) |
| governance | ENS/ISO gap assessment or organizational requirements are in scope | [governance.md](governance.md) |

For a full profile, consider every module and document exclusions. In narrower profiles, include dependencies of the affected feature. Missing documentation makes a relevant module unverified or blocked, not excluded. Use [web-review.md](../web-review.md) for threat modeling, candidate verification, and change/fix review shared by these modules.
