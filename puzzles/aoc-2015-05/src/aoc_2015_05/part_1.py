# flake8: noqa: F401

import re
import string
from pathlib import Path

from advent_of_code import utils
from aoc_2015_05 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_lines(path)

    vowel_pattern = r"[aeiou]"
    double_pattern = "|".join([f"{char}{{2,}}" for char in string.ascii_lowercase])
    negative_pattern = r"(ab)|(cd)|(pq)|(xy)"

    count = 0

    for line in data:
        res = re.findall(vowel_pattern, line)
        if len(res) < 3:
            continue

        res = re.search(double_pattern, line)
        if res is None:
            continue

        res = re.search(negative_pattern, line)
        if res is not None:
            continue

        count += 1

    return count


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
