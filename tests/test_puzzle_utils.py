import json
from typing import Any

import pytest

from advent_of_code import utils


def test_json_print(capsys):
    test_dict = {"key": "value"}
    utils.json_print(test_dict)
    captured = capsys.readouterr()
    assert captured.out == json.dumps(test_dict, indent=4) + "\n"


def test_read_data(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text(" Hello, World!\n")
    assert utils.read_data(str(test_file)) == "Hello, World!"


def test_read_lines(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text(" Line 1\nLine 2\n Line 3")
    assert utils.read_lines(test_file) == ["Line 1", "Line 2", "Line 3"]


@pytest.mark.parametrize(
    ["input_string", "expected"],
    [["Hello 3.14 world -3.14!\nWith 1337 integer", [3.14, -3.14, 1337.0]]],
)
def test_parse_floats(input_string: str, expected: list[float]):
    assert utils.parse_floats(input_string) == expected


def test_parse_floats__as_generator():
    input_string = "Hello 3.14 World!"

    gen = utils.parse_floats(input_string, as_generator=True)

    assert list(gen) == [3.14]
    assert list(gen) == []


@pytest.mark.parametrize(
    ["input_string", "expected"],
    [["Hello -13 world 37!\nWith 3.14 float", [-13, 37, 3, 14]]],
)
def test_parse_integers(input_string: str, expected: list[int]):
    assert utils.parse_integers(input_string) == expected


def test_parse_integers__as_generator():
    input_string = "Hello 1337 World!"

    gen = utils.parse_integers(input_string, as_generator=True)

    assert list(gen) == [1337]
    assert list(gen) == []


@pytest.mark.parametrize(
    ["input_string", "expected"],
    [
        ["1\n2\n3", [1, 2, 3]],
        ["Multiple 13 37 numbers\non 3.14 lines", [13, 37, 3, 14]],
    ],
)
def test_read_numbers(input_string: str, expected: list[int], tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text(input_string)
    assert utils.read_numbers(str(test_file)) == expected


@pytest.mark.parametrize(
    ["input_string", "expected"],
    [
        [
            "1 2 3\n4 5 6",
            [[1, 2, 3], [4, 5, 6]],
        ],
        [
            "1\n2\n3",
            [[1], [2], [3]],
        ],
        [
            "1\n20\n-300",
            [[1], [20], [-300]],
        ],
    ],
)
def test_read_line_numbers(input_string: str, expected: list[list[int]], tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text(input_string)

    assert utils.read_line_numbers(test_file) == expected


@pytest.mark.parametrize(
    "array, window_size, step, include_remainder, expected",
    [
        ([1, 2, 3, 4, 5], 3, None, False, [[1, 2, 3]]),
        ([1, 2, 3, 4, 5], 3, None, True, [[1, 2, 3], [4, 5]]),
        ([1, 2, 3, 4, 5], 2, 1, False, [[1, 2], [2, 3], [3, 4], [4, 5]]),
        ([1, 2, 3, 4, 5], 1, 1, True, [[1], [2], [3], [4], [5]]),
    ],
)
def test_sliding_window(array, window_size, step, include_remainder, expected):
    kwargs = {}
    if step is not None:
        kwargs["step"] = step
    if include_remainder is not None:
        kwargs["include_remainder"] = include_remainder

    assert (
        list(utils.sliding_window(array=array, window_size=window_size, **kwargs))
        == expected
    )


@pytest.mark.parametrize(
    "inp, expected",
    [
        ((0, 0), False),
        ((1, 1), False),
        ((-1, 0), True),
        ((0, 2), True),
        ((2, 0), True),
    ],
)
def test_out_of_bounds(inp: tuple[int, int], expected: bool):
    matrix = [[1, 2], [3, 4]]
    assert utils.out_of_bounds(*inp, matrix) is expected


@pytest.mark.parametrize(
    "pos, matrix, kwargs, expected",
    [
        (
            (1, 1),
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            {},
            {(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)},
        ),
        (
            (0, 0),
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            {"include_corners": False},
            {(0, 1), (1, 0)},
        ),
        (
            (1, 1),
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            {"width": 2, "height": 2},
            {(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)},
        ),
        (
            (1, 1),
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            {"return_values": True},
            {1, 2, 3, 4, 6, 7, 8, 9},
        ),
    ],
)
def test_get_adjacent(
    pos: tuple[int, int],
    matrix: list[list[int]],
    kwargs: dict[str, Any],
    expected: set,
):
    x, y = pos
    res = utils.get_adjacent(x, y, matrix, **kwargs)

    assert len(res) == len(expected)
    assert set(res) == expected
