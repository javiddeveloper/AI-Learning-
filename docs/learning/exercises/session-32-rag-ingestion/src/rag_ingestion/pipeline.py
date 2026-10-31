import hashlib
from dataclasses import dataclass
from pathlib import Path

from rag_ingestion.chunker import Chunk, chunk_text
from rag_ingestion.cleaner import clean_text
from rag_ingestion.embeddings import EmbeddingProvider
from rag_ingestion.metadata import ChunkMetadata, build_chunk_metadata
from rag_ingestion.parser import parse_document

@dataclass(frozen=True, slots=True)
class IngestedChunk:
    content: str
    embedding: list[float]
    metadata: ChunkMetadata

@dataclass(frozen=True, slots=True)
class IngestionResult:
    document_hash: str
    chunks: list[IngestedChunk]
    skipped: bool = False

class IngestionPipeline:
    def __init__(self, embedding_provider: EmbeddingProvider, *,
                 chunk_size_words: int = 100, overlap_words: int = 20) -> None:
        self._embedding_provider = embedding_provider
        self._chunk_size_words = chunk_size_words
        self._overlap_words = overlap_words

    async def ingest(self, path: Path, *, document_id: str,
                     known_content_hash: str | None = None) -> IngestionResult:
        raw_bytes = path.read_bytes()
        digest = hashlib.sha256(raw_bytes).hexdigest()
        if known_content_hash == digest:
            return IngestionResult(digest, [], skipped=True)

        pages = parse_document(path)
        pending: list[tuple[Chunk, int]] = []
        for page in pages:
            cleaned = clean_text(page.text)
            pending.extend(
                (chunk, page.page_number)
                for chunk in chunk_text(cleaned, chunk_size_words=self._chunk_size_words,
                                         overlap_words=self._overlap_words)
            )

        vectors = await self._embedding_provider.embed([chunk.content for chunk, _ in pending])
        if len(vectors) != len(pending):
            raise ValueError("Embedding provider returned an unexpected vector count")

        output: list[IngestedChunk] = []
        for (chunk, page_number), vector in zip(pending, vectors, strict=True):
            metadata = build_chunk_metadata(
                document_id=document_id, source_name=path.name, page_number=page_number,
                chunk_index=chunk.index, content_hash=digest,
            )
            output.append(IngestedChunk(chunk.content, vector, metadata))
        return IngestionResult(digest, output)
