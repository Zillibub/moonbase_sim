import json
from pathlib import Path
from typing import Callable
from dataclasses import dataclass


@dataclass
class Case:

    expected_method: Callable
    validation_method: Callable
    prompt: str
    expected_state: dict

    preparation_method: Callable = None
    initial_state: dict = None

    @classmethod
    def load(
            cls,
            expected_method: Callable,
            validation_method: Callable,
            prompt_path: str,
            expected_state_path: str,
    ):
        prompt = Path(prompt_path).read_text()
        with open(expected_state_path, 'r') as f:
            expected_state = json.load(f)
        return cls(
            expected_method=expected_method,
            validation_method=validation_method,
            prompt=prompt,
            expected_state=expected_state,
        )
