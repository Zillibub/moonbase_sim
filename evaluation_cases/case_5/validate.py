from moon_base.moonbase import MoonBase


def validate_state(state: dict, expected_state: dict):
    moon_bases = [MoonBase.from_json(state) for state in state]
    moon_bases_expected = [MoonBase.from_json(state) for state in expected_state]

    for moon_base, moon_base_expected in zip(moon_bases, moon_bases_expected):
        assert len(moon_base._ground_samples) == len(moon_base_expected._ground_samples)
