# flake8: noqa: F401
import math
from functools import reduce
from uuid import uuid4
from dataclasses import dataclass, field
from pathlib import Path
from typing import Self, Any

from scipy.spatial import KDTree

from advent_of_code import utils
from aoc_2025_08 import DATA_PATH


class Node:
    def __init__(self, id: int, point: tuple[int, ...]):
        self.id = id
        self.point = point


def solve(path: str | Path, num_pairs: int):
    data = utils.read_lines(path)

    nodes: dict[int, Node] = {
        i: Node(id=i, point=tuple(utils.parse_integers(line)))
        for i, line in enumerate(data)
    }

    distances: list[tuple[float, tuple[int, ...]]] = []
    for i, node in nodes.items():
        for other in list(nodes.values())[i + 1 :]:
            d = math.sqrt(
                ((node.point[0] - other.point[0]) ** 2)
                + ((node.point[1] - other.point[1]) ** 2)
                + ((node.point[2] - other.point[2]) ** 2)
            )

            distances.append((d, (node.id, other.id)))

    circuits: dict[int, set[int]] = {node.id: {node.id} for node in nodes.values()}
    for _, (xi, yi) in sorted(distances, key=lambda x: x[0])[:num_pairs]:
        new_c = set([*circuits[xi], *circuits[yi]])

        for i in new_c:
            circuits[i] = new_c

    unique: list[set[int]] = []
    for c in sorted(circuits.values(), key=lambda x: len(x), reverse=True):
        for u in unique:
            for x in c:
                if x in u:
                    break
            else:
                continue

            break
        else:
            unique.append(c)

    return reduce(lambda x, y: x * y, (len(x) for x in unique[:3]))


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt", num_pairs=1_000)
    print(f"Problem 1: {answer}")
