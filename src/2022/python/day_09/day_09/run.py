import json
from functools import reduce
from typing import Any

def json_print(obj: dict | list) -> None:
    print(json.dumps(obj, indent=4))


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


class Node:
    def __init__(self, name, position):
        self.name = name
        self._position = position
        self.visited = [position]

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        self.visited.append(value)
        self._position = value


def solve_1(path: str) -> Any:
    data = read_lines(path)

    head = Node("head", (4, 0))
    tail = Node("tail", (4, 0))

    for line in data:
        move, steps = line.split()
        steps = int(steps)

        if move == "R": 
            delta = [0, 1]
        elif move == "U":
            delta = [-1, 0]
        elif move == "D":
            delta = [1, 0]
        elif move == "L":
            delta = [0, -1]

        for _ in range(steps):
            new_head_pos = (head.position[0] + delta[0], head.position[1] + delta[1])

            if any(tail.position == (new_head_pos[0] + x[0], new_head_pos[1] + x[1]) for x in [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]):
                head.position = new_head_pos
                continue

            new_tail_pos = head.position

            head.position = new_head_pos
            tail.position = new_tail_pos

    
    return len(set(tail.visited))


def solve_2(path: str) -> Any:
    data = read_lines(path)

    snake = [Node(i, (15, 11)) for i in range(10)]

    for line in data:
        move, steps = line.split()
        steps = int(steps)

        if move == "R": 
            delta = [0, 1]
        elif move == "U":
            delta = [-1, 0]
        elif move == "D":
            delta = [1, 0]
        elif move == "L":
            delta = [0, -1]

        for _ in range(steps):
            snake[0].position = (snake[0].position[0] + delta[0], snake[0].position[1] + delta[1])

            for segment in range(1, len(snake)):
                head = snake[segment - 1]
                tail = snake[segment]
                
                if any(head.position == (tail.position[0] + x[0], tail.position[1] + x[1]) for x in [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]):
                    break

                if head.position[1] > tail.position[1]:
                    horizontal_move = 1
                elif head.position[1] < tail.position[1]:
                    horizontal_move = -1
                else:
                    horizontal_move = 0

                if head.position[0] > tail.position[0]:
                    vertical_move = 1
                elif head.position[0] < tail.position[0]:
                    vertical_move = -1
                else:
                    vertical_move = 0

                tail_move = [vertical_move, horizontal_move]



                tail.position = (tail.position[0] + tail_move[0], tail.position[1] + tail_move[1])
        
    return len(set(snake[-1].visited))


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")
