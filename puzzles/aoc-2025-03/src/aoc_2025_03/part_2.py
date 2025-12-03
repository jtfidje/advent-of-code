# flake8: noqa: F401

import string
from pathlib import Path

from advent_of_code import utils
from aoc_2025_03 import DATA_PATH

def worker(line: str, batteries: str) -> str | None:
    if not line:
        return None
    
    for digit in sorted(string.digits, reverse=True):
        for i, char in enumerate(line):
            if char == digit:
                batteries_ = batteries + char
                break
        else:
            continue

        if len(batteries_) == 12:
            return batteries_

        res = worker(line[i + 1:], batteries_)
        if res is None:
            continue

        return res

    return None


def solve(path: str | Path):
    data = utils.read_lines(path)
    result = 0
    
    for line in data:
        res = worker(line, "")
        result += int(res)  # type: ignore

    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
