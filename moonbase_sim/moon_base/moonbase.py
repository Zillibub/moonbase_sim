import json
from typing import Tuple, List
from moon_base.sensor import Sensor
from moon_base.ground_sample import GroundSample
from moon_base.message import Message


class MoonBase:
    """
    Class representing the moon base.
    """
    def __init__(self, moon_base_id: str):
        self.moon_base_id = moon_base_id
        self.sensors = []
        self._ground_samples = []
        self.message_log = []

        self.is_landed = False
        self.landing_location = None

        self.carrying_capacity = 10  # kg

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

    def land(self, location: Tuple[int, int]):
        """
        Lands the moonbase at the specified location.
        :param location:
        :return:
        """
        self.is_landed = True
        self.landing_location = location

    def collect_ground_sample(self, sample: GroundSample):
        """
        Collects a ground sample.
        :param sample:
        ":raises: Exception if the moonbase has not landed
        :return:
        """
        if not self.is_landed:
            raise Exception('Cannot collect ground samples before landing')

        total_sample_weight = sum([sample.weight for sample in self._ground_samples])
        if total_sample_weight + sample.weight > self.carrying_capacity:
            raise Exception('Cannot collect ground sample. Moon base is at carrying capacity')
        self._ground_samples.append(sample)

    def send_samples(self) -> List[GroundSample]:
        """
        Sends the collected samples.
        :return:
        """
        samples = self._ground_samples
        self._ground_samples = []
        return samples

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
            'ground_samples': [sample.__dict__ for sample in self._ground_samples],
            'message_log': [message.__dict__ for message in self.message_log],
            'is_landed': self.is_landed,
            'landing_location': self.landing_location if self.landing_location else ''
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
        self.sensors = [Sensor.from_json(sensor) for sensor in state['sensors']]
        self._ground_samples = [GroundSample(**sample) for sample in state['ground_samples']]
        self.message_log = [Message(**message) for message in state['message_log']]
        self.is_landed = state['is_landed']
        self.landing_location = state['landing_location'] if state['landing_location'] else None