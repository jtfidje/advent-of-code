from copy import copy
from collections import defaultdict
from typing import Dict, List, Optional, Union


class Node:
    def __init__(self, name: str):
        self.name = name
        self.connections = []

    def add_connection(self, node: "Node"):
        if node not in self.connections:
            self.connections.append(node)


def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def search(node: Node, blacklist: List[str] = []) -> List[str]:
    blacklist = blacklist[:]
    if node.name == "end":
        return [["end"]]

    if node.name.islower():
        blacklist.append(node.name)

    valid_paths = []
    for child in node.connections:
        if child.name in blacklist:
            continue

        paths = search(node=child, blacklist=blacklist)
     
        for path in paths:
            if path:
                valid_paths.append([node.name, *path])
    return valid_paths


def search_2(node: Node, blacklist: Dict[str, int]) -> List[str]:
    blacklist = copy(blacklist)
    if node.name == "end":
        return [["end"]]

    if node.name.islower():
        blacklist[node.name] += 1

    valid_paths = []
    for child in node.connections:
        if blacklist[child.name] >= 2:
            continue

        paths = search_2(node=child, blacklist=blacklist)
     
        for path in paths:
            if path:
                valid_paths.append([node.name, *path])
    return valid_paths


def solve_1(path: str) -> int:
    data = read_lines(path)
    nodes = {}

    for line in data:
        name_from, name_to = line.split("-")

        node_from = nodes.get(name_from)
        if node_from is None:
            node_from = Node(name=name_from)
            nodes[name_from] = node_from

        node_to = nodes.get(name_to)
        if node_to is None:
            node_to = Node(name=name_to)
            nodes[name_to] = node_to

        node_from.add_connection(node_to)
        node_to.add_connection(node_from)

    res = search(nodes["start"])
    return len(res)

def solve_2(path: str) -> int:
    data = read_lines(path)
    nodes = {}

    for line in data:
        name_from, name_to = line.split("-")

        node_from = nodes.get(name_from)
        if node_from is None:
            node_from = Node(name=name_from)
            nodes[name_from] = node_from

        node_to = nodes.get(name_to)
        if node_to is None:
            node_to = Node(name=name_to)
            nodes[name_to] = node_to

        node_from.add_connection(node_to)
        node_to.add_connection(node_from)

    unique_paths = set()
    for name in nodes:
        blacklist = defaultdict(int)
        if name in ["start", "end"] or name.isupper():
            continue

        for _name in nodes:
            if _name.islower():
                blacklist[_name] = 1
        
        blacklist[name] = 0
        res = search_2(nodes["start"], blacklist=blacklist)
        for path in res:
            unique_paths.add("-".join(path))
    return len(unique_paths)


if __name__ == "__main__":
    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)
    
    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")
