import re
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve_machine(machine):
    ax, ay, bx, by, px, py = machine
    x, y = 0, 0
    i = 1
    j = 0
    while i * ax < px:
        x = (ax * i) + (bx * j)
        y = (ay * i) + (by * j)

        if x > px or y > py:
            i += 1
            j = 0
            continue

        if x == px and y == py:
            return (i * 3) + j

        j += 1

    return 0


def solve_1(path: Path):
    data = utils.read_data(path).split("\n\n")
    total = 0
    for block in data:
        res = re.search(
            r"A: X\+(\d+), Y\+(\d+)\s+.*B: X\+(\d+), Y\+(\d+)\s+.*X=(\d+), Y=(\d+)",
            block,
            re.MULTILINE,
        )

        if res is None:
            raise ValueError("Invalid input")

        machine = list(map(int, res.groups()))

        total += solve_machine(machine)
    return total


def solve_2(path: Path):
    data = utils.read_lines(path)


if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
