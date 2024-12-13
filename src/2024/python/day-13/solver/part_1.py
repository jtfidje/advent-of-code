# flake8: noqa: F401

import math
import re
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = utils.read_data(path)
    machines_data = data.split("\n\n")
    machines = []
    for block in machines_data:
        machines.append(
            (
                tuple(
                    [
                        *map(
                            int,
                            re.search(r"Button A: X\+(\d+), Y\+(\d+)", block).groups(),
                        ),
                        3,
                    ]  # type: ignore
                ),
                tuple(
                    [
                        *map(
                            int,
                            re.search(r"Button B: X\+(\d+), Y\+(\d+)", block).groups(),
                        ),
                        1,
                    ]  # type: ignore
                ),
                tuple(map(int, re.search(r"Prize: X=(\d+), Y=(\d+)", block).groups())),  # type: ignore
            )
        )

    total_cost = 0
    for machine in machines:
        res = a_star(machine)
        if res is None:
            continue
        total_cost += res

    return total_cost


def _gen_moves(
    node: tuple[int, int, int],
    button_a: tuple[int, int, int],
    button_b: tuple[int, int, int],
) -> list[tuple[int, int, int]]:
    return [
        (node[0] + button_a[0], node[1] + button_a[1], node[2] + button_a[2]),
        (node[0] + button_b[0], node[1] + button_b[1], node[2] + button_b[2]),
    ]


def calc_h(node: tuple[int, int, int], prize: tuple[int, int]):
    return abs(node[0] - prize[0]) + abs(node[1] - prize[1]) + node[2]


def a_star(machine) -> int | None:
    button_a, button_b, prize = machine
    visited = set()
    nodes = [(0, 0, 0)]
    while nodes:
        min_h = math.inf
        min_i = 0
        for i, node in enumerate(nodes):
            if (h := calc_h(node, prize)) < min_h:
                min_h = h
                min_i = i

        x, y, cost = node = nodes.pop(min_i)
        if node in visited:
            continue

        if x < 0 or x > prize[0] or y < 0 or y > prize[1]:
            continue

        if (x, y) == prize:
            print(len(visited))
            return cost

        visited.add(node)
        nodes.extend(_gen_moves(node, button_a, button_b))

    return None


if __name__ == "__main__":
    answer = solve(Path(data_path, "example_1.txt"))
    print(f"Problem 1: {answer}")
