import re
from pathlib import Path

from advent_of_code import utils
from aoc_2015_10 import DATA_PATH


def solver(seq: str, iterations: int) -> int:
    for _ in range(iterations):
        new_seq = ""
        for match in re.finditer(r"(\d)\1*", seq):
            group = match.group()
            new_seq += str(len(group)) + group[0]
        seq = new_seq
    
    return len(seq)


def solve_1(path: Path):
    data = utils.read_data(path)
    return solver(data, 40)


def solve_2(path: Path):
    data = utils.read_data(path)
    return solver(data, 50)


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
