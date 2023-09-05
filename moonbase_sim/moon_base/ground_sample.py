import datetime
import numpy as np
from typing import Tuple
from uuid import uuid4
from dataclasses import dataclass


@dataclass
class GroundSample:
    """
    Class representing a ground sample.
    """
    sample_id: str
    location: Tuple[int, int]
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

    @classmethod
    def create_random(cls):
        return cls(
            sample_id=str(uuid4()),
            location=(np.random.uniform(0, 100), np.random.uniform(0, 100)),
            weight=np.random.uniform(0, 1)
        )
