from copy import copy
from collections import defaultdict
from typing import Dict, List


class Node:
    def __init__(self, name: str):
        self.name = name
        self.connections = []
    
        if self.name.isupper():
            self.size = "big"
        else:
            self.size = "small"

    def add_connection(self, node: "Node"):
        if node not in self.connections:
            self.connections.append(node)


def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def create_nodes(data: List[str]) -> Dict[str, Node]:
    nodes = {}
    for line in data:
        name_a, name_b = line.split("-")

        if name_a not in nodes:
            nodes[name_a] = Node(name=name_a)
        if name_b not in nodes:
            nodes[name_b] = Node(name=name_b)

        node_a, node_b = nodes[name_a], nodes[name_b]
        
        node_b.add_connection(node_a)
        node_a.add_connection(node_b)
    
    return nodes


def search(node: Node, visited: Dict[str, int]) -> List[str]:
    visited = copy(visited)
    if node.name == "end":
        return [["end"]]

    if node.size == "small":
        visited[node.name] += 1

    valid_paths = []
    for child in node.connections:
        if visited[child.name] >= 1:
            continue

        paths = search(node=child, visited=visited)
     
        for path in paths:
            if path:
                valid_paths.append([node.name, *path])
    return valid_paths


def solve_1(path: str) -> int:
    data = read_lines(path)
    nodes = create_nodes(data)
    visited = defaultdict(int)
    return len(search(nodes["start"], visited))


def solve_2(path: str) -> int:
    data = read_lines(path)
    nodes = create_nodes(data)

    unique_paths = set()
    for name, node in nodes.items():
        visited = defaultdict(int)
        if name in ["start", "end"] or node.size == "big":
            continue

        visited[name] = -1
        res = search(nodes["start"], visited=visited)
        for path in res:
            unique_paths.add("-".join(path))
    
    return len(unique_paths)


if __name__ == "__main__":
    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)
    
    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")
