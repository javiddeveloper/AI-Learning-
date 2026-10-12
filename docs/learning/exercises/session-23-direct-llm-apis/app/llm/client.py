from typing import Protocol


class LLMClient(Protocol):
    async def generate(self, message: str) -> str:
        """Generate a text response for a single user message."""
        ...
