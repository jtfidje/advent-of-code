# flake8: noqa: F401
import itertools
from multiprocessing import Pool
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"

operators = ["*", "+", "||"]


def check_numbers(_input):
    target, numbers = _input
    num_ops = len(numbers) - 1
    for operator_combination in itertools.product(operators, repeat=num_ops):
        _operators = list(operator_combination)
        _numbers = numbers[:]
        stack = []
        while _numbers:
            stack.append(_numbers.pop(0))

            if len(stack) == 2:
                op = _operators.pop()
                if op == "||":
                    stack = ["".join(stack)]
                stack = [str(eval(op.join(stack)))]

        if int(stack[0]) == target:
            print(target)
            return True

    return False


def solve(path: str | Path):
    _data = utils.read_lines(path)
    data = []

    for line in _data:
        result, numbers = line.split(":")
        result = int(result)
        numbers = numbers.strip().split()

        data.append((result, numbers))

    with Pool(8) as pool:
        pool.map(check_numbers, data)  # type: ignore

    return 0


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
