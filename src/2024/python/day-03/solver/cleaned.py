import re
from pathlib import Path

from solver.utils import read_data

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve_1(path: Path):
    data = read_data(path)
    commands = re.findall(r"mul\(((\d+),(\d+))\)", data)
    
    return sum(
        int(x) * int(y) for _, x, y in commands
    )

def solve_2(path: Path):
    data = read_data(path)
    commands = re.findall(r"(mul\(\d+,\d+\)|don\'t\(\)|do\(\))", data)
    
    result = 0
    enabled = True
    for cmd in commands:
        match cmd:
            case "don't()":
                enabled = False
            
            case "do()":
                enabled = True

            case _:
                if not enabled:
                    continue

                x, y = re.search(r"(\d+),(\d+)", cmd).groups()  # type: ignore
                result += int(x) * int(y)

    return result


if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
