import pytest

from aoc_2024_01 import DATA_PATH, cleaned, part_1, part_2

# ------------------------------

answer_example_1 = ...
answer_example_2 = ...

answer_part_1 = ...
answer_part_2 = ...

# ------------------------------


def test_solve_1_run_example():
    answer = part_1.solve(DATA_PATH / "example_1.txt")
    if answer is None:
        assert True
    else:
        assert answer == answer_example_1


def test_solve_2_run_example():
    answer = part_2.solve(DATA_PATH / "example_2.txt")
    if answer is None:
        assert True
    else:
        assert answer == answer_example_2


@pytest.mark.skip()
def test_solve_1_run_input():
    assert part_1.solve(DATA_PATH / "input.txt") == answer_part_1


@pytest.mark.skip()
def test_solve_2_run_input():
    assert part_2.solve(DATA_PATH / "input.txt") == answer_part_2


@pytest.mark.skip()
def test_solve_1_cleaned_example():
    assert cleaned.solve_1(DATA_PATH / "example_1.txt") == answer_example_1


@pytest.mark.skip()
def test_solve_2_cleaned_example():
    assert cleaned.solve_2(DATA_PATH / "example_2.txt") == answer_example_2


@pytest.mark.skip()
def test_solve_1_cleaned_input():
    assert cleaned.solve_1(DATA_PATH / "input.txt") == answer_part_1


@pytest.mark.skip()
def test_solve_2_cleaned_input():
    assert cleaned.solve_2(DATA_PATH / "input.txt") == answer_part_2
