from unagent.agent import Unagent
from unagent.config import UnagentConfig


def test_respond_returns_friendly_text() -> None:
    agent = Unagent(config=UnagentConfig(history_size=5, persona="Friend mode."))
    response = agent.respond("help me with deployment")

    assert "Friend mode." in response
    assert "help me with deployment" in response


def test_respond_rejects_empty_message() -> None:
    agent = Unagent(config=UnagentConfig(history_size=5, persona="Persona"))

    try:
        agent.respond("   ")
        raised = False
    except ValueError:
        raised = True

    assert raised is True


def test_history_is_bounded() -> None:
    agent = Unagent(config=UnagentConfig(history_size=2, persona="Persona"))
    agent.respond("one")
    agent.respond("two")
    agent.respond("three")

    assert len(agent.memory.all()) == 2
