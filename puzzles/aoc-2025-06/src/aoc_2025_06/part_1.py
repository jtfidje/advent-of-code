# flake8: noqa: F401
from functools import reduce
import re
from pathlib import Path

from advent_of_code import utils
from aoc_2025_06 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_data(path)
    data = re.sub(r" {2,}", " ", data).splitlines()
    
    number_lines = [list(map(int, line.strip().split(" "))) for line in data[:-1]]
    operators = re.sub(r" {2,}", " ", data[-1]).split()

    result = 0
    for *numbers, operator in zip(*number_lines, operators):
        result += reduce(lambda x, y: eval(f"{x} {operator} {y}"), numbers)        

    return result



if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
