# flake8: noqa: F401
import itertools
from collections import Counter
from pathlib import Path

from advent_of_code import utils
from aoc_2015_15 import DATA_PATH


def solve(path: str | Path):
    ingredients: dict[str, tuple[int, ...]] = {}

    for line in utils.read_lines(path):
        name, line = line.split(": ")
        ingredients[name] = tuple(map(int, utils.parse_integers(line)))

    best = 0
    for combination in itertools.combinations_with_replacement(
        list(ingredients.keys()), 100
    ):
        counter = Counter(combination)
        score = 1
        for i in range(4):
            temp = 0
            for name, count in counter.items():
                temp += ingredients[name][i] * count
            score *= max(0, temp)
        temp = sum(ingredients[name][-1] * count for name, count in counter.items())
        if temp == 500:
            best = max(score, best)

    return best


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
