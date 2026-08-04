# Session Guide

This file defines the recommended sequence for learning sessions. Each session must first read the Project Instructions and the learning state files, then continue from the actual current state rather than blindly restarting the curriculum.

The roadmap is capability-oriented: learn the engineering problem first, then the tool that solves it.

## Phase 1 — Python & FastAPI Backend Foundation

### Session 01 — Python Fundamentals

Teach Python concepts required for Backend and AI Engineering:

- Variables and data types
- Lists, tuples, sets and dictionaries
- Conditions and loops
- Functions
- Exceptions

Compare with Kotlin/Java where useful. Use practical exercises. Do not mark complete until implemented.

### Session 02 — Pythonic Programming

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

### Session 03 — Functions & OOP

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

### Session 04 — Type Hints & Pyright

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

### Session 05 — Dataclasses, Pydantic & ORM Models

Clearly distinguish:

- Dataclass
- Pydantic BaseModel
- SQLAlchemy ORM Model

Use FastAPI/backend examples.

### Session 06 — Modules, Packages & uv

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

### Session 07 — Exceptions, Context Managers, Decorators & Configuration

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

### Session 08 — Async Python

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

### Session 09 — HTTP & REST

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

### Session 10 — FastAPI Fundamentals

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
- Lifespan
- Health/readiness endpoints

Do not introduce advanced architecture yet.

### Session 11 — Pydantic with FastAPI

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

### Session 12 — FastAPI Dependency Injection

Teach:

- Depends
- Dependency lifecycle
- Database dependencies
- Authentication dependencies
- Service dependencies
- Configuration dependencies

Compare with Hilt and Spring DI.

### Session 13 — PostgreSQL & SQLAlchemy 2.x

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

### Session 14 — Alembic

Teach:

- Migration concept
- Revision
- Upgrade
- Downgrade
- Schema evolution

Integrate with FastAPI + PostgreSQL + SQLAlchemy.

### Session 15 — External APIs with httpx

Teach:

- Async HTTP client
- Timeouts
- Connection pooling
- Headers
- Authentication
- Error handling

Build a real external API integration.

### Session 16 — Retry, Timeout & Resilience

Teach:

- Timeout
- Retry
- Exponential backoff
- Maximum retry
- Retry safety
- Idempotency
- Circuit breaker concepts

Use Tenacity where appropriate. Connect to future LLM API calls.

### Session 17 — Authentication & Authorization

Teach:

- Authentication vs authorization
- JWT
- Access tokens
- Refresh tokens
- Password hashing
- OAuth2 concepts

Implement simple JWT authentication without over-engineering.

### Session 18 — Testing

Teach:

- pytest
- Fixtures
- Unit tests
- Integration tests
- Mocking
- Async tests
- httpx testing

Test routes, services, database behavior and external APIs.

### Session 19 — Code Quality

Teach and configure:

- Ruff
- Pyright
- Pre-commit
- Formatting
- Linting
- Static type checking

### Session 20 — Docker & Docker Compose

Containerize:

- FastAPI
- PostgreSQL
- Redis

Cover Dockerfile, images, containers, networks, volumes, environment variables and health checks.

### Session 21 — Phase 1 AI-Ready Backend

Build the final Phase 1 foundation:

Mobile Client
→ FastAPI
→ Authentication
→ Chat Service
→ LLM Client boundary
→ External LLM API boundary

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

Do not implement RAG, agents, or LangGraph yet. The goal is to create the backend foundation for Phase 2.

---

## Phase 2 — LLM Engineering

### Session 22 — LLM Mental Model

Teach:

- Tokens
- Tokenization
- Context windows
- System/developer/user messages
- Temperature
- Model limitations
- Hallucination basics

### Session 23 — Direct LLM APIs

Practice direct API integration before frameworks:

- OpenAI API
- Anthropic API
- Gemini API
- Request/response lifecycle
- Provider abstraction concepts

### Session 24 — Streaming & Conversation State

Teach:

- Streaming
- SSE concepts
- Conversation history
- Context management
- Token budgeting

### Session 25 — Prompt Engineering

Teach:

- System prompts
- User prompts
- Prompt templates
- Constraints
- Few-shot examples
- Prompt versioning
- Prompt injection awareness

### Session 26 — LLM Reliability, Cost & Latency

Teach:

- Token usage
- Cost calculation
- Rate limits
- Timeouts
- Retries
- Fallbacks
- Model selection
- Latency optimization

---

## Phase 3 — Structured AI & Tool Calling

### Session 27 — Structured Outputs

- JSON Schema
- Pydantic structured outputs
- Validation
- Parsing failures
- Schema evolution

### Session 28 — Function & Tool Calling

- Tool schemas
- Tool selection
- Tool execution lifecycle
- Tool errors
- Retry and idempotency

### Session 29 — Reliable Tool-Using AI

Build a workflow that safely calls application tools and handles failures.

---

## Phase 4 — Embeddings & RAG

### Session 30 — Embeddings

- Embedding mental model
- Similarity
- Cosine similarity
- Chunking
- Metadata

### Session 31 — Vector Search with PostgreSQL + pgvector

- Vector storage
- Indexing concepts
- Similarity queries
- Retrieval

### Session 32 — RAG Pipeline

Build:

Ingestion → Chunking → Embedding → Storage → Retrieval → Context → Generation

### Session 33 — Advanced Retrieval

- Hybrid search
- Reranking
- Metadata filters
- Context compression
- Retrieval failure modes

### Session 34 — RAG Evaluation

- Retrieval quality
- Answer quality
- Golden datasets
- Regression tests

---

## Phase 5 — AI Workflows & Agents

### Session 35 — Workflow vs Agent

Understand when deterministic workflows are preferable to autonomous agents.

### Session 36 — LangGraph Fundamentals

- State
- Nodes
- Edges
- Conditional routing

### Session 37 — Tool-Using Agents

Build an agent using multiple tools with validation and error handling.

### Session 38 — Memory & Human-in-the-Loop

- Short-term state
- Long-term memory concepts
- Human approval

### Session 39 — Agent Reliability

- Failure recovery
- Retry
- Timeouts
- Guardrails
- Observability

---

## Phase 6 — AI Security

### Session 40 — AI Threat Model

- Prompt injection
- Indirect prompt injection
- Data leakage
- Untrusted model output

### Session 41 — Secure Tool Use

- Authorization
- Least privilege
- Tool boundaries
- Input/output validation
- Secrets

---

## Phase 7 — Production AI Engineering

### Session 42 — Model Routing

- Model selection
- Cost/quality/latency trade-offs
- Fallback models

### Session 43 — Caching & Rate Limiting

- Response caching
- Semantic caching concepts
- Rate limits

### Session 44 — Resilience at AI Scale

- Queues
- Background jobs
- Circuit breakers
- Backpressure

---

## Phase 8 — Evaluation, Observability & LLMOps

### Session 45 — AI Observability

- Logs
- Traces
- Metrics
- Token usage
- Latency
- Cost

### Session 46 — Langfuse & Tracing

Implement tracing for LLM calls, RAG and agent workflows.

### Session 47 — AI Evaluation

- Offline evaluation
- Online evaluation
- LLM-as-a-judge
- Human evaluation
- Regression testing

---

## Phase 9 — AI System Design

### Session 48 — AI Architecture Patterns

Design production systems involving models, RAG, tools, queues, caches, and observability.

### Session 49 — System Design Case Studies

Practice:

- Enterprise RAG
- AI assistant
- Multi-model assistant
- Tool-using support agent

---

## Phase 10 — ML / DL / Transformer Fundamentals

### Session 50 — Math for AI Engineers

- Probability
- Statistics
- Vectors
- Matrices
- Dot product
- Cosine similarity

### Session 51 — ML Fundamentals

- Training vs inference
- Supervised vs unsupervised
- Overfitting
- Generalization
- Metrics

### Session 52 — Transformers

- Tokenization
- Embeddings
- Attention
- Self-attention
- Transformer architecture
- Context windows

---

## Phase 11 — Fine-Tuning & Local LLMs

### Session 53 — Fine-Tuning

- SFT
- Dataset preparation
- LoRA
- QLoRA
- Evaluation

### Session 54 — Local Inference

- Quantization
- Ollama
- vLLM
- GPU fundamentals
- Serving trade-offs

### Session 55 — API vs Self-Hosted Models

Compare cost, latency, privacy, reliability, and operational complexity.

---

## Phase 12 — Capstone

### Session 56+ — Production AI System

Build one complete production-oriented AI system combining:

- FastAPI
- Authentication
- LLM integration
- Structured outputs
- Tool calling
- RAG
- Agent/workflow orchestration
- PostgreSQL
- Redis
- Observability
- Evaluation
- Security
- Cost controls
- Reliability

The exact capstone should be selected based on the learner's interests and career goals at that point.

---

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
