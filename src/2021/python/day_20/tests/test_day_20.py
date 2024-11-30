
from day_20 import run

def test_solve_1_run_example():
    assert run.solve_1("example.txt") == 35


def test_solve_2_run_example():
    assert run.solve_2("example.txt") == 3351


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == 5622


def test_solve_2_run_input():
    assert run.solve_2("input.txt") == 20395