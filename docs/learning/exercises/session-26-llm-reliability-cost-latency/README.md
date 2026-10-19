# Session 26 — LLM Reliability, Cost & Latency

## Goal

Practice deterministic building blocks for monitoring LLM token usage, estimating cost, measuring elapsed time, classifying retryable HTTP statuses, and enforcing a per-request cost guard before a provider call.

## Files

- `main.py`: provider-independent helpers and validated data classes.
- `test_main.py`: tests for valid/invalid inputs, cost limits, retryable statuses, and backoff.

## Run

From this directory, with project dependencies installed:

```bash
uv run pytest -q
```

## Production considerations

- Provider-specific usage and pricing can include cached tokens, reasoning tokens, and tool charges.
- Pre-call cost is an estimate: reserve against a conservative maximum output-token budget, then reconcile against actual usage after the response.
- The cost guard must run before invoking the provider; it should not be treated as a billing guarantee.
- Retries need a bounded count, exponential backoff with jitter, an overall deadline, and `Retry-After` handling.
- Distinguish connection failures, timeouts, and HTTP status errors.
- Log provider/model, token usage, latency, and estimated cost without logging sensitive prompts.
- Measure streaming time-to-first-token (TTFT) separately from total latency.
- A retry may increase cost and latency; ensure it fits the request budget and deadline.

The retry classifier is a minimal policy, not a complete provider SDK error handler. The exercise uses no real provider calls.
