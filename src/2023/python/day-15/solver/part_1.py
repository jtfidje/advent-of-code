# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def compute_hash(char, current_value):
    _ascii = ord(char)
    
    current_value += _ascii
    current_value *= 17
    current_value %= 256

    return current_value


def solve(path: str):
    data = utils.read_data(path).split(",")

    results =0

    for element in data:
        value = 0
        for char in element:
            value = compute_hash(char, value)
        results += value

    return results


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")