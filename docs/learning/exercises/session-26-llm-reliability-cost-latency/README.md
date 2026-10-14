# Session 26 — LLM Reliability, Cost & Latency

## Goal

Practice deterministic building blocks for monitoring LLM token usage, estimating cost, measuring elapsed time, and choosing when a provider error is retryable.

## Files

- `main.py`: small, provider-independent helper functions and validated data classes.
- `test_main.py`: unit tests for valid inputs, invalid inputs, retryable statuses, and backoff.

## Run

From this directory, with pytest available in the project environment:

```bash
uv run pytest -q
```

## Important production gaps to discuss

This exercise is deliberately small and does not make provider calls. Before production use, consider:

- Provider-specific usage fields and price updates, including cached tokens or tool charges.
- A bounded retry count, exponential backoff with jitter, an overall deadline, and `Retry-After` handling.
- Distinguishing connection failures, timeouts, and HTTP status errors.
- Logging token usage, model/provider, latency, and estimated cost without logging sensitive prompts.
- Tracking streaming time-to-first-token separately from total latency.
- Testing fallback behavior and preventing retries from multiplying cost or exceeding request deadlines.

The retry classifier is a starting policy, not a complete provider SDK error handler.
