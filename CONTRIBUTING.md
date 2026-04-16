# Contributing

Thanks for helping improve `unagent`.

## Development setup

1. Fork and clone the repository.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -e .[dev]
```

## Quality gates

Before opening a PR, run:

```bash
make check
```

That runs:

- Ruff lint
- MyPy type checks
- Pytest suite

## Pull requests

- Keep PRs focused.
- Add/adjust tests for behavior changes.
- Update docs if behavior or public API changes.
- Fill the PR template.
