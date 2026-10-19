import pytest

from main import (
    InvalidModelOutputError,
    TicketClassification,
    classify_ticket,
    parse_ticket_output,
)


VALID_JSON = """
{
  "category": "billing",
  "priority": 3,
  "requires_human": true
}
"""


def test_valid_json_is_parsed_and_validated() -> None:
    ticket = parse_ticket_output(VALID_JSON)
    assert ticket == TicketClassification(
        category="billing",
        priority=3,
        requires_human=True,
    )


@pytest.mark.parametrize("priority", [0, 4, -1])
def test_priority_outside_allowed_range_is_rejected(priority: int) -> None:
    raw = VALID_JSON.replace('"priority": 3', f'"priority": {priority}')
    with pytest.raises(InvalidModelOutputError):
        parse_ticket_output(raw)


def test_unknown_category_is_rejected() -> None:
    raw = VALID_JSON.replace('"billing"', '"unknown"')
    with pytest.raises(InvalidModelOutputError):
        parse_ticket_output(raw)


def test_missing_required_field_is_rejected() -> None:
    raw = VALID_JSON.replace('  "requires_human": true\n', "")
    with pytest.raises(InvalidModelOutputError):
        parse_ticket_output(raw)


def test_extra_field_is_rejected() -> None:
    raw = VALID_JSON.replace('"priority": 3,', '"priority": 3,\n  "unexpected": "value",')
    with pytest.raises(InvalidModelOutputError):
        parse_ticket_output(raw)


def test_non_json_output_is_rejected() -> None:
    with pytest.raises(InvalidModelOutputError):
        parse_ticket_output("Here is the classification: billing")


def test_strict_types_reject_string_priority() -> None:
    raw = VALID_JSON.replace('"priority": 3', '"priority": "3"')
    with pytest.raises(InvalidModelOutputError):
        parse_ticket_output(raw)


def test_only_validated_values_reach_business_logic() -> None:
    result = classify_ticket(VALID_JSON)
    assert result == {
        "category": "billing",
        "priority": 3,
        "requires_human": True,
    }


def test_invalid_output_never_returns_business_result() -> None:
    with pytest.raises(InvalidModelOutputError):
        classify_ticket(VALID_JSON.replace('"priority": 3', '"priority": 5'))
