from collections.abc import Sequence

import pytest

from retrieval.models import RetrievedChunk
from retrieval.retriever import RetrievalService


class FakeEmbedder:
    def __init__(self) -> None:
        self.received_query: str | None = None

    async def embed_query(self, text: str) -> Sequence[float]:
        self.received_query = text
        return [0.8, 0.2, 0.1]


class FakeVectorStore:
    def __init__(self, chunks: list[RetrievedChunk]) -> None:
        self.chunks = chunks
        self.received_tenant_id: str | None = None
        self.received_top_k: int | None = None

    async def search(
        self, *, query_vector: Sequence[float], tenant_id: str, top_k: int
    ) -> list[RetrievedChunk]:
        assert list(query_vector) == [0.8, 0.2, 0.1]
        self.received_tenant_id = tenant_id
        self.received_top_k = top_k
        return self.chunks[:top_k]


def make_chunk(chunk_id: str, distance: float) -> RetrievedChunk:
    return RetrievedChunk(
        chunk_id=chunk_id,
        document_id="doc-1",
        content=f"content {chunk_id}",
        tenant_id="tenant-a",
        source="policy.pdf",
        page=3,
        distance=distance,
        metadata={"tenant_id": "tenant-a"},
    )


@pytest.mark.asyncio
async def test_query_is_preprocessed_and_top_k_is_forwarded() -> None:
    embedder = FakeEmbedder()
    store = FakeVectorStore([make_chunk("c1", 0.1), make_chunk("c2", 0.2)])
    service = RetrievalService(embedder, store)

    results = await service.search(
        query="  how   to cancel?  ",
        tenant_id="tenant-a",
        top_k=2,
    )

    assert embedder.received_query == "how to cancel?"
    assert store.received_tenant_id == "tenant-a"
    assert store.received_top_k == 2
    assert [item.chunk_id for item in results] == ["c1", "c2"]


@pytest.mark.asyncio
async def test_no_results_returns_empty_list() -> None:
    service = RetrievalService(FakeEmbedder(), FakeVectorStore([]))
    assert await service.search(query="unknown topic", tenant_id="tenant-a") == []


@pytest.mark.asyncio
async def test_top_k_limits_returned_results() -> None:
    chunks = [make_chunk("c1", 0.1), make_chunk("c2", 0.2), make_chunk("c3", 0.3)]
    service = RetrievalService(FakeEmbedder(), FakeVectorStore(chunks))

    results = await service.search(query="query", tenant_id="tenant-a", top_k=2)

    assert len(results) == 2


@pytest.mark.asyncio
async def test_empty_tenant_id_is_rejected() -> None:
    service = RetrievalService(FakeEmbedder(), FakeVectorStore([]))
    with pytest.raises(ValueError, match="tenant_id"):
        await service.search(query="query", tenant_id=" ")
