import openai
from evaluator.base_evaluator import BaseEvaluator


class GPTEvaluator(BaseEvaluator):

    def generate_code(self):

        case_prompt = self.load_prompt()

        prompt = f"""[PYTHON] {out} "[/PYTHON] 
        Generate code that will do {case_prompt}. The code must be executable. Always import all required modules.
        Always evaluate generated code. Do not write any tests. Always format generated code with ```python in the 
        beginning of the code block and with ``` in the end of generated code: 
        """
