import re
from pathlib import Path

from solver.utils import (
    read_lines,
)

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str):
    data = read_lines(path)

    total = 0
    for game_number, line in enumerate(data, start=1):
        points = 0
        line = line.split(": ")[1]
        line = re.sub("[ ]{2,}", " ", line)
        winning, numbers = line.split(" | ")
        winning = set(map(int, re.findall(r"\d+", winning)))
        numbers = set(map(int, re.findall(r"\d+", numbers)))

        result = winning & numbers
        if len(result) == 1:
            total += 1
        elif len(result) > 1:
            points = 1
            for _ in range(len(result) - 1):
                points *= 2
            total += points
        else:
            ...
    
    return total

if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")