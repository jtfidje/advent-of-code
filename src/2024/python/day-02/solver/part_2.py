# flake8: noqa: F401
import math
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def check_diff(a, b):
    diff = abs(a - b)
    return 1 <= diff <= 3


def solve(path: str | Path):
    data = utils.read_lines(path)
    numbers_arr = []
    for line in data:
        numbers_arr.append(list(map(int, line.split(" "))))

    safe_count = 0
    for numbers in numbers_arr:
        # Check increase
        has_skipped = False
        skip_next = False
        # 50, 48, 49, 51, 53, 55, 56, 55
        for i, (x, y) in enumerate(utils.sliding_window([-1, *numbers], 2, 1)):
            if skip_next:
                skip_next = False
                continue

            if x >= y:
                if has_skipped:
                    break

                if i == len(numbers) - 2:
                    continue

                has_skipped = True
                skip_next = True
                z = numbers[i + 2]

                if x >= z:
                    break

                if check_diff(x, z):
                    continue

            else:
                if not check_diff:
                    break

                continue
        else:
            safe_count += 1
            continue

        # Check decrease
        has_skipped = False
        skip_next = False
        for i, (x, y) in enumerate(utils.sliding_window(numbers, 2, 1)):
            if skip_next:
                skip_next = False
                continue

            if x <= y:
                if has_skipped:
                    break

                if i == len(numbers) - 2:
                    continue

                has_skipped = True
                skip_next = True
                z = numbers[i + 2]
                if x <= z:
                    break

                if check_diff(x, z):
                    continue

            else:
                if not check_diff(x, y):
                    break

                continue
        else:
            # Check last window
            safe_count += 1
            continue

    return safe_count


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")
