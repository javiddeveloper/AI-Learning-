# Session 18 — Testing with pytest

## Status
COMPLETED

## Topics Covered
- pytest
- FastAPI TestClient
- Route and validation testing
- Fixtures
- Unit vs integration tests
- Mocking external dependencies
- Async tests with pytest-asyncio
- Failure-path and production-oriented testing

## Mental Model

Test → HTTP/FastAPI → Validation → Business Logic → Dependencies → Response

## Production Checklist
- Happy path
- Invalid input
- Authentication/authorization failures
- Not found
- Conflict
- External API failure
- Timeout
- Database failure
- Response contract

## AI Engineering Relevance
Deterministic application behavior should be tested with normal automated tests. LLM behavior will later require evaluation, regression datasets and model-specific testing.

## Confidence
8/10

## Next Session
Session 19 — Code Quality: Ruff, Pyright & Pre-commit
