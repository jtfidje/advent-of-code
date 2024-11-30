
from day_15 import run

def test_solve_1_run_example():
    assert run.solve_1("example.txt") == 40


def test_solve_2_run_example():
    assert run.solve_2("example.txt") == 315


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == 613


def test_solve_2_run_input():
    assert run.solve_2("input.txt") == 2899
