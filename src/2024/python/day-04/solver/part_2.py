# flake8: noqa: F401

import re
from pathlib import Path
from pprint import pprint

import numpy as np

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def check_mas(string: str) -> bool:
    if re.findall(r"(MAS)", string):
        return True

    if re.findall(r"(SAM)", string):
        return True

    return False


def solve(path: str | Path):
    total_count = 0

    # Count diags
    data = utils.read_lines(path)

    for i in range(len(data) - 2):
        lines = [list(line) for line in data[i : i + 3]]

        r1 = list(utils.sliding_window(lines[0], 3, 1))
        r2 = list(utils.sliding_window(lines[1], 3, 1))
        r3 = list(utils.sliding_window(lines[2], 3, 1))

        for i in range(len(r1)):
            box = [r1[i], r2[i], r3[i]]

            d1 = np.diag(box)
            d2 = np.diag([line[::-1] for line in box])

            total_count += all([check_mas("".join(d1)), check_mas("".join(d2))])

    return total_count


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")
