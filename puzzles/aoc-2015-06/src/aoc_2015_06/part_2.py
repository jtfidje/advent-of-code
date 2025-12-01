# flake8: noqa: F401

import re
from collections import defaultdict
from pathlib import Path

from advent_of_code import utils
from aoc_2015_06 import DATA_PATH


def solve(path: str | Path):
    grid = defaultdict(int)

    for line in utils.read_lines(path):
        x1, y1, x2, y2 = map(int, re.findall(r"(-?\d+)", line))

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                pos = (x, y)

                if line.startswith("turn on"):
                    grid[pos] += 1
                
                elif line.startswith("turn off"):
                    grid[pos] -= 1
                    grid[pos] = max(0, grid[pos])
                
                else:
                    grid[pos] += 2

    return sum(grid.values())


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
