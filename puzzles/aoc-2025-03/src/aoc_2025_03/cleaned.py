from pathlib import Path

from advent_of_code import utils
from aoc_2025_03 import DATA_PATH


def worker(line: str, batteries: str, size: int) -> str:
    if not line:
        return ""

    for digit in sorted(set(line), reverse=True):
        for i, char in enumerate(line):
            if char == digit:
                batteries_ = batteries + char
                break
        else:
            continue

        new_line = line[i + 1 :]

        if len(new_line) + len(batteries_) < size:
            continue

        if len(batteries_) == size:
            return batteries_

        batteries_ = worker(new_line, batteries_, size)
        if not batteries_:
            continue

        return batteries_

    return ""


@utils.performance_timer
def solve_1(path: Path):
    data = utils.read_lines(path)
    return sum(int(worker(line, "", 2)) for line in data)


@utils.performance_timer
def solve_2(path: Path):
    data = utils.read_lines(path)
    return sum(int(worker(line, "", 12)) for line in data)


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
    print()
    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
