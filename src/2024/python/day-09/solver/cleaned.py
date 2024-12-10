from pathlib import Path
from typing import Iterable

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def map_sectors(disk_map: Iterable[int]) -> list[tuple[int | str, int]]:
    disk = []
    for i, num in enumerate(disk_map):
        if i % 2 == 0:
            _id = i // 2
            disk.append((_id, num))
        else:
            if num == 0:
                continue
            disk.append((".", num))
    return disk


def solve_1(path: Path):
    disk_map = map(int, utils.read_data(path))
    disk = []
    for sector_id, sector_size in map_sectors(disk_map):
        disk += [sector_id] * sector_size

    checksum = 0
    for i, value in enumerate(disk):
        if value == ".":
            tail_i, tail_value = next(
                (j, disk[j]) for j in range(len(disk) - 1, -1, -1) if disk[j] != "."
            )

            if tail_i < i:
                break

            disk[i] = tail_value
            disk[tail_i] = "."

        checksum += i * disk[i]

    return checksum


def solve_2(path: Path):
    data = utils.read_lines(path)


if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
