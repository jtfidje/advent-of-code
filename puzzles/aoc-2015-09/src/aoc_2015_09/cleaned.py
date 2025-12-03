import math
import re
from collections import defaultdict
from collections.abc import Callable
from pathlib import Path

from advent_of_code import utils
from aoc_2015_09 import DATA_PATH

distance_map: dict[str, dict[str, int]]


def parse_data(path: Path):
    global distance_map
    distance_map = defaultdict(dict)

    data = utils.read_lines(path)

    for line in data:
        x, y, d = re.search(r"(.+) to (.+) = (\d+)", line).groups()
        distance_map[x][y] = int(d)
        distance_map[y][x] = int(d)


def worker(
    city: str, cost: int, visited: set[str], cost_func: Callable[[int | None, int], int]
) -> int:
    best_cost: None | int = None
    for dest in distance_map[city].keys():
        if dest in visited:
            continue

        new_visited = {dest, *visited}
        dest_cost = cost + distance_map[city][dest]

        dest_cost = worker(
            city=dest, cost=dest_cost, visited=new_visited, cost_func=cost_func
        )
        best_cost = cost_func(best_cost, dest_cost)

    return best_cost or cost


def solve_1(path: Path):
    parse_data(path)

    def cost_func(x: int | None, y) -> int:
        return min(x or math.inf, y)

    return min(
        worker(city=city, cost=0, visited={city}, cost_func=cost_func)
        for city in distance_map
    )


def solve_2(path: Path):
    parse_data(path)

    def cost_func(x: int | None, y) -> int:
        return max(x or 0, y)

    return max(
        worker(city=city, cost=0, visited={city}, cost_func=cost_func)
        for city in distance_map
    )


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
