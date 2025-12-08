# flake8: noqa: F401
import itertools
from collections import defaultdict
from pathlib import Path

from advent_of_code import utils
from aoc_2015_17 import DATA_PATH


def solve(path: str | Path, litres: int):
    data = sorted(utils.read_numbers(path), reverse=True)

    results: dict[int, int] = defaultdict(int)

    for i in range(len(data)):
        for containers in itertools.combinations(data, i):
            if sum(containers) == litres:
                results[len(containers)] += 1

    return results[min(results.keys())]


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt", litres=150)
    if answer is not None:
        print(f"Problem 2: {answer}")
