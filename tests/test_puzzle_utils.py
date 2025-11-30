import json

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


def test_read_numbers(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("1\n2\n3")
    assert utils.read_numbers(str(test_file)) == [1, 2, 3]


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
def test_read_all_numbers(input_string: str, expected: list[list[int]], tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text(input_string)

    assert utils.read_all_numbers(test_file) == expected


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
    ],
)
def test_get_adjacent(pos, matrix, kwargs, expected):
    x, y = pos
    assert utils.get_adjacent(x, y, matrix, **kwargs) == expected
