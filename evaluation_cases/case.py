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
            preparation_method: Callable = None,
            initial_state_path: str = None,
    ):
        prompt = Path(prompt_path).read_text()
        with open(expected_state_path, 'r') as f:
            expected_state = json.load(f)

        initial_state = None
        if initial_state_path:
            with open(initial_state_path, 'r') as f:
                initial_state = json.load(f)

        return cls(
            expected_method=expected_method,
            validation_method=validation_method,
            preparation_method=preparation_method,
            prompt=prompt,
            expected_state=expected_state,
            initial_state=initial_state,
        )

    def evaluate(self, output_path: str):
        if self.preparation_method:
            self.preparation_method()

        self.expected_method(output_path)

        with open(output_path, 'r') as f:
            state = json.load(f)

        self.validation_method(state, self.expected_state)
