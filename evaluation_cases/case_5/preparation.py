import json
import numpy as np
from moon_base.moon_base import MoonBase


def main():
    moonbases = [MoonBase(f"BASE-{i:0>3}") for i in range(5)]

    landed_ids = [1, 2, 4]
    for i in landed_ids:
        moonbases[i].land((np.random.uniform(0, 100), np.random.uniform(0, 100)))

    data = [x.to_json() for x in moonbases]

    with open("initial_state.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
