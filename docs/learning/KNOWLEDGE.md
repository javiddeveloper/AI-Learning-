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

### Type Hints

Not yet formally covered as a dedicated topic. Type hints have been used throughout exercises.

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

## Next Learning Target

Continue Session 3 with Python OOP, then proceed to the dedicated Type Hints & Pyright topic according to the roadmap.
