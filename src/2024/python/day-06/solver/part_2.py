# flake8: noqa: F401
from copy import deepcopy
from pathlib import Path
from typing import Literal

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


move_map: dict[str, tuple[int, int]] = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}
next_state: dict[str, Literal["^", "v", ">", "<"]] = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}


def _regular_solve(guard_pos: tuple[int, int], obstacle_positions, grid):
    unique = set([guard_pos])
    state = "^"
    while True:
        new_pos = (
            guard_pos[0] + move_map[state][0],
            guard_pos[1] + move_map[state][1],
        )

        if new_pos in obstacle_positions:
            state = next_state[state]
            continue

        if utils.out_of_bounds(*new_pos, grid):
            break

        guard_pos = new_pos
        unique.add(guard_pos)
    return unique


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

    unique = _regular_solve(guard_pos, obstacle_positions, data)

    loop_counter = 0
    for r, c in unique:
        grid = deepcopy(data)
        if grid[r][c] == "^":
            continue

        grid[r][c] = "#"

        loop_counter += check_loop(grid)

    return loop_counter


def check_loop(grid: list[list[str]]):
    obstacle_positions = set()
    for row_i, row in enumerate(grid):
        for col_i, col in enumerate(row):
            match col:
                case "^":
                    guard_pos = (row_i, col_i, "^")
                case "#":
                    obstacle_positions.add((row_i, col_i))

    unique: set[tuple[int, int, str]] = set([guard_pos])
    while True:
        row, col, state = guard_pos
        new_pos = (
            row + move_map[state][0],
            col + move_map[state][1],
            state,
        )

        if new_pos in unique:
            return True

        if (new_pos[0], new_pos[1]) in obstacle_positions:
            guard_pos = (row, col, next_state[state])
            continue

        if utils.out_of_bounds(new_pos[0], new_pos[1], grid):
            return False

        guard_pos = new_pos
        unique.add(guard_pos)


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
