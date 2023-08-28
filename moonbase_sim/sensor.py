import datetime
from pydantic import BaseModel


class SensorMetadata(BaseModel):
    """
    Class representing the metadata of a sensor in the moonbase.
    """
    measured_value: str
    units: str
    type: str
    calibration_date: str
    description: str


class Sensor:
    """
    Class representing a sensor in the moonbase.
    """
    def __init__(self, sensor_id, sensor_metadata: SensorMetadata):
        self.sensor_id = sensor_id
        self.sensor_metadata = sensor_metadata
        self.data = []

    def collect_data(self, value):
        """
        Collects data from the sensor.
        """
        self.data.append({
            'timestamp': datetime.datetime.now().isoformat(),
            'value': value
        })

    def get_data(self):
        """
        Returns the collected data.
        """
        return self.data
