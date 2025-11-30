# flake8: noqa: F401

from pathlib import Path

from __PKG__ import DATA_PATH

from advent_of_code import utils


def solve(path: str | Path):
    data = utils.read_lines(path)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
