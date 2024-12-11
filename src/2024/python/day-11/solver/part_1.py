# flake8: noqa: F401

import re
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = list(map(int, utils.read_data(path).split()))

    for _ in range(25):
        new_data = []
        for stone in data:
            if stone == 0:
                new_data.append(1)
            elif len((_stone := str(stone))) % 2 == 0:
                new_data.append(int(_stone[: len(_stone) // 2]))
                new_data.append(int(_stone[len(_stone) // 2 :]))
            else:
                new_data.append(stone * 2024)
        data = new_data

    return len(data)


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
