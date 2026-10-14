# Current Learning State

## Current Phase
Phase 1 — Python & FastAPI Backend Foundation

## Current Topic
Session 25 — Prompt Engineering

## Current Status
IN_PROGRESS

## Current Goal
Build the Python and FastAPI foundation required for production AI engineering.

## Session 25 — Current Work
Prompt Engineering — IN_PROGRESS.

Created `docs/learning/exercises/session-25-prompt-engineering/` with versioned prompt templates and pytest tests. Local test execution and implementation review remain pending.

## Session 24 — Previous Work
Streaming & Conversation State — IN_PROGRESS.

Exercise files exist at `docs/learning/exercises/session-24-streaming-conversation-state/`; runtime verification and final review remain pending.

## Session 18 Result
Session 18 — Testing with pytest is COMPLETED with confidence 8/10.

Covered:
- pytest
- FastAPI TestClient
- Route testing
- Validation error testing
- Fixtures
- Unit vs integration tests
- Mocking external dependencies
- Async tests with pytest-asyncio
- Failure-path and production-oriented testing

## Key Mental Model
```
Test
 ↓
HTTP / FastAPI
 ↓
Validation
 ↓
Business Logic
 ↓
Dependencies
 ↓
Response
```

## Next Recommended Step
Session 19 — Code Quality

Focus on:
- Ruff
- Pyright
- Formatting
- Linting
- Pre-commit
- CI-oriented quality checks


## Session 20 Result

Session 20 — Docker & Docker Compose is COMPLETED with confidence 8/10.

Implemented:
- FastAPI containerization with Dockerfile
- Docker Compose multi-service stack
- PostgreSQL service with named persistent volume
- Redis service
- Compose internal networking and service-name DNS
- Environment variables
- PostgreSQL and Redis health checks
- FastAPI health and readiness endpoints
- `depends_on` with `service_healthy`
- Docker Compose lifecycle commands
- Production considerations for secrets, image pinning, resources, migrations, logging and backups

Implementation:
`docs/learning/exercises/session-20-docker-compose/`

## Session 19 Result

Session 19 — Code Quality is COMPLETED with confidence 8/10.

Covered:
- Ruff formatting and linting
- Pyright strict static type checking
- Pre-commit
- local quality gates
- CI-oriented checks
- distinction between linting, formatting, static typing and runtime tests

Implementation:
`docs/learning/exercises/session-19-code-quality/`

## Session 22 Result

Session 22 — LLM Mental Model is COMPLETED with confidence 8/10.

Covered:
- Tokens and tokenization
- Context windows
- System/developer/user messages
- Temperature and generation controls
- Model capabilities and limitations
- Hallucination basics

## Session 23 — Current Work

Direct LLM APIs — IN_PROGRESS.

Implemented in `docs/learning/exercises/session-23-direct-llm-apis/`:
- FastAPI `POST /chat` with Pydantic request/response models
- `LLMClient` Protocol and `ChatService` boundary
- Async `OpenAIClient` using the official SDK and Responses API
- Provider-level error normalization and finite timeout
- Environment-based settings with `pydantic-settings`
- `MockLLMClient` and pytest route tests that do not call the real provider
- FastAPI dependency overrides wired through `Depends`

Not yet verified in a live runtime during this session; no real API key or provider call was used.

Remaining for Session 23:
- Run `uv sync`, Ruff and pytest in a local runtime
- Verify a real OpenAI request with a valid API key
- Add/compare another provider adapter (Gemini or Anthropic)
- Review lifecycle cleanup, provider errors, and production readiness

## Next Recommended Step

Run the exercise locally, fix any runtime/type/lint issues, and verify the live OpenAI path before adding a second provider.

## Future Infrastructure Track

The Production AI Engineering phase will include a dedicated container-orchestration track covering:

- Kubernetes
- Helm
- Service Mesh
- Docker Swarm
- Advanced container orchestration

These topics will come after Docker/Docker Compose fundamentals and will be treated as production infrastructure knowledge rather than generic DevOps study.
