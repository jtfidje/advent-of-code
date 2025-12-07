import functools
import json
import re
import time
from collections.abc import Callable, Iterator, Sequence
from pathlib import Path
from typing import Any, Literal, overload


def performance_timer[**P, T](func: Callable[P, T]) -> Callable[P, T]:
    """
    Decorator that measures and prints the execution time of a function.

    :param func: The function to be timed.
    :type func: Callable[P, T]
    :return: A wrapper function that times the execution of the decorated function and returns its result.
    :rtype: Callable[P, T]

    .. note::
        Execution times less than 1 second are displayed in milliseconds,
        otherwise they are displayed in seconds. Both with 4 decimals.
    """  # noqa: E501

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        """
        Wrapper function that times the execution of the decorated function.

        :param args: Positional arguments to pass to the decorated function.
        :param kwargs: Keyword arguments to pass to the decorated function.
        :return: The result of the decorated function.
        :rtype: T
        """
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()

        if (elapsed := end - start) < 1:
            print(f"Elapsed: {(elapsed) * 1_000:.4f}ms")
        else:
            print(f"Elapsed: {(elapsed):.4f}s")

        return res

    return wrapper


def json_print(obj: dict | list) -> None:
    """
    Print a JSON-formatted representation of the given object with indentation.

    :param obj: The object to be printed as JSON.
    :type obj: dict | list
    """
    print(json.dumps(obj, indent=4))


def read_data(path: str | Path) -> str:
    """
    Read and return the contents of a file as a string.

    :param path: The path to the file to be read.
    :type path: str | Path
    :return: The contents of the file, with leading and trailing whitespace removed.
    :rtype: str
    """
    with open(path, "r") as f:
        return f.read().strip()


def read_lines(path: str | Path) -> list[str]:
    """
    Read lines from a file and return them as a list of stripped strings.

    :param path: The path to the file to be read.
    :type path: str | Path
    :return: A list of strings, each representing a line from the file.
    :rtype: list[str]
    """
    return [line.strip() for line in read_data(path).splitlines()]


@overload
def parse_floats(s: str, as_generator: Literal[False] = ...) -> list[float]: ...


@overload
def parse_floats(s: str, as_generator: Literal[True]) -> map[float]: ...


def parse_floats(s, as_generator=False):
    """
    Finds all floats in a string, including negative

    :param s: String to parse floats from
    :type s: str
    :return: A list of all floats in string
    :rtype: list[float]
    """
    res = map(float, re.findall(r"(-?\d+(?:\.\d+)?)", s))
    if as_generator:
        return res

    return list(res)


@overload
def parse_integers(s: str, as_generator: Literal[False] = ...) -> list[int]: ...


@overload
def parse_integers(s: str, as_generator: Literal[True]) -> map[int]: ...


def parse_integers(s, as_generator=False):
    """
    Finds all integers in a string, including negative

    :param s: String to parse integers from
    :type s: str
    :return: A list of all integers in string
    :rtype: list[int]
    """
    res = map(int, re.findall(r"(-?\d+)", s))
    if as_generator:
        return res

    return list(res)


def read_numbers(path: str | Path) -> list[int]:
    """
    Read all numbers in a file as integers and return them as a single list.

    :param path: The path to the file to be read.
    :type path: str | Path
    :return: A list of integers read from the file.
    :rtype: list[int]
    """
    with open(path, "r") as f:
        return parse_integers(f.read())


def read_line_numbers(path: str | Path) -> list[list[int]]:
    """
    For each line in a file, read all numbers on that line

    :param path: The path to the file to be read.
    :type path: str | Path
    :return: A list of lists of integers read from each line of the file.
    :rtype: list[list[int]]
    """
    lines = read_lines(path)
    data = [parse_integers(line) for line in lines]
    return data


def sliding_window[T](
    array: Sequence[T],
    window_size: int,
    step: int | None = None,
    include_remainder: bool = False,
) -> Iterator[Sequence[T]]:
    """
    Generate sliding windows from the input array.

    :param array: The input array to generate windows from.
    :type array: Sequence[T]
    :param window_size: The size of each window.
    :type window_size: int
    :param step: The step size between windows. Defaults to window_size if None.
    :type step: int | None
    :param include_remainder: If True, include the remaining elements that don't fill a complete window. Defaults to False.
    :type include_remainder: bool
    :return: A window of the specified size from the input array.
    :rtype: Iterator[Sequence[T]]
    """  # noqa: E501
    if step is None:
        step = window_size

    for i in range(0, len(array) - window_size + 1, step):
        yield array[i : i + window_size]

    if include_remainder and i + step < len(array):  # type: ignore
        yield array[i + step :]  # type: ignore


def out_of_bounds(row: int, col: int, matrix: Sequence[Sequence[Any]]) -> bool:
    """
    Check if the given row and column are out of bounds in the matrix.

    :param row: The row index to check.
    :type row: int
    :param col: The column index to check.
    :type col: int
    :param matrix: The 2D matrix to check against.
    :type matrix: Sequence[Sequence[Any]]
    :return: True if the position is out of bounds, False otherwise.
    :rtype: bool
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

    :param row: Starting row of the area.
    :type row: int
    :param col: Starting column of the area.
    :type col: int
    :param matrix: The 2D matrix.
    :type matrix: Sequence[Sequence[T]]
    :param width: Width of the area. Defaults to 1.
    :type width: int
    :param height: Height of the area. Defaults to 1.
    :type height: int
    :param include_corners: Include corner positions. Defaults to True.
    :type include_corners: bool
    :param return_values: If True, return values will contain the values at each position instead of the coordinates.
    :type return_values: bool
    :return: Set of adjacent positions or values.
    :rtype: set[tuple[int, int]] | list[T]

    .. note::
        We use sets and tuples in this function for improved performance.
        Sets offer fast membership testing and uniqueness, while tuples are
        immutable and more memory-efficient than lists for storing coordinates.
    """  # noqa: E501
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
