from evaluation_cases.case import Case
from evaluation_cases.case_1.expected_code import main as expected_method
from evaluation_cases.case_1.validate import validate_state as validation_method

case = Case.load(
    expected_method=expected_method,
    validation_method=validation_method,
    prompt_path="evaluation_cases/case_1/prompt",
    expected_state_path="evaluation_cases/case_1/expected_state.json",
)
