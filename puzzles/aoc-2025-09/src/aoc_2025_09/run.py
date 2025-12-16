# flake8: noqa: F401

import itertools
from pathlib import Path

from advent_of_code import utils
from aoc_2025_09 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_line_numbers(path)
    counter = 0
    for i, X in enumerate(data[-1]):
        for Y in data[i + 1 :]:
            counter += 1

    print(counter)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
