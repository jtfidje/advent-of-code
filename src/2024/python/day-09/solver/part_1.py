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

        print(disk)

        next_free: re.Match[str] = re.search(r"\.+", disk)  # type: ignore
        next_block: re.Match[str] = re.search(r"\d+\.*$", disk)  # type: ignore

        i_free = next_free.start()
        i_block = next_block.start()

        free_count = next_free.end() - i_free
        print(disk[:i_free])
        print(disk[i_block:].replace(".", "")[-free_count:][::-1])
        print(disk[i_free + free_count : next_block.end() - free_count - 1])

        disk = (
            disk[:i_free]
            + disk[i_block:].replace(".", "")[-free_count:][::-1]
            + disk[i_free + free_count : next_block.start()]
            + "." * (len(disk[next_block.start() :]) - free_count)
        )
        print()

    return sum(i * int(num) for i, num in enumerate(disk) if num != ".")


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
