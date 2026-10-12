from fastapi.testclient import TestClient

from app.api.deps import get_llm_client
from app.llm.mock import MockLLMClient
from app.main import create_app


def test_chat_returns_mock_response() -> None:
    app = create_app()
    app.dependency_overrides[get_llm_client] = MockLLMClient

    with TestClient(app) as client:
        response = client.post(
            "/chat",
            json={"message": "Explain RAG"},
        )

    assert response.status_code == 200
    assert response.json() == {"response": "Mock response to: Explain RAG"}


def test_chat_rejects_empty_message() -> None:
    app = create_app()
    app.dependency_overrides[get_llm_client] = MockLLMClient

    with TestClient(app) as client:
        response = client.post("/chat", json={"message": ""})

    assert response.status_code == 422
