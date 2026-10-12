# Session 23 — Direct LLM APIs

## Goal

Build a small FastAPI application that calls an LLM through a provider-independent boundary:

```text
HTTP request → FastAPI route → ChatService → LLMClient → OpenAI Responses API
```

Tests replace the provider with `MockLLMClient`; they do not need an API key, network access, or tokens.

## Requirements

- Python 3.12+
- uv
- An OpenAI API key only for a live provider call

## Setup

From this directory:

```bash
uv sync
cp .env.example .env
# Set OPENAI_API_KEY in .env before making a live request
uv run uvicorn app.main:app --reload
```

Open `/docs` for the generated OpenAPI UI.

## Try the endpoint

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"Explain RAG in two sentences."}'
```

Expected shape:

```json
{"response":"...generated text..."}
```

The exact model output varies. Configure the model with `OPENAI_MODEL` if needed.

## Run tests

```bash
uv run pytest
```

The tests override FastAPI's `get_llm_client` dependency with a deterministic fake. They do not call OpenAI.

## Switch implementation

The route depends on `ChatService`, and `ChatService` depends on the `LLMClient` Protocol. The composition root (`app/api/deps.py`) chooses the concrete implementation. A future Gemini or Anthropic adapter can implement the same protocol without changing the service or route.

## Production notes

- Never commit `.env`; use a secret manager in deployment.
- Set a finite request timeout.
- Normalize provider exceptions into application-level exceptions.
- Do not blindly retry every failure: authentication and invalid-request errors are not transient.
- Add rate limiting, usage/cost telemetry, request IDs, output limits, and provider-specific integration tests before production.
- Do not expose raw provider exception details to clients.
- The model name and availability depend on the API account; configure it rather than hard-coding it throughout the codebase.

## Scope

This exercise intentionally returns plain text only. Streaming, conversation history, structured outputs, and tool calling are separate roadmap topics.
