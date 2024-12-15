# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = utils.read_data(path)

    grid, moves = data.split("\n\n")
    moves = list(moves.replace("\n", ""))
    grid = [list(line) for line in grid.split()]

    move_map = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    current_pos = next(
        (row_i, col_i)
        for row_i, row in enumerate(grid)
        for col_i, col in enumerate(row)
        if col == "@"
    )
    grid[current_pos[0]][current_pos[1]] = "."
    while moves:
        move = moves.pop(0)
        velocity = move_map[move]
        row_i, col_i = current_pos
        row_j, col_j = next_pos = get_next_pos(current_pos, velocity)

        if grid[row_j][col_j] == "#":
            continue

        if grid[row_j][col_j] == ".":
            current_pos = next_pos
            continue

        # We hit a rock - check lane
        temp_pos = next_pos
        while (char := grid[temp_pos[0]][temp_pos[1]]) == "O":
            row_k, col_k = temp_pos = get_next_pos(temp_pos, velocity)

        match char:
            case "#":
                # All rocks are up against a wall, we do nothing
                continue

            case ".":
                # Shift everything
                grid[row_k][col_k] = "O"
                grid[row_j][col_j] = "."  # <-- Represents our new position

        current_pos = next_pos

    return sum(
        (row_i * 100) + col_i
        for row_i, row in enumerate(grid)
        for col_i, col in enumerate(row)
        if col == "O"
    )


def get_next_pos(current, velocity):
    return (current[0] + velocity[0], current[1] + velocity[1])


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
