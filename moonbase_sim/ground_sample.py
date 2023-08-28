@dataclass
class GroundSample:
    """
    Class representing a ground sample.
    """
    sample_id: str
    location: str
    composition: str
    collected_at: str = datetime.datetime.now().isoformat()

    def collect_sample(self, location, composition):
        """
        Collects a ground sample.
        """
        self.location = location
        self.composition = composition

    def get_sample(self):
        """
        Returns the collected sample.
        """
        return {
            'sample_id': self.sample_id,
            'location': self.location,
            'composition': self.composition,
            'collected_at': self.collected_at
        }
