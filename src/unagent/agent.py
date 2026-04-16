"""Core Unagent orchestration."""

from __future__ import annotations

from unagent.config import UnagentConfig
from unagent.memory import ConversationMemory
from unagent.providers.base import ResponseProvider
from unagent.providers.mock import MockProvider


class Unagent:
    """Lightweight chat orchestrator."""

    def __init__(
        self,
        config: UnagentConfig | None = None,
        provider: ResponseProvider | None = None,
    ) -> None:
        self.config = config or UnagentConfig.from_env()
        self.provider = provider or MockProvider()
        self.memory = ConversationMemory(max_messages=self.config.history_size)

    def respond(self, message: str) -> str:
        """Generate a response and store conversation context."""
        message = message.strip()
        if not message:
            msg = "message cannot be empty"
            raise ValueError(msg)

        self.memory.add(role="user", content=message)
        response = self.provider.generate(persona=self.config.persona, messages=self.memory.all())
        self.memory.add(role="assistant", content=response)
        return response
