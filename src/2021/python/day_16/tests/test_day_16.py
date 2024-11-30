
from day_16 import run

def test_solve_1_run_example_1():
    assert run.solve_1("8A004A801A8002F478") == 16


def test_solve_1_run_example_2():
    assert run.solve_1("620080001611562C8802118E34") == 12


def test_solve_1_run_example_3():
    assert run.solve_1("C0015000016115A2E0802F182340") == 23


def test_solve_1_run_example_4():
    assert run.solve_1("A0016C880162017C3686B18A3D4780") == 31


def test_solve_2_run_example():
    assert run.solve_2("C200B40A82") == 3


def test_solve_2_run_example():
    assert run.solve_2("04005AC33890") == 54


def test_solve_2_run_example():
    assert run.solve_2("880086C3E88112") == 7


def test_solve_2_run_example():
    assert run.solve_2("CE00C43D881120") == 9


def test_solve_2_run_example():
    assert run.solve_2("D8005AC2A8F0") == 1


def test_solve_2_run_example():
    assert run.solve_2("F600BC2D8F") == 0


def test_solve_2_run_example():
    assert run.solve_2("9C005AC2F8F0") == 0


def test_solve_2_run_example():
    assert run.solve_2("9C0141080250320F1802104A08") == 1


def test_solve_1_run_input():
    input_data = run.read_line("input.txt")
    assert run.solve_1(input_data) == 883


def test_solve_2_run_input():
    input_data = run.read_line("input.txt")
    assert run.solve_2(input_data) == 1675198555015
