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
    locked_disk = []

    while disk:
        ### Print
        # print(
        #     "".join(
        #         str(x[0]) * x[1]
        #         for x in [*sorted_disk, (" | ", 1), *disk, (" | ", 1), *locked_disk]
        #     )
        # )
        ###

        try:
            while disk[0][0] != ".":
                sorted_disk.append(disk.pop(0))
        except IndexError:
            break

        _file = disk.pop(-1)

        if _file[0] == ".":
            locked_disk.insert(0, _file)
            continue

        for block_i, _block in enumerate(disk):
            _block = disk[block_i]

            if _block[0] != ".":
                continue

            if _block[1] < _file[1]:
                continue

            disk.pop(block_i)

            if _block[1] == _file[1]:
                locked_disk.insert(0, _block)
                disk.insert(block_i, _file)

            else:
                disk.insert(block_i, (".", _block[1] - _file[1]))
                disk.insert(block_i, _file)

                locked_disk.insert(0, (".", _file[1]))

            break
        else:
            locked_disk.insert(0, _file)

    ### Print
    # print("".join(str(x[0]) * x[1] for x in sorted_disk))
    ###

    total = 0
    i = 0
    for block in [*sorted_disk, *disk, *locked_disk]:
        for _ in range(block[1]):
            if block[0] == ".":
                i += 1
                continue
            total += block[0] * i
            i += 1

    return total


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
