from pathlib import Path

from advent_of_code import utils
from aoc_2025_04 import DATA_PATH

def solve_1(path: str | Path):
    data = utils.read_lines(path)

    result = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] != "@":
                    continue
            
            box = utils.get_adjacent(
                x, y, data, include_corners=True, return_values=True
            )
            result += box.count("@") < 4

    return result


def solve_2(path: str | Path):
    data = [list(line) for line in utils.read_lines(path)]

    result = 0
    repeat = True
    while repeat:
        repeat = False
        for x in range(0, len(data)):
            for y in range(0, len(data[0])):
                if data[x][y] != "@":
                    continue

                box = utils.get_adjacent(
                    x, y, data, include_corners=True, return_values=True
                )
                
                if box.count("@") < 4:
                    repeat = True
                    data[x][y] = "."
                    result += 1

    return result


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
