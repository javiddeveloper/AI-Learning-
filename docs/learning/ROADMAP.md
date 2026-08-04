# AI Engineering Learning Roadmap

## Goal

Become a production-oriented AI Engineer by building on existing software engineering skills.

The goal is not to become a generic Python developer, ML researcher, or framework specialist. The goal is to design, build, deploy, evaluate, and maintain reliable AI-powered production systems.

## Personalized Learning Strategy

This roadmap combines:

1. The learner's existing software engineering background.
2. Production-oriented AI Engineering requirements.
3. Practical concepts represented in modern AI Engineer roadmaps such as roadmap.sh.
4. A project-first learning approach.

The learner already has strong experience in Kotlin, Java, Android, REST, SQL, Docker, testing, reliability, system design, and production systems. Therefore, general software engineering topics should not be unnecessarily repeated.

## Long-Term Path

1. Python & FastAPI Backend Foundation
2. LLM Engineering
3. Structured Outputs & Tool Calling
4. Embeddings, Vector Search & RAG
5. AI Workflows & Agents
6. AI Security
7. Production AI Engineering
8. Evaluation, Observability & LLMOps
9. AI System Design
10. ML / DL / Transformer Fundamentals
11. Fine-Tuning & Local LLMs
12. Capstone Production AI System

---

# Phase 1 — Python & FastAPI Backend Foundation

## Objective

Build the Python and backend foundation required for production AI Engineering.

This is not a generic Python course. Focus on concepts that will be used later for LLM APIs, RAG, agents, asynchronous workflows, data pipelines, and production AI services.

## Python

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

## Async & Networking

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

## FastAPI

- Routes and request handling
- Query/path/body parameters
- Response models
- Pydantic validation
- Dependency Injection
- Middleware
- OpenAPI
- Authentication and authorization
- Lifespan and graceful shutdown
- Health/readiness endpoints

## Data

- PostgreSQL
- SQLAlchemy 2.x
- Async sessions
- Transactions
- Alembic migrations
- Redis basics

## Production Engineering

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

## Phase 1 Outcome

Build a production-oriented AI-ready FastAPI backend that can later integrate with LLMs, RAG, tools, and agents.

---

# Phase 2 — LLM Engineering

## Objective

Understand LLM applications from an engineering perspective before using complex frameworks.

## Topics

- Tokens and tokenization
- Context windows
- System, developer, and user messages
- Temperature and generation controls
- Model capabilities and limitations
- OpenAI API
- Anthropic API
- Gemini API
- Streaming responses
- Conversation state
- Prompt engineering
- Prompt templates
- Structured prompting
- Cost and latency
- Token budgeting
- Rate limits and provider failures

## Outcome

Build reliable applications that call LLM APIs directly without depending on orchestration frameworks.

---

# Phase 3 — Structured AI & Tool Calling

## Objective

Turn probabilistic model output into reliable software behavior.

## Topics

- Structured outputs
- JSON Schema
- Pydantic structured responses
- Function calling
- Tool calling
- Tool schemas
- Validation of model output
- Tool execution lifecycle
- Tool errors
- Retry behavior
- Idempotency
- Human approval for sensitive actions

## Outcome

Build an AI workflow where the model can reliably choose and invoke application capabilities.

---

# Phase 4 — Embeddings, Vector Search & RAG

## Objective

Build systems that retrieve relevant external knowledge before generating answers.

## Topics

- Embeddings
- Vector representations
- Chunking strategies
- Metadata
- Vector similarity
- pgvector
- Qdrant
- Vector indexing concepts
- Retrieval strategies
- Hybrid search concepts
- Reranking
- Context assembly
- Citation and source attribution
- RAG failure modes
- RAG evaluation

## Tool Strategy

Do not learn multiple vector databases deeply at the same time.

Start with **PostgreSQL + pgvector** to reuse existing SQL knowledge, then learn Qdrant when its capabilities provide a clear reason.

## Outcome

Build and evaluate a production-oriented RAG service.

---

# Phase 5 — AI Workflows & Agents

## Objective

Understand when to use deterministic workflows and when an agent is justified.

## Topics

- Workflow vs Agent
- Tool-using agents
- State management
- Memory concepts
- Multi-step workflows
- LangGraph
- Parallel execution
- Conditional routing
- Human-in-the-loop
- Durable execution concepts
- Failure recovery
- Retry and timeout policies
- Agent guardrails

## Framework Strategy

Learn the underlying concepts first.

Use **LangGraph** as the primary agent/workflow framework. Introduce LangChain or LlamaIndex only when a concrete use case justifies them.

Temporal is treated as a broader durable workflow technology and should be learned later when workflow durability requirements justify it.

## Outcome

Build an agent that can safely use multiple tools and recover from common failures.

---

# Phase 6 — AI Security

## Objective

Understand security risks specific to AI applications.

## Topics

- Prompt injection
- Indirect prompt injection
- Data leakage
- Sensitive information handling
- Secrets management
- Tool authorization
- Least privilege
- Untrusted tool output
- Input validation
- Output validation
- Sandboxing concepts
- Model abuse and misuse
- Rate limiting
- Authentication and authorization

## Outcome

Design AI systems with explicit security boundaries instead of trusting model output by default.

---

# Phase 7 — Production AI Engineering

## Objective

Operate AI systems reliably under real production constraints.

## Topics

- Model routing
- Model selection
- Caching
- Semantic caching concepts
- Rate limiting
- Retries
- Timeouts
- Circuit breakers
- Cost optimization
- Token budgets
- Latency optimization
- Batch processing
- Queues and background jobs
- Async workloads
- Deployment
- Scalability
- Reliability

## Outcome

Design AI services that remain reliable when models are slow, unavailable, expensive, or rate-limited.

---

# Phase 8 — Evaluation, Observability & LLMOps

## Objective

Measure whether an AI system is actually working and detect regressions.

## Topics

- Logging
- Tracing
- Metrics
- Token usage tracking
- Latency tracking
- Cost tracking
- Langfuse
- Offline evaluation
- Online evaluation
- Golden datasets
- LLM-as-a-judge
- Human evaluation
- Regression testing
- Quality metrics
- RAG evaluation
- Agent evaluation
- Prompt/version management

## Outcome

Build an AI system where quality, cost, latency, and failures are observable and measurable.

---

# Phase 9 — AI System Design

## Objective

Apply existing system design skills to AI-specific architectures.

## Topics

Design scalable systems involving:

- API gateways
- Model routers
- LLM providers
- RAG pipelines
- Vector stores
- Caches
- Queues
- Databases
- Tool services
- Agent orchestration
- Observability
- Evaluation
- Cost controls
- Security boundaries

## Design Problems

Practice designing systems such as:

- Production RAG platform
- Multi-model AI assistant
- Enterprise AI chatbot
- Tool-using customer support agent
- Document intelligence system
- AI workflow platform

## Outcome

Be able to explain architecture, trade-offs, failure modes, scaling strategy, and cost of production AI systems.

---

# Phase 10 — ML / DL / Transformer Fundamentals

## Objective

Learn enough mathematics and model fundamentals to understand how modern AI systems work without unnecessarily switching career tracks into ML research.

## Mathematics

- Probability fundamentals
- Statistics fundamentals
- Vectors and matrices
- Dot product
- Cosine similarity
- Basic optimization concepts

## Machine Learning

- Supervised vs unsupervised learning
- Training vs inference
- Features and labels
- Overfitting
- Generalization
- Evaluation metrics

## Deep Learning & Transformers

- Neural network mental model
- Embeddings
- Tokenization
- Attention
- Self-attention
- Transformer architecture
- Positional information
- Context windows
- Inference
- Quantization concepts

## Outcome

Understand why LLMs and embeddings behave as they do and make informed engineering decisions.

---

# Phase 11 — Fine-Tuning & Local LLMs

## Objective

Understand when customization or local inference is justified.

## Topics

- Fine-tuning concepts
- Dataset preparation
- Supervised fine-tuning
- LoRA
- QLoRA
- Evaluation
- Quantization
- Local inference
- Ollama
- vLLM
- GPU fundamentals
- Model serving
- Throughput vs latency
- Cost comparison: API vs self-hosted

## Outcome

Understand the trade-offs between prompting, RAG, fine-tuning, and self-hosted models.

---

# Phase 12 — Capstone Production AI System

Build one complete production-oriented AI system combining the skills from the roadmap.

Possible architecture:

```text
Mobile / Web Client
        ↓
FastAPI API
        ↓
Authentication & Authorization
        ↓
AI Orchestration Layer
        ↓
Model Router
   ↙         ↘
LLM API     Local Model
        ↓
Tools / RAG / Vector Search
        ↓
PostgreSQL / Redis
        ↓
Observability & Evaluation
```

Requirements should include:

- Reliability
- Security
- Observability
- Evaluation
- Rate limiting
- Retry and resilience
- Cost management
- Latency optimization
- Scalability

---

# Learning Principles

## 1. Capability over Frameworks

Learn what the system must accomplish before learning a framework.

## 2. Production over Tutorials

Every major topic should include failure modes, reliability, security, observability, cost, and scalability.

## 3. Projects are Separate

This repository is the central learning knowledge base. Practical projects live in separate repositories.

## 4. Do Not Over-Learn Equivalent Tools

Prefer one primary tool per problem until a real use case requires alternatives.

## 5. Completion Requires Evidence

A topic is not COMPLETED because it was discussed. The learner must explain the concept and demonstrate it through practical implementation.

## 6. Use Existing Strengths

Connect new concepts to Kotlin, Java, Android, REST, SQL, Docker, system design, reliability, and production engineering experience.
