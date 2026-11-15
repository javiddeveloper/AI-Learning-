from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class RetrievedChunk:
    """A retrieved chunk together with its source attribution."""

    chunk_id: str
    document_id: str
    content: str
    tenant_id: str
    source: str
    page: int | None
    distance: float
    metadata: dict[str, Any]


@dataclass(frozen=True, slots=True)
class Citation:
    document_id: str
    chunk_id: str
    source: str
    page: int | None


@dataclass(frozen=True, slots=True)
class BuiltContext:
    text: str
    citations: tuple[Citation, ...]
    included_chunk_ids: tuple[str, ...]
