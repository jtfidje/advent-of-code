# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2015_02 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_all_numbers(path)

    result = 0
    for line in data:
        line.sort()
        x, y, z = line

        result += (x * 2) + (y * 2)
        result += x * y * z

    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
