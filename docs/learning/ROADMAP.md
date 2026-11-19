# AI Engineering Learning Roadmap

## Goal

Become a Senior AI Engineer who can independently design, build, train or fine-tune, evaluate, deploy, optimize, and maintain production AI systems.

The goal is to combine strong software engineering with practical Machine Learning, NLP, Deep Learning, LLM Engineering, model serving, and MLOps. This is an engineering-oriented path: learn enough model internals to make sound decisions and deliver working systems, without turning the curriculum into an academic ML research track.

## Personalized Learning Strategy

This roadmap combines:

1. The learner's existing software engineering background.
2. Production-oriented AI Engineering requirements.
3. Practical concepts represented in modern AI Engineer roadmaps such as roadmap.sh.
4. A project-first learning approach.

The learner already has strong experience in Kotlin, Java, Android, REST, SQL, Docker, testing, reliability, system design, and production systems. Therefore, general software engineering topics should not be unnecessarily repeated.

## Explanation Requirement

New concepts must not be treated as completed merely because code was shown or copied.

When a topic contains a concept whose internal behavior, lifecycle, control flow, syntax, or abstraction is not obvious, the concept must be explicitly explained before moving on. This includes explaining what happens behind the syntax, why the abstraction exists, and how execution flows through it.

For such concepts, prefer this sequence:

1. Simple mental model.
2. Step-by-step execution flow.
3. Connection to a familiar Kotlin/Java/Android concept when useful.
4. Minimal example.
5. Production use case.
6. Hands-on exercise or verification of understanding.

Do not skip explanations just because the learner can read the code. Examples such as decorators, `*args`/`**kwargs`, `functools.wraps`, context managers, `with`, `yield`, async execution, event loops, dependency injection, and other non-obvious Python/AI abstractions should be broken down when they are introduced.

If the learner explicitly says a concept is not understood, stop progressing through the curriculum and explain that concept from a simpler level before marking the section complete.

---

## Long-Term Path

1. Python & FastAPI Backend Foundation
2. LLM Engineering
3. Structured Outputs & Tool Calling
4. Embeddings, Vector Search & RAG
5. AI Workflows & Agents
6. Applied Machine Learning & NLP
7. Deep Learning & Transformer Engineering
8. Model Fine-Tuning, Serving & Optimization
9. Speech & Voice AI
10. AI Security
11. Production AI Engineering
12. Evaluation, Observability & MLOps
13. AI System Design
14. Capstone Production AI System

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
- RAGAS and evaluation datasets
- Persian text normalization and retrieval
- Enterprise document ingestion
- Document-level authorization in RAG
- Citation/source attribution
- Retrieval + reranking pipelines

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
- LangChain fundamentals
- Parallel execution
- Conditional routing
- Human-in-the-loop
- Durable execution concepts
- Failure recovery
- Retry and timeout policies
- Agent guardrails
- Tool authorization policies
- Agent evaluation

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
- Container orchestration
- Kubernetes
- Helm
- Service Mesh concepts and architecture
- Docker Swarm and comparison with Kubernetes
- Advanced container orchestration patterns
- Scalability
- Reliability

## Container Orchestration Track

After Docker and Docker Compose foundations, learn production container orchestration in a dedicated track:

- Kubernetes fundamentals and architecture
- Pods, Deployments, Services, ConfigMaps and Secrets
- Health probes and resource management
- Scaling and rolling updates
- Helm charts and templating
- Service Mesh concepts, traffic management and observability
- Docker Swarm architecture and operational model
- Kubernetes vs Docker Swarm trade-offs
- Advanced container orchestration patterns
- Production failure modes and operational considerations

These topics are intentionally introduced after the Docker/Compose foundation and before the capstone infrastructure work.

## Outcome

Design AI services that remain reliable when models are slow, unavailable, expensive, or rate-limited, and understand how containerized AI services are orchestrated in production.

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
- RAGAS
- Retrieval evaluation
- Faithfulness / answer relevance
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
- Persian enterprise RAG
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

# Phase 11 — Applied Machine Learning & NLP

## Objective

Build practical ML and NLP systems for real business problems such as classification, semantic similarity, content moderation, and fraud detection.

## Topics

- NumPy and Pandas essentials for ML data workflows
- Dataset inspection, cleaning, preprocessing and splitting
- Scikit-learn estimators, pipelines and preprocessing
- Supervised learning: classification and regression
- Baseline models and feature engineering
- Text preprocessing and Persian text normalization
- Bag of Words and TF-IDF
- Text classification and semantic similarity
- Precision, Recall, F1, confusion matrix, ROC-AUC and PR-AUC
- Class imbalance, sampling, class weights and threshold tuning
- Data leakage, overfitting and cross-validation
- Fraud detection and anomaly detection fundamentals
- Experiment tracking and reproducible evaluation
- Error analysis and model selection

## Outcome

Build and evaluate practical ML/NLP baselines, explain metric trade-offs, and identify when a classical ML model is more appropriate than an LLM.

---

# Phase 12 — Deep Learning & Transformer Engineering

## Objective

Gain hands-on ability to understand, fine-tune, evaluate and operate neural and Transformer-based models.

## Topics

- PyTorch tensors, devices and tensor operations
- Autograd, loss functions and optimizers
- Dataset and DataLoader
- Training and validation loops
- Neural network fundamentals
- Hugging Face ecosystem and Transformers
- Tokenizers and pretrained model lifecycle
- BERT architecture and encoder models
- Fine-tuning BERT for text classification
- ParsBERT and multilingual models
- Training stability, overfitting and regularization
- GPU/CUDA fundamentals and memory constraints
- Batch size, throughput and inference latency
- Model checkpointing and reproducibility
- Model evaluation and error analysis

## Outcome

Fine-tune a pretrained Transformer for a real classification task and compare it against a Scikit-learn baseline.

---

# Phase 13 — Model Serving & Inference Optimization

## Objective

Deploy trained models as reliable, measurable and efficient production services.

## Topics

- Model serving patterns and lifecycle
- FastAPI inference endpoints
- CPU vs GPU inference
- ONNX export and ONNX Runtime
- Quantization concepts and practical trade-offs
- Dynamic batching and concurrency
- Throughput, latency and memory profiling
- vLLM architecture and continuous batching
- NVIDIA Triton concepts and model serving
- Model versioning and rollout strategies
- Load testing and performance benchmarks
- API-level timeouts, backpressure and resource limits

## Outcome

Serve a trained model behind an API, benchmark it under load, and justify optimization decisions using measured latency, throughput, and resource usage.

---

# Phase 14 — Speech & Voice AI

## Objective

Build practical speech-processing capabilities and understand their production constraints.

## Topics

- Audio representation and sampling basics
- Speech-to-Text (STT) pipeline
- Whisper architecture and inference
- Transcription quality evaluation
- Persian speech recognition considerations
- Text-to-Speech (TTS) concepts and integration
- Streaming audio and chunked transcription
- Voice AI pipeline architecture
- Latency, accuracy, privacy and cost trade-offs

## Outcome

Build a transcription service and expose it through a production-oriented API, with measurable quality and latency.

---

# Phase 15 — Fine-Tuning & Local LLMs

## Objective

Understand when prompting, RAG, fine-tuning or self-hosting is the right solution.

## Topics

- Fine-tuning strategy selection
- Dataset preparation and quality
- Supervised fine-tuning (SFT)
- LoRA and QLoRA
- LLM evaluation before and after fine-tuning
- Quantization
- Ollama
- vLLM for LLM serving
- GPU memory and inference fundamentals
- Throughput vs latency
- API vs self-hosted model cost comparison
- Model deployment and operational trade-offs

## Outcome

Make evidence-based decisions about adapting and hosting models, and complete a controlled fine-tuning or local-inference experiment.

---

# Phase 16 — Capstone Production AI System

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
