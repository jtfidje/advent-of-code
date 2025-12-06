# flake8: noqa: F401
import json
import re

from pathlib import Path
from typing import TypeGuard

from advent_of_code import utils
from aoc_2015_12 import DATA_PATH

type JSONElement = list[int | str | list | dict] | dict[str, str | int | list | dict]

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


def solve(path: str | Path):
    data_string = utils.read_data(path)
    data = json.loads(data_string)
    data = worker(data)

    data_string = json.dumps(data)

    return sum(map(int, re.findall(r"(-?\d+)", data_string)))



if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
