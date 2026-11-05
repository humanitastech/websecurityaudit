# Usage credits and wallet integrity

Apply to any plugin or service that creates, consumes, reserves, transfers, expires, or refunds usage credits, including free grants. Include payment-provider flows only when present. These are project audit requirements, not ENS/ISO control identifiers or claims about payment regulation.

## Define the accounting contract

Trace one operation from user intent through server authorization, price calculation, reservation or debit, service delivery, settlement, ledger, and user-visible history. Include alternate writers: AJAX/REST, jobs, callbacks, retries, admin tools, bulk imports, legacy APIs, and direct integrations with wallet plugins. Identify the authoritative balance source, persistence engine, transaction boundary, and external side effects.

Record the confirmed rules for charge timing, retry behavior, insufficient funds, expiry, refunds, and bonuses. Unknown policy remains an open question; do not invent permission to charge or refund. Internal credits and monetary payments must have separate units, identifiers, and accounting. Capture before/after balances and ledger entries using synthetic accounts only.

## Required checks

| ID | Verify | Evidence for acceptance |
| --- | --- | --- |
| CRED-01 | Authorization and pricing | Server binds account, tenant, operation, price, unit and quantity to trusted state. Cross-account and tampered requests are denied without balance changes. WordPress nonce checks complement, never replace, capability and ownership checks. |
| CRED-02 | Arithmetic and balance invariants | Integral credits or exact fixed-scale arithmetic; reject invalid signs, overflow, unsupported precision and unit mismatches. Available balance respects the confirmed overdraft policy. Ledger entries reconcile per account and unit; cached balances cannot authorize spending. |
| CRED-03 | Idempotency | A durable uniqueness rule protects each logical operation under retries, timeouts and concurrent deliveries. Scope keys to the right actor and operation; mismatched payload reuse fails without mutation. A lost response can be retried without charging again. Distinct legitimate operations still execute. |
| CRED-04 | Concurrency and atomicity | Verify the actual storage isolation/locking or conditional-write semantics and the balance/ledger commit boundary. Use simultaneous requests against the deployed storage type in a safe environment; total debits cannot exceed allowed funds. A check-then-write sequence or lock in only one process is insufficient. |
| CRED-05 | Delivery and failure recovery | Model pending/reserved/settled/released transitions as applicable. Simulate interruption before and after commit and around external side effects. Every outcome is recoverable: no duplicate charge or delivery, silent lost balance, or permanent reservation. Use durable retry/reconciliation and explicit compensation where a shared transaction is impossible. |
| CRED-06 | Grants, refunds and corrections | Link credits and reversals to original operations; enforce eligible amounts, policy and cumulative caps. Repeated or simultaneous refunds cannot over-credit. Audit manual changes with actor, target, reason and immutable linkage; restrict approval and execution according to risk. |
| CRED-07 | Provider callbacks, if used | Verify authenticity using provider documentation, then bind account, amount/currency, order and expected state. Deduplicate deliveries and handle delayed/out-of-order events, partial refunds and disputes. Redirects or client claims cannot settle a purchase. Exercise unsigned, duplicate and mismatched events with fixtures. |
| CRED-08 | Reconciliation and customer evidence | Independently compare ledger, balance, operation and provider records where applicable. Detect and alert on orphan entries and mismatches; preserve original entries when correcting. Users can identify the operation, charged amount, balance impact and reversal or dispute reference without seeing another user's data. |
| CRED-09 | Upgrade and recovery | Check balance/ledger preservation through migrations, rollback, restore and job replay. Test with realistic synthetic pre-upgrade data. Restoring local data does not undo external fulfillment or provider events: reconcile before reopening writes. |

## Severity and release recommendation

Do not mark the credit flow ready if an applicable check has an unresolved integrity failure or missing evidence on a path that can debit, grant, or reverse credits. Report the exact blocker, user impact, required evidence, and retest criteria; distinguish a confirmed vulnerability from a verification gap. Prioritize unauthorized or repeatable balance changes, cross-tenant effects, and systemic reconciliation failures based on impact and reachability. Source inspection alone cannot demonstrate live concurrency or recovery semantics.

Keep findings pending human review until a reviewer makes a recorded decision. Recommend independent human review of the accounting contract, test artifacts, reconciliation results, and rollout safeguards. Do not approve a release, charge accounts, adjust real balances, invoke live providers, or run disruptive tests as part of an audit. See the [behavioral cases](../../tests/credits-cases.md) in the source repository for evaluation scenarios.

## Technical references

- [OWASP Transaction Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html) for server-controlled transaction data and state transitions.
- [WordPress nonces](https://developer.wordpress.org/apis/security/nonces/) for platform-specific limits of nonce checks.
- [Stripe webhooks](https://docs.stripe.com/webhooks), only for Stripe integrations; use the actual provider's official documentation for other integrations.
