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
    def __init__(self, sensor_id, sensor_metadata: SensorMetadata, data=None):
        self.sensor_id = sensor_id
        self.sensor_metadata = sensor_metadata
        self.data = data or []

    def collect_data(self, value: float):
        """
        Collects data from the sensor.
        :param value:
        :return:
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

    @classmethod
    def from_json(cls, json):
        return cls(
            sensor_id=json['sensor_id'],
            sensor_metadata=SensorMetadata(**json['sensor_metadata']),
            data=json['data']
        )

    def to_json(self):
        return {
            'sensor_id': self.sensor_id,
            'sensor_metadata': self.sensor_metadata.dict(),
            'data': self.data
        }
