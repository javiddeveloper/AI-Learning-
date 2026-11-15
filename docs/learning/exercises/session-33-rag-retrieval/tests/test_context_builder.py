import pytest

from retrieval.context_builder import build_context
from retrieval.models import RetrievedChunk


def chunk(
    chunk_id: str,
    content: str,
    *,
    distance: float = 0.1,
    source: str = "guide.pdf",
    page: int | None = 4,
) -> RetrievedChunk:
    return RetrievedChunk(
        chunk_id=chunk_id,
        document_id="doc-1",
        content=content,
        company_id="company-a",
        source=source,
        page=page,
        distance=distance,
        metadata={"source": source},
    )


def test_context_preserves_source_and_page_citations() -> None:
    result = build_context([chunk("c1", "Cancellation policy")])

    assert "Cancellation policy" in result.text
    assert result.citations[0].source == "guide.pdf"
    assert result.citations[0].page == 4
    assert result.included_chunk_ids == ("c1",)


def test_context_respects_character_budget() -> None:
    result = build_context(
        [chunk("c1", "first"), chunk("c2", "second")],
        max_chars=45,
    )

    assert len(result.text) <= 45
    assert len(result.citations) == len(result.included_chunk_ids)


def test_duplicate_chunks_are_included_only_once() -> None:
    result = build_context([chunk("c1", "same"), chunk("c1", "same")])

    assert result.included_chunk_ids == ("c1",)
    assert len(result.citations) == 1


def test_invalid_context_budget_is_rejected() -> None:
    with pytest.raises(ValueError, match="max_chars"):
        build_context([], max_chars=0)
