# Session 19 — Code Quality Exercise

## Goal

Apply production-oriented Python code quality checks with:

- Ruff
- Pyright
- Pre-commit
- formatting
- linting
- static type checking

## Project configuration

Recommended `pyproject.toml` configuration:

```toml
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP"]

[tool.ruff.format]
quote-style = "double"

[tool.pyright]
include = ["app", "tests"]
typeCheckingMode = "strict"
pythonVersion = "3.12"

[tool.pytest.ini_options]
asyncio_mode = "auto"
```

## Commands

```bash
uv run ruff check .
uv run ruff format --check .
uv run pyright
uv run pytest
```

To automatically format and fix supported Ruff issues:

```bash
uv run ruff format .
uv run ruff check . --fix
```

## Pre-commit

A production repository can run the same checks before every commit:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.10
    hooks:
      - id: ruff-check
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/RobertCraigie/pyright-python
    rev: v1.1.395
    hooks:
      - id: pyright
```

Install and run:

```bash
uv add --dev pre-commit
uv run pre-commit install
uv run pre-commit run --all-files
```

## Mental model

```text
Source Code
    │
    ├── Ruff ──────► style + lint + common bugs
    │
    ├── Pyright ───► static type correctness
    │
    ├── pytest ────► runtime behavior
    │
    └── pre-commit ► run quality gates before commit
```

Ruff and Pyright solve different problems. Ruff primarily analyzes source-code quality and lint rules; Pyright reasons about the static type system. Neither replaces runtime tests.

## Production rule

Quality checks should be automated in local development and CI. A developer should not need to remember every command manually.

The CI gate should fail when formatting, linting, type checking or tests fail.

## Completion

This exercise demonstrates the complete Code Quality workflow required for the Phase 1 backend foundation.
