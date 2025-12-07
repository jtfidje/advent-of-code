import time
from pathlib import Path

from advent_of_code.utils import read_lines
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


def solve_1(path: Path):
    data = read_lines(path)
    return sum(int(worker(line, "", 2)) for line in data)


def solve_2(path: Path):
    data = read_lines(path)
    return sum(int(worker(line, "", 12)) for line in data)


if __name__ == "__main__":
    start = time.perf_counter()
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
    end = time.perf_counter()

    elapsed = end - start

    if elapsed > 0:
        print(f"Elapsed: {(end - start) * 1_000:.4f}ms")
    else:
        print(f"Elapsed: {(end - start):.4f}s")
