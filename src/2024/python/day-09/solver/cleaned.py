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
    disk = map_sectors(disk_map)

    compact_disk = []

    while disk:
        while (tail_block := disk.pop(-1))[0] == ".":
            continue

        if not disk:
            compact_disk.append(tail_block)
            break

        while (head_block := disk.pop(0))[0] != ".":
            compact_disk.append(head_block)

        if not disk:
            compact_disk.append(tail_block)
            break

        h_block_id, h_block_size = head_block
        t_block_id, t_block_size = tail_block

        if h_block_size > t_block_size:
            disk.insert(0, (".", h_block_size - t_block_size))
            compact_disk.append(tail_block)

        elif h_block_size < t_block_size:
            compact_disk.append((t_block_id, h_block_size))
            disk.append((t_block_id, t_block_size - h_block_size))

        else:
            compact_disk.append(tail_block)

    total = 0
    i = -1
    for block_id, block_size in compact_disk:
        for i in range(i + 1, i + block_size + 1):
            total += block_id * i

    return total


def solve_2(path: Path):
    disk_map = map(int, utils.read_data(path))
    disk = map_sectors(disk_map)

    compact_disk_head = []
    compact_disk_tail = []

    while disk:
        # Add file-blocks to compact disk
        if disk[0][0] != ".":
            compact_disk_head.append(disk.pop(0))
            continue

        t_block_id, t_block_size = tail_block = disk.pop(-1)

        # Insert dangling free space to compact_disk_tail
        # Continue parent loop in case this was the last block
        if t_block_id == ".":
            compact_disk_tail.insert(0, tail_block)
            continue

        for disk_i, head_block in enumerate(disk):
            h_block_id, h_block_size = head_block

            if h_block_id != ".":
                continue

            if h_block_size < t_block_size:
                continue

            compact_disk_tail.insert(0, (".", t_block_size))

            if h_block_size > t_block_size:
                disk[disk_i] = (".", h_block_size - t_block_size)
                disk.insert(disk_i, tail_block)
            else:
                disk[disk_i] = tail_block

            break

        else:
            # No free blocks for tail_block!
            compact_disk_tail.insert(0, tail_block)

    total = 0
    i = -1
    for block_id, block_size in [*compact_disk_head, *compact_disk_tail]:
        if block_id == ".":
            i += block_size
            continue

        for i in range(i + 1, i + block_size + 1):
            total += block_id * i

    return total


if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
