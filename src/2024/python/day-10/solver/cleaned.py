from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def get_starting_positions(topo_map: list[list[int]]) -> list[tuple[int, int]]:
    return [
        (row_i, col_i)
        for row_i, row in enumerate(topo_map)
        for col_i, col in enumerate(row)
        if col == 0
    ]


def solve_1(path: Path):
    topo_map = [list(map(int, line)) for line in utils.read_lines(path)]
    starting_points = get_starting_positions(topo_map)

    trailhead_score = 0
    for starting_point in starting_points:
        stack = [starting_point]
        visited = set()
        while stack:
            pos = stack.pop(-1)

            if pos in visited:
                continue
            visited.add(pos)

            row_i, col_i = pos
            value = topo_map[row_i][col_i]

            if value == 9:
                trailhead_score += 1
                continue

            for point in utils.get_adjacent(
                row_i, col_i, topo_map, include_corners=False
            ):
                if topo_map[point[0]][point[1]] == value + 1:
                    stack.append(point)

    return trailhead_score


def solve_2(path: Path):
    topo_map = [list(map(int, line)) for line in utils.read_lines(path)]
    starting_points = get_starting_positions(topo_map)

    trailhead_score = 0
    for starting_point in starting_points:
        stack = [starting_point]
        while stack:
            pos = stack.pop(-1)

            row_i, col_i = pos
            value = topo_map[row_i][col_i]

            if value == 9:
                trailhead_score += 1
                continue

            for point in utils.get_adjacent(
                row_i, col_i, topo_map, include_corners=False
            ):
                if topo_map[point[0]][point[1]] == value + 1:
                    stack.append(point)

    return trailhead_score


if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
