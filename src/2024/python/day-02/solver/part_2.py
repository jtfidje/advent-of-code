# flake8: noqa: F401
import math
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def check_diff(a, b):
    diff = abs(a - b)
    return 1 <= diff <= 3


def check_increase(numbers: list[int]) -> bool:
    for x, y in utils.sliding_window(numbers, 2, 1):
        if x >= y:
            return False

        if not check_diff(x, y):
            return False

    return True


def check_decrease(numbers: list[int]) -> bool:
    for x, y in utils.sliding_window(numbers, 2, 1):
        if x <= y:
            return False

        if not check_diff(x, y):
            return False

    return True


def solve(path: str | Path):
    data = utils.read_lines(path)
    numbers_arr: list[list[int]] = []
    for line in data:
        numbers_arr.append(list(map(int, line.split(" "))))

    safe_count = 0
    for numbers in numbers_arr:
        # Check increase
        if check_increase(numbers):
            safe_count += 1
            continue

        # Check decrease
        if check_decrease(numbers):
            safe_count += 1
            continue

        for i in range(len(numbers)):
            removed_numbers = numbers[:]
            removed_numbers.pop(i)
            # Check increase
            if check_increase(removed_numbers):
                safe_count += 1
                break

            # Check decrease
            if check_decrease(removed_numbers):
                safe_count += 1
                break

    return safe_count


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")
