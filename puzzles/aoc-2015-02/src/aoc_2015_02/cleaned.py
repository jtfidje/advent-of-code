from pathlib import Path

from advent_of_code import utils
from aoc_2015_02 import DATA_PATH


def solve_1(path: Path):
    result = 0
    for l, w, h in utils.read_line_numbers(path):  # noqa: E741
        areas = [l * w, w * h, h * l]

        result += sum(map(lambda x: x * 2, areas)) + min(areas)

    return result


def solve_2(path: Path):
    result = 0
    for line in utils.read_line_numbers(path):
        x, y, z = sorted(line)

        result += (x * 2) + (y * 2) + (x * y * z)

    return result


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
