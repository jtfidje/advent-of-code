# flake8: noqa: F401

import re
from pathlib import Path

from advent_of_code import utils
from aoc_2025_05 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_data(path)
    data = data.split("\n\n")

    ranges = list(
        map(
            lambda x: range(int(x[0]), int(x[1]) + 1),
            re.findall(r"(\d+)-(\d+)", data[0]),
        )
    )

    fresh = {}
    for num in map(int, data[1].split()):
        for range_ in ranges:
            if num in range_:
                fresh[num] = None
                break

    return len(fresh)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
