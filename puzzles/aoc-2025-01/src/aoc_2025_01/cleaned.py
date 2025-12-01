from pathlib import Path

from advent_of_code.utils import read_lines
from aoc_2025_01 import DATA_PATH


def solve_1(path: Path):
    data = map(lambda line: (line[0], int(line[1:])), read_lines(path))

    dial = 50
    password = 0

    for direction, rotation in data:
        match direction:
            case "L":
                dial = (dial - rotation) % 100
            case "R":
                dial = (dial + rotation) % 100

        password += dial == 0
    
    return password
        
    
def solve_2(path: Path):
    data = map(lambda line: (line[0], int(line[1:])), read_lines(path))

    dial = 50
    password = 0

    for direction, rotation in data:
        match direction:
            case "R":
                value = dial + rotation
                password += value // 100

            case "L":
                value = dial - rotation
                password += (((value * -1) + 100) // 100) - int(dial == 0)
        
        dial = value % 100  # type: ignore
    
    return password


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
