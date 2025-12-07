import re
from pathlib import Path

from advent_of_code import utils
from aoc_2015_16 import DATA_PATH

MESSAGE = {
    "children": "3",
    "cats": "7",
    "samoyeds": "2",
    "pomeranians": "3",
    "akitas": "0",
    "vizslas": "0",
    "goldfish": "5",
    "trees": "3",
    "cars": "2",
    "perfumes": "1",
}


@utils.performance_timer
def solve_1(path: Path):
    data = utils.read_lines(path)

    for i, line in enumerate(data, start=1):
        matches = re.findall(r"(\w+): (\d+)", line)

        for key, value in matches:
            if MESSAGE[key] != value:
                break
        else:
            return i


@utils.performance_timer
def solve_2(path: Path):
    data = utils.read_lines(path)

    for i, line in enumerate(data, start=1):
        matches = re.findall(r"(\w+): (\d+)", line)

        for key, value in matches:
            match key:
                case "cats" | "trees":
                    if value <= MESSAGE[key]:
                        break
                case "pomeranians" | "goldfish":
                    if value >= MESSAGE[key]:
                        break
                case _:
                    if MESSAGE[key] != value:
                        break
        else:
            return i


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
    print()
    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
