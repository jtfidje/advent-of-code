# flake8: noqa: F401

from pathlib import Path
import re

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = utils.read_data(path)

    mults = re.finditer(r"mul\((\d+,\d+)\)", data)
    donts = re.finditer(r"(don\'t\(\))", data)
    dos = re.finditer(r"(do\(\))", data)

    commands = []

    for cmd in mults:
        commands.append(
            (cmd.start(), cmd.groups()[0])
        )

    for cmd in donts:
        commands.append(
            (cmd.start(), cmd.group())
        )

    for cmd in dos:
        commands.append(
            (cmd.start(), cmd.group())
        )

    active = True
    _sum = 0
    commands.sort(key=lambda x: x[0])
    for _, cmd in commands:
        match cmd:
            case "do()":
                active = True
            case "don't()":
                active = False
            case _:
                if active:
                    x, y = cmd.split(",")
                    _sum += int(x) * int(y)
    
    return _sum



if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")
