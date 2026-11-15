from collections.abc import Sequence
from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from retrieval.models import RetrievedChunk


# Bind values are parameters, never interpolated into SQL. The tenant filter is
# applied inside the database query, before any chunk can reach the application.
SEARCH_SQL = text("""
    SELECT
        c.id AS chunk_id,
        c.document_id,
        c.content,
        c.metadata,
        c.tenant_id,
        d.source_name AS source,
        c.page_number AS page,
        c.embedding <=> CAST(:query_vector AS vector) AS distance
    FROM document_chunks AS c
    INNER JOIN documents AS d ON d.id = c.document_id
    WHERE c.tenant_id = CAST(:tenant_id AS uuid)
    ORDER BY c.embedding <=> CAST(:query_vector AS vector) ASC
    LIMIT :top_k
""")


class PgVectorStore:
    """PostgreSQL + pgvector adapter.

    Uses the Session 32 schema: document_chunks.id/document_id/tenant_id/page_number/
    content/embedding/metadata and documents.id/source_name. The embedding dimension must match ingestion.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def search(
        self,
        *,
        query_vector: Sequence[float],
        tenant_id: str,
        top_k: int,
    ) -> list[RetrievedChunk]:
        vector_literal = "[" + ",".join(str(float(value)) for value in query_vector) + "]"
        result = await self._session.execute(
            SEARCH_SQL,
            {
                "query_vector": vector_literal,
                "tenant_id": tenant_id,
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
                    company_id=str(row["tenant_id"]),
                    source=str(source),
                    page=row["page"],
                    distance=float(row["distance"]),
                    metadata=metadata,
                )
            )
        return chunks
