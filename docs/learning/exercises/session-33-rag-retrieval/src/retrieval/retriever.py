from typing import Protocol, Sequence

from retrieval.models import RetrievedChunk
from retrieval.query_processor import preprocess_query


class EmbeddingProvider(Protocol):
    async def embed_query(self, text: str) -> Sequence[float]:
        """Return a vector produced by the same embedding space as ingested chunks."""


class VectorStore(Protocol):
    async def search(
        self,
        *,
        query_vector: Sequence[float],
        tenant_id: str,
        top_k: int,
    ) -> list[RetrievedChunk]:
        """Search only within the authorized tenant and return nearest chunks first."""


class RetrievalService:
    def __init__(
        self,
        embedding_provider: EmbeddingProvider,
        vector_store: VectorStore,
    ) -> None:
        self._embedding_provider = embedding_provider
        self._vector_store = vector_store

    async def search(
        self,
        *,
        query: str,
        tenant_id: str,
        top_k: int = 5,
    ) -> list[RetrievedChunk]:
        if not tenant_id.strip():
            raise ValueError("tenant_id must not be empty")
        if top_k < 1:
            raise ValueError("top_k must be greater than zero")

        normalized_query = preprocess_query(query)
        query_vector = await self._embedding_provider.embed_query(normalized_query)
        if not query_vector:
            raise ValueError("embedding provider returned an empty vector")

        return await self._vector_store.search(
            query_vector=query_vector,
            tenant_id=tenant_id,
            top_k=top_k,
        )
