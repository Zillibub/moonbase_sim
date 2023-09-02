from moon_base.sensor import Sensor, SensorMetadata
from moon_base.moonbase import MoonBase


def main():
    dates = [
        "2021-02-17", "2021-07-15", "2021-09-11", "2021-05-02", "2021-03-29",
        "2021-04-07", "2021-01-23", "2021-11-01", "2021-08-16", "2021-11-09",
        "2021-07-22", "2021-04-08", "2021-02-03", "2021-03-12", "2021-08-24",
        "2021-11-26", "2021-09-13", "2021-05-19", "2021-10-06", "2021-12-21"
    ]

    moonbase = MoonBase("BASE-001")

    # Create 10 temperature sensors
    for i in range(1, 11):
        sensor = Sensor(
            sensor_id=f"TEMP-{i:0>3}",
            sensor_metadata=SensorMetadata(
                measured_value="Temperature",
                units="Celsius",
                type="Thermometer",
                calibration_date=dates[i - 1],
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
                calibration_date=dates[i + 9],
                description=f"Magnetometer Sensor {i}"
            )
        )
        moonbase.add_sensor(sensor)

    moonbase.save_state("initial_state.json")


if __name__ == "__main__":
    main()
