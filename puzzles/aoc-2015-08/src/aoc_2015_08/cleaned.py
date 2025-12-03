import re
from pathlib import Path

from advent_of_code.utils import read_lines
from aoc_2015_08 import DATA_PATH


def solve_1(path: Path):
    data = read_lines(path)

    counter = 0
    for line in data:
        mem_str = re.sub(r"(\\x[\da-f]{2}|\\\\|\\\")", "_", line[1:-1])
        counter += len(line) - len(mem_str)

    return counter


def solve_2(path: Path):
    data = read_lines(path)
    return sum(len(re.findall(r"\\|\"", line)) + 2 for line in data)


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
