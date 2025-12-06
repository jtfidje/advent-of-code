import itertools
import re
from collections import defaultdict
from pathlib import Path

from advent_of_code import utils
from aoc_2015_13 import DATA_PATH


def get_seating_map(path: Path) -> dict[str, dict[str, int]]:
    data = utils.read_data(path).replace("lose ", "-").splitlines()
    data = [re.findall(r"^(\w+) .* (-?\d+) .* (\w+)\.$", line)[0] for line in data]

    seating_map = defaultdict(dict)
    for x, n, y in data:
        seating_map[x][y] = int(n)

    return seating_map


def solve(seating_map: dict[str, dict[str, int]]) -> int:
    happiness = 0
    for permutation in itertools.permutations(seating_map.keys(), len(seating_map)):
        score = 0
        for x, y in utils.sliding_window(permutation, window_size=2, step=1):
            score += seating_map[x][y] + seating_map[y][x]
        else:
            x, y = permutation[0], permutation[-1]
            score += seating_map[x][y] + seating_map[y][x]

        happiness = max(happiness, score)

    return happiness


def solve_1(path: Path):
    seating_map = get_seating_map(path)
    return solve(seating_map)


def solve_2(path: Path):
    seating_map = get_seating_map(path)

    for key in list(seating_map.keys()):
        seating_map["me"][key] = 0
        seating_map[key]["me"] = 0

    return solve(seating_map)


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
