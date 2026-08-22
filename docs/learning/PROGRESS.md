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
**Session 8 — Async Python & asyncio**

## Phase 1 Progress
| Topic | Status | Confidence | Notes |
|---|---|---:|---|
| Python Fundamentals | COMPLETED | 8/10 | Core fundamentals practiced. |
| Pythonic Programming | PRACTICING | 8/10 | Core collections/data-model concepts practiced; more Pythonic constructs remain. |
| Functions & OOP | PRACTICING | 8.5/10 | Functions, parameters, return values, default/keyword arguments, scope, modules/imports and docstrings completed. OOP remains to be formalized. |
| Type Hints & Pyright | COMPLETED | 9/10 | Practiced annotations, generics, Literal, TypedDict, Callable, Protocol and static checking with Pyright. |
| Dataclasses vs Pydantic vs ORM | COMPLETED | 8.8/10 | Implemented and reviewed a payment-domain flow using Dataclass, Pydantic v2 and SQLAlchemy 2.x ORM models. |
| Modules, Packages & uv | COMPLETED | 9/10 | Implemented a src-layout package, imports, __init__.py, dependency direction, uv, pyproject.toml and uv.lock. Compared uv with pip + requirements.txt. |
| Exceptions, Context Managers & Decorators | COMPLETED | 8/10 | Practiced custom exceptions, try/except/else/finally, context managers, decorators and functools.wraps. Core execution flow and mental models were explained. |
| Configuration & pydantic-settings | COMPLETED | 8/10 | Practiced .env-based configuration and pydantic-settings in the Session 7 payment exercise. |
| Async Python & asyncio | NOT_STARTED | - | |
| HTTP & REST | NOT_STARTED | - | |
| FastAPI Fundamentals | NOT_STARTED | - | |
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

Practiced a payment-service exercise covering:

- Exception hierarchy and custom exceptions.
- try / except / else / finally execution flow.
- Context managers and with, including transaction-style BEGIN / COMMIT / ROLLBACK / CLOSE lifecycle.
- Decorators as functions that wrap another function to add behavior without modifying the original business logic.
- *args and **kwargs for forwarding arbitrary function arguments.
- functools.wraps for preserving the wrapped function's metadata.
- Environment configuration using .env and pydantic-settings.

The non-obvious execution flow of decorators and context managers was explicitly explained with simple mental models and Kotlin-style resource lifecycle comparisons.

**Confidence:** 8/10

**Next:** Session 8 — Async Python & asyncio.
