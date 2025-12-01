import json
import re
from pathlib import Path
from collections.abc import Generator, Sequence


def json_print(obj: dict | list) -> None:
    """
    Print a JSON-formatted representation of the given object with indentation.

    Args:
        obj (dict | list): The object to be printed as JSON.
    """
    print(json.dumps(obj, indent=4))


def read_data(path: str | Path) -> str:
    """
    Read and return the contents of a file as a string.

    Args:
        path (str): The path to the file to be read.

    Returns:
        str: The contents of the file, with leading and trailing whitespace removed.
    """
    with open(path, "r") as f:
        return f.read().strip()


def read_lines(path: str | Path) -> list[str]:
    """
    Read lines from a file and return them as a list of stripped strings.

    Args:
        path (str | Path): The path to the file to be read.

    Returns:
        list[str]: A list of strings, each representing a line from the file.
    """
    return read_data(path).splitlines()


def read_numbers(path: str | Path) -> list[int]:
    """
    Read numbers from a file and return them as a list of integers.

    Args:
        path (str): The path to the file to be read.

    Returns:
        list[int]: A list of integers read from the file.
    """
    lines = read_lines(path)
    return list(map(int, lines))


def read_all_numbers(path: str | Path) -> list[list[int]]:
    """
    For each line in a file, read all numbers on that line

    Args:
        path (str | Path): The path to the file to be read.

    Returns:
        list[list[int]]: A list of lists of integers read from each line of the file.
    """
    lines = read_lines(path)
    data = [re.findall(r"(-?\d+)", line) for line in lines]
    data = [list(map(int, line)) for line in data]
    return data


def sliding_window(
    array: Sequence,
    window_size: int,
    step: int | None = None,
    include_remainder: bool = False,
) -> Generator[list, None, None]:
    """
    Generate sliding windows from the input array.

    Args:
        array (list): The input array to generate windows from.
        window_size (int): The size of each window.
        step (int | None, optional): The step size between windows. Defaults to window_size if None.
        include_remainder (bool, optional): If True, include the remaining elements
                                            that don't fill a complete window. Defaults to False.

    Yields:
        list: A window of the specified size from the input array.
    """  # noqa: E501
    if step is None:
        step = window_size

    for i in range(0, len(array) - window_size + 1, step):
        yield array[i : i + window_size]

    if include_remainder and i + step < len(array):  # type: ignore
        yield array[i + step :]  # type: ignore


def out_of_bounds(row: int, col: int, matrix: list[list]) -> bool:
    """
    Check if the given row and column are out of bounds in the matrix.

    Args:
        row (int): The row index to check.
        col (int): The column index to check.
        matrix (list[list]): The 2D matrix to check against.

    Returns:
        bool: True if the position is out of bounds, False otherwise.
    """
    if row < 0 or row >= len(matrix):
        return True

    if col < 0 or col >= len(matrix[0]):
        return True

    return False


def get_adjacent(
    row: int,
    col: int,
    matrix: list[list],
    width: int = 1,
    height: int = 1,
    include_corners: bool = True,
) -> set[tuple[int, int]]:
    """
    Get adjacent positions in a matrix for a given area.

    Args:
        row (int): Starting row of the area.
        col (int): Starting column of the area.
        matrix (list[list]): The 2D matrix.
        width (int, optional): Width of the area. Defaults to 1.
        height (int, optional): Height of the area. Defaults to 1.
        include_corners (bool, optional): Include corner positions. Defaults to True.

    Returns:
        set[tuple[int, int]]: Set of adjacent positions.

    Note:
        We use sets and tuples in this function for improved performance.
        Sets offer fast membership testing and uniqueness, while tuples are
        immutable and more memory-efficient than lists for storing coordinates.
    """
    skip_positions = set(
        (row + i, col + j) for i in range(height) for j in range(width)
    )

    if not include_corners:
        skip_positions.update(
            [
                (row - 1, col - 1),  # top left
                (row + height, col - 1),  # bottom left
                (row - 1, col + width),  # top right
                (row + height, col + width),  # bottom right
            ]
        )

    adjacent = set()
    row_range = range(row - 1, row + height + 1)
    col_range = range(col - 1, col + width + 1)

    for i in row_range:
        for j in col_range:
            position = (i, j)
            if position in skip_positions:
                continue

            if out_of_bounds(i, j, matrix):
                continue

            adjacent.add(position)

    return adjacent
