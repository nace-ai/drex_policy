"""Runs every Python block in the README against the installed package.

Drex is replaced by a fake client, so no API key or network is needed.
"""

import json
import re
import runpy
from pathlib import Path

import pytest
from nace_sdk import Noul, SystemOneResponse

README = Path(__file__).resolve().parent.parent / "README.md"
BLOCKS = re.findall(r"```python\n(.*?)```", README.read_text(), re.DOTALL)


class FakeNaceClient:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def system_one(self, state, questions, *, model=None, images=None):
        question = questions["policy"]
        if isinstance(question, Noul):
            answer = {"type": "noul", "noul": 0.9 if "+1 415" in state else 0.1}
        else:
            answer = {
                "type": "score",
                "score": 0.5,
                "confidence": 0.8,
                "legend": ["safe", "borderline", "unsafe"],
                "probabilities": {"0": 0.6, "1": 0.3, "2": 0.1},
            }
        return SystemOneResponse.model_validate_json(
            json.dumps(
                {
                    "model": model,
                    "usage": {"input_tokens": 4, "image_tokens": 0, "output_tokens": 1},
                    "answers": {"policy": answer},
                }
            )
        )


def test_readme_has_python_blocks():
    assert len(BLOCKS) >= 4


@pytest.mark.parametrize("block", BLOCKS)
def test_readme_block_runs(block, monkeypatch, tmp_path):
    assert "guardrails.hub" not in block
    monkeypatch.setattr("drex_policy.main.NaceClient", FakeNaceClient)
    script = tmp_path / "example.py"
    script.write_text(block)
    if "+1 415 555 0100" in block:
        # The first example ends with a call that must fail.
        with pytest.raises(Exception, match="Validation failed"):
            runpy.run_path(str(script))
    else:
        runpy.run_path(str(script))
