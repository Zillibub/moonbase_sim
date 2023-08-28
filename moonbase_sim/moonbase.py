import json
from moonbase_sim.sensor import Sensor
from moonbase_sim.ground_sample import GroundSample
from moonbase_sim.message import Message


class MoonBase:
    """
    Class representing the moon base.
    """
    def __init__(self, moon_base_id: str):
        self.moon_base_id = moon_base_id
        self.sensors = []
        self.ground_samples = []
        self.message_log = []
        self.is_landed = False

    def add_sensor(self, sensor):
        """
        Adds a sensor to the moonbase.
        :param sensor:
        :raises: Exception if the moonbase has already landed
        :return:
        """
        if self.is_landed:
            raise Exception('Cannot add sensors after landing')

        self.sensors.append(sensor)

    def collect_ground_sample(self, sample):
        """
        Collects a ground sample.
        :param sample:
        ":raises: Exception if the moonbase has not landed
        :return:
        """
        if not self.is_landed:
            raise Exception('Cannot collect ground samples before landing')
        self.ground_samples.append(sample)

    def send_message(self, message: Message):
        """
        Sends a message to Earth.
        :param message:
        :return:
        """
        self.message_log.append(message)

    def receive_message(self, message: Message):
        """
        Receives a message from Earth.
        :param message:
        :return:
        """
        self.message_log.append(message)

    def save_state(self, filename: str):
        """
        Saves the state of the moon base to a file.
        :param filename:
        :return:
        """
        state = {
            'sensors': [sensor.to_json() for sensor in self.sensors],
            'ground_samples': [sample.__dict__ for sample in self.ground_samples],
            'message_log': [message.__dict__ for message in self.message_log]
        }
        with open(filename, 'w') as f:
            json.dump(state, f, indent=4)

    def load_state(self, filename):
        """
        Loads the state of the moon base from a file.
        :param filename:
        :return:
        """
        with open(filename, 'r') as f:
            state = json.load(f)
        self.sensors = [Sensor(**sensor) for sensor in state['sensors']]
        self.ground_samples = [GroundSample(**sample) for sample in state['ground_samples']]
        self.message_log = [Message(**message) for message in state['message_log']]
