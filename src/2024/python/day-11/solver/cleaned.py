from collections import defaultdict
from pathlib import Path
from typing import Iterable

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(data: Iterable[int], iterations: int) -> int:
    numbers = defaultdict(int)
    for num in data:
        numbers[num] += 1

    for _ in range(iterations):
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


def solve_1(path: Path):
    data = map(int, utils.read_data(path).split())
    return solve(data, 25)


def solve_2(path: Path):
    data = map(int, utils.read_data(path).split())
    return solve(data, 75)


if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
