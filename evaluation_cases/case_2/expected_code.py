from moonbase_sim.sensor import Sensor, SensorMetadata
from moonbase_sim.moonbase import MoonBase
import random
from datetime import datetime, timedelta

moonbase = MoonBase("BASE-001")

start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)


def random_date(start_date, end_date):
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())))


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
            description=f"Magnetometer {i}"
        )
    )
    moonbase.add_sensor(sensor)
