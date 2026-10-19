# Session 27 — Structured Outputs & Pydantic Validation

## Goal

Treat model output as untrusted input. Parse it into a strict Pydantic schema and allow only validated data to reach business logic.

## Files

- `main.py`: schema, JSON parsing boundary, normalized validation exception, and example application function.
- `test_main.py`: deterministic tests for valid output, invalid ranges/types, unknown categories, missing/extra fields, malformed JSON, and the business boundary.

## Run

From this directory:

```bash
uv run pytest -q
```

No API key or real LLM request is needed.

## Design decisions

- `Literal` restricts category to an explicit allow-list.
- `Field(ge=1, le=3)` enforces the priority range.
- `strict=True` prevents silent coercion such as the string `"3"` into integer `3`.
- `extra="forbid"` rejects unexpected fields so schema drift is visible.
- `model_validate_json` parses JSON and validates it in one operation.
- `InvalidModelOutputError` gives the application a stable failure type without exposing raw model output or Pydantic internals to callers.
- Validation failure must not enter business logic. A caller may perform one bounded repair attempt or return a controlled error/fallback; do not retry indefinitely.

## Production notes

Pydantic validation proves the output matches the declared data contract; it does not prove the model's claims are factually correct or authorized. Business rules and authorization must still be enforced separately. When using a provider's Structured Outputs / JSON Schema feature, keep local validation as a defense-in-depth boundary.
