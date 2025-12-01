# flake8: noqa: F401
import hashlib
from pathlib import Path

from advent_of_code import utils
from aoc_2015_04 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_data(path)
    counter = 1
    while True:
        hex_hash = hashlib.md5(f"{data}{counter}".encode()).hexdigest()
        if hex_hash.startswith("00000"):
            return counter
        counter += 1


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
