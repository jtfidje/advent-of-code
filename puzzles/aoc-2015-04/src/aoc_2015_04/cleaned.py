import hashlib
from pathlib import Path

from advent_of_code.utils import read_data
from aoc_2015_04 import DATA_PATH

def solver(key: str, target: str) -> int:
    counter = 1
    while True:
        hex_hash = hashlib.md5(f"{key}{counter}".encode()).hexdigest()
        if hex_hash.startswith(target):
            return counter
        counter += 1

def solve_1(path: Path):
    data = read_data(path)
    return solver(key=data, target="00000")



def solve_2(path: Path):
    data = read_data(path)
    return solver(key=data, target="000000")
    


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
