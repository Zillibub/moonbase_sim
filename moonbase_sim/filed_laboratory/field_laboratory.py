from typing import List
from moon_base.ground_sample import GroundSample


class FieldLaboratory:

    def __init__(
            self,
            field_lab_id: str,
            ground_samples: List[GroundSample] = None,
            analysis_results: List[dict] = None
    ):
        self.field_lab_id = field_lab_id
        self.ground_samples = ground_samples or []
        self.analysis_results = analysis_results or []
        self.message_log = []
        self.location = None
