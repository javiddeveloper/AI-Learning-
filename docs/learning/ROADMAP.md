# AI Engineering Learning Roadmap

## Goal

Become a production-oriented AI Engineer by building on existing software engineering skills.

## Long-Term Path

1. Python & FastAPI Backend Foundation
2. LLM Engineering
3. Structured Outputs & Tool Calling
4. Embeddings & RAG
5. Agents & LangGraph
6. Production AI Engineering
7. Evaluation & Observability
8. AI System Design
9. Model Fundamentals
10. Fine-Tuning & Local LLMs

## Phase 1 — Python & FastAPI

### Python
- Core syntax and data types
- Collections and comprehensions
- Functions and Pythonic programming
- OOP, composition, protocols
- Dataclasses
- Type hints and Pyright
- Iterators and generators
- Context managers
- Decorators
- Modules and packages
- Exceptions and custom exceptions
- Configuration and environment variables
- `uv` and `pyproject.toml`

### Async & Networking
- `async` / `await`
- Coroutines
- Event loop
- `asyncio`
- Concurrent I/O
- Blocking vs non-blocking
- HTTP fundamentals
- REST API design
- Timeouts
- Retry and idempotency
- Rate limiting

### FastAPI
- Routes and request handling
- Query/path/body parameters
- Response models
- Pydantic validation
- Dependency Injection
- Middleware
- OpenAPI
- Authentication and authorization

### Data
- PostgreSQL
- SQLAlchemy 2.x
- Async sessions
- Transactions
- Alembic migrations
- Redis basics

### Production Engineering
- `httpx`
- Tenacity
- Structured logging with `structlog`
- pytest and pytest-asyncio
- Ruff
- Pyright
- Pre-commit
- Docker
- Docker Compose
- Health checks
- Graceful shutdown

### Phase 1 Outcome

Build a production-oriented AI-ready FastAPI backend that can later integrate with LLMs, RAG and agents.

## Phase 2 — LLM Engineering

- Tokens
- Context windows
- System/user/developer messages
- Temperature and generation controls
- OpenAI API
- Anthropic API
- Gemini API
- Streaming
- Conversation state
- Prompt engineering
- Cost and latency

## Phase 3 — Structured AI

- Structured outputs
- JSON Schema
- Function calling
- Tool calling
- Validation of model output
- Reliable AI workflows

## Phase 4 — Embeddings & RAG

- Embeddings
- Chunking
- Vector similarity
- pgvector
- Qdrant
- Retrieval strategies
- Reranking
- RAG evaluation

## Phase 5 — Agents

- Tool-using agents
- LangGraph
- State and memory
- Workflow orchestration
- Parallel execution
- Human-in-the-loop
- Failure handling

## Phase 6 — Production AI

- Model routing
- Caching
- Rate limiting
- Retries
- Cost optimization
- Security
- Prompt injection
- Data privacy
- Observability
- Deployment

## Phase 7 — Evaluation & Observability

- Tracing
- Langfuse
- Offline evaluation
- Online evaluation
- Golden datasets
- LLM-as-a-judge
- Regression testing
- Quality metrics

## Phase 8 — AI System Design

Design scalable AI systems involving:

- API gateways
- Model routers
- LLM providers
- RAG pipelines
- Vector stores
- Caches
- Queues
- Databases
- Observability
- Evaluation
- Cost controls

## Phase 9 — Model Fundamentals

- Transformer mental model
- Attention
- Embeddings
- Tokenization
- Inference
- Quantization
- Context windows

## Phase 10 — Fine-Tuning & Local LLMs

- Fine-tuning concepts
- LoRA / QLoRA
- Dataset preparation
- Evaluation
- Local inference
- Ollama
- vLLM
- GPU fundamentals
