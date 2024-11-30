# flake8: noqa: F401

from pathlib import Path
from pprint import pprint

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"

class Node:
    def __init__(self, name: str, left: str, right: str):
        self.name = name
        self.left = left
        self.right = right

    def get_neighbour(self, dir: str):
        return self.left if dir == "L" else self.right

    def __repr__(self):
        return f"{self.left} <-- {self.name} --> {self.right}"

def solve(path: str):
    data = utils.read_lines(path)
    
    instructions = data.pop(0)
    data.pop(0)

    node_map = {}
    for line in data:
        name, dirs = line.split(" = ")
        left, right = dirs[1:-1].split(", ")

        node_map[name] = Node(name, left, right)

    current = "AAA"
    counter = 0
    while current != "ZZZ":
        i = counter % len(instructions)
        instruction = instructions[i]
        current = node_map[current].get_neighbour(instruction)

        counter += 1

    return counter


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")