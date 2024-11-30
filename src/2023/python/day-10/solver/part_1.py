# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


class Pipe:
    def __init__(self, symbol: str, pos: tuple[int, int], steps: int):
        self.symbol = symbol
        self.pos = pos
        self.steps = steps
        self.row, self.col = pos

    def can_connect(self, symbol: str, pos: tuple[int, int]):
        row, col = pos

        if col == self.col:
            if row == self.row - 1:
                return symbol in ("7", "F", "|")

            if row == self.row + 1:
                return symbol in ("J", "L", "|")
            
        if row == self.row:
            if col == self.col - 1:
                return symbol in ("F", "-", "L")
            
            if col == self.col + 1:
                return symbol in ("7", "-", "J")
            

        return False


def solve(path: str):
    data = utils.read_lines(path)

    # Find Start position
    pipe = None
    for row, line in enumerate(data):
        col  = line.find("S")
        if col != -1:
            pipe = Pipe(symbol="S", pos=(row, col), steps=0)

    visited = {}
    to_visit = [pipe]
    max_steps = 0
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
            to_visit.append(new_pipe)
            
            max_steps = max(max_steps, new_pipe.steps)

    return max_steps
            

if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")