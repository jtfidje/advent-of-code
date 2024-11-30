
from day_17 import run

def test_solve_1_run_example():
    assert run.solve_1("example.txt") == 45


def test_solve_2_run_example():
    assert run.solve_2("example.txt") == 112


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == 5050


def test_solve_2_run_input():
    assert run.solve_2("input.txt") == 2223


