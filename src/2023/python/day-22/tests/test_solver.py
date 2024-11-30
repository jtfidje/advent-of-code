from pathlib import Path

from solver import part_1, part_2, cleaned

data_path = Path(__file__).parent.parent.absolute() / "data"


def test_solve_1_run_example():
    answer = part_1.solve(data_path / "example_1.txt")
    if answer is None:
        assert True
    else:
        assert answer == 5


def test_solve_2_run_example():
    answer = part_2.solve(data_path / "example_2.txt")
    if answer is None:
        assert True
    else:
        assert answer == 7


# def test_solve_1_run_input():
#    assert part_1.solve(data_path / "input.txt") == ...
#
#
# def test_solve_2_run_input():
#    assert part_2.solve(data_path / "input.txt") == ...
#
#
# def test_solve_1_cleaned_example():
#    assert cleaned.solve_1(data_path / "example_1.txt") == ...
#
#
# def test_solve_2_cleaned_example():
#    assert cleaned.solve_2(data_path / "example_2.txt") == ...
#
#
# def test_solve_1_cleaned_input():
#    assert cleaned.solve_1(data_path / "input.txt") == ...
#
#
# def test_solve_2_cleaned_input():
#    assert cleaned.solve_2(data_path / "input.txt") == ...
