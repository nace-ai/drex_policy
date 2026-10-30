# Contributing to drex-policy

This repository holds the `DrexPolicy` Guardrails validator. It is published to PyPI as `drex-policy`, and the import is `from drex_policy import DrexPolicy`.

## Layout

- [drex_policy/main.py](drex_policy/main.py): the `DrexPolicy` validator and `DrexPolicyError`.
- [drex_policy/\_\_init\_\_.py](drex_policy/__init__.py): exports `DrexPolicy`.
- [tests/test_validator.py](tests/test_validator.py): tests that use a fake Nace client. They need no API key and make no network calls.

The package directory is `drex_policy`, not the template's `validator`. A top-level `validator` module installed from PyPI would collide with other validators built from the same template.

## Set up and test

1. Install the package and the dev tools with `make dev` (or `pip install -e ".[dev]"`). Python 3.10 or later is required.
2. Run `make qa`. It runs `ruff`, `pyright` and `pytest`.

To call Drex yourself, set the keys listed in [.env.example](.env.example). Do not commit a `.env` file.

## Release

1. Update `version` in [pyproject.toml](pyproject.toml).
2. Push a tag `v<version>`, for example `v0.1.0`.

The [publish workflow](.github/workflows/publish.yml) builds the package and publishes it to PyPI with Trusted Publishing. It fails if the tag does not match the version in `pyproject.toml`.
