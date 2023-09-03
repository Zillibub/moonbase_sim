import os
import subprocess
import pytest
from evaluation_cases import cases


@pytest.mark.parametrize('validate_cases', cases)
def test_main_scripts(validate_cases):
    """Test that each main.py script runs successfully."""
    if "preparation.py" in os.listdir(case_folder):
        preparation_script = os.path.join(case_folder, 'preparation.py')
        result = subprocess.run(['python', preparation_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        assert result.returncode == 0, f"Script {preparation_script} failed with error: {result.stderr.decode()}"
    main_script = os.path.join(case_folder, 'expected_code.py')
    result = subprocess.run(['python', main_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert result.returncode == 0, f"Script {main_script} failed with error: {result.stderr.decode()}"
