# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2015_03 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_data(path)

    pos = (0, 0)
    houses = {pos: None}
    for char in data:
        x, y = pos
        match char:
            case "<":
                pos = (x - 1, y)
            case ">":
                pos = (x + 1, y)
            case "^":
                pos = (x, y + 1)
            case "v":
                pos = (x, y - 1)

        houses[pos] = None

    return len(houses)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
