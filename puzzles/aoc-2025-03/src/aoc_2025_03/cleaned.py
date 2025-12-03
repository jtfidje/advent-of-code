import string
from pathlib import Path

from advent_of_code.utils import read_lines
from aoc_2025_03 import DATA_PATH

DIGITS = sorted(string.digits, reverse=True)


def worker(line: str, batteries: str, size: int) -> str:
    if not line:
        return ""

    for digit in DIGITS:
        for i, char in enumerate(line):
            if char == digit:
                batteries_ = batteries + char
                break
        else:
            continue

        if len(batteries_) == size:
            return batteries_

        batteries_ = worker(line[i + 1 :], batteries_, size)
        if not batteries_:
            continue

        return batteries_

    return ""


def solve_1(path: Path):
    data = read_lines(path)
    return sum(int(worker(line, "", 2)) for line in data)


def solve_2(path: Path):
    data = read_lines(path)
    return sum(int(worker(line, "", 12)) for line in data)


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
