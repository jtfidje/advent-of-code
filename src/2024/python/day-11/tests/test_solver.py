from pathlib import Path

import pytest

from solver import cleaned, part_1, part_2

data_path = Path(__file__).parent.parent.absolute() / "data"


# ------------------------------

answer_example_1 = 55312
answer_example_2 = 65601038650482

answer_part_1 = 172484
answer_part_2 = 205913561055242

# ------------------------------


def test_solve_1_run_example():
    answer = part_1.solve(data_path / "example_1.txt")
    if answer is None:
        assert True
    else:
        assert answer == answer_example_1


def test_solve_2_run_example():
    answer = part_2.solve(data_path / "example_2.txt")
    if answer is None:
        assert True
    else:
        assert answer == answer_example_2


def test_solve_1_run_input():
    assert part_1.solve(data_path / "input.txt") == answer_part_1


def test_solve_2_run_input():
    assert part_2.solve(data_path / "input.txt") == answer_part_2


def test_solve_1_cleaned_example():
    assert cleaned.solve_1(data_path / "example_1.txt") == answer_example_1


def test_solve_2_cleaned_example():
    assert cleaned.solve_2(data_path / "example_2.txt") == answer_example_2


def test_solve_1_cleaned_input():
    assert cleaned.solve_1(data_path / "input.txt") == answer_part_1


def test_solve_2_cleaned_input():
    assert cleaned.solve_2(data_path / "input.txt") == answer_part_2
