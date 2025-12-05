# flake8: noqa: F401

import re
from pathlib import Path

from advent_of_code import utils
from aoc_2025_05 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_data(path)
    data = data.split("\n\n")

    all_ranges = sorted(
        map(lambda x: [int(x[0]), int(x[1])], re.findall(r"(\d+)-(\d+)", data[0])),
        key=lambda x: x[0],
    )

    ranges = [all_ranges[0]]
    for x, y in all_ranges[1:]:
        a, b = ranges[-1]
        if x > b:
            ranges.append([x, y])
            continue

        if x <= b and y > b:
            ranges[-1][1] = y
            continue

    return sum(len(range(x, y + 1)) for x, y in ranges)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
