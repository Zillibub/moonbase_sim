import datetime
from typing import Dict, Tuple
from dataclasses import dataclass


@dataclass
class LabGroundSample:
    """
    Class representing a ground sample with its properties.
    """
    sample_id: str
    location: Tuple[float, float]
    weight: float
    collected_at: str

    volume: float = None
    density: float = None
    porosity: float = None
    composition: Dict[str, float] = None
    is_processed: bool = False
