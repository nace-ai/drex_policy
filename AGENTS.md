# Notes for coding agents

This repo is `drex-policy`: one Guardrails validator, `DrexPolicy`, that asks Drex a `noul` or `score` question through `nace-sdk`. See [CONTRIBUTING.md](CONTRIBUTING.md) for the layout, setup and release steps.

## Rules

- Call Drex only through `nace-sdk`. Do not add another HTTP client or an LLM library.
- The default model is `drex-v2.0`. Pass other model ids through unchanged; `drex-latest` is not `drex-max`.
- Images are allowed only with `model="drex-max"`, at most 8. Raise `DrexPolicyError` before the call otherwise; never drop images.
- Tests use a fake Nace client. They must not need an API key or the network.
- Every package imported by `drex_policy/` is listed in `[project] dependencies`; test and lint tools go in the `dev` extra.
- Keys are listed in `.env.example` with no values. Never commit `.env`.
- Run `make qa` (ruff, pyright, pytest) before you push.
- The package directory stays `drex_policy/`. A top-level `validator` module from PyPI would collide with other validators.
- The code is MIT-licensed, copyright Nace.AI. Do not copy code into this repo from projects under other licenses.
