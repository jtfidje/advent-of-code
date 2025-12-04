# flake8: noqa: F401
from collections import Counter
from pathlib import Path

from advent_of_code import utils
from aoc_2025_04 import DATA_PATH

def print_grid(data):
    for row in data:
        print(" ".join(row))

def solve(path: str | Path):
    data = utils.read_lines(path)
    data = [list(line) for line in data]

    result = 0
    while True:
        to_remove = []
        for x in range(0, len(data)):
            for y in range(0, len(data[0])):
                if data[x][y] != "@":
                    continue

                box = utils.get_adjacent(x, y, data, include_corners=True)
                values = [data[x][y] for x, y in box]
                if Counter(values).get("@", 0) < 4:
                    to_remove.append((x, y))
                    result += 1
                
        
        if not to_remove:
            break
        
        for x, y in to_remove:
            data[x][y] = "x"


    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
