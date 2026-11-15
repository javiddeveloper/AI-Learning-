class InvalidQueryError(ValueError):
    """Raised when a query is empty after preprocessing."""


def preprocess_query(query: str) -> str:
    """Apply conservative normalization without changing query semantics."""
    normalized = " ".join(query.split())
    if not normalized:
        raise InvalidQueryError("query must not be empty")
    return normalized
