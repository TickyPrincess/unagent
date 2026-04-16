import pytest

from unagent.config import UnagentConfig


def test_from_env_reads_custom_values(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("UNAGENT_HISTORY_SIZE", "12")
    monkeypatch.setenv("UNAGENT_PERSONA", "custom persona")

    cfg = UnagentConfig.from_env()

    assert cfg.history_size == 12
    assert cfg.persona == "custom persona"


def test_from_env_rejects_invalid_history(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("UNAGENT_HISTORY_SIZE", "0")

    with pytest.raises(ValueError):
        UnagentConfig.from_env()


def test_from_env_defaults_when_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("UNAGENT_HISTORY_SIZE", raising=False)
    monkeypatch.delenv("UNAGENT_PERSONA", raising=False)

    cfg = UnagentConfig.from_env()

    assert cfg == UnagentConfig()


def test_from_env_rejects_empty_persona(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("UNAGENT_PERSONA", "  ")

    with pytest.raises(ValueError):
        UnagentConfig.from_env()
