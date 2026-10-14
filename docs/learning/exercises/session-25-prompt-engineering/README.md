# Session 25 — Prompt Engineering

## Goal

Design prompts that are reusable, testable, versioned, and safer to use in an AI-backed service.

This exercise deliberately does **not** call a real LLM. Prompt unit tests should be deterministic and must not require an API key or incur provider costs.

## Concepts

- System instructions vs user input
- Prompt templates
- Output constraints
- Few-shot examples
- Prompt versioning
- Prompt injection awareness
- Unit testing prompt construction

## Project structure

```text
session-25-prompt-engineering/
├── prompts.py
├── pyproject.toml
├── README.md
└── tests/
    └── test_prompts.py
```

## Run

From this directory:

```bash
uv sync
uv run pytest
```

## Exercise requirements

1. Read both prompt versions in `prompts.py`; explain how their instructions differ.
2. Implement or review `get_system_prompt()` and `build_user_prompt()`.
3. Add at least eight test cases covering:
   - refund requests
   - technical problems
   - account access
   - messages that fit no category
   - empty and whitespace-only input
   - text containing prompt-injection attempts
4. Add at least three few-shot examples and explain why each example was selected.
5. Add a new prompt version without silently changing the existing version.
6. Explain which behavior can be tested locally and which behavior requires evaluation against an actual LLM.

## Allowed categories

- `refund`
- `technical_support`
- `account_access`
- `other`

## Important distinction

Tests for prompt construction can verify that instructions and untrusted user text are placed correctly. They cannot prove that an LLM will always obey the prompt. Prompt injection cannot be reliably prevented by delimiters or wording alone. Enforce authorization and business rules in application code, and validate model outputs before using them.

## Production considerations

- Keep prompts outside route handlers.
- Track prompt versions in evaluation results and logs.
- Avoid logging secrets or unnecessary personal data.
- Use structured outputs / schema validation when a machine-readable response is required (covered in Session 27).
- Do not retry permanent provider errors just because a prompt failed.
