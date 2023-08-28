from datetime import datetime
from moonbase_sim.moonbase import MoonBase
from moonbase_sim.message import Message


def main():

    # Load the moon base instance from initial_state.json file
    moonbase = MoonBase("BASE-001")
    moonbase.load_state("initial_state.json")

    # Get a list of sensor ids which calibration date is more than 2021.06.01
    date_threshold = datetime.strptime("2021-06-01", "%Y-%m-%d")
    sensor_ids = [
        sensor.sensor_id for sensor in moonbase.sensors
        if datetime.strptime(sensor.sensor_metadata.calibration_date, "%Y-%m-%d") > date_threshold
    ]

    # Send a message with a list of sensor ids to the earth
    message = Message(content=str(sensor_ids))
    moonbase.send_message(message)
    moonbase.save_state("expected_state.json")


if __name__ == "__main__":
    main()