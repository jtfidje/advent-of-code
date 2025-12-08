import math
from collections.abc import Generator
from dataclasses import dataclass
from pathlib import Path

from advent_of_code import utils
from aoc_2025_08 import DATA_PATH


@dataclass
class Node:
    id: int
    point: tuple[int, ...]


def parse_input(path: Path) -> list[Node]:
    data = utils.read_lines(path)

    return [
        Node(id=i, point=tuple(utils.parse_integers(line)))
        for i, line in enumerate(data)
    ]


def calc_distances(nodes: list[Node]) -> Generator[tuple[int, int]]:
    distances: list[tuple[float, int, int]] = []
    for node in nodes:
        for other in list(nodes)[node.id + 1 :]:
            d = math.sqrt(
                ((node.point[0] - other.point[0]) ** 2)
                + ((node.point[1] - other.point[1]) ** 2)
                + ((node.point[2] - other.point[2]) ** 2)
            )

            distances.append((d, node.id, other.id))
    return ((x, y) for _, x, y in sorted(distances, key=lambda x: x[0]))


@utils.performance_timer
def solve_1(path: Path, num_pairs: int):
    nodes = parse_input(path)
    distances = calc_distances(nodes)
    circuits: dict[int, set[int]] = {node.id: {node.id} for node in nodes}
    for xi, yi in (next(distances) for _ in range(num_pairs)):
        new_c = set([*circuits[xi], *circuits[yi]])

        for i in new_c:
            circuits[i] = new_c

    res = []
    seen: set[int] = set()
    for c in sorted(circuits.values(), key=lambda x: len(x), reverse=True):
        if seen.issuperset(c):
            continue

        seen.update(c)
        res.append(len(c))

        if len(res) == 3:
            return res[0] * res[1] * res[2]


@utils.performance_timer
def solve_2(path: Path):
    nodes = parse_input(path)
    distances = calc_distances(nodes)

    circuits: dict[int, set[int]] = {node.id: {node.id} for node in nodes}
    for xi, yi in distances:
        new_c = set([*circuits[xi], *circuits[yi]])

        if len(new_c) == len(nodes):
            return nodes[xi].point[0] * nodes[yi].point[0]

        for i in new_c:
            circuits[i] = new_c


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt", num_pairs=1_000)
    print(f"Problem 1: {answer}")
    print()
    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
