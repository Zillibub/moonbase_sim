from datetime import datetime
from moon_base.moon_base import MoonBase
from moon_base.message import Message


def main(output_path: str = "expected_state.json"):

    # Load the moon base instance from initial_state.json file
    moonbase = MoonBase.load_state("evaluation_cases/case_3/initial_state.json")

    # Get a list of sensor ids which calibration date is more than 2021.06.01
    date_threshold = datetime.strptime("2021-06-01", "%Y-%m-%d")
    sensor_ids = [
        sensor.sensor_id for sensor in moonbase.sensors
        if datetime.strptime(sensor.sensor_metadata.calibration_date, "%Y-%m-%d") > date_threshold
    ]

    # Send a message with a list of sensor ids to the earth
    message = Message(content=str(sensor_ids))
    moonbase.send_message(message)
    moonbase.save_state(output_path)


if __name__ == "__main__":
    main()
