import datetime
from dataclasses import dataclass


@dataclass
class Sensor:
    """
    Class representing a sensor in the moonbase.
    """
    def __init__(self, sensor_id, sensor_type):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.data = []

    def collect_data(self, data):
        """
        Collects data from the sensor.
        """
        self.data.append({
            'timestamp': datetime.datetime.now().isoformat(),
            'data': data
        })

    def get_data(self):
        """
        Returns the collected data.
        """
        return self.data