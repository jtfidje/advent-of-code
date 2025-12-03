# flake8: noqa: F401

import re
from collections import defaultdict
from pathlib import Path

from advent_of_code import utils
from aoc_2015_09 import DATA_PATH


distance_map: dict[str, dict[str, int]]


def worker(city: str, cost: int, visited: set[str]) -> int:
    best_cost = 0
    for dest in distance_map[city].keys():
        if dest in visited:
            continue

        new_visited = {dest, *visited}
        dest_cost = cost + distance_map[city][dest]

        new_cost = worker(city=dest, cost=dest_cost, visited=new_visited)

        best_cost = max(best_cost, new_cost)

    if best_cost == 0:
        return cost

    return best_cost


def solve(path: str | Path):
    global distance_map
    distance_map = defaultdict(dict)

    data = utils.read_lines(path)

    for line in data:
        x, y, d = re.search(r"(.+) to (.+) = (\d+)", line).groups()
        distance_map[x][y] = int(d)
        distance_map[y][x] = int(d)

    best_cost = 0

    for city in distance_map.keys():
        cost = worker(city=city, cost=0, visited={city})
        best_cost = max(best_cost, cost)

    return best_cost


if __name__ == "__main__":
    distance_map = defaultdict(dict)
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
