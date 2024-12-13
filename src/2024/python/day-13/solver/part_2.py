# flake8: noqa: F401
import re
from pathlib import Path

import sympy

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
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


def solve_machine(machine):
    ax, ay, bx, by, px, py = machine

    px += 10000000000000
    py += 10000000000000

    x, y = sympy.symbols("x y")

    eq1 = sympy.Eq(ax * x + bx * y, px)
    eq2 = sympy.Eq(ay * x + by * y, py)

    solution = sympy.solve((eq1, eq2), (x, y))

    if not isinstance(solution[x], sympy.core.numbers.Integer):
        return 0
    if not isinstance(solution[y], sympy.core.numbers.Integer):
        return 0

    return (solution[x] * 3) + solution[y]


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")
