# flake8: noqa: F401
import re
from functools import reduce
from pathlib import Path

from advent_of_code import utils
from aoc_2025_06 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_data(path).splitlines()

    number_lines = [line[::-1] for line in data[:-1]]
    operators = re.sub(r" {2,}", " ", data[-1]).strip().split()[::-1]

    result = 0

    operator = operators.pop(0)
    numbers = []
    for numbers_ in zip(*number_lines):
        if all(num == " " for num in numbers_):
            expression = f"{operator}".join(numbers)
            result += eval(expression)
            operator = operators.pop(0)
            numbers = []
        else:
            numbers.append("".join(numbers_))
    expression = f"{operator}".join(numbers)
    result += eval(expression)

    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
