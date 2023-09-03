def validate_state(state: dict, expected_state: dict):

    # Check moon base id
    assert state["moon_base_id"] == expected_state["moon_base_id"], "Moon base id doesn't match."

    # Check sensors
    assert len(state["sensors"]) == len(expected_state["sensors"]), "Number of sensors doesn't match."
    for sensor, expected_sensor in zip(state["sensors"], expected_state["sensors"]):
        assert sensor["sensor_id"] == expected_sensor["sensor_id"], "Sensor id doesn't match."
        assert sensor["sensor_metadata"]["measured_value"] == expected_sensor["sensor_metadata"]["measured_value"], "Sensor metadata doesn't match."
        assert sensor["data"] == expected_sensor["data"], "Sensor data doesn't match."

    # Check message log
    assert len(state["message_log"]) == len(expected_state["message_log"]), "Number of messages doesn't match."
    for message, expected_message in zip(state["message_log"], expected_state["message_log"]):
        assert message.content == expected_message["content"], "Message content doesn't match."
