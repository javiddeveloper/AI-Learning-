import pytest
from rag_ingestion.chunker import chunk_text

def test_chunk_text_creates_expected_overlap() -> None:
    chunks = chunk_text("one two three four five six seven eight", chunk_size_words=4, overlap_words=2)
    assert [chunk.content for chunk in chunks] == [
        "one two three four", "three four five six", "five six seven eight"
    ]

def test_chunk_text_rejects_invalid_size() -> None:
    with pytest.raises(ValueError):
        chunk_text("some words", chunk_size_words=0)

def test_chunk_text_rejects_overlap_equal_to_size() -> None:
    with pytest.raises(ValueError):
        chunk_text("some words", chunk_size_words=4, overlap_words=4)

def test_chunk_text_empty_input() -> None:
    assert chunk_text("   ") == []
