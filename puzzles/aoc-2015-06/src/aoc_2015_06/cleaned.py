import re
from collections import defaultdict
from pathlib import Path

from advent_of_code.utils import read_lines
from aoc_2015_06 import DATA_PATH

pattern = r"(.+) (\d+),(\d+) through (\d+),(\d+)"

def solve_1(path: Path):
    grid = defaultdict(bool)

    for line in read_lines(path):
        op, *numbers = re.search(pattern, line).groups()  # type: ignore
        x1, y1, x2, y2 = map(int, numbers)

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                pos = (x, y)

                match op:
                    case "turn on":
                        grid[pos] = True
                    
                    case "turn off":
                        grid[pos] = False
                    
                    case "toggle":
                        grid[pos] = not grid[pos]

    return sum(grid.values())


def solve_2(path: Path):
    grid = defaultdict(int)

    for line in read_lines(path):
        op, *numbers = re.search(pattern, line).groups()  # type: ignore
        x1, y1, x2, y2 = map(int, numbers)

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                pos = (x, y)

                match op:
                    case "turn on":
                        grid[pos] += 1
                    
                    case "turn off":
                        grid[pos] = max(0, grid[pos] -1)
                    
                    case "toggle":
                        grid[pos] += 2

    return sum(grid.values())


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
