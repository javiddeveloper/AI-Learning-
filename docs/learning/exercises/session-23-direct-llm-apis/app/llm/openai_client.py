from openai import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AsyncOpenAI,
    AuthenticationError,
    RateLimitError,
)

from app.config import Settings
from app.llm.errors import (
    LLMAuthenticationError,
    LLMProviderError,
    LLMRateLimitError,
    LLMTimeoutError,
)


class OpenAIClient:
    def __init__(self, settings: Settings) -> None:
        if not settings.openai_api_key:
            raise ValueError(
                "OPENAI_API_KEY is required when the OpenAI provider is selected."
            )

        self._model = settings.openai_model
        self._client = AsyncOpenAI(
            api_key=settings.openai_api_key,
            timeout=settings.openai_timeout_seconds,
            max_retries=0,
        )

    async def generate(self, message: str) -> str:
        try:
            response = await self._client.responses.create(
                model=self._model,
                input=message,
            )
            return response.output_text
        except RateLimitError as exc:
            raise LLMRateLimitError("The LLM provider rate limit was reached.") from exc
        except AuthenticationError as exc:
            raise LLMAuthenticationError("The LLM provider rejected its credentials.") from exc
        except APITimeoutError as exc:
            raise LLMTimeoutError("The LLM provider request timed out.") from exc
        except (APIConnectionError, APIStatusError) as exc:
            raise LLMProviderError("The LLM provider request failed.") from exc

    async def close(self) -> None:
        await self._client.close()
