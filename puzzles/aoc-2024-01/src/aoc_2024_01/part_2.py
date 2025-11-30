# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2024_01 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_lines(path)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
