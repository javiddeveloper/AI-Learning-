# AI Engineering Learning Journey

A structured, long-term learning knowledge base for becoming a **Production-oriented AI Engineer**.

This repository is intentionally focused on **learning, progress tracking, durable knowledge, and learning decisions**. Practical projects will be created in separate repositories and can reference this repository as the central learning source of truth.

## Goal

The goal is not simply to learn Python, call an LLM API, or use AI frameworks.

The goal is to become capable of:

- Designing AI-powered systems
- Building reliable AI backends
- Integrating LLMs into production applications
- Building structured AI workflows
- Implementing RAG systems
- Building tool-using agents
- Deploying and monitoring AI systems
- Evaluating AI quality and reliability
- Managing latency, cost, security, and scalability

## Learning Path

```text
Python & FastAPI
        ↓
LLM Engineering
        ↓
Structured Outputs & Tool Calling
        ↓
Embeddings & RAG
        ↓
Agents & LangGraph
        ↓
Production AI Engineering
        ↓
Evaluation & Observability
        ↓
AI System Design
        ↓
Model Fundamentals
        ↓
Fine-Tuning & Local LLMs
```

## Current Phase

**Phase 1 — Python & FastAPI Backend Foundation**

The current focus is learning Python and FastAPI specifically as the backend foundation for AI Engineering.

The curriculum is intentionally not a generic Python course. It prioritizes the concepts needed to build production-oriented AI services.

## Existing Engineering Background

The learner already has strong experience with:

- Kotlin
- Java
- Android Development
- Jetpack Compose
- Kotlin Multiplatform / Compose Multiplatform
- Clean Architecture
- MVVM / MVI
- REST APIs and HTTP
- JSON
- SQL and databases
- Git
- Docker
- Error handling
- Logging
- Retry logic
- System design
- Production software development
- Banking, POS and payment systems

The learning process should build on this background instead of restarting general software engineering education.

## Repository Structure

```text
AI-Learning-/
│
├── README.md
│
├── docs/
│   ├── learning/
│   │   ├── ROADMAP.md
│   │   ├── PROGRESS.md
│   │   ├── CURRENT_STATE.md
│   │   ├── KNOWLEDGE.md
│   │   └── SESSION_GUIDE.md
│   │
│   └── decisions/
│       └── DECISIONS.md
```

### `docs/learning/ROADMAP.md`

The complete learning roadmap and technology areas to cover.

### `docs/learning/PROGRESS.md`

Tracks topic status, confidence, completed sessions, weaknesses, and practical validation.

### `docs/learning/CURRENT_STATE.md`

The single file that describes exactly where the learner is right now and what should be learned next.

### `docs/learning/KNOWLEDGE.md`

The durable personal knowledge base containing important concepts, mental models, production lessons, and comparisons with Kotlin/Java/Android concepts.

### `docs/learning/SESSION_GUIDE.md`

The recommended session-by-session learning sequence. It defines what each learning session should cover and how progress should be recorded.

### `docs/decisions/DECISIONS.md`

Records important technology and architecture decisions made during the learning journey.

## Learning Philosophy

The learning process follows:

```text
Concept
  ↓
Why it matters
  ↓
Connection to existing knowledge
  ↓
Minimal example
  ↓
Production considerations
  ↓
Hands-on implementation
  ↓
Review
  ↓
Progress update
```

A topic is **not considered completed just because it was discussed**. Completion requires practical implementation and review.

## Source of Truth

For the AI Engineering learning journey, the files under `docs/learning/` are the central knowledge base.

The current learning position should always be determined from:

1. `CURRENT_STATE.md`
2. `PROGRESS.md`
3. `ROADMAP.md`
4. `KNOWLEDGE.md`

## Practical Projects

Practical implementations are intentionally kept outside this repository.

Each major phase may have its own dedicated repository, for example:

```text
AI-Learning-
    ↓
Learning Knowledge Base

AI-Python-Backend
    ↓
Python/FastAPI Practice Project

AI-RAG-System
    ↓
RAG Practice Project

AI-Agent-System
    ↓
Agent Practice Project
```

This repository remains the central learning and knowledge reference across those projects.

## Long-Term Outcome

The target is to become an engineer capable of building systems such as:

```text
Mobile / Web Client
        ↓
FastAPI Backend
        ↓
AI Orchestration Layer
        ↓
Model Router / LLM Provider
        ↓
RAG / Vector Search
        ↓
Tools / External APIs
        ↓
Databases / Services
```

with production concerns including:

- Reliability
- Security
- Observability
- Evaluation
- Rate limiting
- Retry and resilience
- Cost management
- Latency optimization
- Scalability
- Monitoring

## Status

**Current Phase:** Phase 1 — Python & FastAPI Backend Foundation

**Current Session:** Session 01 — Python Fundamentals

**Overall Progress:** Just started
