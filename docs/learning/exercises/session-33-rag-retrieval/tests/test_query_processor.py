import pytest

from retrieval.query_processor import InvalidQueryError, preprocess_query


def test_query_whitespace_is_normalized() -> None:
    assert preprocess_query("  cancel   my subscription ") == "cancel my subscription"


@pytest.mark.parametrize("query", ["", " ", "\n\t"])
def test_empty_query_is_rejected(query: str) -> None:
    with pytest.raises(InvalidQueryError):
        preprocess_query(query)
