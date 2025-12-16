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
    node: Node, connections: dict[str, list[str]], totals: dict[str, list[int | bool]]
) -> list[int | bool]:
    if node.name == "out":
        return [1, 0, 0]

    result = [0, 0, 0]
    for name in connections[node.name]:
        if name in node.path:
            continue

        if name in totals:
            res = totals[name]
            result[0] += res[0]
            result[1] += res[1]
            result[2] += res[2]
            continue

        child = Node(name, parent=node)
        res = worker(child, connections, totals)
        result[0] += res[0]
        result[1] += res[1]
        result[2] += res[2]

    if node.name == "dac":
        result = [result[0], sum(result), result[2]]

    if node.name == "fft":
        result = [result[0], result[1], result[2] + result[1]]

    totals[node.name] = result
    return result


@utils.performance_timer
def solve(path: str | Path):
    data = utils.read_lines(path)

    connections: dict[str, list[str]] = {"out": []}
    for line in data:
        x, y = line.split(": ")
        y = y.split()

        connections[x] = y

    totals: dict[str, list[int | bool]] = {}
    res = worker(node=Node("svr"), connections=connections, totals=totals)
    return res[2]


if __name__ == "__main__":
    # answer = solve(DATA_PATH / "example_2_1.txt")
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
