import numpy as np
from typing import List
from moon_base.ground_sample import GroundSample


class FieldLaboratory:
    """
    Class representing a field laboratory.
    Can recieve ground samples, analyze them
    """

    def __init__(
            self,
            field_lab_id: str,
            new_ground_samples: List[GroundSample] = None,
            analyzed_samples: List[GroundSample] = None,
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

    def calculate_density(self, sample: GroundSample, porosity):
        # Assume a constant mineral density of 3 g/cm^3
        mineral_density = 3
        return (1 - porosity) * mineral_density

    def calculate_volume(self, sample: GroundSample):
        # Assume the rock is a sphere and calculate the volume
        diameter = (self.weight / self.density)**(1/3)  # diameter in cm
        return 4/3 * math.pi * (diameter/2)**3

    def calculate_mass(self, sample: GroundSample):
        # Convert density from g/cm^3 to kg/m^3 and volume from cm^3 to m^3
        density_kg_m3 = self.density * 1000
        volume_m3 = self.volume * 1e-6
        return density_kg_m3 * volume_m3

    def calculate_force(self):
        # Assume the rock is at the surface of the moon and calculate the gravitational force it would exert on a 1 kg object
        G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
        mass_object = 1  # mass of the object in kg
        distance = 1  # distance from the rock to the object in m
        return G * (self.mass * mass_object) / distance**2

    def analyze_sample(self, sample: GroundSample):
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
