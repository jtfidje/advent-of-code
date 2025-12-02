import re
from pathlib import Path

from advent_of_code.utils import read_data
from aoc_2025_02 import DATA_PATH


def solve_1(path: Path):
    data = read_data(path)
    range_limits = map(
        lambda r: (int(r[1]), int(r[2]) + 1), re.findall(r"((\d+)-(\d+))", data)
    )

    ids = ((str(n), n) for limits in range_limits for n in range(*limits))

    result = 0
    for str_id, int_id in ids:
        n = len(str_id) // 2
        x, y = str_id[n:], str_id[:n]

        if x == y:
            result += int_id
            continue

    return result


def solve_2(path: Path):
    data = read_data(path)
    range_limits = map(
        lambda r: (int(r[1]), int(r[2]) + 1), re.findall(r"((\d+)-(\d+))", data)
    )

    ids = ((str(n), n) for limits in range_limits for n in range(*limits))
    result = 0

    for str_id, int_id in ids:
        len_id = len(str_id)
        for j in range(1, (len_id // 2) + 1):
            if len_id % j != 0:
                continue

            if not len(str_id.replace(str_id[:j], "")):
                result += int_id
                break

    return result


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
