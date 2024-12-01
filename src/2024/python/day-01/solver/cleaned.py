import re
from collections import defaultdict
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def _read_numbers(data: str) -> tuple[list[int], list[int]]:
    numbers = re.findall(r"^(\d+)\s+(\d+)$", data, flags=re.MULTILINE)
    
    left, right = [], []
    for n1, n2 in numbers:
        left.append(int(n1))
        right.append(int(n2))

    left.sort()
    right.sort()

    return (left, right)


def solve_1(path: Path):
    data = utils.read_data(path)
    left, right = _read_numbers(data)

    return sum(abs(n1 - n2) for n1, n2 in zip(left, right))


def solve_2(path: Path):
    data = utils.read_data(path)
    left, right = _read_numbers(data)
    
    number_count = defaultdict(int)
    for number in right:
        number_count[number] += 1

    return sum(number * number_count[number] for number in left)


if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
