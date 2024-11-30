
from day_13 import run, cleaned

def test_solve_1_run_example():
    assert run.solve_1("example.txt") == 17


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == 671


def test_solve_1_cleaned_example():
    assert cleaned.solve_1("example.txt") == 17



def test_solve_1_cleaned_input():
    assert cleaned.solve_1("input.txt") == 671


