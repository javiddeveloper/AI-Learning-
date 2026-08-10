# Knowledge Base

This file stores durable knowledge acquired during the learning journey. It should contain concise explanations, important mental models, production lessons, and comparisons to concepts already known from Kotlin/Java/Android.

## Python

### Python Fundamentals

Completed initial fundamentals required for backend and AI engineering.

### Python Data Model / Core Collections

- `list`: ordered, mutable collection; useful when items may change.
- `tuple`: ordered, immutable collection; useful for fixed-structure values such as `(x, y)` or `(latitude, longitude)`.
- `set`: unique values; useful for membership and deduplication when ordering is not required.
- `dict`: key/value mapping.
- Preserve input order while removing duplicates with `dict.fromkeys(...)` when appropriate.

### Functions & Modules

- Python functions are defined with `def` and should use type annotations for parameters and return values.
- Default parameters provide optional behavior without overloads.
- Keyword arguments improve call-site clarity.
- Tuple unpacking can receive multiple returned values.
- Function variables are scoped locally; module-level names have broader scope.
- Modules are `.py` files and can expose functions/classes through `import`.
- `if __name__ == "__main__":` prevents a module's entry-point code from running when imported.
- Docstrings document functions and modules for developers and tooling.
- Keep domain responsibilities separated across modules instead of putting all logic in `main.py`.
- Explicit imports are preferred over wildcard imports.

### Type Hints & Pyright

- Type annotations describe expected types but do not by themselves provide runtime validation.
- `str | None` expresses a value that may be a string or `None` and is the modern Python syntax for this common nullable type.
- Generic collections use syntax such as `list[str]` and `dict[int, str]`.
- `TypeVar` allows a generic function to preserve the relationship between input and output types, e.g. `def first(items: list[T]) -> T`.
- `Literal` restricts a value to a fixed set of allowed values and is useful for bounded states such as payment status.
- `TypedDict` describes the expected keys and value types of dictionary-shaped data for static type checking.
- `Callable[[int, int], int]` describes a function that accepts two integers and returns an integer.
- `Protocol` defines a structural contract. A class can satisfy the protocol by providing the required members without explicitly inheriting from it.
- Pyright performs static type checking during development; it does not replace runtime validation.
- Pydantic is used for runtime validation at application boundaries, while Pyright checks the source code statically. They are complementary.
- Prefer modern built-in generic syntax such as `list[T]` over legacy `List[T]` in new Python code.

## Async Python

Not started.

## FastAPI

Not started.

## Pydantic

Used practically through `BaseModel` in an exercise, but dedicated validation, serialization, schema behavior, and FastAPI integration remain to be learned.

## PostgreSQL / SQLAlchemy

Not started.

## Testing

Not started.

## Production Engineering

### Lessons So Far

- Separate reusable business logic from the application entry point.
- Handle expected errors explicitly, e.g. rejecting division by zero.
- Avoid unnecessary abstractions; introduce modules when responsibilities become distinct.
- Static typing improves development-time safety but should not be confused with runtime input validation.

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

To be documented during learning.

### Pydantic Schema vs SQLAlchemy ORM Model

To be documented during learning.

### pytest vs JUnit

To be documented during learning.

## Production Lessons

To be documented from practical sessions.

## Common Mistakes

- Using `list(set(items))` when preserving the original order matters.
- Putting reusable functions inside `main()` when they belong to a separate module.
- Using wildcard imports such as `from module import *`.
- Assuming Python type annotations enforce runtime validation; use appropriate runtime validation such as Pydantic at external boundaries.

## Next Learning Target

Session 5 — Dataclasses, Pydantic & ORM Models.
