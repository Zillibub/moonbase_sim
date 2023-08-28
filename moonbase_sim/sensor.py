@dataclass
class Sensor:
    """
    Class representing a sensor in the moonbase.
    """
    sensor_id: str
    sensor_type: str
    data: List[dict] = []

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