import json
from functools import reduce
from typing import Any

def json_print(obj: dict | list) -> None:
    print(json.dumps(obj, indent=4))


class Node:
    def __init__(self, elevation, pos, parent=None):
        self.elevation = elevation
        self.pos = pos
        self.parent = parent

        if parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

    def __eq__(self, node):
        return node.pos == self.pos


def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def read_numbers(path: str) -> list[int]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return list(map(int, lines))


def solve_1(path: str) -> Any:
    data = read_lines(path)

    min_x = 0
    max_x = len(data[0])

    min_y = 0
    max_y = len(data)

    # Find start
    for y, line in enumerate(data):
        if "S" in line:
            start = (line.index("S"), y)
            break

    # Find end
    for y, line in enumerate(data):
        if "E" in line:
            end = (line.index("E"), y)
            break

    elevation_map = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            elevation_map[(x, y)] = ord(char)

    elevation_map[start] = ord("a")
    elevation_map[end] = ord("z")

    start_node = Node(elevation=ord("a"), pos=start)
    queue: list[Node] = [start_node]
    visited: list[Node] = []

    while queue:
        queue.sort(key=lambda x: x.depth)
        node = queue.pop(0)

        if node.pos == end:
            return node.depth

        visited.append(node)

        for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_x = node.pos[0] + dx
            new_y = node.pos[1] + dy

            if new_x < min_x or new_x >= max_x:
                continue

            if new_y < min_y or new_y >= max_y:
                continue

            new_elevation = elevation_map[(new_x, new_y)]
            if new_elevation - node.elevation >= 2:
                continue
            
            child = Node(elevation=new_elevation, pos=(new_x, new_y), parent=node)

            # Check visited
            duplicate = next((_node for _node in visited if _node.pos == child.pos), None)
            if duplicate:
                if child.depth < duplicate.depth:
                    visited.remove(duplicate)
                else:
                    continue

            duplicate = next((_node for _node in queue if _node.pos == child.pos), None)
            if duplicate:
                if child.depth < duplicate.depth:
                    queue.remove(duplicate)
                else:
                    continue

            queue.append(child)



def solve_2(path: str) -> Any:
    data = read_lines(path)

    min_x = 0
    max_x = len(data[0])

    min_y = 0
    max_y = len(data)

    # Find start
    for line in data:
        line = line.replace("S", "a")

    # Find end
    for y, line in enumerate(data):
        if "E" in line:
            end = (line.index("E"), y)
            break

    queue: list[Node] = []
    visited: list[Node] = []
    elevation_map = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            elevation = ord(char)
            elevation_map[(x, y)] = elevation

            if char == "a":
                queue.append(Node(elevation=elevation, pos=(x, y), parent=None))

    elevation_map[end] = ord("z")
    while queue:
        queue.sort(key=lambda x: x.depth)
        node = queue.pop(0)

        if node.pos == end:
            return node.depth

        visited.append(node)

        for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_x = node.pos[0] + dx
            new_y = node.pos[1] + dy

            if new_x < min_x or new_x >= max_x:
                continue

            if new_y < min_y or new_y >= max_y:
                continue

            new_elevation = elevation_map[(new_x, new_y)]
            if new_elevation - node.elevation >= 2:
                continue
            
            child = Node(elevation=new_elevation, pos=(new_x, new_y), parent=node)

            # Check visited
            duplicate = next((_node for _node in visited if _node.pos == child.pos), None)
            if duplicate:
                if child.depth < duplicate.depth:
                    visited.remove(duplicate)
                else:
                    continue

            duplicate = next((_node for _node in queue if _node.pos == child.pos), None)
            if duplicate:
                if child.depth < duplicate.depth:
                    queue.remove(duplicate)
                else:
                    continue

            queue.append(child)


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")
