# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = utils.read_lines(path)

    numbers_1 = []
    numbers_2 = []
    for line in data:
        n1, n2 = line.split("   ")
        n1 = int(n1)
        n2 = int(n2)

        numbers_1.append(n1)
        numbers_2.append(n2)

    from collections import defaultdict
    number_count = defaultdict(int)

    for n in numbers_2:
        number_count[n] +=1

    _sum = 0
    for n in numbers_1:
        _sum += (n * number_count[n])

    return _sum
if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")
