import json
import math
from collections import deque
from functools import reduce
from itertools import permutations
from typing import List


def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [json.loads(line) for line in lines]
        return lines



class Node:
    def __init__(self, left=None, right=None, value=None, parent=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent
        
        if self.parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

    def to_list(self):
        if self.value is not None:
            return self.value
        
        return [
            self.left.to_list(),
            self.right.to_list()
        ]

    def add_left(self, value):
        node = self
        while node.parent and node.parent.left == node:
            node = node.parent
        else:
            if node.parent is None:
                return

        node = node.parent.left
        while node.value is None:
            node = node.right

        node.value += value

    def add_right(self, value):
        node = self
        while node.parent and node.parent.right == node:
            node = node.parent
        else:
            if node.parent is None:
                return

        node = node.parent.right
        while node.value is None:
            node = node.left

        node.value += value


def build_tree(equation, parent=None):
    if parent is None:
        parent = Node()
    a, b = equation
    
    if isinstance(a, int):
        node_a = Node(value=a, parent=parent)
    else:
        node_a = Node(parent=parent)
        node_a = build_tree(equation=a, parent=node_a)

    if isinstance(b, int):
        node_b = Node(value=b, parent=parent)
    else:
        node_b = Node(parent=parent)
        node_b = build_tree(equation=b, parent=node_b)

    parent.left = node_a
    parent.right = node_b

    return parent


def check_explode(node: Node):
    if node.depth <= 4:
        if node.value is not None:
            return False
        
        if node.depth == 4:
            a = node.left.value
            b = node.right.value

            node.add_left(a)
            node.add_right(b)

            node.left = None
            node.right = None
            node.value = 0

            return True

        else:
            if check_explode(node.left):
                return True
            if check_explode(node.right):
                return True


def check_split(node: Node):
    if node.value is not None:
        if node.value < 10:
            return False
        else:
            node_a = Node(value=node.value // 2, parent=node)
            node_b = Node(value=math.ceil(node.value / 2), parent=node)

            node.left = node_a
            node.right = node_b
            node.value = None

            return True

    else:
        if check_split(node.left):
            return True
        if check_split(node.right):
            return True


def calculate_magnitude(node: Node):
    if node.value is not None:
        return node.value
    else:
        return sum((
            calculate_magnitude(node.left) * 3,
            calculate_magnitude(node.right) * 2
        ))


def snail_reduce(a, b):
    equation = [a, b]
    binary_tree = build_tree(equation)

    while True:
        if check_explode(binary_tree):
            continue

        if check_split(binary_tree):
            continue

        return binary_tree.to_list()


def solve_1(path: str):
    data = read_lines(path)
    result_equation = reduce(snail_reduce, data)
    binary_tree = build_tree(result_equation)
    return calculate_magnitude(binary_tree)
    


def solve_2(path: str):
    data = read_lines(path)
    number_pairs = permutations(data, 2)
    _max = 0
    for pair in number_pairs:
        result_equation = reduce(snail_reduce, pair)
        binary_tree = build_tree(result_equation)
        magnitude = calculate_magnitude(binary_tree)
        _max = max(_max, magnitude)
    return _max


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
