import pytest

from main import (
    ModelPricing,
    TokenUsage,
    calculate_cost,
    ensure_within_cost_limit,
    exponential_backoff_seconds,
    latency_ms,
    should_retry_status,
)


def test_calculate_cost() -> None:
    usage = TokenUsage(input_tokens=2_000, output_tokens=500)
    pricing = ModelPricing(input_per_million=2.0, output_per_million=8.0)
    assert calculate_cost(usage, pricing) == pytest.approx(0.008)


@pytest.mark.parametrize("input_tokens,output_tokens", [(-1, 0), (0, -1)])
def test_negative_token_counts_are_rejected(input_tokens: int, output_tokens: int) -> None:
    with pytest.raises(ValueError):
        TokenUsage(input_tokens=input_tokens, output_tokens=output_tokens)


def test_negative_pricing_is_rejected() -> None:
    with pytest.raises(ValueError):
        ModelPricing(input_per_million=-1, output_per_million=0)


def test_cost_limit_allows_cost_at_limit() -> None:
    ensure_within_cost_limit(estimated_cost=0.01, max_cost=0.01)


def test_cost_limit_rejects_expensive_request() -> None:
    with pytest.raises(ValueError, match="exceeds"):
        ensure_within_cost_limit(estimated_cost=0.02, max_cost=0.01)


def test_invalid_cost_limit_inputs_are_rejected() -> None:
    with pytest.raises(ValueError):
        ensure_within_cost_limit(estimated_cost=-0.01, max_cost=1.0)
    with pytest.raises(ValueError):
        ensure_within_cost_limit(estimated_cost=0.01, max_cost=-1.0)


def test_cost_guard_runs_before_provider_call() -> None:
    provider_calls = 0

    def provider_call() -> str:
        nonlocal provider_calls
        provider_calls += 1
        return "response"

    with pytest.raises(ValueError, match="exceeds"):
        ensure_within_cost_limit(estimated_cost=0.05, max_cost=0.01)

    assert provider_calls == 0


def test_latency_in_milliseconds() -> None:
    assert latency_ms(10.0, 10.25) == pytest.approx(250.0)


def test_invalid_latency_range_is_rejected() -> None:
    with pytest.raises(ValueError):
        latency_ms(11.0, 10.0)


@pytest.mark.parametrize("status", [429, 500, 502, 503, 504])
def test_transient_statuses_are_retryable(status: int) -> None:
    assert should_retry_status(status) is True


@pytest.mark.parametrize("status", [400, 401, 403, 404, 422])
def test_non_transient_statuses_are_not_retryable(status: int) -> None:
    assert should_retry_status(status) is False


def test_exponential_backoff() -> None:
    assert exponential_backoff_seconds(1) == pytest.approx(0.5)
    assert exponential_backoff_seconds(2) == pytest.approx(1.0)
    assert exponential_backoff_seconds(3) == pytest.approx(2.0)


def test_invalid_retry_attempt_is_rejected() -> None:
    with pytest.raises(ValueError):
        exponential_backoff_seconds(0)
