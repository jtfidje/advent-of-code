from pathlib import Path

import pytest

from solver import cleaned, part_1, part_2

data_path = Path(__file__).parent.parent.absolute() / "data"


# ------------------------------

answer_example_1_1 = 2028
answer_example_1_2 = 10092
answer_example_2_1 = 105
answer_example_2_2 = 9021

answer_part_1 = 1463512
answer_part_2 = ...

# ------------------------------


def test_solve_1_run_example_1_1():
    answer = part_1.solve(data_path / "example_1_1.txt")
    if answer is None:
        assert True
    else:
        assert answer == answer_example_1_1


def test_solve_1_run_example_1_2():
    answer = part_1.solve(data_path / "example_1_2.txt")
    if answer is None:
        assert True
    else:
        assert answer == answer_example_1_2


def test_solve_2_run_example_2_1():
    answer = part_2.solve(data_path / "example_2_1.txt")
    if answer is None:
        assert True
    else:
        assert answer == answer_example_2_1


def test_solve_2_run_example_2_2():
    answer = part_2.solve(data_path / "example_2_2.txt")
    if answer is None:
        assert True
    else:
        assert answer == answer_example_2_2


def test_solve_1_run_input():
    assert part_1.solve(data_path / "input.txt") == answer_part_1


@pytest.mark.skip()
def test_solve_2_run_input():
    assert part_2.solve(data_path / "input.txt") == answer_part_2


@pytest.mark.skip()
def test_solve_1_cleaned_example():
    assert cleaned.solve_1(data_path / "example_1.txt") == answer_example_1_1


@pytest.mark.skip()
def test_solve_2_cleaned_example():
    assert cleaned.solve_2(data_path / "example_2.txt") == answer_example_2


@pytest.mark.skip()
def test_solve_1_cleaned_input():
    assert cleaned.solve_1(data_path / "input.txt") == answer_part_1


@pytest.mark.skip()
def test_solve_2_cleaned_input():
    assert cleaned.solve_2(data_path / "input.txt") == answer_part_2
