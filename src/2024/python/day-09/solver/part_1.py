# flake8: noqa: F401
import re
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = list(map(int, list(utils.read_data(path))))
    disk = []

    for i, num in enumerate(data):
        if i % 2 == 0:
            _id = i // 2
            disk.append((_id, num))
        else:
            if num == 0:
                continue
            disk.append((".", num))

    sorted_disk = []
    while disk:
        block = disk.pop(0)

        if block[0] != ".":
            sorted_disk.append(block)
            continue

        try:
            while (last_block := disk.pop(-1))[0] == ".":
                continue
        except Exception:
            break

        if block[1] < last_block[1]:
            sorted_disk.append((last_block[0], block[1]))
            disk.append((last_block[0], last_block[1] - block[1]))

        elif block[1] > last_block[1]:
            sorted_disk.append(last_block)
            disk.insert(0, (block[0], block[1] - last_block[1]))

        else:
            sorted_disk.append(last_block)

    total = 0
    i = 0
    for block in sorted_disk:
        for _ in range(block[1]):
            total += block[0] * i
            i += 1

    return total


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
