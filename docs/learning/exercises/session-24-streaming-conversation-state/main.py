from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI(title="Session 24 - Streaming & Conversation State")


class ConversationStore:
    def __init__(self) -> None:
        self._messages: dict[str, list[dict[str, str]]] = {}

    def get(self, conversation_id: str) -> list[dict[str, str]]:
        return list(self._messages.get(conversation_id, []))

    def append(self, conversation_id: str, role: str, content: str) -> None:
        self._messages.setdefault(conversation_id, []).append(
            {"role": role, "content": content}
        )


def truncate_history(
    messages: list[dict[str, str]],
    max_messages: int,
) -> list[dict[str, str]]:
    if max_messages < 1:
        raise ValueError("max_messages must be greater than zero")

    return messages[-max_messages:]


class MockLLMClient:
    async def stream(self, messages: list[dict[str, str]]) -> AsyncIterator[str]:
        user_message = messages[-1]["content"]

        for chunk in [f"Echo: {user_message[:8]}", user_message[8:]]:
            if chunk:
                yield chunk


store = ConversationStore()
llm = MockLLMClient()


async def generate_sse(
    conversation_id: str,
    user_message: str,
) -> AsyncIterator[str]:
    store.append(conversation_id, "user", user_message)

    history = truncate_history(
        store.get(conversation_id),
        max_messages=20,
    )

    full_response = ""

    async for chunk in llm.stream(history):
        full_response += chunk
        yield f"data: {chunk}\\n\\n"

    store.append(conversation_id, "assistant", full_response)
    yield "data: [DONE]\\n\\n"


@app.get("/chat/{conversation_id}")
async def chat(conversation_id: str, message: str) -> StreamingResponse:
    return StreamingResponse(
        generate_sse(conversation_id, message),
        media_type="text/event-stream",
    )
