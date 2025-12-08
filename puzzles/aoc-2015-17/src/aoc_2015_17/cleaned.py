import itertools
from collections import defaultdict
from pathlib import Path

from advent_of_code import utils
from aoc_2015_17 import DATA_PATH


@utils.performance_timer
def solve_1(path: Path, litres: int):
    data = sorted(utils.read_numbers(path), reverse=True)

    return sum(
        sum(containers) == litres
        for i in range(len(data))
        for containers in itertools.combinations(data, i)
    )


@utils.performance_timer
def solve_2(path: Path, litres: int):
    data = sorted(utils.read_numbers(path), reverse=True)

    results: dict[int, int] = defaultdict(int)
    min_containers = len(data)
    for i in range(len(data)):
        if i > min_containers:
            break

        for containers in itertools.combinations(data, i):
            if sum(containers) == litres:
                results[len(containers)] += 1
                min_containers = i

    return results[min(results.keys())]


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt", litres=150)
    print(f"Problem 1: {answer}")
    print()
    answer = solve_2(DATA_PATH / "input.txt", litres=150)
    print(f"Problem 2: {answer}")
