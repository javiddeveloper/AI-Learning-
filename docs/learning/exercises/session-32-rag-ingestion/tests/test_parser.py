from pathlib import Path

import pytest

from rag_ingestion.parser import parse_document


def test_parse_text_file_keeps_content_and_page_number(tmp_path: Path) -> None:
    source = tmp_path / "guide.txt"
    source.write_text("first line\nsecond line", encoding="utf-8")

    pages = parse_document(source)

    assert len(pages) == 1
    assert pages[0].page_number == 1
    assert pages[0].text == "first line\nsecond line"


def test_parse_document_rejects_unsupported_extension(tmp_path: Path) -> None:
    source = tmp_path / "guide.docx"
    source.write_text("not actually a docx", encoding="utf-8")

    with pytest.raises(ValueError, match="Unsupported document type"):
        parse_document(source)
