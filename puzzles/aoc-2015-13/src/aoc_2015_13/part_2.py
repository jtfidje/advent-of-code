# flake8: noqa: F401

import itertools
import re
from collections import defaultdict
from pathlib import Path

from advent_of_code import utils
from aoc_2015_13 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_data(path).replace("lose ", "-").splitlines()
    data = [re.findall(r"^(\w+) .* (-?\d+) .* (\w+)\.$", line)[0] for line in data]

    seating_map = defaultdict(dict)

    for x, n, y in data:
        seating_map[x][y] = int(n)

    happiness = 0
    for permutation in itertools.permutations(
        ["me", *seating_map.keys()], len(seating_map) + 1
    ):
        score = 0
        for x, y in utils.sliding_window(permutation, window_size=2, step=1):
            if "me" in [x, y]:
                continue

            score += seating_map[x][y] + seating_map[y][x]

        x, y = permutation[0], permutation[-1]
        if "me" in [x, y]:
            continue
        score += seating_map[x][y] + seating_map[y][x]

        happiness = max(happiness, score)

    return happiness


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
