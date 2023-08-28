import json


class MoonBase:
    """
    Class representing the moonbase.
    """
    def __init__(self):
        self.sensors = []
        self.ground_samples = []
        self.message_log = []
        self.is_landed = False

    def add_sensor(self, sensor):
        """
        Adds a sensor to the moonbase.
        """
        self.sensors.append(sensor)

    def collect_ground_sample(self, sample):
        """
        Collects a ground sample.
        """
        self.ground_samples.append(sample)

    def send_message(self, message):
        """
        Sends a message to Earth.
        """
        self.message_log.append(message)

    def receive_message(self, message):
        """
        Receives a message from Earth.
        """
        self.message_log.append(message)

    def save_state(self, filename):
        """
        Saves the state of the moonbase to a file.
        """
        state = {
            'sensors': [sensor.__dict__ for sensor in self.sensors],
            'ground_samples': [sample.__dict__ for sample in self.ground_samples],
            'message_log': [message.__dict__ for message in self.message_log]
        }
        with open(filename, 'w') as f:
            json.dump(state, f)

    def load_state(self, filename):
        """
        Loads the state of the moonbase from a file.
        """
        with open(filename, 'r') as f:
            state = json.load(f)
        self.sensors = [Sensor(**sensor) for sensor in state['sensors']]
        self.ground_samples = [GroundSample(**sample) for sample in state['ground_samples']]
        self.message_log = [Message(**message) for message in state['message_log']]