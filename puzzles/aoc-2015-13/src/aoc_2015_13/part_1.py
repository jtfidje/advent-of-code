# flake8: noqa: F401
import re
import itertools
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
    for permutation in itertools.permutations(seating_map.keys(), len(seating_map)):
        score = 0
        for x, y in utils.sliding_window(permutation, window_size=2, step=1):
            score += seating_map[x][y] + seating_map[y][x]
        score += (
            seating_map[permutation[0]][permutation[-1]]
            + seating_map[permutation[-1]][permutation[0]]
        )

        happiness = max(happiness, score)

    return happiness


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
