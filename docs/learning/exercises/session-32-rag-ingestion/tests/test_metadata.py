from rag_ingestion.metadata import build_chunk_metadata


def test_chunk_metadata_is_stable_for_same_inputs() -> None:
    args = {
        "document_id": "doc-1",
        "source_name": "guide.pdf",
        "page_number": 3,
        "chunk_index": 2,
        "content_hash": "a" * 64,
    }

    first = build_chunk_metadata(**args)
    second = build_chunk_metadata(**args)

    assert first == second
    assert first.chunk_id == second.chunk_id


def test_chunk_metadata_changes_for_different_chunk_index() -> None:
    common = {
        "document_id": "doc-1",
        "source_name": "guide.pdf",
        "page_number": 3,
        "content_hash": "a" * 64,
    }

    first = build_chunk_metadata(**common, chunk_index=1)
    second = build_chunk_metadata(**common, chunk_index=2)

    assert first.chunk_id != second.chunk_id
