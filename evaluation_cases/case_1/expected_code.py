from moonbase_sim.sensor import Sensor, SensorMetadata
from moonbase_sim.moonbase import MoonBase
from moonbase_sim.message import Message


def main():
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


if __name__ == "__main__":
    main()
