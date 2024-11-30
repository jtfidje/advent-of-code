
from day_24 import run, cleaned

def test_solve_1_run_example_1():
    instructions = run.read_lines("example_1.txt")
    assert run.run_alu(instructions, 39) == 1

def test_solve_1_run_example_2():
    instructions = run.read_lines("example_2.txt")
    assert run.run_alu(instructions, 7) == 1

def test_solve_1_run_example_mul():
    instructions = [["inp", "z"], ["mul", "z","-1"]]
    assert run.run_alu(instructions, 1) == -1

    instructions = [["inp", "x"], ["inp", "y"], ["mul", "x", "y"], ["add", "z", "x"]]
    assert run.run_alu(instructions, 23) == 6


def test_alu_div():
    instructions = [["inp", "z"], ["div", "z", "2"]]
    assert run.run_alu(instructions, 5) == 2

#def test_solve_1_run_example_3():
#    instructions = run.read_lines("input.txt")
#    assert run.run_alu(instructions, 13579246899999) == 0


#def test_solve_2_run_example():
#    assert run.solve_2("example.txt") == None


#def test_solve_1_run_input():
#    assert run.solve_1("input.txt") == None
#
#
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



