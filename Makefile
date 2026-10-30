.PHONY: dev lint type test qa

# Editable install with ruff, pyright and pytest.
dev:
	python -m pip install -e ".[dev]"

lint:
	ruff check drex_policy tests

type:
	pyright

test:
	pytest

# Everything CI runs.
qa: lint type test
