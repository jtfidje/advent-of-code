# flake8: noqa: F401
import math
from pathlib import Path
from typing import Literal, Self

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"

DIRECTIONS: list[tuple[int, int, Literal["<", ">", "v", "^"]]] = [
    (-1, 0, "^"),
    (0, 1, ">"),
    (1, 0, "v"),
    (0, -1, "<"),
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

    visited: dict[tuple[int, int], Node] = {}
    nodes = [Node(pos=start_pos, direction=">", parent=None)]

    best_nodes = []
    best_score = math.inf

    while nodes:
        # nodes.sort(key=lambda x: x.score)
        node = nodes.pop(0)

        if node.pos == target_pos:
            if node.score < best_score:
                best_score = node.score
                best_nodes = [node]
            elif node.score == best_score:
                best_nodes.append(node)

            continue

        visited[node.pos] = node

        for direction in DIRECTIONS:
            new_pos = (node.pos[0] + direction[0], node.pos[1] + direction[1])

            # Check if the new position is valid!
            if maze[new_pos[0]][new_pos[1]] == "#":
                continue

            child = Node(pos=new_pos, direction=direction[2], parent=node)

            # Increase direction score if they've turned
            if child.direction != node.direction:
                child.direction_score += 1000

            # Check if we've been here before
            if (_visited := visited.get(child.pos)) is not None:
                if _visited.score < child.score:
                    continue

                if _visited.score > child.score:
                    visited.pop(_visited.pos)

            nodes.append(child)

    unique_positions = set()
    for node in best_nodes:
        unique_positions |= set(node.get_path())

    return len(unique_positions)


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
