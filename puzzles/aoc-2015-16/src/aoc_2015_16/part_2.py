# flake8: noqa: F401

import re
from pathlib import Path

from advent_of_code import utils
from aoc_2015_16 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_lines(path)

    message = {
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

    for i, line in enumerate(data, start=1):
        matches = re.findall(r"(\w+): (\d+)", line)

        for key, value in matches:
            match key:
                case "cats" | "trees":
                    if value <= message[key]:
                        break
                case "pomeranians" | "goldfish":
                    if value >= message[key]:
                        break
                case _:
                    if message[key] != value:
                        break
        else:
            return i

    return 0


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
