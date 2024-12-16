# flake8: noqa: F401
import math
from collections import defaultdict
from copy import deepcopy
from pathlib import Path
from typing import Literal, Self

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"

DIRECTIONS: list[tuple[int, int, Literal["<", ">", "v", "^"]]] = [
    (-1, 0, "^"),
    (1, 0, "v"),
    (0, -1, "<"),
    (0, 1, ">"),
]


class Node:
    def __init__(
        self,
        pos: tuple[int, int],
        direction: Literal["<", ">", "v", "^"],
        parent: Self | None = None,
    ):
        self.pos = pos
        self.direction = direction
        self.parent = parent

        if parent:
            self.depth = parent.depth + 1
            self.direction_score = parent.direction_score
        else:
            self.depth = 0
            self.direction_score = 0

    def __repr__(self) -> str:
        return f"Node {self.pos} {self.score}"

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def score(self):
        return self.depth + self.direction_score

    def get_path(self):
        positions = []
        node = self

        while True:
            positions.append(node.pos)

            if node.parent is None:
                break

            node = node.parent
        return positions


def solve(path: str | Path):
    data = utils.read_lines(path)
    maze = [list(line) for line in data]

    start_pos = next(
        (row_i, col_i)
        for row_i, row in enumerate(maze)
        for col_i, col in enumerate(row)
        if col == "S"
    )

    target_pos = next(
        (row_i, col_i)
        for row_i, row in enumerate(maze)
        for col_i, col in enumerate(row)
        if col == "E"
    )

    nodes = [Node(pos=start_pos, direction=">", parent=None)]
    visited: dict[tuple[int, int], int] = {}
    unique_paths = set()
    best_score = math.inf
    while nodes:
        nodes.sort(key=lambda node: node.score)

        node = nodes.pop(0)

        if node.pos == target_pos:
            if node.score > best_score:
                continue

            if node.score < best_score:
                best_score = node.score
                unique_paths = set()

            unique_paths |= set(node.get_path())
            # _maze = deepcopy(maze)
            # for r, c in node.get_path():
            #     _maze[r][c] = "O"
            # print(node.score)

            continue

        visited[node.pos] = node.score

        for direction in DIRECTIONS:
            new_pos = (node.pos[0] + direction[0], node.pos[1] + direction[1])

            # Check if the new position is valid!
            if maze[new_pos[0]][new_pos[1]] == "#":
                continue

            child = Node(pos=new_pos, direction=direction[2], parent=node)

            # _maze = deepcopy(maze)
            # for r, c in visited:
            #     _maze[r][c] = "-"
            # for r, c in node.get_path():
            #     _maze[r][c] = "O"
            # for n in nodes:
            #     _maze[n.pos[0]][n.pos[1]] = "*"

            # _maze[child.pos[0]][child.pos[1]] = "X"
            # for line in _maze:
            #     print("".join(line))

            # Increase direction score if they've turned
            if child.direction != node.direction:
                child.direction_score += 1000

            # Check if we've been here before
            if (_score := visited.get(child.pos)) is not None:
                if _score + 1000 < child.score:
                    continue

                if _score > child.score:
                    visited.pop(child.pos)

            nodes.append(child)

    return len(unique_paths)


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    # answer = solve(Path(data_path, "example_2.txt"))
    print(f"Problem 2: {answer}")
