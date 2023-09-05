import json
from moon_base.moonbase import MoonBase
from moon_base.ground_sample import GroundSample


def main(output_path: str = "expected_state.json"):

    with open("evaluation_cases/case_5/initial_state.json", "r") as f:
        data = json.load(f)

    moon_bases = []
    for state in data:
        moon_base = MoonBase.from_json(state)
        moon_bases.append(moon_base)
        if moon_base.is_landed:
            for i in range(3):
                moon_base.collect_ground_sample(GroundSample.create_random())

    with open(output_path, "w") as f:
        json.dump([x.to_json() for x in moon_bases], f, indent=4)


if __name__ == "__main__":
    main()
