# flake8: noqa: F401
import re
from collections import Counter
from pathlib import Path

from advent_of_code import utils
from aoc_2015_10 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_data(path)
    for _ in range(40):
        new_data = ""
        for match in re.finditer(r"(\d)\1*", data):
            group = match.group()
            new_data += str(len(group)) + group[0]
        data = new_data

    return len(data)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
