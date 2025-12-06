# flake8: noqa: F401
from collections import Counter
from pathlib import Path

from advent_of_code import utils
from aoc_2025_04 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_lines(path)
    data = [list(line) for line in data]

    result = 0
    for x in range(0, len(data)):
        for y in range(0, len(data[0])):
            box = utils.get_adjacent(x, y, data, include_corners=True)
            values = [data[x][y] for x, y in box]
            result += Counter(values).get("@", 0) < 4 and data[x][y] == "@"

    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
