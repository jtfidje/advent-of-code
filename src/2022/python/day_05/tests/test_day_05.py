from day_05 import run, cleaned


def test_solve_1_run_example():
    assert run.solve_1("example.txt") == "CMZ"


def test_solve_2_run_example():
    assert run.solve_2("example.txt") == "MCD"


def test_solve_1_run_input():
    assert run.solve_1("input.txt") == "LJSVLTWQM"


def test_solve_2_run_input():
    assert run.solve_2("input.txt") == "BRQWDBBJM"


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
