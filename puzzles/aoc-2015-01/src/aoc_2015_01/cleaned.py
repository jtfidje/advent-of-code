from pathlib import Path

from advent_of_code.utils import read_data
from aoc_2015_01 import DATA_PATH


def solve_1(path: Path):
    return sum([1 if char == "(" else -1 for char in read_data(path)])


def solve_2(path: Path):
    data = read_data(path)
    floor = 0
    for pos, char in enumerate(data, start=1):
        match char:
            case "(":
                floor += 1
            case ")":
                floor -= 1

        if floor == -1:
            return pos


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
