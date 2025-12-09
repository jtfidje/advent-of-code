# flake8: noqa: F401

import itertools
from pathlib import Path

from advent_of_code import utils
from aoc_2025_09 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_line_numbers(path)

    best = 0
    for X, A in itertools.combinations(data, 2):
        x, y = X
        (
            a,
            b,
        ) = A

        best = max(best, ((abs(a - x) + 1) * (abs(b - y) + 1)))

    return best


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
