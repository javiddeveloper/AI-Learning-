# Session Guide

This file defines the recommended sequence for learning sessions. Each session should first read the project instructions and the current state files, then continue from the actual progress rather than blindly following the list.

## Session 01 — Python Fundamentals

Start with Python concepts required for Backend and AI Engineering:

- Variables and data types
- Lists, tuples, sets and dictionaries
- Conditions and loops
- Functions
- Exceptions

Compare with Kotlin/Java where useful. Use practical exercises. Do not mark complete until implemented.

## Session 02 — Pythonic Programming

Teach:

- Comprehensions
- Iterables and iterators
- Generators and `yield`
- `enumerate`
- `zip`
- `map`
- `filter`
- `any` and `all`

Focus on readable backend data processing.

## Session 03 — Functions & OOP

Teach:

- Function arguments
- `*args` and `**kwargs`
- Keyword-only arguments
- Classes and methods
- `classmethod`
- `staticmethod`
- Composition
- Inheritance
- Abstract Base Classes
- Protocol

Compare with Kotlin/Java.

## Session 04 — Type Hints & Pyright

Teach modern Python typing:

- Type annotations
- Optional / Union
- Generics
- Literal
- TypedDict
- Callable
- TypeVar
- Protocol
- Static checking vs runtime validation
- Pyright

## Session 05 — Dataclasses, Pydantic & ORM Models

Clearly distinguish:

- Dataclass
- Pydantic BaseModel
- SQLAlchemy ORM Model

Use FastAPI/backend examples.

## Session 06 — Modules, Packages & uv

Teach:

- Modules
- Packages
- Imports
- `__init__.py`
- Absolute vs relative imports
- Circular dependencies
- Virtual environments
- uv
- pyproject.toml
- Dependency management

Create a small production-oriented project structure.

## Session 07 — Exceptions, Context Managers & Decorators

Teach:

- Exception handling
- Custom exceptions
- Context managers
- `with`
- `contextlib`
- Decorators
- `functools.wraps`
- Configuration
- Environment variables
- `.env`
- pydantic-settings

## Session 08 — Async Python

Deeply teach:

- Sync vs async
- I/O-bound vs CPU-bound
- `async` / `await`
- Coroutines
- Event loop
- asyncio
- `asyncio.gather`
- Blocking vs non-blocking

Compare with Kotlin Coroutines. Practice with httpx. Do not move on until the learner understands why async matters for AI applications.

## Session 09 — HTTP & REST

Teach:

- HTTP methods
- Headers
- Request body
- Query/path parameters
- Status codes
- Authentication
- Timeout
- Retry
- Rate limiting
- Idempotency

Connect to Android/REST experience.

## Session 10 — FastAPI Fundamentals

Teach and implement:

- FastAPI application
- Routing
- GET/POST/PUT/PATCH/DELETE
- Path and query parameters
- Request body
- Response models
- Status codes
- OpenAPI
- Swagger

Do not introduce advanced architecture yet.

## Session 11 — Pydantic with FastAPI

Teach:

- BaseModel
- Validation
- Nested models
- Optional fields
- Defaults
- Field
- Serialization
- Deserialization
- JSON Schema

Connect to future structured LLM outputs.

## Session 12 — FastAPI Dependency Injection

Teach:

- Depends
- Dependency lifecycle
- Database dependencies
- Authentication dependencies
- Service dependencies
- Configuration dependencies

Compare with Hilt and Spring DI.

## Session 13 — PostgreSQL & SQLAlchemy 2.x

Teach:

- Database connections
- ORM
- Models
- Sessions
- Async sessions
- Relationships
- Transactions
- Queries

Build a database-backed FastAPI feature.

## Session 14 — Alembic

Teach:

- Migration concept
- Revision
- Upgrade
- Downgrade
- Schema evolution

Integrate with FastAPI + PostgreSQL + SQLAlchemy.

## Session 15 — External APIs with httpx

Teach:

- Async HTTP client
- Timeouts
- Connection pooling
- Headers
- Authentication
- Error handling

Build a real external API integration.

## Session 16 — Retry, Timeout & Resilience

Teach:

- Timeout
- Retry
- Exponential backoff
- Maximum retry
- Retry safety
- Idempotency
- Circuit breaker concepts

Use Tenacity where appropriate. Connect to future LLM API calls.

## Session 17 — Authentication & Authorization

Teach:

- Authentication vs authorization
- JWT
- Access tokens
- Refresh tokens
- Password hashing
- OAuth2 concepts

Implement simple JWT authentication without over-engineering.

## Session 18 — Testing

Teach:

- pytest
- Fixtures
- Unit tests
- Integration tests
- Mocking
- Async tests
- httpx testing

Test routes, services, database behavior and external APIs.

## Session 19 — Code Quality

Teach and configure:

- Ruff
- Pyright
- Pre-commit
- Formatting
- Linting
- Static type checking

## Session 20 — Docker & Docker Compose

Containerize:

- FastAPI
- PostgreSQL
- Redis

Cover Dockerfile, images, containers, networks, volumes, environment variables and health checks.

## Session 21 — AI-Ready Backend

Build the final Phase 1 foundation:

Mobile Client
→ FastAPI
→ Authentication
→ Chat Service
→ LLM Client
→ External LLM API

Requirements:

- FastAPI
- Pydantic
- PostgreSQL
- SQLAlchemy
- Alembic
- Async Python
- httpx
- Authentication
- Error handling
- Logging
- Retry
- Timeout
- Rate limiting
- Testing
- Docker

Do not introduce RAG, agents or LangGraph yet. This project is the bridge to Phase 2.

## Session Completion Protocol

At the end of every session:

1. Review the learner's implementation.
2. Identify gaps and weaknesses.
3. Assign confidence from 1–10.
4. Update `PROGRESS.md`.
5. Update `CURRENT_STATE.md`.
6. Add durable concepts to `KNOWLEDGE.md`.
7. Recommend the next session.

Never mark a topic completed based only on discussion.
