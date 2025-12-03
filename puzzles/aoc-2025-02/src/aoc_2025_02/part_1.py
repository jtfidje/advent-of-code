# flake8: noqa: F401

import re
import string
from pathlib import Path

from advent_of_code import utils
from aoc_2025_02 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_data(path)
    ranges = data.split(",")
    invalid_ids: list[int] = []

    for range_ in ranges:
        x, y = map(int, range_.split("-"))

        for i in range(x, y + 1):
            s = str(i)
            n = len(s) // 2
            x, y = s[n:], s[:n]

            if x == y:
                invalid_ids.append(i)
                continue

    return sum(invalid_ids)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
