from pathlib import Path

import pytest

from rag_ingestion.embeddings import MockEmbeddingProvider
from rag_ingestion.pipeline import IngestionPipeline


@pytest.mark.asyncio
async def test_pipeline_parses_chunks_and_embeds(tmp_path: Path) -> None:
    source = tmp_path / "policy.txt"
    source.write_text("شرایط بیمه افراد\nسابقه پرداخت", encoding="utf-8")
    pipeline = IngestionPipeline(
        MockEmbeddingProvider(),
        chunk_size_words=3,
        overlap_words=1,
    )

    result = await pipeline.ingest(source, document_id="doc-1")

    assert not result.skipped
    assert len(result.chunks) == 2
    assert result.chunks[0].metadata.document_id == "doc-1"
    assert result.chunks[0].metadata.source_name == "policy.txt"
    assert len(result.chunks[0].embedding) == 3


@pytest.mark.asyncio
async def test_pipeline_skips_unchanged_file(tmp_path: Path) -> None:
    source = tmp_path / "policy.txt"
    source.write_text("unchanged document", encoding="utf-8")
    pipeline = IngestionPipeline(MockEmbeddingProvider())

    first = await pipeline.ingest(source, document_id="doc-1")
    second = await pipeline.ingest(
        source,
        document_id="doc-1",
        known_content_hash=first.document_hash,
    )

    assert second.skipped
    assert second.chunks == []


@pytest.mark.asyncio
async def test_pipeline_rejects_embedding_count_mismatch(tmp_path: Path) -> None:
    class BrokenProvider:
        async def embed(self, texts: list[str]) -> list[list[float]]:
            return []

    source = tmp_path / "policy.txt"
    source.write_text("some useful text", encoding="utf-8")
    pipeline = IngestionPipeline(
        BrokenProvider(),
        chunk_size_words=2,
        overlap_words=1,
    )

    with pytest.raises(ValueError, match="unexpected vector count"):
        await pipeline.ingest(source, document_id="doc-1")
