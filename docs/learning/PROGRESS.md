# Learning Progress

## Status Legend
- NOT_STARTED
- IN_PROGRESS
- PRACTICING
- REVIEW
- COMPLETED

## Current Phase
**Phase 1 — Python & FastAPI Backend Foundation**

## Current Topic
**Session 27 — Structured Outputs & Pydantic Validation**

## Phase 1 Progress
| Topic | Status | Confidence | Notes |
|---|---|---:|---|
| Python Fundamentals | COMPLETED | 8/10 | Core fundamentals practiced. |
| Pythonic Programming | PRACTICING | 8/10 | Core collections/data-model concepts practiced; more Pythonic constructs remain. |
| Functions & OOP | PRACTICING | 8.5/10 | Functions, parameters, return values, default/keyword arguments, scope, modules/imports and docstrings completed. OOP remains to be formalized. |
| Type Hints & Pyright | COMPLETED | 9/10 | Practiced annotations, generics, Literal, TypedDict, Callable, Protocol and static checking with Pyright. |
| Dataclasses vs Pydantic vs ORM | COMPLETED | 8.8/10 | Implemented and reviewed a payment-domain flow using Dataclass, Pydantic v2 and SQLAlchemy 2.x ORM models. |
| Modules, Packages & uv | COMPLETED | 9/10 | Implemented a src-layout package, imports, __init__.py, dependency direction, uv, pyproject.toml and uv.lock. Compared uv with pip + requirements.txt. |
| Exceptions, Context Managers & Decorators | COMPLETED | 8/10 | Practiced custom exceptions, try/except/else/finally, context managers, decorators, functools.wraps and configuration with pydantic-settings. |
| Configuration & pydantic-settings | COMPLETED | 8/10 | Practiced .env-based configuration and pydantic-settings in the Session 7 payment exercise. |
| Async Python & asyncio | PRACTICING | 8/10 | Covered async/await, coroutines, event loop, blocking vs non-blocking, concurrent I/O and asyncio.gather. Practical exercise implemented as a payment-processing simulation. |
| HTTP & REST | COMPLETED | 9/10 | HTTP methods, request/response model, status codes, headers, REST resources and practical REST API design reviewed. |
| FastAPI Fundamentals | COMPLETED | 9/10 | FastAPI application, routing, GET/POST/PUT/PATCH/DELETE, path/query parameters, request bodies, response handling and Swagger/OpenAPI practiced. |
| Pydantic with FastAPI | COMPLETED | 9/10 | FastAPI/Pydantic validation and serialization practiced. |
| FastAPI Dependency Injection | COMPLETED | 8/10 | Depends and dependency patterns covered. |
| PostgreSQL | NOT_STARTED | - | |
| SQLAlchemy 2.x | PRACTICING | 8/10 | ORM model syntax practiced; sessions, relationships, transactions and queries remain. |
| Alembic | NOT_STARTED | - | |
| httpx | NOT_STARTED | - | |
| Retry, Timeout & Resilience | NOT_STARTED | - | |
| Authentication & Authorization | COMPLETED | 8/10 | JWT, access/refresh tokens, password hashing and OAuth2 concepts covered. |
| Testing with pytest | COMPLETED | 8/10 | pytest, TestClient, fixtures, unit/integration testing, mocking and async tests covered. |
| Ruff, Pyright & Pre-commit | COMPLETED | 8/10 | Completed the Code Quality workflow with Ruff formatting/linting, Pyright strict static typing, Pre-commit hooks and CI-oriented quality gates. |
| Docker & Docker Compose | COMPLETED | 8/10 | Built and documented a FastAPI + PostgreSQL + Redis Docker Compose stack with networking, named volume, environment variables, health checks and readiness verification. |
| Kubernetes & Container Orchestration | NOT_STARTED | - | Planned for the Production AI Engineering infrastructure track. |
| Helm | NOT_STARTED | - | Planned after Kubernetes fundamentals. |
| Service Mesh | NOT_STARTED | - | Planned after Kubernetes and networking fundamentals. |
| Docker Swarm | NOT_STARTED | - | Planned as a comparative orchestration technology. |
| Advanced Container Orchestration | NOT_STARTED | - | Planned after Kubernetes, Helm and Service Mesh fundamentals. |
| Production Backend Concepts | NOT_STARTED | - | |
| AI-Ready Backend | COMPLETED | 8/10 | Phase 1 foundation reviewed through the AI-ready backend boundary. |

## Phase 2 Progress
| Topic | Status | Confidence | Notes |
|---|---|---:|---|
| LLM Mental Model | COMPLETED | 8/10 | Tokens, tokenization, context windows, message roles, temperature, model limitations and hallucination basics covered. |
| Direct LLM APIs | IN_PROGRESS | - | Implemented FastAPI `/chat`, `LLMClient` Protocol, `ChatService`, async OpenAI Responses API adapter, normalized provider errors, settings, Mock provider and pytest route tests. Local/live execution and a second provider adapter remain. |
| LLM Reliability, Cost & Latency | COMPLETED | 8/10 | Added a per-request cost guard before provider invocation, cost/latency/retry helpers, and failure-path tests. Test suite: 23 passed in isolated verification. Provider-specific integration remains future work. |
| Structured Outputs & Pydantic | PRACTICING | 8/10 | Implemented strict Pydantic schema, JSON parsing boundary, normalized validation error, and tests for valid/invalid/missing/extra fields. Test suite: 11 passed in isolated verification. Awaiting learner explanation of the validation boundary before marking the learning topic completed. |

## Completion Rule
A topic is COMPLETED only after explanation in the learner's own words plus a practical implementation reviewed in a session. For non-obvious concepts, code alone is insufficient: the execution model and mental model must also be understood and explained before completion.

## Session History
### Session 27 — Structured Outputs & Pydantic Validation
**Status:** PRACTICING (implementation completed; concept checkpoint pending)

**Implementation:** `docs/learning/exercises/session-27-structured-outputs/`

Implemented:
- Strict Pydantic v2 model with `Literal`, `Field(ge=1, le=3)`, `strict=True`, and `extra="forbid"`
- JSON parsing and validation with `model_validate_json`
- Normalized `InvalidModelOutputError` boundary
- Business logic receives only validated data
- Tests for valid output, invalid range/type/category, missing/extra fields, malformed JSON, and boundary behavior

**Verification:** 11 tests passed in isolated verification using Pydantic 2.13.5 and pytest 9.0.2.

**Remaining learning checkpoint:** Explain why schema validation is necessary even with provider Structured Outputs, and why invalid output must not enter business logic. After that, mark the topic COMPLETED.

### Session 26 — LLM Reliability, Cost & Latency
**Status:** COMPLETED — confidence 8/10

**Implementation:** `docs/learning/exercises/session-26-llm-reliability-cost-latency/`

Added a per-request cost guard and tests ensuring an over-budget request is rejected before provider invocation. Existing helpers cover token cost, elapsed latency, retryable status classification, and exponential backoff.

**Verification:** 23 tests passed in isolated verification using pytest.

**Production gaps:** Provider integration, Retry-After, jitter, bounded retries/deadlines, actual TTFT instrumentation, and provider-specific usage/pricing remain beyond this deterministic exercise.

### Session 25 — Prompt Engineering
**Status:** IN_PROGRESS

Created the exercise package at `docs/learning/exercises/session-25-prompt-engineering/` with versioned prompt templates, user-input delimiting, and deterministic pytest coverage. The tests have not yet been executed in a local runtime, and few-shot examples plus an LLM-level prompt evaluation are still outstanding.

**Next:** Run `uv sync` and `uv run pytest`, review the implementation, then add few-shot examples and an evaluation approach.

### Session 24 — Streaming & Conversation State
**Status:** IN_PROGRESS

Exercise files were created at `docs/learning/exercises/session-24-streaming-conversation-state/` for StreamingResponse/SSE, conversation state, truncation and tests. Runtime verification and a complete review have not been confirmed.

**Next:** Run the exercise tests and review streaming lifecycle, conversation isolation, cancellation, and context-budget behavior.

### Session 23 — Direct LLM APIs
**Status:** IN_PROGRESS

Started Phase 2 with direct provider integrations before introducing orchestration frameworks.

Covered and implemented so far:
- LLM API request/response lifecycle and provider abstraction
- `LLMClient` Protocol and provider-independent `ChatService`
- Async `OpenAIClient` using the official SDK and Responses API
- FastAPI `POST /chat` with Pydantic request/response schemas
- Provider error normalization, timeout configuration and secure API-key handling
- `MockLLMClient` plus route tests that do not call the provider

**Implementation:** `docs/learning/exercises/session-23-direct-llm-apis/`

**Status note:** Files are committed, but local execution and a live API call have not yet been verified. A second provider adapter remains.

**Next:** Run tests/lint locally, verify the live OpenAI request, then add a second provider adapter.

### Session 22 — LLM Mental Model
**Status:** COMPLETED

Covered:
- Tokens and tokenization
- Context windows
- System/developer/user messages
- Temperature and generation controls
- Model capabilities and limitations
- Hallucination basics

**Confidence:** 8/10

### Session 21 — Phase 1 AI-Ready Backend
**Status:** COMPLETED

Implemented a solved Docker Compose exercise containing FastAPI, PostgreSQL and Redis. Covered Dockerfile, image/container lifecycle, Compose networking and service-name DNS, environment variables, PostgreSQL named volume, Redis, health checks, readiness, and `depends_on` health conditions.

**Confidence:** 8/10

**Implementation:** `docs/learning/exercises/session-20-docker-compose/`

**Next:** Resolve/complete Session 19 — Code Quality before proceeding to Session 21.
 
### Session 18 — Testing
**Status:** COMPLETED

Covered pytest, FastAPI TestClient, route and validation testing, fixtures, unit vs integration tests, mocking, async tests with pytest-asyncio and production failure-path testing.

**Confidence:** 8/10

**Next:** Session 19 — Code Quality.

### Session 1 — Python Fundamentals
**Status:** COMPLETED

### Session 2 — Python Data Model / Core Collections
**Status:** COMPLETED

### Session 3 — Functions & Modules
**Status:** PRACTICING

Implemented a multi-module exercise and practiced functions, type hints, parameters, scope, imports, entry points, docstrings, exception handling and separation of concerns.

**Confidence:** 8.5/10

### Session 4 — Type Hints & Pyright
**Status:** COMPLETED

Practiced type annotations, nullable types, generics, TypeVar, Literal, TypedDict, Callable, Protocol, structural typing and Pyright.

**Confidence:** 9/10

### Session 5 — Dataclasses, Pydantic & ORM Models
**Status:** COMPLETED

Implemented and reviewed a payment-domain model flow with Dataclass, Pydantic v2 and SQLAlchemy 2.x ORM models. Practiced validation, serialization, ORM mapping, SQLite persistence simulation and API/domain/persistence separation.

**Confidence:** 8.8/10

### Session 6 — Modules, Packages & uv
**Status:** COMPLETED

Implemented and reviewed a production-oriented payment project using src layout. Practiced modules, packages, __init__.py, __all__, absolute/relative imports, dependency direction, circular dependency avoidance, virtual environments, uv, pyproject.toml, uv.lock, uv sync and uv run.

Also compared the modern uv + pyproject.toml + uv.lock workflow with pip + requirements.txt.

**Confidence:** 9/10

### Session 7 — Exceptions, Context Managers, Decorators & Configuration
**Status:** COMPLETED

Practiced a payment-service exercise covering custom exception hierarchy, try/except/else/finally, context managers and transaction lifecycle, decorators, functools.wraps, argument forwarding with *args/**kwargs, and .env configuration with pydantic-settings.

**Confidence:** 8/10

### Session 8 — Async Python & asyncio
**Status:** PRACTICING

Covered the mental model of sync vs async, I/O-bound vs CPU-bound work, async/await, coroutines, the event loop, blocking vs non-blocking execution and concurrent I/O.

A practical payment-processing exercise was implemented with three simulated requests of different durations. The sequential version demonstrates that awaiting each coroutine one by one takes approximately the sum of all delays. The concurrent version uses asyncio.gather to start independent I/O operations together and completes in approximately the longest individual delay.

Production relevance: async is essential for efficiently handling concurrent network-bound work such as LLM API calls, database/network I/O and external service integrations. Blocking calls inside async code can stall the event loop and reduce throughput.

**Confidence:** 8/10

**Next:** Session 9 — HTTP & REST.

### Session 9 — HTTP & REST
**Status:** COMPLETED

Reviewed HTTP request/response semantics, methods, status codes, headers, REST resource modeling and practical REST API design.

**Confidence:** 9/10

### Session 10 — FastAPI Fundamentals
**Status:** COMPLETED

Reviewed FastAPI application setup, path operations and routing, HTTP methods, path parameters, query parameters, request bodies, Pydantic request models, JSON responses and Swagger/OpenAPI. The learner already had sufficient practical understanding, so the session was completed without repeating implementation exercises.

**Confidence:** 9/10

**Next:** Session 11 — Pydantic with FastAPI.
