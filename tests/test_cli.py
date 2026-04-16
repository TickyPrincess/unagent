from unagent.cli import main


def test_cli_runs_and_prints_response(capsys) -> None:  # type: ignore[no-untyped-def]
    exit_code = main(["hello", "team"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "hello team" in output


def test_cli_returns_non_zero_on_empty_input(capsys) -> None:  # type: ignore[no-untyped-def]
    exit_code = main([])
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "usage:" in output
