# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = utils.read_data(path)

    grid_data, moves = data.split("\n\n")
    moves = list(moves.replace("\n", ""))
    grid_data = grid_data.split()

    grid = []
    for line in grid_data:
        row = ""
        for char in line:
            match char:
                case "#":
                    row += "##"
                case "O":
                    row += "[]"
                case ".":
                    row += ".."
                case "@":
                    row += "@."
        grid.append(list(row))

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

        # If we're going horizontally, nothing changes:
        if move in "<>":
            temp_pos = next_pos
            visited = [current_pos, next_pos]
            while (char := grid[temp_pos[0]][temp_pos[1]]) in "[]":
                temp_pos = get_next_pos(temp_pos, velocity)
                visited.append(temp_pos)
            match char:
                case "#":
                    # All boxes are up against a wall, we do nothing
                    continue

                case ".":
                    # Shift everything
                    visited.reverse()
                    for i in range(1, len(visited)):
                        # fmt: off
                        grid[visited[i - 1][0]][visited[i - 1][1]] = \
                        grid[visited[i][0]][visited[i][1]]
                        # fmt: on

            current_pos = next_pos

        # If however we're moving up or down, we need to check a window
        else:
            all_windows = []
            search_window = [next_pos]
            match grid[row_j][col_j]:
                case "[":
                    search_window.append((next_pos[0], next_pos[1] + 1))
                case "]":
                    search_window.append((next_pos[0], next_pos[1] - 1))

            while True:
                chars = [grid[r][c] for r, c in search_window]

                if "#" in chars:
                    break

                all_windows.append(search_window)

                if all(c == "." for c in chars):
                    break

                temp_r, temp_c = search_window[0]
                if grid[temp_r][temp_c] == "]":
                    # Increase window
                    search_window.insert(
                        0, (search_window[0][0], search_window[0][1] - 1)
                    )

                temp_r, temp_c = search_window[-1]
                if grid[temp_r][temp_c] == "[":
                    # Increase_window
                    search_window.insert(
                        0, (search_window[0][0], search_window[0][1] + 1)
                    )

                search_window = [get_next_pos(pos, velocity) for pos in search_window]

            all_windows.reverse()
            for i in range(1, len(all_windows)):
                for r, c in all_windows[i - 1]:
                    grid[r][c] = "."

                for r, c in all_windows[i]:
                    match move:
                        case "^":
                            grid[r - 1][c] = grid[r][c]
                        case "v":
                            grid[r + 1][c] = grid[r][c]

    grid[current_pos[0]][current_pos[1]] = "@"
    print_grid(grid)
    return sum(
        (row_i * 100) + col_i
        for row_i, row in enumerate(grid)
        for col_i, col in enumerate(row)
        if col == "O"
    )


def print_grid(grid):
    for line in grid:
        print("".join(line))


def get_next_pos(current, velocity):
    return (current[0] + velocity[0], current[1] + velocity[1])


if __name__ == "__main__":
    # answer = solve(Path(data_path, "input.txt"))
    answer = solve(Path(data_path, "example_test.txt"))
    print(f"Problem 1: {answer}")
