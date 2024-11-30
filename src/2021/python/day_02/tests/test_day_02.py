from day_02 import run, cleaned

def test_task_1_1():
    assert run.solve_1("example.txt") == 150

def test_task_2_1():
    assert run.solve_2("example.txt") == 900


def test_task_1_cleaned():
    assert cleaned.solve_1("example.txt") == 150

def test_task_2_cleaned():
    assert cleaned.solve_2("example.txt") == 900