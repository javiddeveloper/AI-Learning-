from functools import lru_cache
from typing import cast

from app.config import get_settings
from app.llm.client import LLMClient
from app.llm.openai_client import OpenAIClient
from app.services.chat import ChatService


@lru_cache
def get_llm_client() -> LLMClient:
    settings = get_settings()
    return OpenAIClient(settings)


def get_chat_service() -> ChatService:
    return ChatService(llm=cast(LLMClient, get_llm_client()))
