import os
import pytest
from evaluation_cases import cases
from evaluation_cases.case import Case
from tempfile import TemporaryDirectory


@pytest.mark.parametrize('validate_case', cases)
def test_main_scripts(validate_case: Case):
    with TemporaryDirectory() as temp_dir:
        file_path = "state.json"
        temp = os.path.join(temp_dir, file_path)
        validate_case.evaluate(temp)

