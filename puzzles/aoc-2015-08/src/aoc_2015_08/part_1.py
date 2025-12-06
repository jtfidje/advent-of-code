# flake8: noqa: F401
import re
from pathlib import Path

from advent_of_code import utils
from aoc_2015_08 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_lines(path)

    counter = 0

    for line in data:
        mem_str = line[1:-1]
        mem_str = mem_str.replace("\\\\", "X").replace('\\"', "X")
        mem_str = re.sub(r"\\x[\da-f]{2}", "X", mem_str)

        counter += len(line) - len(mem_str)

    return counter


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
