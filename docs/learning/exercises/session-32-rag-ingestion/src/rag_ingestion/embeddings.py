from typing import Protocol

class EmbeddingProvider(Protocol):
    async def embed(self, texts: list[str]) -> list[list[float]]:
        """Return one vector for each input text."""

class MockEmbeddingProvider:
    """Deterministic fake for tests only; vectors are not semantically meaningful."""
    async def embed(self, texts: list[str]) -> list[list[float]]:
        return [
            [float(len(text)), float(sum(text.encode("utf-8")) % 997), float(len(text.split()))]
            for text in texts
        ]
