from functools import lru_cache

from fastapi import Depends

from app.config import get_settings
from app.llm.client import LLMClient
from app.llm.openai_client import OpenAIClient
from app.services.chat import ChatService


@lru_cache
def get_llm_client() -> LLMClient:
    settings = get_settings()
    return OpenAIClient(settings)


def get_chat_service(
    llm: LLMClient = Depends(get_llm_client),
) -> ChatService:
    return ChatService(llm=llm)
