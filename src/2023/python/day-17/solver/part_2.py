import math
from copy import deepcopy
from enum import Enum
from typing import Self
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"



class Direction(Enum):
    left = (0, -1)
    right = (0, 1)
    up = (-1, 0)
    down = (1, 0)


class Node:
    def __init__(self, position: tuple[int, int], heat_loss: int, direction: str | None=None, parent: Self | None=None):
        self.position = position
        self.direction = direction
        self.heat_loss = heat_loss
        self.parent = parent
        self.tail = {self.position: None}


        if self.parent:
            self.heat_loss += self.parent.heat_loss
            self.tail |= self.parent.tail
        

    def _dir_count(self, direction: Direction | None=None) -> int:
            if direction is None:
                direction = self.direction
            
            count = 1
            node = self
            while node.parent is not None:
                node = node.parent
                if node.direction != direction:
                    break

                count += 1

            return count
    

    def valid_directions(self) -> list[Direction]:
        if self.direction is None:
            return [Direction.up, Direction.down, Direction.left, Direction.right]
        
        dir_count = self._dir_count()
        if dir_count < 4:
            return [self.direction]
        
        valid_directions = []
        match self.direction:
            case Direction.left:
                valid_directions += [Direction.up, Direction.down]

            case Direction.right:
                valid_directions += [Direction.up, Direction.down]

            case Direction.up:
                valid_directions += [Direction.left, Direction.right]

            case Direction.down:
                valid_directions += [Direction.left, Direction.right]
        
        if dir_count < 10:
            valid_directions.append(self.direction)

        return valid_directions
    
    def print_path(self, matrix):
        matrix = deepcopy(matrix)
        node = self
        while node.parent:
            match node.direction:
                case Direction.up:
                    char = "^"
                case Direction.down:
                    char = "v"
                case Direction.left:
                    char = "<"
                case Direction.right:
                    char = ">"
            
            row, col = node.position
            matrix[row][col] = char

            node = node.parent

        for line in matrix:
            print("".join(list(map(str, line))))

    
    @property
    def key(self) -> tuple[tuple[int, int], Direction]:
        return (self.position, self.direction, self._dir_count(self.direction))

    
    def __repr__(self) -> str:
        return " ".join(list(map(str, [self.position, self.direction, self.heat_loss])))

def solve(path: str):
    data = utils.read_lines(path)
    data = [list(map(int, list(line))) for line in data]

    goal_position = (len(data) - 1, len(data[0]) - 1)
    start_node = Node(
        position=(0, 0),
        heat_loss=0,
        direction=None,
        parent=None
    )

    open_set = {start_node.key: start_node}
    closed_set = {}
    
    best_score = math.inf
    best_node = None
    while open_set:
        # Sort open_set by lowest heat loss and pop node a 0
        key = min(open_set.items(), key=lambda n: n[1].heat_loss)[0]
        node = open_set.pop(key)

        closed_set[node.key] = node

        # Check if new best
        if node.position == goal_position and node._dir_count() >= 4:
            if node.heat_loss < best_score:
                best_score = node.heat_loss
                best_node = node
            continue

        for direction in node.valid_directions():
            row, col = (
                node.position[0] + direction.value[0],
                node.position[1] + direction.value[1],
            )

            if utils.out_of_bounds(row, col, data):
                continue

            if (row, col) in node.tail:
                continue

            heat_loss = data[row][col]
            child = Node(
                position=(row, col),
                heat_loss=heat_loss,
                direction=direction,
                parent=node
            )

            if child.key in closed_set:
                _in_closed = closed_set.pop(child.key)

                if _in_closed.heat_loss > child.heat_loss:
                    # Child is better, do nothing
                    ...
                else:
                    # Child is worse or equal. Add _in_closed back to set and continue loop
                    closed_set[_in_closed.key] = _in_closed
                    continue

            if child.key in open_set:
                _in_open = open_set.pop(child.key)

                if _in_open.heat_loss > child.heat_loss:
                    # Child is better, do nothing
                    ...
                else:
                    # Child is worse or equal. Add _in_open back to set, mark child as closed and continue loop
                    open_set[_in_open.key] = _in_open
                    #closed_set[child.key] = child
                    continue

            # All good!
            open_set[child.key] = child

    return best_score

if __name__ == "__main__":
    #answer = solve(Path(data_path, "example_2_2.txt"))
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")