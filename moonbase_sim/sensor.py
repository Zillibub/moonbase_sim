class Sensor:
    def __init__(self, id, type, metadata):
        """
        Initialize a sensor with an id, type and metadata.
        """
        self.id = id
        self.type = type
        self.metadata = metadata

    def collect_data(self):
        """
        Collect data from the sensor. This will need to be implemented.
        """
        pass