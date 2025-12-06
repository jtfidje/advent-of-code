import pytest

from aoc_2015_12 import DATA_PATH, cleaned, part_1, part_2

# ------------------------------

answers_example_1 = [6, 6, 3, 3, 0, 0, 0, 0]
answers_example_2 = [6, 4, 0, 6]

answer_part_1 = 111754
answer_part_2 = 65402

# ------------------------------


@pytest.mark.parametrize("i", range(len(answers_example_1)))
def test_solve_1_run_example(i: int):
    answer = part_1.solve(DATA_PATH / f"example_1_{i + 1}.txt")
    if answer is None:
        assert True
    else:
        assert answer == answers_example_1[i]


@pytest.mark.parametrize("i", range(len(answers_example_2)))
def test_solve_2_run_example(i: int):
    answer = part_2.solve(DATA_PATH / f"example_2_{i + 1}.txt")
    if answer is None:
        assert True
    else:
        assert answer == answers_example_2[i]


def test_solve_1_run_input():
    assert part_1.solve(DATA_PATH / "input.txt") == answer_part_1


def test_solve_2_run_input():
    assert part_2.solve(DATA_PATH / "input.txt") == answer_part_2


@pytest.mark.parametrize("i", range(len(answers_example_1)))
def test_solve_1_cleaned_example(i: int):
    assert cleaned.solve_1(DATA_PATH / f"example_1_{i + 1}.txt") == answers_example_1[i]


@pytest.mark.parametrize("i", range(len(answers_example_2)))
def test_solve_2_cleaned_example(i: int):
    assert cleaned.solve_2(DATA_PATH / f"example_2_{i + 1}.txt") == answers_example_2[i]


def test_solve_1_cleaned_input():
    assert cleaned.solve_1(DATA_PATH / "input.txt") == answer_part_1


def test_solve_2_cleaned_input():
    assert cleaned.solve_2(DATA_PATH / "input.txt") == answer_part_2
