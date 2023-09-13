import re
import subprocess
import threading
import queue
import importlib
from abc import abstractmethod
from pathlib import Path
from typing import Tuple


class BaseEvaluator:

    def __init__(
            self,
            output_path: Path,
            case_id: int,
            evaluation_cases_path: Path,
    ):
        self.output_path = output_path
        self.evaluation_cases_path = evaluation_cases_path
        self.case_id = case_id

    @staticmethod
    def save_code(
            sequence: str,
            output_path: Path,
            path_setup_code: str,
            code_stopwords: Tuple[str, str]
    ):
        # Find the text between [PYTHON] and [/PYTHON]
        search_result = re.search(
            f"{code_stopwords[0]}(.*?){code_stopwords[1]}",
            sequence,
            re.DOTALL
        )

        if not search_result:
            raise ValueError("No code found")
        code = search_result.group(1)
        code = path_setup_code + code
        # Save the code into a file
        with open(output_path, 'w') as f:
            f.write(code)

    def load_prompt(self):
        with open(self.evaluation_cases_path / f"case_{self.case_id}" / "prompt", 'r') as f:
            prompt = f.read()
        prompt = prompt.format(
            case_folder=str(self.evaluation_cases_path),
            output_path=str(self.output_path)
        )
        return prompt

    @abstractmethod
    def generate_code(self):
        raise NotImplementedError()

    @staticmethod
    def execute_code(executable_path: Path):
        def execute_code():
            try:
                subprocess.run(['python', executable_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                q.put(None)
            except subprocess.CalledProcessError as e:
                q.put(e.stderr.decode())

        q = queue.Queue()
        # Create a thread to execute the code
        t = threading.Thread(target=execute_code)

        # Start the thread
        t.start()

        # Get the result from the queue
        t.join()  # Ensure the thread has finished
        result = q.get()
        return result

    def validate(self, result_path: Path):
        with open(self.evaluation_cases_path / f"case_{self.case_id}" / "expected_state.json", 'r') as f:
            expected_state = f.read()
        with open(result_path, 'r') as f:
            state = f.read()

        validation_module = importlib.import_module(f"evaluation_cases.case_{self.case_id}.validate")
        validation_module.validate_state(state, expected_state)

        return False


