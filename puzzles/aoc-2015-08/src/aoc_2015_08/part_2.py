# flake8: noqa: F401
import re
from pathlib import Path

from advent_of_code import utils
from aoc_2015_08 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_lines(path)

    counter = 0

    for line in data:
        mem_str = line.replace('"', "__Q__").replace("\\", "__B__")
        mem_str = re.sub(r"(\\x[\da-f]{2})", "\\\1", mem_str)

        mem_str = mem_str.replace("__Q__", '\\"').replace("__B__", "\\\\")

        mem_str = f'"{mem_str}"'

        counter += len(mem_str) - len(line)

    return counter


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
