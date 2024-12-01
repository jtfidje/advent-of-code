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

    numbers_1 = sorted(numbers_1)
    numbers_2 = sorted(numbers_2)

    distances  = []
    for n1, n2 in zip(numbers_1, numbers_2):
        dist = abs(n1-n2)
        distances.append(dist)

    return sum(distances)

if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
