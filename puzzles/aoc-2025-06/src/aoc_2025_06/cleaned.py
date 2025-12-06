import re
from pathlib import Path

from advent_of_code import utils
from aoc_2025_06 import DATA_PATH


def solve_1(path: Path):
    data = re.sub(r" {2,}", " ", utils.read_data(path)).splitlines()
    number_lines = map(lambda x: x.strip().split(), data[:-1])
    operators = data[-1].strip().split()

    return sum(
        eval(operator.join(numbers))
        for *numbers, operator in zip(*number_lines, operators)
    )


def solve_2(path: Path):
    data = utils.read_data(path).splitlines()

    number_lines = [line[::-1] for line in data[:-1]]
    operators = re.findall(r"(\S)", data[-1])[::-1]

    result = 0
    numbers, operator = [], operators.pop(0)
    for numbers_ in zip(*number_lines):
        if not all(num == " " for num in numbers_):
            numbers.append("".join(numbers_))
            continue

        result += eval(operator.join(numbers))
        numbers, operator = [], operators.pop(0)
    else:
        result += eval(operator.join(numbers))

    return result


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
