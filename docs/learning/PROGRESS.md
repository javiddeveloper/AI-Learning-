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
**Session 6 — Modules, Packages & uv**

## Phase 1 Progress
| Topic | Status | Confidence | Notes |
|---|---|---:|---|
| Python Fundamentals | COMPLETED | 8/10 | Core fundamentals practiced. |
| Pythonic Programming | PRACTICING | 8/10 | Core collections/data-model concepts practiced; more Pythonic constructs remain. |
| Functions & OOP | PRACTICING | 8.5/10 | Functions, parameters, return values, default/keyword arguments, scope, modules/imports and docstrings completed. OOP remains to be formalized. |
| Type Hints & Pyright | COMPLETED | 9/10 | Practiced annotations, str | None, generics/TypeVar, Literal, TypedDict, Callable, Protocol, structural typing, and static checking with Pyright. |
| Dataclasses vs Pydantic vs ORM | COMPLETED | 8.8/10 | Implemented a payment-domain flow using Dataclass, Pydantic v2 and SQLAlchemy 2.x ORM models. Clearly distinguished business data, API validation/serialization, and persistence models. |
| Modules, Packages & uv | IN_PROGRESS | 8/10 | Basic modules/imports completed; packages, uv and pyproject.toml remain. |
| Exceptions, Context Managers & Decorators | PRACTICING | 7/10 | Basic exception handling practiced; full topic remains. |
| Configuration & pydantic-settings | NOT_STARTED | - | |
| Async Python & asyncio | NOT_STARTED | - | |
| HTTP & REST | NOT_STARTED | - | |
| FastAPI Fundamentals | NOT_STARTED | - | |
| Pydantic with FastAPI | NOT_STARTED | - | |
| FastAPI Dependency Injection | NOT_STARTED | - | |
| PostgreSQL | NOT_STARTED | - | |
| SQLAlchemy 2.x | PRACTICING | 8/10 | SQLAlchemy 2.x ORM model syntax practiced in Session 5; sessions, relationships, transactions and queries remain for Session 13. |
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

Practiced list, tuple, set, dict, mutable vs immutable collections, and tuple use for coordinate-style values such as (x, y) and (latitude, longitude).

### Session 3 — Functions & Modules
**Status:** PRACTICING

Implemented a multi-module exercise with models.py, math_service.py, user_service.py, and main.py.

Practiced functions, type hints in signatures, default parameters, keyword arguments, tuple unpacking, scope, modules/imports, if __name__ == "__main__", docstrings, ZeroDivisionError, and separation of concerns.

Pydantic BaseModel was used as early practical exposure, but Pydantic is not considered completed until Session 5.

**Confidence:** 8.5/10

### Session 4 — Type Hints & Pyright
**Status:** COMPLETED

Practiced:
- Type annotations
- str | None and Union concepts
- Generic collections
- TypeVar
- Literal
- TypedDict
- Callable
- Protocol and structural typing
- Static type checking vs runtime validation
- Pyright configuration and type checking

Implemented and reviewed a practical payment-oriented exercise containing User, PaymentStatus, a generic first() function, callable operations, and PaymentProcessor protocol implementations.

**Confidence:** 9/10

### Session 5 — Dataclasses, Pydantic & ORM Models
**Status:** COMPLETED

Implemented and reviewed a payment-domain model flow with three distinct representations:
- Payment as a Python dataclass for business/domain logic.
- PaymentRequest as a Pydantic v2 BaseModel for API input validation and serialization boundaries.
- PaymentModel as a SQLAlchemy 2.x ORM model for database persistence.

Practiced:
- Dataclass fields and __post_init__
- Business methods on a dataclass
- Pydantic Field
- Runtime validation with field_validator
- Pydantic v2 conventions
- SQLAlchemy 2.x DeclarativeBase
- Mapped and mapped_column
- Enum mapping for payment status
- Mapping between API, domain and persistence representations
- SQLite in-memory database simulation
- Persisting and retrieving an ORM entity
- Decimal and Numeric for monetary values instead of float in the corrected implementation

Key architectural distinction learned:
- Pydantic → API/input-output validation boundary
- Dataclass → application/domain data and behavior
- SQLAlchemy ORM → database persistence model

**Confidence:** 8.8/10

**Production note:** Conversion methods were kept in the exercise for clarity; in larger systems, mapping is often moved into dedicated mapper/application-layer code to keep models focused.

**Next:** Session 6 — Modules, Packages & uv.
