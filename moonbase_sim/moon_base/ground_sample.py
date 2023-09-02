import datetime
from dataclasses import dataclass


@dataclass
class GroundSample:
    """
    Class representing a ground sample.
    """
    sample_id: str
    location: str
    weight: float
    collected_at: str = datetime.datetime.now().isoformat()

    def get_sample(self):
        """
        Returns the collected sample.
        """
        return {
            'sample_id': self.sample_id,
            'location': self.location,
            'collected_at': self.collected_at
        }
