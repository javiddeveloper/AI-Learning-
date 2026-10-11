import pytest

from main import ConversationStore, truncate_history


def test_conversation_store_keeps_messages_separate() -> None:
    store = ConversationStore()

    store.append("a", "user", "hello")
    store.append("b", "user", "world")

    assert store.get("a") == [{"role": "user", "content": "hello"}]
    assert store.get("b") == [{"role": "user", "content": "world"}]


def test_truncate_history_keeps_latest_messages() -> None:
    messages = [
        {"role": "user", "content": "1"},
        {"role": "assistant", "content": "2"},
        {"role": "user", "content": "3"},
    ]

    assert truncate_history(messages, 2) == messages[-2:]


def test_truncate_history_rejects_invalid_limit() -> None:
    with pytest.raises(ValueError):
        truncate_history([], 0)
