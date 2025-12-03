# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2025_02 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_data(path)
    ranges = data.split(",")
    invalid_ids: list[int] = []

    for range_ in ranges:
        x, y = map(int, range_.split("-"))

        for i in range(x, y + 1):
            s = str(i)
            n = len(s) // 2
            for j in range(1, n + 1):
                windows = [
                    window
                    for window in utils.sliding_window(
                        s, window_size=j, step=j, include_remainder=True
                    )
                ]
                if len(set(windows)) == 1:
                    invalid_ids.append(i)
                    break

    return sum(invalid_ids)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
