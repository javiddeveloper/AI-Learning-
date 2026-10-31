# Session 32 — RAG Ingestion Pipeline

A deterministic, testable document-ingestion exercise.

## Pipeline

Document bytes → Parsing → Cleaning → Chunking → Metadata → Embedding → Storage boundary

The exercise starts with TXT and text-based PDF files. Scanned PDFs require OCR and are intentionally out of scope.

## Setup

```bash
cd docs/learning/exercises/session-32-rag-ingestion
uv sync
uv run pytest
```

## Design

- `parser.py`: extracts page-aware text from TXT/PDF.
- `cleaner.py`: performs conservative Unicode and whitespace cleanup.
- `chunker.py`: creates overlapping chunks. This exercise uses whitespace words as a deterministic approximation; production systems should use the tokenizer associated with the embedding model.
- `metadata.py`: creates stable document/chunk identifiers and source metadata.
- `embeddings.py`: defines an async provider contract and deterministic mock provider.
- `pipeline.py`: orchestrates the stages and skips unchanged content by SHA-256.
- `schema.sql`: PostgreSQL + pgvector persistence schema.

## Important production notes

1. Store the original file and calculate its SHA-256 before processing.
2. Do not treat a filename as a unique document identity.
3. Keep document versioning and ingestion status in the database.
4. Generate embeddings in bounded batches with provider timeouts and rate limits.
5. Persist a new version completely before switching the active version; do not destroy the last good index on a failed re-index.
6. Enforce tenant/document authorization in retrieval queries. Metadata is not an authorization mechanism by itself.
7. Use OCR for scanned PDFs, and evaluate Persian normalization carefully.
8. The mock embedding provider is only for deterministic tests; it is not semantically meaningful.

## Tests

The suite contains 14 tests across `test_parser.py`, `test_cleaner.py`, `test_chunker.py`, `test_metadata.py` and `test_pipeline.py`.

Run them with `uv run pytest`. They have been authored but are not yet runtime-verified.

## Learner verification

Run the tests, inspect chunk boundaries and overlap, then explain:
- why chunking is needed;
- why overlap can help and also increase cost;
- why a content hash is useful;
- why metadata filters must be combined with authorization checks.

The session remains PRACTICING until the learner runs and reviews the implementation.
