from pathlib import Path

from solver.utils import read_lines

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve_1(path: str):
    data = read_lines(path)


def solve_2(path: str):
    data = read_lines(path)


if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")