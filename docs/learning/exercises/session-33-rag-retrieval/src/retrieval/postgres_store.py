from collections.abc import Sequence
from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from retrieval.models import RetrievedChunk


# Bind values are parameters, never interpolated into SQL. The tenant filter is
# applied inside the database query, before any chunk can reach the application.
SEARCH_SQL = text("""
    SELECT
        chunk_id,
        document_id,
        content,
        metadata,
        metadata->>'company_id' AS company_id,
        metadata->>'source' AS source,
        NULLIF(metadata->>'page', '')::integer AS page,
        embedding <=> CAST(:query_vector AS vector) AS distance
    FROM document_chunks
    WHERE metadata->>'company_id' = :company_id
    ORDER BY embedding <=> CAST(:query_vector AS vector) ASC
    LIMIT :top_k
""")


class PgVectorStore:
    """PostgreSQL + pgvector adapter.

    Assumes document_chunks has chunk_id, document_id, content, metadata (JSONB),
    and embedding (vector) columns. The embedding dimension must match ingestion.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def search(
        self,
        *,
        query_vector: Sequence[float],
        company_id: str,
        top_k: int,
    ) -> list[RetrievedChunk]:
        vector_literal = "[" + ",".join(str(float(value)) for value in query_vector) + "]"
        result = await self._session.execute(
            SEARCH_SQL,
            {
                "query_vector": vector_literal,
                "company_id": company_id,
                "top_k": top_k,
            },
        )
        rows = result.mappings().all()

        chunks: list[RetrievedChunk] = []
        for row in rows:
            metadata: dict[str, Any] = dict(row["metadata"] or {})
            source = row["source"] or metadata.get("source") or "unknown"
            chunks.append(
                RetrievedChunk(
                    chunk_id=str(row["chunk_id"]),
                    document_id=str(row["document_id"]),
                    content=str(row["content"]),
                    company_id=str(row["company_id"]),
                    source=str(source),
                    page=row["page"],
                    distance=float(row["distance"]),
                    metadata=metadata,
                )
            )
        return chunks
