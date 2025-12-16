from pathlib import Path
from typing import Self

from advent_of_code import utils
from aoc_2025_11 import DATA_PATH


class Node:
    def __init__(self, name: str, parent: Self | None = None):
        self.name = name
        self.parent = parent

        if parent is None:
            self.visited = {name}
        else:
            self.visited = {*parent.visited, name}


def parse_input(path: Path) -> dict[str, list[str]]:
    data = utils.read_lines(path)
    connections = {}
    for line in data:
        x, y = line.split(": ")
        y = y.split()

        connections[x] = y
    return connections


def worker_1(
    node: str, connections: dict[str, list[str]], visited: dict[str, int]
) -> int:
    if node == "out":
        return 1

    if node in visited:
        return visited[node]

    visited[node] = sum(
        worker_1(name, connections, visited) for name in connections[node]
    )
    return visited[node]


def worker_2(
    node: str, connections: dict[str, list[str]], visited: dict[str, list[int]]
) -> list[int]:
    if node == "out":
        return [1, 0, 0]

    if node in visited:
        return visited[node]

    result = [0, 0, 0]
    for child in connections[node]:
        res = worker_2(child, connections, visited)
        result[0] += res[0]
        result[1] += res[1]
        result[2] += res[2]

    if node == "dac":
        result[1] = sum(result)

    if node == "fft":
        result[2] += result[1]

    visited[node] = result
    return visited[node]


@utils.performance_timer
def solve_1(path: Path):
    connections = parse_input(path)

    return worker_1("you", connections, visited={})


@utils.performance_timer
def solve_2(path: Path):
    connections = parse_input(path)

    *_, res = worker_2("svr", connections, {})

    return res


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
    print()
    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
