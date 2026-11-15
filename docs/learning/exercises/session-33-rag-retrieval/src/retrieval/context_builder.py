from retrieval.models import BuiltContext, Citation, RetrievedChunk


def build_context(
    chunks: list[RetrievedChunk],
    *,
    max_chars: int = 6_000,
) -> BuiltContext:
    """Build a bounded context and preserve citations for included chunks.

    Character budget is a deterministic teaching baseline, not a token budget.
    A production implementation should use the target model's tokenizer.
    """
    if max_chars < 1:
        raise ValueError("max_chars must be greater than zero")

    sections: list[str] = []
    citations: list[Citation] = []
    included_ids: list[str] = []
    seen_ids: set[str] = set()
    used_chars = 0

    for chunk in chunks:
        if chunk.chunk_id in seen_ids:
            continue
        section = f"[Source: {chunk.source}, page: {chunk.page or 'N/A'}]\n{chunk.content}"
        separator = "\n\n" if sections else ""
        required = len(separator) + len(section)
        if used_chars + required > max_chars:
            continue

        sections.append(section)
        used_chars += required
        seen_ids.add(chunk.chunk_id)
        included_ids.append(chunk.chunk_id)
        citations.append(
            Citation(
                document_id=chunk.document_id,
                chunk_id=chunk.chunk_id,
                source=chunk.source,
                page=chunk.page,
            )
        )

    return BuiltContext(
        text="\n\n".join(sections),
        citations=tuple(citations),
        included_chunk_ids=tuple(included_ids),
    )
