import numpy as np
from typing import List
from moon_base.ground_sample import GroundSample
from field_laboratory.lab_ground_sample import LabGroundSample


class FieldLaboratory:
    """
    Class representing a field laboratory.
    Can recieve ground samples, analyze them
    """

    def __init__(
            self,
            field_lab_id: str,
            new_ground_samples: List[GroundSample] = None,
            analyzed_samples: List[LabGroundSample] = None,
            analysis_results: List[dict] = None
    ):
        """
        Class representing a field laboratory.
        :param field_lab_id: field laboratory id
        :param new_ground_samples:  a list of new ground samples
        :param analyzed_samples:  a list of analyzed ground samples
        :param analysis_results: a list of analysis results
        """
        self.field_lab_id = field_lab_id
        self.new_ground_samples = new_ground_samples or []
        self.analyzed_samples = analyzed_samples or []
        self.analysis_results = analysis_results or []
        self.message_log = []
        self.location = None

    def recieve_sample(self, sample: GroundSample):
        """
        Recieves a ground sample and adds it to the list of new ground samples.
        :param sample:
        :return:
        """
        self.new_ground_samples.append(sample)

    def calculate_density(self, sample: LabGroundSample):
        # Assume a constant mineral density of 3 g/cm^3
        mineral_density = 3
        return (1 - sample.porosity) * mineral_density

    def calculate_volume(self, sample: LabGroundSample):
        # Assume the rock is a sphere and calculate the volume
        volume = np.random.uniform(sample.weight / 3 * 0.8, sample.weight / 3 * 1.2)
        sample.volume = volume
        return volume

    @staticmethod
    def calculate_porosity(sample: LabGroundSample):
        location = sample.location
        # TODO think how to use location here
        _ = location[0] * location[1]
        porosity = np.random.uniform(0, 0.03)
        return porosity

    def analyze_sample(self, sample: LabGroundSample):
        """
        Analyzes a ground sample and adds the results to the list of analysis results.
        :param sample: The ground sample to be analyzed.
        :return: The results of the analysis.
        """

        # Calculate the porosity of the sample
        self.calculate_porosity(sample)

        # Calculate the volume of the sample
        self.calculate_volume(sample)

        # Calculate the density of the sample
        density = self.calculate_density(sample)
        sample.density = density

        # Add the analyzed sample to the list of analyzed samples
        self.analyzed_samples.append(sample)

        # Create the analysis results dictionary
        analysis_results = {
            'id': sample.sample_id,
            'location': sample.location,
            'weight': sample.weight,
            'porosity': sample.porosity,
            'volume': sample.volume,
            'density': sample.density
        }

        # Add the analysis results to the list of analysis results
        self.analysis_results.append(analysis_results)

        return analysis_results

    def analyze_samples(self, sample: GroundSample):
        mineral_compositions = [rock.mineral_composition for rock in sample]
        weights = [rock.weight for rock in sample]
        ages = [rock.age for rock in sample]
        porosities = [rock.porosity for rock in sample]
        densities = [rock.density for rock in sample]

        # Calculate the average, median, and standard deviation of the weights
        average_weight = sum(weights) / len(weights)
        median_weight = np.median(weights)
        std_dev_weight = np.std(weights)

        # Calculate the average, median, and standard deviation of the ages
        average_age = sum(ages) / len(ages)
        median_age = np.median(ages)
        std_dev_age = np.std(ages)

        # Calculate the average, median, and standard deviation of the porosities
        average_porosity = sum(porosities) / len(porosities)
        median_porosity = np.median(porosities)
        std_dev_porosity = np.std(porosities)

        # Calculate the average, median, and standard deviation of the densities
        average_density = sum(densities) / len(densities)
        median_density = np.median(densities)
        std_dev_density = np.std(densities)

        # Count the number of each mineral composition
        mineral_counts = {mineral: mineral_compositions.count(mineral) for mineral in set(mineral_compositions)}

        # Package the results into a dictionary
        results = {
            "mineral_counts": mineral_counts,
            "weight_stats": {
                "average": average_weight,
                "median": median_weight,
                "std_dev": std_dev_weight,
            },
            "age_stats": {
                "average": average_age,
                "median": median_age,
                "std_dev": std_dev_age,
            },
            "porosity_stats": {
                "average": average_porosity,
                "median": median_porosity,
                "std_dev": std_dev_porosity,
            },
            "density_stats": {
                "average": average_density,
                "median": median_density,
                "std_dev": std_dev_density,
            },
        }

        return results
