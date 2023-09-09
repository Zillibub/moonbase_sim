import numpy as np
from moon_base.ground_sample import GroundSample
from moon_base.moon_base import MoonBase


def main(output_path: str = "expected_state.json"):

    moonbase = MoonBase("BASE-001")

    moonbase.land((np.random.uniform(0, 100), np.random.uniform(0, 100)))

    # Create 10 temperature sensors
    for i in range(10):
        ground_sample = GroundSample.create_random()
        moonbase.collect_ground_sample(ground_sample)

    moonbase.save_state(output_path)


if __name__ == "__main__":
    main()
