from retrieval.context_builder import build_context
from retrieval.models import BuiltContext
from retrieval.retriever import RetrievalService


class RagRetrievalPipeline:
    def __init__(self, retriever: RetrievalService) -> None:
        self._retriever = retriever

    async def retrieve_context(
        self,
        *,
        query: str,
        company_id: str,
        top_k: int = 5,
        max_context_chars: int = 6_000,
    ) -> BuiltContext:
        chunks = await self._retriever.search(
            query=query,
            company_id=company_id,
            top_k=top_k,
        )
        return build_context(chunks, max_chars=max_context_chars)
