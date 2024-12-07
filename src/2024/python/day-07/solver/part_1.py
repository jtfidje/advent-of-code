# flake8: noqa: F401
import itertools
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    _data = utils.read_lines(path)
    data = []

    for line in _data:
        result, numbers = line.split(":")
        result = int(result)
        numbers = numbers.strip().split()

        data.append((result, numbers))

    operators = ["*", "+"]

    _sum = 0
    for target, numbers in data:
        num_ops = len(numbers) - 1

        res = eval("*".join(numbers))

        if target > res:
            continue

        if target == res:
            _sum += res
            continue

        for i, operator_combination in enumerate(
            itertools.product(operators, repeat=num_ops)
        ):
            _operators = list(operator_combination)
            _numbers = numbers[:]
            if i == 0:
                continue

            stack = []
            while _numbers:
                stack.append(_numbers.pop(0))

                if len(stack) == 2:
                    op = _operators.pop()
                    stack = [str(eval(op.join(stack)))]

            if int(stack[0]) == target:
                _sum += target
                break

    return _sum


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
