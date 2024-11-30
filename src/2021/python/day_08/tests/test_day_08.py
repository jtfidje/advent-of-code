
from day_08 import run, cleaned

def test_solve_1_run_example():
    assert run.solve_1("example.txt") == 26


def test_solve_2_run_example():
    assert run.solve_2("example.txt") == 61229


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == 512


def test_solve_2_run_input():
    assert run.solve_2("input.txt") == 1091165
