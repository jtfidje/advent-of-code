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

    visited: dict[tuple[int, int], int | float] = {}
    nodes: list[tuple[int, int, int | float]] = [(0, 0, math.inf)]

    while nodes:
        nodes.sort(key=lambda n: n[2])
        node = nodes.pop(0)
        row_i, col_i = current_point = (node[0], node[1])

        if (node[0], node[1]) == target:
            return node[2]

        visited[current_point] = node[2]
        for move in MOVES:
            next_point: tuple[int, int] = (
                row_i + move[0],
                col_i + move[1],
            )

            if utils.out_of_bounds(*next_point, grid):
                continue

            if next_point in corrupted:
                continue

            child = (*next_point, node[2] + 1)
            # child.calc_h(target)

            if _visited := visited.get(next_point):
                if _visited <= child[2]:
                    continue

                visited.pop(next_point)

            for i, n in enumerate(nodes):
                if (n[0], n[1]) == next_point:
                    if n[2] > child[2]:
                        nodes.pop(i)
                        nodes.append(child)
            else:
                nodes.append(child)

    return "Error"


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
