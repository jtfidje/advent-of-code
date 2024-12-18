# flake8: noqa: F401

import math
from pathlib import Path
from typing import Self

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


class Node:
    def __init__(self, point: tuple[int, int], parent: Self | None = None):
        self.point = point
        self.parent = parent
        self.depth = parent.depth + 1 if parent else 0
        self.h = math.inf

    def calc_h(self, target):
        self.h = (
            abs(self.point[0] - target[0]) + abs(self.point[1] - target[1])
        ) + self.depth

    def __repr__(self) -> str:
        return f"Node {self.point} - {self.depth} / {self.h}"

    def __str__(self) -> str:
        return self.__repr__()


MOVES = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solve(path: str | Path):
    data = utils.read_lines(path)
    points = []
    for line in data:
        col_i, row_i = line.split(",")
        points.append((int(row_i), int(col_i)))

    target = (6, 6) if "example" in str(path) else (70, 70)
    num_bytes = 12 if "example" in str(path) else 1024
    grid = [["."] * (target[1] + 1) for _ in range(target[0] + 1)]

    corrupted = set(points[:num_bytes])

    visited: dict[tuple[int, int], Node] = {}
    nodes: list[Node] = [Node(point=(0, 0))]
    while nodes:
        nodes.sort(key=lambda n: n.h)
        node = nodes.pop(0)

        if node.point == target:
            return node.depth

        visited[node.point] = node
        for move in MOVES:
            next_point: tuple[int, int] = (
                node.point[0] + move[0],
                node.point[1] + move[1],
            )

            if utils.out_of_bounds(*next_point, grid):
                continue

            if next_point in corrupted:
                continue

            child = Node(point=next_point, parent=node)
            child.calc_h(target)

            if _visited := visited.get(child.point):
                if _visited.h <= child.h:
                    continue

                visited.pop(child.point)

            nodes.append(child)

    return "Error"


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
