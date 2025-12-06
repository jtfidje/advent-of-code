import json
import re
from collections.abc import Generator, Sequence
from pathlib import Path
from typing import Literal, overload


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


@overload
def parse_integers(s: str, as_generator: Literal[False] = ...) -> list[int]: ...


@overload
def parse_integers(s: str, as_generator: Literal[True]) -> map[int]: ...


def parse_integers(s, as_generator=False):
    """
    Finds all integers in a string, including negative

    :param s: String to pars integers from
    :type s: str
    :return: A list of all integers in string
    :rtype: list[int]
    """
    res = map(int, re.findall(r"(-?\d+)", s))
    if as_generator:
        return res

    return list(res)


def read_all_numbers(path: str | Path) -> list[list[int]]:
    """
    For each line in a file, read all numbers on that line

    Args:
        path (str | Path): The path to the file to be read.

    Returns:
        list[list[int]]: A list of lists of integers read from each line of the file.
    """
    lines = read_lines(path)
    data = [parse_integers(line) for line in lines]
    return data


def sliding_window[T](
    array: Sequence[T],
    window_size: int,
    step: int | None = None,
    include_remainder: bool = False,
) -> Generator[Sequence[T], None, None]:
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


@overload
def get_adjacent[T](
    row: int,
    col: int,
    matrix: Sequence[Sequence[T]],
    width: int = ...,
    height: int = ...,
    include_corners: bool = ...,
    *,
    return_values: Literal[True],
) -> list[T]: ...


@overload
def get_adjacent[T](
    row: int,
    col: int,
    matrix: Sequence[Sequence[T]],
    width: int = ...,
    height: int = ...,
    include_corners: bool = ...,
    *,
    return_values: Literal[False] = ...,
) -> set[tuple[int, int]]: ...


def get_adjacent(
    row, col, matrix, width=1, height=1, include_corners=True, return_values=False
):
    """
    Get adjacent positions in a matrix for a given area.

    Args:
        row (int): Starting row of the area.
        col (int): Starting column of the area.
        matrix (Sequence[Sequence[T]]): The 2D matrix.
        width (int, optional): Width of the area. Defaults to 1.
        height (int, optional): Height of the area. Defaults to 1.
        include_corners (bool, optional): Include corner positions. Defaults to True.
        return_values (bool, optional): If True, return values will contain the values
          at each position instead of the coordinates.

    Returns:
        set[tuple[int, int]] | list[T]: Set of adjacent positions or values.

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

    if return_values:
        return [matrix[x][y] for x, y in adjacent]

    return adjacent
