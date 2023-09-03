from datetime import datetime


def validate_state(state: dict, expected_state: dict):
    date_threshold = datetime.strptime("2021-06-01", "%Y-%m-%d")

    # Check sensors
    assert len(state["sensors"]) == len(expected_state["sensors"]), "Number of sensors doesn't match."
    for sensor in state["sensors"]:
        datetime.strptime(sensor.sensor_metadata.calibration_date, "%Y-%m-%d")
        assert datetime.strptime(sensor["sensor_metadata"]["calibration_date"], "%Y-%m-%d") > date_threshold
