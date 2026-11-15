# Session 33 — RAG Retrieval Pipeline

## Goal

Implement the retrieval half of RAG:

`Query → Preprocessing → Query Embedding → Tenant-scoped Vector Search → Context Selection → Citations`

This exercise uses PostgreSQL + pgvector as the production adapter and fake dependencies for deterministic unit tests.

## Structure

- `query_processor.py`: conservative query whitespace normalization.
- `retriever.py`: orchestration boundary using EmbeddingProvider and VectorStore protocols.
- `postgres_store.py`: async SQLAlchemy adapter for pgvector cosine-distance search.
- `context_builder.py`: bounded context assembly with source attribution.
- `service.py`: retrieval-to-context orchestration.
- `tests/`: unit tests that do not require PostgreSQL or an embedding API.

## Database assumptions

The SQL adapter matches the Session 32 schema:

- `document_chunks.id`, `document_id`, `tenant_id`, `page_number`, `content`, `embedding vector(N)`, `metadata JSONB`
- `documents.id`, `source_name`

It joins `documents` to recover the source filename and filters by `document_chunks.tenant_id`.

The vector dimension and embedding model must be identical/compatible with the ingestion pipeline. The pgvector extension must be enabled.

The SQL uses `<=>` (cosine distance), orders ascending (smaller distance is closer), applies the tenant predicate in the database, and parameterizes all values. The authenticated application layer must derive `tenant_id`; never trust a tenant ID supplied by the model or arbitrary user query. For stronger defense in depth, add PostgreSQL Row-Level Security (RLS).

## Context budget

The exercise uses a character budget so tests remain deterministic and do not require a tokenizer. This is only a teaching baseline. Production context limits should be enforced using the tokenizer for the selected generation model, reserving tokens for system instructions, user input, and output.

Chunks that do not fit are skipped rather than truncated, so source attribution remains tied to complete retrieved chunks. Citations are generated from retrieved metadata by the application, not invented by the LLM.

## Run

From this directory:

```bash
uv sync --extra dev
uv run pytest
uv run ruff check .
uv run pyright
```

## Deliberate scope

This session implements dense retrieval and safe context assembly. Hybrid search, query expansion, reranking, and model-based compression are introduced conceptually and evaluated in later sessions. Do not add them before a dense baseline is tested.
