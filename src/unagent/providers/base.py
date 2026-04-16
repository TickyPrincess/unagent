"""Provider contracts."""

from __future__ import annotations

from typing import Protocol

from unagent.memory import Message


class ResponseProvider(Protocol):
    """Protocol for provider adapters."""

    def generate(self, *, persona: str, messages: list[Message]) -> str:
        """Generate assistant text from full message history."""
        ...
