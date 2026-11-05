# Usage credits: behavioral evaluation scenarios

Use disposable accounts, synthetic credits, an isolated database with the target engine, and provider mocks or fixtures. These are manual model and integration evaluation specifications, not executed tests.

1. **Replay and lost response:** start at 10 credits, charge 3, then resend the same operation after simulating a lost response. Expect 7 and one debit. Reuse the operation ID with different inputs: reject without mutation.
2. **Contended debit:** start at 10; synchronize two distinct 7-credit requests at the same boundary. Expect one success, one insufficient-funds result, 3 credits and one debit. Repeat with valid 3-credit requests to detect false deduplication.
3. **Partial failure:** simulate failure after reservation and before delivery, and after delivery but before confirmation. Recover both paths; reconcile ledger and delivered work without charging or delivering twice.
4. **Authorization and input:** tamper with owner, tenant, price and signed quantity; try a valid WordPress nonce without permission. Expect rejection or authoritative server pricing with no unauthorized mutation.
5. **Partial refund race:** debit 7, refund 3, then submit two distinct 4-credit refunds concurrently. At most one succeeds; cumulative reversals never exceed 7. Replay a successful refund without granting again.
6. **Provider ordering:** deliver unsigned, duplicate, mismatched and late events. Expect no state mutation from invalid events and one authorized transition per logical event. Reconcile provider and local records.
7. **Migration and restore:** compare synthetic opening balances, movement totals and pending operations before and after upgrade/restore, including replay from an external event source. Expect unexplained drift to block readiness.
8. **Missing evidence:** give only code and no storage semantics or concurrency results. The audit must record the gap and withhold readiness without claiming confirmed double charging.
