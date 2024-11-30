# flake8: noqa: F401

from pathlib import Path
from functools import reduce

from solver.utils import (
    json_print,
    read_lines,
    read_numbers,
    sliding_window
)

data_path = Path(__file__).parent.parent.absolute() / "data"

class Number:
    def __init__(self, row: int):
        self.row = row
        self.value = ""
        self.positions = []
        self.adjacent = []

    def add_part(self, part: str, col: int):
        self.value += part
        self.positions.append((self.row, col))

        try:
            self.adjacent.remove((self.row, col))
        except Exception:
            ...

        # add left
        if not col == 0:
            self.adjacent.append((self.row, col - 1))

        # add right
        self.adjacent.append((self.row, col + 1))

        # add up
        if not self.row == 0:
            self.adjacent.append((self.row - 1, col))

        # add down
        self.adjacent.append((self.row + 1, col))

        # add down left
        if not col == 0:
            self.adjacent.append((self.row + 1, col - 1))

        # add down right
        self.adjacent.append((self.row + 1, col + 1))

        # add up left
        if not self.row == 0 and not col == 0:
            self.adjacent.append((self.row - 1, col - 1))

        # add up right
        if not self.row == 0:
            self.adjacent.append((self.row - 1, col + 1))


    def is_empty(self):
        return len(self.positions) == 0
    
    def __repr__(self) -> str:
        return self.value

def solve(path: str):
    data = read_lines(path)
    symbol_positions = {}
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbol_positions[(row, col)] = {"symbol": char, "part_numbers": []}
    
    numbers = []
    for row, line in(enumerate(data)):
        number = Number(row)
        for col, char in enumerate(line):
            if char.isdigit():
                number.add_part(char, col)
                continue
            
            if number.is_empty():
                continue

            numbers.append(number)
            number = Number(row)
        
        if not number.is_empty():
            numbers.append(number)

    # check positions
    for number in numbers:
        for pos in number.adjacent:
            symbol = symbol_positions.get(pos)
            if symbol is not None and symbol["symbol"] == "*":
                symbol["part_numbers"].append(number)
                break

    res = 0
    for symbol in symbol_positions.values():
        if symbol["symbol"] == "*" and len(symbol["part_numbers"]) == 2:
            res += reduce(lambda x, y: int(x.value) * int(y.value), symbol["part_numbers"])

    return res


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")