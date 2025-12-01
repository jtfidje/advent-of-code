# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2015_02 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_all_numbers(path)

    result = 0
    for l, w, h in data:  # noqa: E741
        areas = [l * w, w * h, h * l]

        result += sum(map(lambda x: x * 2, areas))
        result += min(areas)

    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
