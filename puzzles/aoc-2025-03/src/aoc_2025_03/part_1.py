# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2025_03 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_lines(path)
    result = 0
    for line in data:
        max_ = 0
        for i in range(len(line)-1):
            for j in range(i + 1, len(line)):
                n = int(line[i] + line[j])
                max_ = max(max_, n)

        result += max_

    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
