# flake8: noqa: F401
from functools import cache
from pathlib import Path
from typing import Self

from advent_of_code import utils
from aoc_2025_11 import DATA_PATH


class Node:
    def __init__(self, name: str, parent: Self | None = None):
        self.name = name
        self.parent = parent

    @cache
    def get_path(self) -> list[str]:
        node = self
        path = [node.name]
        while node.parent:
            node = node.parent
            path.append(node.name)
        return path


def solve(path: str | Path):
    data = utils.read_lines(path)

    connections: dict[str, list[str]] = {}
    for line in data:
        x, y = line.split(": ")
        y = y.split()

        connections[x] = y

    res = 0
    to_visit = [Node("you")]
    while to_visit:
        node = to_visit.pop(-1)

        if node.name == "out":
            res += 1
            continue

        for name in connections[node.name]:
            if name in node.get_path():
                continue

            child = Node(name, parent=node)
            to_visit.append(child)

    return res


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
