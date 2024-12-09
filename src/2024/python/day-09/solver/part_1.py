# flake8: noqa: F401
import re
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = list(map(int, list(utils.read_data(path))))
    disk = ""
    _disk = []

    blocks = []
    free = []

    for i, num in enumerate(data):
        if i % 2 == 0:
            _id = i // 2
            _disk.append((_id, num))
            disk += str(_id) * num
        else:
            _disk.append((".", num))
            disk += "." * num

    while True:
        if re.match(r"^\d+\.+$", disk):
            break

        next_free: re.Match[str] = re.search(r"\.+", disk)  # type: ignore
        # next_block: re.Match[str] = re.search(r"\d+\.*$", disk)  # type: ignore

        i_free = next_free.start()
        # i_block = next_block.start()

        free_count = next_free.end() - i_free

        next_block = ""
        i = len(disk)
        while len(next_block) < free_count:
            i -= 1
            char = disk[i]
            if disk[i] != ".":
                next_block += char

        disk = (
            disk[:i_free]
            + next_block
            + disk[i_free + free_count : i]
            + "." * len(disk[i:])
        )

    return sum(i * int(num) for i, num in enumerate(disk) if num != ".")


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
