import math
from copy import deepcopy
from pathlib import Path
from typing import Self
from shapely import Polygon, Point
from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


class Pipe:
    def __init__(self, symbol: str, pos: tuple[int, int], steps: int, parent: Self | None = None):
        self.symbol = symbol
        self.pos = pos
        self.steps = steps
        self.row, self.col = pos
        self.parent = parent
        self.child = None

    def can_connect(self, symbol: str, pos: tuple[int, int]):
        row, col = pos

        match self.symbol:
            case "S":
                if row == self.row and col == self.col - 1:
                    return symbol in ("-", "F", "L")
                
                if row == self.row and col == self.col + 1:
                    return symbol in ("-", "J", "7")
                
                if row == self.row - 1 and col == self.col:
                    return symbol in ("|", "F", "7")
                
                if row == self.row + 1 and col == self.col:
                    return symbol in ("|", "J", "L")

            case "7":  # ╗
                if row == self.row and col == self.col - 1:
                    return symbol in ("-", "F", "L")
                
                if row == self.row + 1 and col == self.col:
                    return symbol in ("|", "J", "L")
                
            case "F":  # ╔
                if row == self.row and col == self.col + 1:
                    return symbol in ("-", "J", "7")
                
                if row == self.row + 1 and col == self.col:
                    return symbol in ("|", "J", "L")

            case "J":  # ╝
                if row == self.row and col == self.col - 1:
                    return symbol in ("-", "L", "F")
                
                if row == self.row - 1 and col == self.col:
                    return symbol in ("|", "F", "7", )

            case "L":  # ╚
                if row == self.row and col == self.col + 1:
                    return symbol in ("-", "7", "J")
                
                if row == self.row - 1 and col == self.col:
                    return symbol in ("|", "7", "F")

            case "|":  # ║
                if col == self.col:
                    if row == self.row + 1:
                        return symbol in ("|", "J", "L")
                
                    if row == self.row - 1:
                        return symbol in ("|", "7", "F")

            case "-":  # ═ 
                if row == self.row:
                    if col == self.col + 1:
                        return symbol in ("-", "J", "7")
                
                    if col == self.col - 1:
                        return symbol in ("-", "L", "F")

        return False

    def __repr__(self) -> str:
        return f"{self.symbol} {self.pos}"
    

def solve(path: str):
    data = utils.read_lines(path)
    
    # Find Start position
    start_pipe = None
    for row, line in enumerate(data):
        col  = line.find("S")
        if col != -1:
            start_pipe = Pipe(symbol="S", pos=(row, col), steps=0)

    pipes = [start_pipe]
    visited = {}
    to_visit = [start_pipe]
    while to_visit:
        pipe = to_visit.pop(0)
        visited[pipe.pos] = None

        for row, col in utils.get_adjacent(*pipe.pos, matrix=data, include_corners=False):
            new_pos = (row, col)
            symbol = data[row][col]

            if new_pos in visited or new_pos in to_visit:
                continue

            if not pipe.can_connect(symbol, pos=new_pos):
                continue

            new_pipe = Pipe(symbol=symbol, pos=(row, col), steps=pipe.steps + 1)
            pipe.child = new_pipe
            to_visit.append(new_pipe)
            pipes.append(new_pipe)
            
            break

    points = [Point(*pipe.pos) for pipe in pipes]
    points.append(points[0])

    area = Polygon(points).area
    return int(area + 1 - ((len(points) - 1) / 2))


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")