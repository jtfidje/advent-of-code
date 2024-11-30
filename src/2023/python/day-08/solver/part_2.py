from __future__ import annotations

import math
from pathlib import Path
from typing import Self

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"

class Node:
    def __init__(self, name: str, left: Self | None, right: Self | None):
        self.name = name
        self.left = left
        self.right = right

    def get_neighbour(self, dir: str) -> Self:
        return self.left if dir == "L" else self.right
    
    def is_terminal(self) -> bool:
        return self.name.endswith("Z")

    def __repr__(self):
        return f"{self.left.name} <-- {self.name} --> {self.right.name}"


def solve(path: str):
    data = utils.read_lines(path)
    
    instructions = data.pop(0)
    data.pop(0)

    node_map = {}
    for line in data:
        name, dirs = line.split(" = ")
        left, right = dirs[1:-1].split(", ")

        node_map[name] = Node(name, None, None)

    for line in data:
        name, dirs = line.split(" = ")
        left, right = dirs[1: -1].split(", ")

        node = node_map[name]
        node.left = node_map[left]
        node.right = node_map[right]
    
    
    
    z_positions = []
    for node in node_map.values():
        if not node.name.endswith("A"):
            continue

        current = node
        counter = 0
        while True:
            i = counter % len(instructions)

            if current.name.endswith("Z"):
                z_positions.append(counter)
                break

            instruction = instructions[i]
            current = current.get_neighbour(instruction)
            counter += 1

    return math.lcm(*z_positions)

if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")


# TOO LOW  : 200657053
# WRONG    : 6762553731
# WRONG    : 6762574977
# WRONG    : 6762574985
# WRONG    : 6762574992
# WRONG    : 1534419482965997741250
# WRONG    : 16296199706229261503750
# WRONG    : 14321371777539885335137009
# WRONG    : 16622685663084705650822704
# TOO HIGH : 24085386913221873651759779