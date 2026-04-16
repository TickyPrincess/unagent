"""Runtime configuration for Unagent."""

from __future__ import annotations

import os
from dataclasses import dataclass

DEFAULT_HISTORY_SIZE = 10
DEFAULT_PERSONA = "Not an agent but a friend, coworker, and homie."


@dataclass(frozen=True, slots=True)
class UnagentConfig:
    """Configuration used by the Unagent core."""

    history_size: int = DEFAULT_HISTORY_SIZE
    persona: str = DEFAULT_PERSONA

    @classmethod
    def from_env(cls) -> UnagentConfig:
        """Build config from environment variables."""
        history_size_raw = os.getenv("UNAGENT_HISTORY_SIZE", str(DEFAULT_HISTORY_SIZE))
        persona = os.getenv("UNAGENT_PERSONA", DEFAULT_PERSONA)

        history_size = int(history_size_raw)
        if history_size <= 0:
            msg = "UNAGENT_HISTORY_SIZE must be greater than zero"
            raise ValueError(msg)

        persona = persona.strip()
        if not persona:
            msg = "UNAGENT_PERSONA cannot be empty"
            raise ValueError(msg)

        return cls(history_size=history_size, persona=persona)
