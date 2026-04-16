"""Conversation memory primitives."""

from __future__ import annotations

from collections import deque
from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Message:
    """Single message in a chat exchange."""

    role: str
    content: str


class ConversationMemory:
    """Bounded in-memory conversation history."""

    def __init__(self, max_messages: int) -> None:
        if max_messages <= 0:
            msg = "max_messages must be greater than zero"
            raise ValueError(msg)
        self._items: deque[Message] = deque(maxlen=max_messages)

    def add(self, role: str, content: str) -> None:
        content = content.strip()
        if not content:
            msg = "message content cannot be empty"
            raise ValueError(msg)
        self._items.append(Message(role=role, content=content))

    def extend(self, messages: Iterable[Message]) -> None:
        for message in messages:
            self.add(role=message.role, content=message.content)

    def all(self) -> list[Message]:
        return list(self._items)
