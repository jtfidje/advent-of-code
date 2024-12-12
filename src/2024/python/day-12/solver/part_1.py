# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = [list(line) for line in utils.read_lines(path)]
    _total_size = len(data) * len(data[0])

    visited = set()

    nodes = []
    regions = []
    current_region = {}
    while len(visited) != _total_size:
        if not nodes:
            if current_region:
                regions.extend(current_region.values())

            try:
                node = next(
                    (row_i, col_i)
                    for row_i, row in enumerate(data)
                    for col_i, col in enumerate(row)
                    if col != "."
                )
            except StopIteration:
                ...

            nodes = [node]
            current_region = {data[node[0]][node[1]]: []}

        current = nodes.pop()
        row_i, col_i = current
        value = data[row_i][col_i]

        if current in visited:
            continue
        else:
            visited.add(current)
            current_region[value].append(current)
            data[row_i][col_i] = "."

        for n in utils.get_adjacent(*current, data, include_corners=False):
            # Only add new values from the current region
            if value == data[n[0]][n[1]] and n not in visited:
                nodes.append(n)

    regions.extend(current_region.values())

    return 0


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
