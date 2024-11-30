import argparse
import os
import pathlib
import requests
import subprocess
from datetime import datetime

_year, _today = datetime.now().strftime("%Y,%d").split(",")

parser = argparse.ArgumentParser()
parser.add_argument(
    "year",
    type=str,
    help="AoC year (i.e.: 2021)",
    nargs="?",
    default=_year
)

parser.add_argument(
    "day",
    type=str,
    help="AoC Day as string (i.e.: 02)",
    nargs="?",
    default=_today
)
args = parser.parse_args()

year = args.year
day = args.day

aoc_input_url = f"https://adventofcode.com/{year}/day/{int(day)}/input"
project_path = f"{pathlib.Path(__file__).parent.absolute()}/day_{day}"


subprocess.run(["poetry", "new", f"day_{day}"])
os.chdir(project_path)
subprocess.run(["poetry", "update"])
subprocess.run(["touch", "example.txt", f"day_{day}/cleaned.py"])


print("Getting input from:", aoc_input_url)
sess = requests.Session()
sess.cookies.set("session", os.environ.get("AOC_SESSION"))
res = sess.get(aoc_input_url)
res.raise_for_status()

project_input_path = f"{project_path}/input.txt"
print("Writing input to:", project_input_path)
with open(project_input_path, "w") as f:
    f.write(res.text)

project_tests_path = f"{project_path}/tests/test_day_{day}.py"
print("Writing test templates into:", project_tests_path)
test_template = f"""
from day_{day} import run, cleaned

def test_solve_1_run_example():
    assert run.solve_1("example.txt") == None


def test_solve_2_run_example():
    assert run.solve_2("example.txt") == None


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
"""
with open(project_tests_path, "w") as f:
    f.write(test_template)

project_run_path = f"{project_path}/day_{day}/run.py"
print("Writing run templates into:", project_run_path)
run_template = f"""
from typing import List

def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def solve_1(path: str):
    data = read_lines(path)
    ...


def solve_2(path: str):
    data = read_lines(path)
    ...


if __name__ == "__main__":
    path = "example.txt"
    ans_1_example = solve_1(path)    
    ans_2_example = solve_2(path)

    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)
    
    print(f"Example 1: {{ans_1_example}}")
    print(f"Example 2: {{ans_2_example}}")
    print("\\n- - -\\n")
    print(f"Problem 1: {{ans_1_input}}")
    print(f"Problem 2: {{ans_2_input}}")
"""
with open(project_run_path, "w") as f:
    f.write(run_template)

project_readme_path = f"{project_path}/README.rst"
print("Writing README template into:", project_readme_path)
readme_template = """
**************************
--- Day xxx: yyy ---
**************************
`<https://adventofcode.com/2021/day/xxx>`_


Personal Stats:
###############


========  ====  =====  ========  ====  =====
Part 1                 Part 2       
---------------------  ---------------------
Time      Rank  Score  Time      Rank  Score
========  ====  =====  ========  ====  =====
zzzz
========  ====  =====  ========  ====  =====
"""
with open(project_readme_path, "w") as f:
    f.write(readme_template)

# Starting watchdog!
try:
    subprocess.run(
        f"while inotifywait -re modify {project_path}; do poetry run pytest tests/; done",
        shell=True
    )
except KeyboardInterrupt:
    ...
