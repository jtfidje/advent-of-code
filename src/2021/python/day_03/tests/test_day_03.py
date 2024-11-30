
from day_03 import run, cleaned

def test_solve_1_run_example():
    assert run.solve_1("example.txt") == 198


def test_solve_2_run_example():
    assert run.solve_2("example.txt") == 230


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == 1540244


def test_solve_2_run_input():
    assert run.solve_2("input.txt") == 4203981


def test_solve_1_cleaned_example():
    assert cleaned.solve_1("example.txt") == 198


def test_solve_2_cleaned_example():
    assert cleaned.solve_2("example.txt") == 230


def test_solve_1_cleaned_input():
    assert cleaned.solve_1("input.txt") == 1540244


def test_solve_2_cleaned_input():
    assert cleaned.solve_2("input.txt") == 4203981
