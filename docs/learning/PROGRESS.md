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
**Session 5 — Dataclasses, Pydantic & ORM Models**

## Phase 1 Progress
| Topic | Status | Confidence | Notes |
|---|---|---:|---|
| Python Fundamentals | COMPLETED | 8/10 | Core fundamentals practiced. |
| Pythonic Programming | PRACTICING | 8/10 | Core collections/data-model concepts practiced; more Pythonic constructs remain. |
| Functions & OOP | PRACTICING | 8.5/10 | Functions, parameters, return values, default/keyword arguments, scope, modules/imports and docstrings completed. OOP remains to be formalized. |
| Type Hints & Pyright | COMPLETED | 9/10 | Practiced annotations, `str | None`, generics/TypeVar, Literal, TypedDict, Callable, Protocol, structural typing, and static checking with Pyright. |
| Dataclasses vs Pydantic vs ORM | NOT_STARTED | - | Next topic. Pydantic was used practically earlier, but comparison is not completed. |
| Modules, Packages & uv | IN_PROGRESS | 8/10 | Basic modules/imports completed; packages, uv and pyproject.toml remain. |
| Exceptions, Context Managers & Decorators | PRACTICING | 7/10 | Basic exception handling practiced; full topic remains. |
| Configuration & pydantic-settings | NOT_STARTED | - | |
| Async Python & asyncio | NOT_STARTED | - | |
| HTTP & REST | NOT_STARTED | - | |
| FastAPI Fundamentals | NOT_STARTED | - | |
| Pydantic with FastAPI | NOT_STARTED | - | |
| FastAPI Dependency Injection | NOT_STARTED | - | |
| PostgreSQL | NOT_STARTED | - | |
| SQLAlchemy 2.x | NOT_STARTED | - | |
| Alembic | NOT_STARTED | - | |
| httpx | NOT_STARTED | - | |
| Retry, Timeout & Resilience | NOT_STARTED | - | |
| Authentication & Authorization | NOT_STARTED | - | |
| Testing with pytest | NOT_STARTED | - | |
| Ruff, Pyright & Pre-commit | IN_PROGRESS | 8/10 | Pyright was introduced and practiced in Session 4; Ruff and pre-commit remain. |
| Docker & Docker Compose | NOT_STARTED | - | |
| Production Backend Concepts | NOT_STARTED | - | |
| AI-Ready Backend | NOT_STARTED | - | |

## Completion Rule
A topic is not COMPLETED merely because it was discussed. It requires explanation in the learner's own words plus a practical implementation reviewed in a session.

## Session History
### Session 1 — Python Fundamentals
**Status:** COMPLETED

### Session 2 — Python Data Model / Core Collections
**Status:** COMPLETED

Practiced `list`, `tuple`, `set`, `dict`, mutable vs immutable collections, and tuple use for coordinate-style values such as `(x, y)` and `(latitude, longitude)`.

### Session 3 — Functions & Modules
**Status:** PRACTICING

Implemented a multi-module exercise with `models.py`, `math_service.py`, `user_service.py`, and `main.py`.

Practiced functions, type hints in signatures, default parameters, keyword arguments, tuple unpacking, scope, modules/imports, `if __name__ == "__main__"`, docstrings, `ZeroDivisionError`, and separation of concerns.

Pydantic `BaseModel` was used as early practical exposure, but Pydantic is not considered completed.

**Confidence:** 8.5/10

**Next:** OOP fundamentals remain to be formalized.

### Session 4 — Type Hints & Pyright
**Status:** COMPLETED

Practiced:
- Type annotations
- `str | None` and Union concepts
- Generic collections
- `TypeVar`
- `Literal`
- `TypedDict`
- `Callable`
- `Protocol` and structural typing
- Static type checking vs runtime validation
- Pyright configuration and type checking

Implemented and reviewed a practical payment-oriented exercise containing `User`, `PaymentStatus`, a generic `first()` function, callable operations, and `PaymentProcessor` protocol implementations.

**Confidence:** 9/10

**Note:** Pyright was introduced here; the broader Ruff/Pyright/pre-commit tooling topic remains partially incomplete.

**Next:** Session 5 — Dataclasses, Pydantic & ORM Models.
