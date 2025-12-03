# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2015_05 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_lines(path)

    count = 0
    for line in data:
        found = False
        for i, pattern in enumerate(
            utils.sliding_window(line[:-2], window_size=2, step=1)
        ):  # noqa: E501
            for window in utils.sliding_window(line[i + 2 :], window_size=2, step=1):
                if pattern == window:
                    found = True
                    break
            if found:
                break
        else:
            continue

        for x, _, y in utils.sliding_window(line, window_size=3, step=1):
            if x == y:
                break
        else:
            continue

        count += 1

    return count


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")


"[al]skdfjhalskdjfh"
