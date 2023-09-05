from datetime import datetime


def validate_state(state: dict, expected_state: dict):
    date_threshold = datetime.strptime("2021-06-01", "%Y-%m-%d")

    # Check sensors
    assert len(state["sensors"]) == len(expected_state["sensors"]), "Number of sensors doesn't match."
    assert expected_state['message_log'][-1]['content'] in state['message_log'][-1]['content'], "Message content doesn't match."
