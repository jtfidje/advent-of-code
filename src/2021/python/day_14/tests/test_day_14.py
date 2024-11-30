
from day_14 import run, cleaned

def test_solve_1_run_example():
    assert run.solve_1("example.txt") == 1588


def test_solve_2_run_example():
    assert run.solve_2("example.txt") == 2188189693529


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == 3118


def test_solve_2_run_input():
    assert run.solve_2("input.txt") == 4332887448171


def test_solve_1_cleaned_example():
    assert cleaned.solve(input_path="example.txt", runs=10) == 1588


def test_solve_2_cleaned_example():
    assert cleaned.solve(input_path="example.txt", runs=40) == 2188189693529


def test_solve_1_cleaned_input():
    assert cleaned.solve(input_path="input.txt", runs=10) == 3118


def test_solve_2_cleaned_input():
    assert cleaned.solve(input_path="input.txt", runs=40) == 4332887448171
