from rag_ingestion.cleaner import clean_text

def test_clean_text_normalizes_unicode_and_whitespace() -> None:
    assert clean_text("  قوانین   بیمه  \r\n\r\n\r\n  ماده ۷۶  ") == "قوانین بیمه\n\nماده ۷۶"

def test_clean_text_preserves_single_newlines() -> None:
    assert clean_text("line one\nline two") == "line one\nline two"

def test_clean_text_empty_input() -> None:
    assert clean_text("  \n  ") == ""
