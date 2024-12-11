# flake8: noqa: F401

from collections import defaultdict
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    numbers = defaultdict(int)

    for num in map(int, utils.read_data(path).split()):
        numbers[num] += 1

    for _ in range(75):
        new_numbers = defaultdict(int)
        for num, count in numbers.items():
            if num == 0:
                new_numbers[1] += count

            elif len((_num := str(num))) % 2 == 0:
                new_numbers[int(_num[: len(_num) // 2])] += count
                new_numbers[int(_num[len(_num) // 2 :])] += count

            else:
                new_numbers[num * 2024] += count
        numbers = new_numbers
    return sum(count for count in numbers.values())


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")
