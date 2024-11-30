
from day_21 import run

def test_solve_1_run_example():
    assert run.solve_1("example.txt") == 739785


def test_solve_2_run_example():
    assert run.solve_2("example.txt") == 444356092776315


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == 571032


def test_solve_2_run_input():
    assert run.solve_2("input.txt") == 49975322685009

