from pathlib import Path

from advent_of_code import utils
from aoc_2025_09 import DATA_PATH


@utils.performance_timer
def solve_1(path: Path):
    data = utils.read_lines(path)


@utils.performance_timer
def solve_2(path: Path):
    data = utils.read_lines(path)


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
    print()
    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
