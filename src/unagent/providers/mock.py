"""Local deterministic provider used by default."""

from __future__ import annotations

from unagent.memory import Message


class MockProvider:
    """Simple provider with friendly deterministic responses."""

    def generate(self, *, persona: str, messages: list[Message]) -> str:
        latest_user_message = ""
        for message in reversed(messages):
            if message.role == "user":
                latest_user_message = message.content
                break

        if not latest_user_message:
            return "I am here. Tell me what you need."

        return f"{persona} Got it: {latest_user_message}"
