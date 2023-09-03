import os
import subprocess
import pytest


def find_main_scripts(directory):
    """Find all cases in the given directory."""
    cases = []
    
    for root, dirs, files in os.walk(directory):
        for directory in dirs:
            if 'case' in directory:
                cases.append(os.path.join(root, directory))
    return cases


@pytest.mark.parametrize('case_folder', find_main_scripts('evaluation_cases/'))
def test_main_scripts(case_folder):
    """Test that each main.py script runs successfully."""
    if "preparation.py" in os.listdir(case_folder):
        preparation_script = os.path.join(case_folder, 'preparation.py')
        result = subprocess.run(['python', preparation_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        assert result.returncode == 0, f"Script {preparation_script} failed with error: {result.stderr.decode()}"
    main_script = os.path.join(case_folder, 'expected_code.py')
    result = subprocess.run(['python', main_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert result.returncode == 0, f"Script {main_script} failed with error: {result.stderr.decode()}"
