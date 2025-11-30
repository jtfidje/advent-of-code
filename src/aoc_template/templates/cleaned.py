from pathlib import Path

from __PKG__ import DATA_PATH

from advent_of_code.utils import read_lines


def solve_1(path: Path):
    data = read_lines(path)


def solve_2(path: Path):
    data = read_lines(path)


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
