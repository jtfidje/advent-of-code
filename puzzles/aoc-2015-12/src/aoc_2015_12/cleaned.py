import json
from pathlib import Path
from typing import TypeGuard

from advent_of_code import utils
from aoc_2015_12 import DATA_PATH


def solve_1(path: Path):
    data = utils.read_data(path)
    return sum(utils.parse_integers(data, as_generator=True))


type JSONElement = list[int | str | list | dict] | dict[str, str | int | list | dict]


def solve_2(path: Path):
    def is_list_or_dict(obj: list | dict | int | str) -> TypeGuard[list | dict]:
        return isinstance(obj, list) or isinstance(obj, dict)

    def worker(obj: JSONElement) -> JSONElement:
        if isinstance(obj, list):
            for i, element in enumerate(obj):
                if is_list_or_dict(element):
                    obj[i] = worker(element)
        else:
            if "red" in obj.values():
                return {}

            for key, value in obj.items():
                if is_list_or_dict(value):
                    obj[key] = worker(value)

        return obj

    data_string = utils.read_data(path)
    data = json.loads(data_string)
    data = worker(data)
    data_string = json.dumps(data)

    return sum(utils.parse_integers(data_string, as_generator=True))


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
