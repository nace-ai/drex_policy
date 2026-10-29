dev:
	pip install -e ".[dev]"

lint:
	ruff check .

test:
	pytest ./tests

type:
	pyright drex_policy

qa:
	make lint
	make type
	make test
