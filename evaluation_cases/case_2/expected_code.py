from moon_base.sensor import Sensor, SensorMetadata
from moon_base.moon_base import MoonBase
import random
from datetime import datetime, timedelta


def random_date(start_date, end_date):
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())))


def main(output_path: str = "expected_state.json"):

    moonbase = MoonBase("BASE-001")

    start_date = datetime(2021, 1, 1)
    end_date = datetime(2021, 12, 31)

    # Create 10 temperature sensors
    for i in range(1, 11):
        sensor = Sensor(
            sensor_id=f"TEMP-{i:0>3}",
            sensor_metadata=SensorMetadata(
                measured_value="Temperature",
                units="Celsius",
                type="Thermometer",
                calibration_date=random_date(start_date, end_date).strftime("%Y-%m-%d"),
                description=f"Temperature Sensor {i}"
            )
        )
        moonbase.add_sensor(sensor)

    # Create 10 magnetometers
    for i in range(1, 11):
        sensor = Sensor(
            sensor_id=f"MAG-{i:0>3}",
            sensor_metadata=SensorMetadata(
                measured_value="Magnetic Field",
                units="Tesla",
                type="Magnetometer",
                calibration_date=random_date(start_date, end_date).strftime("%Y-%m-%d"),
                description=f"Magnetometer Sensor {i}"
            )
        )
        moonbase.add_sensor(sensor)

    moonbase.save_state(output_path)


if __name__ == "__main__":
    main()
