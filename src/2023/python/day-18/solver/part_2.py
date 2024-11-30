import math
import re
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def shoelace(points: list[tuple[int, int]], include_perimiter: bool=False) -> float:
    A = 0
    for a, b in zip(points, [*points[1:], points[0]]):
        A += (a[1] * b[0]) - (b[1] * a[0])
    
    A = abs(A * 0.5)

    if include_perimiter:
        min_rows = min(point[0] for point in points)
        max_rows = max(point[0] for point in points)
        min_cols = min(point[1] for point in points)
        max_cols = max(point[1] for point in points)

        A += ((max_rows - min_rows) + 1) + ((max_cols - min_cols) + 1)


    return A


def solve(path: str):
    # data = utils.read_data(path)
    # for match in re.finditer(r"([RDLU]) (\d)", data):
    #     direction, distance = match.groups()
    #     distance = int(distance)
    
    pos = (0,0)
    points = []
    perimiter = 0
    
    data = utils.read_data(path)
    for match in re.finditer(r"\(#([0-9a-f]{5})(\d)\)", data):
        distance, direction = match.groups()
        distance = int(distance, 16)

        match direction:
            case "0":
                pos = (
                    pos[0],
                    pos[1] + distance
                )
                points.append(pos)
                perimiter += distance
                    
            case "2":
                pos = (
                    pos[0], 
                    pos[1] - distance
                )
                points.append(pos)

            case "3":
                pos = (
                    pos[0] - distance, 
                    pos[1]
                )
                points.append(pos)
                perimiter += distance

            case "1":
                pos = (
                    pos[0] + distance, 
                    pos[1]
                )
                points.append(pos)

        res = shoelace(points) + perimiter + 1
    return int(res)


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    #answer = solve(Path(data_path, "example_2.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")