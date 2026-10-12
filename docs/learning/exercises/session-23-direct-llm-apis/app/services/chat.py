from app.llm.client import LLMClient


class ChatService:
    def __init__(self, llm: LLMClient) -> None:
        self._llm = llm

    async def chat(self, message: str) -> str:
        return await self._llm.generate(message)
