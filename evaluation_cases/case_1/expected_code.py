from moon_base.sensor import Sensor, SensorMetadata
from moon_base.moon_base import MoonBase
from moon_base.message import Message


def main(output_path: str = "expected_state.json"):
    moonbase = MoonBase("BASE-001")

    sensor1 = Sensor(
        sensor_id="TEMP-001",
        sensor_metadata=SensorMetadata(
            measured_value="Temperature",
            units="Celsius",
            type="Thermometer",
            calibration_date="2021-01-01",
            description="Measures the temperature"
        )
    )
    sensor2 = Sensor(
        sensor_id="MAG-001",
        sensor_metadata=SensorMetadata(
            measured_value="Magnetic Field",
            units="Tesla",
            type="Magnetometer",
            calibration_date="2021-01-01",
            description="Measures the magnetic field")
    )

    moonbase.add_sensor(sensor1)
    moonbase.add_sensor(sensor2)

    message = Message(content="Sensors added: Temperature Sensor, Magnetometer")
    moonbase.send_message(message)

    moonbase.save_state(output_path)


if __name__ == "__main__":
    main()
