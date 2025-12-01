import pytest

from aoc_2015_01 import DATA_PATH, cleaned, part_1, part_2

# ------------------------------
answers_example_1 = [0, 0, 3, 3, 3, -1, -1, -3, -3]
answers_example_2 = [1, 5]

answer_part_1 = 232
answer_part_2 = 1783

# ------------------------------


@pytest.mark.parametrize("i", list(range(len(answers_example_1))))
def test_solve_1_run_example(i: int):
    answer = part_1.solve(DATA_PATH / f"example_1_{i + 1}.txt")
    assert answer == answers_example_1[i]


@pytest.mark.parametrize("i", list(range(len(answers_example_2))))
def test_solve_2_run_example(i: int):
    answer = part_2.solve(DATA_PATH / f"example_2_{i + 1}.txt")
    assert answer == answers_example_2[i]


def test_solve_1_run_input():
    assert part_1.solve(DATA_PATH / "input.txt") == answer_part_1


def test_solve_2_run_input():
    assert part_2.solve(DATA_PATH / "input.txt") == answer_part_2


@pytest.mark.parametrize("i", list(range(len(answers_example_1))))
def test_solve_1_cleaned_example(i: int):
    answer = cleaned.solve_1(DATA_PATH / f"example_1_{i + 1}.txt")
    assert answer == answers_example_1[i]


@pytest.mark.parametrize("i", list(range(len(answers_example_2))))
def test_solve_2_cleaned_example(i: int):
    answer = cleaned.solve_2(DATA_PATH / f"example_2_{i + 1}.txt")
    assert answer == answers_example_2[i]


def test_solve_1_cleaned_input():
    assert cleaned.solve_1(DATA_PATH / "input.txt") == answer_part_1


def test_solve_2_cleaned_input():
    assert cleaned.solve_2(DATA_PATH / "input.txt") == answer_part_2
