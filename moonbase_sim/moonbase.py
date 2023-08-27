import json


class LunarBase:
    def __init__(self):
        """
        Initialize a lunar base with empty lists of sensors and ground samples.
        """
        self.sensors = []
        self.ground_samples = []

    def add_sensor(self, sensor):
        """
        Add a sensor to the lunar base.
        """
        self.sensors.append(sensor)

    def collect_ground_sample(self, ground_sample):
        """
        Collect a ground sample and add it to the lunar base.
        """
        self.ground_samples.append(ground_sample)

    def send_message(self, message):
        """
        Send a message to Earth. This will need to be implemented.
        """
        pass

    def receive_message(self):
        """
        Receive a message from Earth. This will need to be implemented.
        """
        pass

    def save(self, filename):
        """
        Save the state of the lunar base to a file.
        """
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f)

    def load(self, filename):
        """
        Load the state of the lunar base from a file.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        self.__dict__.update(data)
