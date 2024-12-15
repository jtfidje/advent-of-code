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
    num_moves = 0
    while moves:
        num_moves += 1
        move = moves.pop(0)

        if 21 < num_moves < 24:
            grid[current_pos[0]][current_pos[1]] = "@"
            print(move)
            print_grid(grid)
            print()
            grid[current_pos[0]][current_pos[1]] = "."

        velocity = move_map[move]
        row_j, col_j = next_pos = get_next_pos(current_pos, velocity)
        next_char = grid[row_j][col_j]

        if next_char == "#":
            continue

        if next_char == ".":
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
            match next_char:
                case "[":
                    boxes = [(next_pos, (row_j, col_j + 1))]
                case "]":
                    boxes = [((row_j, col_j - 1), next_pos)]

            visited = []

            while boxes:
                box = boxes.pop(0)
                visited.append(box)
                for point in box:
                    next_r, next_c = next_point = get_next_pos(point, velocity)

                    match grid[next_r][next_c]:
                        case "#":
                            break

                        case ".":
                            continue

                        case "[":
                            new_box = (next_point, (next_r, next_c + 1))

                        case "]":
                            new_box = ((next_r, next_c - 1), next_point)

                    if new_box in [*visited, *boxes]:
                        continue

                    boxes.append(new_box)
                else:
                    # No breaks - go to next
                    continue

                # We only hit this if # - break out of while loop
                break

            else:
                # No breaks - let's shift the boxes
                for b1, b2 in visited[::-1]:
                    match move:
                        case "v":
                            grid[b1[0] + 1][b1[1]] = grid[b1[0]][b1[1]]
                            grid[b2[0] + 1][b2[1]] = grid[b2[0]][b2[1]]
                        case "^":
                            grid[b1[0] - 1][b1[1]] = grid[b1[0]][b1[1]]
                            grid[b2[0] - 1][b2[1]] = grid[b2[0]][b2[1]]
                    grid[b1[0]][b1[1]] = "."
                    grid[b2[0]][b2[1]] = "."

                current_pos = next_pos

    # grid[current_pos[0]][current_pos[1]] = "@"
    # print_grid(grid)
    return sum(
        (row_i * 100) + col_i
        for row_i, row in enumerate(grid)
        for col_i, col in enumerate(row)
        if col == "["
    )


def print_grid(grid):
    for line in grid:
        print("".join(line))


def get_next_pos(current, velocity):
    return (current[0] + velocity[0], current[1] + velocity[1])


if __name__ == "__main__":
    # answer = solve(Path(data_path, "input.txt"))
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
