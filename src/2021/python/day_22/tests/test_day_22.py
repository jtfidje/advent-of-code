
from day_22 import run, cleaned

def test_solve_1_run_example():
    assert run.solve_1("example.txt") == 590784


def test_solve_2_run_example():
    assert run.solve_1("example_2.txt") == 474140
    #assert run.solve_2("example_2.txt") == 2758514936282235


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == 547648


#def test_solve_2_run_input():
#    assert run.solve_2("input.txt") == None
#
#
#def test_solve_1_cleaned_example():
#    assert cleaned.solve_1("example.txt") == None
#
#
#def test_solve_2_cleaned_example():
#    assert cleaned.solve_2("example.txt") == None
#
#
#def test_solve_1_cleaned_input():
#    assert cleaned.solve_1("input.txt") == None
#
#
#def test_solve_2_cleaned_input():
#    assert cleaned.solve_2("input.txt") == None
