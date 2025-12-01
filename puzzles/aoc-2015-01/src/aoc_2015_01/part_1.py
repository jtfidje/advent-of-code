# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2015_01 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_data(path)
    floor = 0
    for char in data:
        match char:
            case "(":
                floor += 1
            case ")":
                floor -= 1

    return floor


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
