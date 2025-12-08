# flake8: noqa: F401

import itertools
from pathlib import Path

from advent_of_code import utils
from aoc_2015_17 import DATA_PATH


def solve(path: str | Path, litres: int):
    data = sorted(utils.read_numbers(path), reverse=True)

    return sum(
        sum(containers) == litres
        for i in range(len(data))
        for containers in itertools.combinations(data, i)
    )


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt", litres=150)
    print(f"Problem 1: {answer}")
