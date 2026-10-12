from app.llm.client import LLMClient


class MockLLMClient:
    """Deterministic fake for tests and local development."""

    async def generate(self, message: str) -> str:
        return f"Mock response to: {message}"
