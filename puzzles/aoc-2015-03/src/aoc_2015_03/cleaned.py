from pathlib import Path

from advent_of_code.utils import read_data
from aoc_2015_03 import DATA_PATH


def solve_1(path: Path):
    pos = (0, 0)
    houses = {pos: None}
    for direction in read_data(path):
        x, y = pos
        match direction:
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


def solve_2(path: Path):
    santa = [(0, 0), (0, 0)]
    houses = {(0, 0): None}

    for i, char in enumerate(read_data(path)):
        x, y = santa[i % 2]

        match char:
            case "<":
                pos = (x - 1, y)
            case ">":
                pos = (x + 1, y)
            case "^":
                pos = (x, y + 1)
            case "v":
                pos = (x, y - 1)

        santa[i % 2] = pos

        houses[pos] = None

    return len(houses)


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
