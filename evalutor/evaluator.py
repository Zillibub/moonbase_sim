import re
from pathlib import Path


class BaseEvaluator:

    def __init__(self, output_path: str, case_id: int):
        self.output_path = output_path
        self.case_id = case_id

    @property
    

    def save_code(self, sequence: str, output_path: Path, path_setup_code: str):
        # Find the text between [PYTHON] and [/PYTHON]
        search_result = re.search("```python(.*?)```", sequence, re.DOTALL)
        if not search_result:
            raise ValueError("No python code found")
        code = search_result.group(1)
        code = path_setup_code + code
        # Save the code into a file
        with open(output_path, 'w') as f:
            f.write(code)

   def evaluate(self):
