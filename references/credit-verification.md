# Credit verification and release evidence

Use this procedure with the [credit module](modules/credits.md). Its technical references complement ENS/ISO; an OWASP requirement, vendor pattern, or internal release rule is not an ENS/ISO mapping. Record the edition and identifier actually consulted. OWASP WSTG's `latest` page can change: record the consultation date or use a pinned revision.

## Establish the expected behavior

Get confirmed rules for pricing, timing, delivery, refunds, expiry, bonuses and privileged adjustments. Record the requirement source and version. A missing rule is a verification gap; do not invent one. If available, use `swdocumentation` to resolve policy gaps and `software-user-acceptance` to verify that users can understand the price, identify a charge and follow a reversal. These are optional handoffs; the audit can proceed without either skill.

## Run the priority proofs

Run through the actual plugin entry point or an integration harness that uses its production transaction path. Use synthetic accounts, an isolated database matching the target engine, and a deterministic delivery spy or provider fixture. Record engine/version, isolation configuration, workers, revision, and fixture. Use separate connections and a barrier at the contested operation; sequential requests do not establish concurrency. No live payments or customer balances.

| Proof | Setup and action | Required observations |
| --- | --- | --- |
| CREDIT-P01 / CRED-02, 04, 05 | Seed 10 credits; release two different 7-credit operations together. Under a no-overdraft policy, repeat with two different 3-credit operations as a positive control. | First run: one debit, one denial, balance 3, one delivery. Positive control: two debits, balance 4, two deliveries. Check durable entries after both workers finish. |
| CREDIT-P02 / CRED-03, 05 | Seed 10; debit 3 and deliberately lose the response after commit. Retry with the same operation ID, then reuse it with a changed amount or target. | Original and retry represent the same logical result; balance 7, one debit, one delivery. Changed intent is rejected without mutation. Test a delayed retry within the documented retry horizon; document what happens after retention expires. |
| CREDIT-P03 / CRED-04, 06 | Seed 10, debit 7, refund 3, then simultaneously request two distinct 4-credit reversals of the same debit. Replay the successful reversal. | Exactly one additional reversal if policy permits it; balance 10, cumulative refund 7, original debit preserved, no extra refund on replay. Verify no duplicate external refund if applicable. |

These expected values assume immediate settlement and the stated refund and overdraft rules. Adapt fixtures for reservations, asynchronous delivery, or other confirmed policies, retaining equivalent invariants. Record the command, pre/post balances and holds, durable ledger and delivery counts, observed status, and sanitized outputs. Mark unavailable execution as `not_verified`, even if code appears sound. Save integration tests in the audited project only if authorized; otherwise provide reproducible steps and evidence in the audit record.

## Explore sequences and failure boundaries

Model allowed actions (grant, reserve, settle, expire, debit, reverse) and compare the actual plugin against an independent accounting model. Generate sequences with retries, two distinct legitimate operations, and invalid transitions. Check invariants after each step: balance/ledger agreement, unique settlement per operation, no excess refund and no stuck reservation after recovery. Save the seed and smallest reproducible failing sequence. Generated sequential tests complement, but cannot replace, controlled concurrent tests.

Where work crosses a database and external system, inject interruptions before commit, after commit and before sending, and after delivery and before acknowledging it. Verify that recovery reconciles both records. An outbox is one option for durable publication; it does not remove the need for an idempotent consumer. Verify the mechanism actually used; do not require a specific architecture or database.

## Record the human release decision

For each proof, link requirement ID and source → check ID → test/command → evidence ID → finding or verified outcome → human decision. Use the existing [audit record contract](audit-records.md); record any release decision and its owner in the decision summary and history, separate from acceptance of an individual finding. The agent recommends readiness or identifies blockers; it does not authorize production charges.

Before recommending rollout, ask the responsible owner to define a limited initial audience, observation period, thresholds, and who can pause new debits. Verify alerts for duplicate debit, ledger/balance drift, and aged reservations. Treat confirmed unauthorized debits or unexplained accounting drift as stop-and-investigate events. Record a recovery procedure that preserves evidence, prevents additional incorrect charges, reconciles outstanding operations, and defines who may authorize reopening. Rolling back code alone does not reverse settled movements.

## Technical and procedural bibliography

- [OWASP ASVS 5.0, V2](https://github.com/OWASP/ASVS/blob/master/5.0/en/0x11-V2-Validation-and-Business-Logic.md): business rules, validation, atomicity, limits and high-impact approvals. [OWASP WSTG-BUSL-10](https://owasp.github.io/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic/10-Payment_Functionality): payment-flow abuse tests, applicable when payment is present.
- [Trail of Bits — Property-Based Testing](https://github.com/trailofbits/skills/tree/main/plugins/property-based-testing) and [Hypothesis — stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html): generated action sequences, invariants and reproducible counterexamples. No dependency on these tools is required.
- [MySQL 8.4 — InnoDB locking reads](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-reads.html): example of engine-specific concurrency semantics. Use the actual engine and version's documentation.
- [AWS Builders' Library — idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) and [AWS — transactional outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html): replay intent and recovery across systems.
- [Google SRE Workbook — Canarying Releases](https://sre.google/workbook/canarying-releases/): limited rollout, monitoring and decision criteria.
