from day_01 import run, cleaned


def test_solve_1_run_example():
    assert run.solve_1("example_1.txt") == 142


def test_solve_2_run_example():
    assert run.solve_2("example_2.txt") == 281


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == 55712


def test_solve_2_run_input():
    assert run.solve_2("input.txt") == 55413


def test_solve_1_cleaned_example():
    assert cleaned.solve_1("example_1.txt") == 142


def test_solve_2_cleaned_example():
    assert cleaned.solve_2("example_2.txt") == 281


def test_solve_1_cleaned_input():
    assert cleaned.solve_1("input.txt") == 55712


def test_solve_2_cleaned_input():
    assert cleaned.solve_2("input.txt") == 55413
