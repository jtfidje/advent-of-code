import re
import string
from pathlib import Path

from advent_of_code.utils import read_lines, sliding_window
from aoc_2015_05 import DATA_PATH


def solve_1(path: Path):
    vowel_pattern = r"[aeiou]"
    double_pattern = "|".join(f"({char * 2})" for char in string.ascii_lowercase)
    negative_pattern = r"(ab)|(cd)|(pq)|(xy)"

    count = 0

    for line in read_lines(path):
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


def solve_2(path: Path):
    count = 0
    for line in read_lines(path):
        for i, pattern in enumerate(sliding_window(line[:-2], window_size=2, step=1)):  # noqa: E501
            for window in sliding_window(line[i + 2:], window_size=2, step=1):
                if pattern == window:
                    break
            else:
                continue
            break
        else:
            continue

        for x, _, y in sliding_window(line, window_size=3, step=1):
            if x == y:
                break
        else:
            continue

        count += 1

    return count


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
