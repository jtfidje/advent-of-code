# flake8: noqa: F401
import re
from pathlib import Path
from pprint import pprint

import numpy as np

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def count(string: str) -> int:
    total = 0

    res = re.findall(r"(XMAS)", string)
    total += len(res)

    res = re.findall(r"(SAMX)", string)
    total += len(res)

    return total


def solve(path: str | Path):
    total_count = 0

    # Count rows
    data = utils.read_data(path)
    total_count += count(data)

    # Count cols
    data = np.array(utils.read_lines(path))
    data = [list(line) for line in data]
    data = np.rot90(data)
    data = "\n".join("".join(line) for line in data)

    total_count += count(data)

    # Count diags
    data = utils.read_lines(path)

    for i in range(len(data) - 3):
        lines = [list(line) for line in data[i : i + 4]]

        r1 = list(utils.sliding_window(lines[0], 4, 1))
        r2 = list(utils.sliding_window(lines[1], 4, 1))
        r3 = list(utils.sliding_window(lines[2], 4, 1))
        r4 = list(utils.sliding_window(lines[3], 4, 1))

        for i in range(len(r1)):
            box = [r1[i], r2[i], r3[i], r4[i]]

            matrix = "\n".join(
                [
                    "".join(r1[i]),
                    "".join(r2[i]),
                    "".join(r3[i]),
                    "".join(r4[i]),
                ]
            )
            diags = "\n".join(
                [
                    "".join(np.diag(box)),
                    "".join(np.diag([line[::-1] for line in box])),
                ]
            )

            total_count += count(diags)

    return total_count


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
