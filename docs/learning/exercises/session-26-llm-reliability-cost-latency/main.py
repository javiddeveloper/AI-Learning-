"""Deterministic helpers for LLM usage, cost, latency, and retry policy."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TokenUsage:
    input_tokens: int
    output_tokens: int

    def __post_init__(self) -> None:
        if self.input_tokens < 0 or self.output_tokens < 0:
            raise ValueError("Token counts cannot be negative")


@dataclass(frozen=True)
class ModelPricing:
    input_per_million: float
    output_per_million: float

    def __post_init__(self) -> None:
        if self.input_per_million < 0 or self.output_per_million < 0:
            raise ValueError("Prices cannot be negative")


def calculate_cost(usage: TokenUsage, pricing: ModelPricing) -> float:
    """Calculate estimated USD cost from per-million-token prices."""
    input_cost = usage.input_tokens * pricing.input_per_million / 1_000_000
    output_cost = usage.output_tokens * pricing.output_per_million / 1_000_000
    return input_cost + output_cost


def latency_ms(started_at: float, finished_at: float) -> float:
    """Convert monotonic timer readings to elapsed milliseconds."""
    if finished_at < started_at:
        raise ValueError("finished_at cannot be earlier than started_at")
    return (finished_at - started_at) * 1_000


def should_retry_status(status_code: int) -> bool:
    """A minimal policy; real clients should also inspect provider headers and errors."""
    return status_code in {429, 500, 502, 503, 504}


def exponential_backoff_seconds(attempt: int, base_seconds: float = 0.5) -> float:
    """Return uncapped exponential delay for a 1-based retry attempt."""
    if attempt < 1:
        raise ValueError("attempt must be >= 1")
    if base_seconds < 0:
        raise ValueError("base_seconds cannot be negative")
    return base_seconds * (2 ** (attempt - 1))
