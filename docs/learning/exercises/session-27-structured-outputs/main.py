"""Validate structured output returned by an LLM before business logic uses it."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError


class TicketClassification(BaseModel):
    """Application contract for a classified support ticket."""

    model_config = ConfigDict(extra="forbid", strict=True)

    category: Literal["billing", "technical", "account"]
    priority: int = Field(ge=1, le=3)
    requires_human: bool


class InvalidModelOutputError(ValueError):
    """Raised when an LLM response cannot satisfy the application's output contract."""


def parse_ticket_output(raw_json: str) -> TicketClassification:
    """Parse and validate raw JSON; never return unvalidated model output."""
    try:
        return TicketClassification.model_validate_json(raw_json)
    except ValidationError as exc:
        raise InvalidModelOutputError("LLM output did not match TicketClassification schema") from exc


def classify_ticket(raw_json: str) -> dict[str, object]:
    """Example application boundary: validated data only reaches business logic."""
    ticket = parse_ticket_output(raw_json)
    return {
        "category": ticket.category,
        "priority": ticket.priority,
        "requires_human": ticket.requires_human,
    }
