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
        self._node_path = []

    @property
    def path(self) -> list[str]:
        if not self._node_path:
            node = self
            self._node_path = [node.name]
            while node.parent:
                node = node.parent
                self._node_path.append(node.name)

        return self._node_path

    def __repr__(self) -> str:
        return f"<Node {self.name}>"


def worker(
    node: Node, connections: dict[str, list[str]], totals: dict[str, int]
) -> int:
    if node.name == "out":
        totals["__score__"] += "dac" in node.path and "fft" in node.path
        return 1

    if ("dac" in node.path and "fft" in node.path) and node.name in totals:
        totals["__score__"] += totals[node.name]
        return totals[node.name]

    result = 0
    for name in connections[node.name]:
        if name in node.path:
            continue

        child = Node(name, parent=node)
        result += worker(child, connections, totals)

    totals[node.name] = result
    return result


def solve(path: str | Path):
    data = utils.read_lines(path)

    connections: dict[str, list[str]] = {}
    for line in data:
        x, y = line.split(": ")
        y = y.split()

        connections[x] = y

    totals = {"__score__": 0}
    worker(node=Node("svr"), connections=connections, totals=totals)

    return totals["__score__"]


if __name__ == "__main__":
    # answer = solve(DATA_PATH / "example_2_1.txt")
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
