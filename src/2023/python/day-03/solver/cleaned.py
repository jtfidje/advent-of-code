import re
from collections import defaultdict
from functools import reduce
from pathlib import Path

from solver.utils import read_lines, get_adjacent

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve_1(path: str) -> int:
    data = read_lines(path)

    result = 0
    for row, line in enumerate(data):
        # Find numbers
        for match in re.finditer(r"\d+", line):
            value = match.group()
            col = match.start()
            for r, c in get_adjacent(row, col, data, width=len(value)):
                char = data[r][c]
                if not char.isdigit() and char != ".":
                    result += int(value)
                    break
    
    return result


def solve_2(path: str):
    data = read_lines(path)

    gear_candidates = defaultdict(list)
    for row, line in enumerate(data):
        # Find numbers
        for match in re.finditer(r"\d+", line):
            value = match.group()
            col = match.start()
            for r, c in get_adjacent(row, col, data, width=len(value)):
                if data[r][c] == "*":
                    gear_candidates[(r, c)].append(int(value))

    total = 0
    for number_list in gear_candidates.values():
        if len(number_list) == 2:
            total += reduce(lambda x, y: x * y, number_list)

    return total


if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")