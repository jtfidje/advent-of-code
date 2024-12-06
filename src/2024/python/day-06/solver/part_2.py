# flake8: noqa: F401

from pathlib import Path
from typing import Literal

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = utils.read_lines(path)
    data = [list(line) for line in data]

    obstacle_positions = set()
    for row_i, row in enumerate(data):
        for col_i, col in enumerate(row):
            match col:
                case "^":
                    guard_pos = (row_i, col_i)
                case "#":
                    obstacle_positions.add((row_i, col_i))

    state: Literal["^", "v", ">", "<"] = "^"
    next_state: dict[str, Literal["^", "v", ">", "<"]] = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^",
    }
    move_map = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    unique: set[tuple[int, int, str]] = set([(*guard_pos, "^")])
    while True:
        new_pos = (
            guard_pos[0] + move_map[state][0],
            guard_pos[1] + move_map[state][1],
        )

        if new_pos in obstacle_positions:
            state = next_state[state]
            continue

        if utils.out_of_bounds(*new_pos, data):
            break

        guard_pos = new_pos
        unique.add((*guard_pos, state))

    for i, row in enumerate(data):
        data[i] = list("".join(row).replace(".", " "))

    for row, col, _ in unique:
        data[row][col] = "."

    for row in data:
        print("".join(row))

    return 0


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
