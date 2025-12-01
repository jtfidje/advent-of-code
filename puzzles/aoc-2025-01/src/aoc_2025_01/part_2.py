# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2025_01 import DATA_PATH


def solve(path: str | Path):
    with open(path, "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    dial = 50
    counter = 0
    for line in data:
        match line[0]:
            case "R":
                number = int(line[1:])

                x = (dial + number) // 100

                counter += x

                dial = (dial + number) % 100
            case "L":
                number = int(line[1:])

                x = (((dial - number) * -1) + 100) // 100

                if dial == 0 and number > 0:
                    x -= 1

                counter += x

                dial = (dial - number) % 100

    return counter


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
