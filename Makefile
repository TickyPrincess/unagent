.PHONY: format lint typecheck test check

format:
	ruff format .

lint:
	ruff check .

typecheck:
	mypy src

test:
	pytest --cov=unagent --cov-report=term-missing

check: lint typecheck test
