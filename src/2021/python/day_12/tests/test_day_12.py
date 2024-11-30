
from day_12 import run, cleaned

def test_solve_1_run_example_1():
    assert run.solve_1("example_1.txt") == 10


def test_solve_1_run_example_2():
    assert run.solve_1("example_2.txt") == 19


def test_solve_1_run_example_3():
    assert run.solve_1("example_3.txt") == 226


def test_solve_2_run_example():
    assert run.solve_2("example_1.txt") == 36


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == 3887


def test_solve_2_run_input():
    assert run.solve_2("input.txt") == 104834


def test_solve_1_cleaned_example_1():
    assert cleaned.solve_1("example_1.txt") == 10


def test_solve_1_cleaned_example_2():
    assert cleaned.solve_1("example_2.txt") == 19


def test_solve_1_cleaned_example_3():
    assert cleaned.solve_1("example_3.txt") == 226


def test_solve_2_cleaned_example():
    assert cleaned.solve_2("example_1.txt") == 36


def test_solve_1_cleaned_input():
    assert cleaned.solve_1("input.txt") == 3887


def test_solve_2_cleaned_input():
    assert cleaned.solve_2("input.txt") == 104834
