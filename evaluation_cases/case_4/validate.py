def validate_state(state: dict, expected_state: dict):
    assert state['is_landed']
    assert len(state['ground_samples']) == len(expected_state['ground_samples'])
