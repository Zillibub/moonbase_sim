from evaluation_cases.case import Case
from evaluation_cases.case_3.expected_code import main as expected_method
from evaluation_cases.case_3.validate import validate_state as validation_method
from evaluation_cases.case_3.preparation import main as preparation_method


def init_case():
    return Case.load(
        expected_method=expected_method,
        validation_method=validation_method,
        prompt_path="evaluation_cases/case_3/prompt",
        expected_state_path="evaluation_cases/case_3/expected_state.json",
        preparation_method=preparation_method,
        initial_state_path="evaluation_cases/case_3/initial_state.json"
    )
