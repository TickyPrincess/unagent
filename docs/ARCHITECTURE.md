# Architecture

`unagent` follows a small layered design:

1. **CLI (`cli.py`)** — parses user input and prints responses.
2. **Core (`agent.py`)** — manages persona, history, and response flow.
3. **Memory (`memory.py`)** — bounded in-memory conversation history.
4. **Providers (`providers/`)** — pluggable response engines.

The default provider is deterministic and local, so the project works out of the box.
Real LLM providers can be added without changing the CLI contract.
