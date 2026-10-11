# Session 24 — Streaming & Conversation State

This exercise demonstrates the core mechanics from Session 24 without depending on a real LLM provider.

## What is implemented

- FastAPI streaming endpoint using SSE
- Async generator for incremental response chunks
- Conversation state stored by conversation ID
- Conversation isolation between users/conversations
- Basic history truncation
- Mock LLM streaming client
- Tests for conversation storage and truncation

## Run

From this directory:

```bash
uv run uvicorn main:app --reload
```

Then:

```bash
curl -N "http://localhost:8000/chat/demo?message=Hello%20Javid"
```

Expected shape:

```text
data: Echo: Hello

data: Javid

data: [DONE]
```

## Test

```bash
uv run pytest
```

## Architecture

```text
HTTP Request
    ↓
FastAPI
    ↓
ConversationStore
    ↓
truncate_history()
    ↓
MockLLMClient.stream()
    ↓
SSE StreamingResponse
    ↓
Client
```

The mock provider is intentionally isolated behind a streaming interface so it can later be replaced by the real provider adapter from Session 23.
