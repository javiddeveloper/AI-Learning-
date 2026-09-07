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
**Session 11 — Pydantic with FastAPI**

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
| Pydantic with FastAPI | NOT_STARTED | - | |
| FastAPI Dependency Injection | NOT_STARTED | - | |
| PostgreSQL | NOT_STARTED | - | |
| SQLAlchemy 2.x | PRACTICING | 8/10 | ORM model syntax practiced; sessions, relationships, transactions and queries remain. |
| Alembic | NOT_STARTED | - | |
| httpx | NOT_STARTED | - | |
| Retry, Timeout & Resilience | NOT_STARTED | - | |
| Authentication & Authorization | NOT_STARTED | - | |
| Testing with pytest | NOT_STARTED | - | |
| Ruff, Pyright & Pre-commit | IN_PROGRESS | 8/10 | Pyright practiced; Ruff and pre-commit remain. |
| Docker & Docker Compose | NOT_STARTED | - | |
| Production Backend Concepts | NOT_STARTED | - | |
| AI-Ready Backend | NOT_STARTED | - | |

## Completion Rule
A topic is COMPLETED only after explanation in the learner's own words plus a practical implementation reviewed in a session. For non-obvious concepts, code alone is insufficient: the execution model and mental model must also be understood and explained before completion.

## Session History
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
