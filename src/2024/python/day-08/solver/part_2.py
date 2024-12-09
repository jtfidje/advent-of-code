# flake8: noqa: F401

import itertools
import re
from collections import defaultdict
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def manhatten(a, b):
    return abs(a[0] - b[0]), abs(a[1] - b[1])


def solve(path: str | Path):
    data = utils.read_lines(path)
    data = [list(line) for line in data]
    char_map = defaultdict(list)

    for row_i, line in enumerate(data):
        for match in re.finditer(r"[a-zA-Z0-9]", "".join(line)):
            char_map[match.group()].append((row_i, match.start()))

    antinodes = set()
    for char, positions in char_map.items():
        if len(positions) <= 1:
            continue

        for x, y in itertools.combinations(positions, 2):
            r_len = abs(x[0] - y[0])
            c_len = abs(x[1] - y[1])

            antinodes.add(x)
            antinodes.add(y)

            i = 1
            while True:
                if x[1] > y[1]:
                    p1 = (x[0] - (r_len * i), x[1] + (c_len * i))
                    p2 = (y[0] + (r_len * i), y[1] - (c_len * i))
                else:
                    p1 = (x[0] - (r_len * i), x[1] - (c_len * i))
                    p2 = (y[0] + (r_len * i), y[1] + (c_len * i))

                oob1 = utils.out_of_bounds(*p1, data)
                oob2 = utils.out_of_bounds(*p2, data)

                if not oob1:
                    antinodes.add(p1)
                if not oob2:
                    antinodes.add(p2)

                if oob1 and oob2:
                    break

                i += 1

    return len(antinodes)


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
