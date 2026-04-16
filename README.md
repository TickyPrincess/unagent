# unagent

> Not an agent but a friend, coworker, and homie.

[![CI](https://github.com/your-username/unagent/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/unagent/actions/workflows/ci.yml)
[![CodeQL](https://github.com/your-username/unagent/actions/workflows/codeql.yml/badge.svg)](https://github.com/your-username/unagent/actions/workflows/codeql.yml)

`unagent` is a clean starter repository for a lightweight AI-style CLI assistant.
It includes a production-looking structure with CI, linting, typing, tests, and security automation.

## Features

- Friendly CLI persona
- Typed Python package (`src/` layout)
- Unit tests with coverage support
- Ruff + MyPy quality checks
- GitHub Actions for CI and CodeQL
- Dependabot + security policy

## Quick start

```bash
git clone https://github.com/your-username/unagent.git
cd unagent
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

Run checks:

```bash
make check
```

Run the CLI:

```bash
unagent "can you help me set up release notes?"
```

## Project layout

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   ├── dependabot.yml
│   └── pull_request_template.md
├── docs/
├── src/unagent/
├── tests/
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── README.md
├── SECURITY.md
└── pyproject.toml
```

## Roadmap

- Add provider adapters (OpenAI / local LLM / custom HTTP)
- Add streaming CLI mode
- Add memory backends (file/Redis)
- Add plugin hooks

## License

MIT
