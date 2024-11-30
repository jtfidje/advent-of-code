import math
from queue import PriorityQueue
from collections import defaultdict
import numpy as np
from typing import List

class Node:
    def __init__(self, position, risk, parent=None):
        self.parent = parent

        self.position = position
        self.risk = risk

        self.cost = self.score()

    def score(self, _print=False):
        node = self
        score = self.risk
        if _print:
            print(node.position, node.risk)
        while node.parent:
            node = node.parent
            if _print:
                print(node.position, node.risk)
            score += node.risk
        return score


def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def get_moves(pos, data):
    max_x, max_y = data.shape
    moves = []

    if pos[0] < max_x - 1:
        moves.append((1, 0))

    if pos[1] < max_y - 1:
        moves.append((0, 1))

    if pos[0] > 0:
        moves.append((-1, 0))
    
    if pos[1] > 0:
        moves.append((0, -1))

    return moves


def expand(grid):
    expanded = grid
    temp = grid
    for _ in range(4):
        temp = (temp + 1) % 10
        temp[temp == 0] = 1
        expanded = np.concatenate((expanded, temp), axis=1)
        
    temp = expanded
    for _ in range(4):
        temp = (temp + 1) % 10
        temp[temp == 0] = 1
        expanded = np.concatenate((expanded, temp), axis=0)
        
    return expanded


def solve_1(path: str):
    data = read_lines(path)
    data = np.array([list(map(int, line)) for line in data])

    return solve(data)


def solve_2(path: str):
    data = read_lines(path)
    data = np.array([list(map(int, line)) for line in data])
    data = expand(data)

    return djikstra(data)


def djikstra(data):
    running_costs = np.ones(data.shape) * np.inf
    running_costs[(0, 0)] = 0
    visited = {}

    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        (risk, position) = pq.get()
 
        if position in visited:
            continue

        visited[position] = True

        for move in get_moves(position, data):
            new_pos = (
                position[0] + move[0],
                position[1] + move[1]
            )

            risk = data[new_pos]
            _min = min(
                running_costs[new_pos],
                running_costs[position] + risk
            )
            running_costs[new_pos] = _min
            pq.put((running_costs[new_pos], new_pos))

    x, y = data.shape
    return int(running_costs[(x - 1, y - 1)])


def solve(data):
    max_x, max_y = data.shape

    goal = (max_x - 1, max_y -1)
    start_node = Node(position=(0,0), risk=data[(0, 0)])
    start_node.risk = 0

    solutions = []

    open_list = {start_node.position: start_node}
    visited = {}
    while open_list:
        node = min(open_list.values(), key=lambda x: x.cost)
        del open_list[node.position]

        if node.position == goal:
            solutions.append(node.cost)
            continue

        visited[node.position] = node

        for move in get_moves(node.position, data):
            new_pos = (
                node.position[0] + move[0],
                node.position[1] + move[1]
            )
            child = Node(position=new_pos, risk=data[new_pos], parent=node)

            # Check if there exist a node in the open list with the same position
            duplicate = open_list.get(child.position, None)
            if duplicate:
                if child.cost < duplicate.cost:
                    del open_list[child.position] # Remove existing because new child is better
                else:
                    continue # Skip because this node is worse

            # Check if there exist a node in the closed list with the same position
            duplicate = visited.get(child.position, None)
            if duplicate:
                if child.cost < duplicate.cost:
                    del visited[child.position] # Remove existing because new child is better
                else:
                    continue # Skip because this node is worse

            open_list[child.position] = child

    return min(solutions)



if __name__ == "__main__":
    path = "example.txt"
    ans_1_example = solve_1(path)    
    ans_2_example = solve_2(path)

    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)
    
    print(f"Example 1: {ans_1_example}")
    print(f"Example 2: {ans_2_example}")
    print("\n- - -\n")
    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")
