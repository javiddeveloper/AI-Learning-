# Knowledge Base

This file stores durable knowledge acquired during the learning journey. It should contain concise explanations, important mental models, production lessons, and comparisons to concepts already known from Kotlin/Java/Android.

## Python

### Python Fundamentals

Completed initial fundamentals required for backend and AI engineering.

### Python Data Model / Core Collections

- list: ordered, mutable collection; useful when items may change.
- tuple: ordered, immutable collection; useful for fixed-structure values such as (x, y) or (latitude, longitude).
- set: unique values; useful for membership and deduplication when ordering is not required.
- dict: key/value mapping.
- Preserve input order while removing duplicates with dict.fromkeys(...) when appropriate.

### Functions & Modules

- Python functions are defined with def and should use type annotations for parameters and return values.
- Default parameters provide optional behavior without overloads.
- Keyword arguments improve call-site clarity.
- Tuple unpacking can receive multiple returned values.
- Function variables are scoped locally; module-level names have broader scope.
- Modules are .py files and can expose functions/classes through import.
- if __name__ == "__main__": prevents a module's entry-point code from running when imported.
- Docstrings document functions and modules for developers and tooling.
- Keep domain responsibilities separated across modules instead of putting all logic in main.py.
- Explicit imports are preferred over wildcard imports.

### Modules, Packages & uv

- A module is a Python .py file containing reusable code.
- A package is a structured Python namespace containing related modules. Modern Python also supports namespace packages without __init__.py.
- __init__.py can define package initialization behavior and convenient exports; it is not mandatory for every modern package.
- __all__ mainly controls names exported by wildcard imports such as from package import *; it does not make names truly public/private.
- Absolute imports use the package path, e.g. from payment_app.models.payment import Payment.
- Relative imports use dots relative to the current package, e.g. from .payment import Payment or from ..models.payment import Payment.
- Keep dependency direction one-way where possible to avoid circular imports and improve testability and maintainability.
- pyproject.toml is the modern standard project metadata/configuration file and can declare project dependencies and tool configuration.
- uv manages Python project environments, dependencies, resolution and command execution in a single workflow.
- uv.lock records the resolved dependency graph so environments can be reproduced consistently.
- For new projects in this curriculum, prefer uv + pyproject.toml + uv.lock + uv sync/uv run.
- requirements.txt remains valid for some legacy and deployment workflows, but it is not the same abstraction as uv or pyproject.toml.

### Type Hints & Pyright

- Type annotations describe expected types but do not by themselves provide runtime validation.
- str | None expresses a value that may be a string or None and is the modern Python syntax for this common nullable type.
- Generic collections use syntax such as list[str] and dict[int, str].
- TypeVar allows a generic function to preserve the relationship between input and output types.
- Literal restricts a value to a fixed set of allowed values and is useful for bounded states such as payment status.
- TypedDict describes the expected keys and value types of dictionary-shaped data for static type checking.
- Callable[[int, int], int] describes a function that accepts two integers and returns an integer.
- Protocol defines a structural contract. A class can satisfy the protocol by providing the required members without explicitly inheriting from it.
- Pyright performs static type checking during development; it does not replace runtime validation.
- Pydantic is used for runtime validation at application boundaries, while Pyright checks the source code statically. They are complementary.
- Prefer modern built-in generic syntax such as list[T] over legacy List[T] in new Python code.

### Dataclasses, Pydantic & SQLAlchemy ORM

- Dataclass is useful for lightweight Python data/domain objects and can contain business behavior. It does not automatically perform runtime validation of field types.
- Pydantic BaseModel is suited to external/application boundaries where runtime validation, parsing, serialization and JSON Schema are required.
- Pydantic v2 uses field_validator for custom field validation. Older @validator examples are legacy syntax.
- Pydantic models are not immutable by default. Immutability must be explicitly configured when required.
- SQLAlchemy 2.x uses DeclarativeBase, Mapped and mapped_column as the modern typed ORM model style.
- SQLAlchemy ORM models represent database persistence and should not automatically be treated as API schemas or domain models.
- For monetary values, Decimal in Python and Numeric in SQLAlchemy are preferable to float when exact decimal semantics are required.
- Enum values can provide a controlled mapping between domain status values and database representation.
- A useful backend mental model is: API request → Pydantic validation → domain/business model → SQLAlchemy persistence model → database.
- Mapping methods are acceptable in a small exercise for clarity; larger systems can move mapping into dedicated mapper/application-layer code to keep models focused.
- Pydantic validation and Pyright static checking solve different problems: runtime input safety vs development-time type safety.

## Async Python

Not started.

## FastAPI

Not started.

## Pydantic

Session 5 completed the foundational model concepts: BaseModel, Field, field_validator, runtime validation, serialization and the distinction between API schemas and domain/database models. Dedicated FastAPI integration remains to be learned.

## PostgreSQL / SQLAlchemy

SQLAlchemy 2.x ORM model definitions were practiced in Session 5. Database sessions, relationships, transactions and production queries remain for Session 13.

## Testing

Not started.

## Production Engineering

### Lessons So Far

- Separate reusable business logic from the application entry point.
- Handle expected errors explicitly, e.g. rejecting division by zero.
- Avoid unnecessary abstractions; introduce modules when responsibilities become distinct.
- Static typing improves development-time safety but should not be confused with runtime input validation.
- Separate API schemas, domain models and persistence models when their responsibilities differ.
- Prefer exact decimal representations for financial amounts rather than binary floating-point values.
- Keep package dependencies directional and avoid circular imports.
- Prefer reproducible dependency resolution through a lock file for production projects.

## AI Engineering

Not started.

## Important Comparisons

### FastAPI vs Spring Boot

To be documented during learning.

### FastAPI Dependency Injection vs Hilt / Spring DI

To be documented during learning.

### Python async/await vs Kotlin Coroutines

To be documented during learning.

### Pydantic vs Kotlin Data Classes

Pydantic BaseModel is not simply Python's equivalent of a Kotlin data class. A Kotlin data class primarily models data, while Pydantic adds runtime validation, parsing, serialization and schema generation. Python dataclass is conceptually closer to a Kotlin data class.

### Pydantic Schema vs SQLAlchemy ORM Model

Pydantic models define validated application/API data contracts; SQLAlchemy ORM models define persistence mappings to database tables. They may contain similar fields but have different responsibilities and lifecycle concerns.

### pytest vs JUnit

To be documented during learning.

### uv + pyproject.toml vs pip + requirements.txt

pip + requirements.txt is a package installation workflow commonly used by existing Python projects. uv is a broader project/dependency/environment workflow. pyproject.toml defines project metadata and dependency requirements, while uv.lock records the resolved versions. The preferred workflow for this curriculum is uv + pyproject.toml + uv.lock.

## Production Lessons

- Keep API contracts independent from persistence models when the system has meaningful domain boundaries.
- Use modern library APIs rather than legacy syntax when starting new production code.
- For payment systems, choose numeric representations deliberately; do not use float for exact money calculations.
- Use explicit package boundaries and one-way dependencies where practical.
- Treat dependency locking as part of reproducible production builds.

## Common Mistakes

- Using list(set(items)) when preserving the original order matters.
- Putting reusable functions inside main() when they belong to a separate module.
- Using wildcard imports such as from module import *.
- Assuming Python type annotations enforce runtime validation; use appropriate runtime validation such as Pydantic at external boundaries.
- Assuming Pydantic BaseModel is immutable by default.
- Starting new SQLAlchemy 2.x code with the older declarative_base()/Column style when the typed DeclarativeBase/Mapped/mapped_column style is appropriate.
- Treating requirements.txt as a direct equivalent of uv; they operate at different abstraction levels.

## Next Learning Target

Session 7 — Exceptions, Context Managers, Decorators & Configuration.
