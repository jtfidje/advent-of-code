import re
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str):
    data = utils.read_data(path)
    workflow_data, parts_data = data.split("\n\n")

    workflows = {}
    for w_name, rule_string in re.findall(r"(\w+){(.*)}", workflow_data):
        rule_list = rule_string.split(",")
        rule = ""
        for i, r in enumerate(rule_list):
            if "<" in r or ">" in r:
                comp, val = r.split(":")
                comp = comp.replace(">", " > ").replace("<", " < ")

                prefix = "if" if i == 0 else "elif"

                rule += f"{prefix} {comp}:\n    res = '{val}'\n"
            else:
                rule += f"else:\n    res = '{r}'"

        workflows[w_name] = compile(rule, filename="string", mode="exec")


    results = 0
    for ratings in parts_data.split():
        values = list(map(int, re.findall(r"\d+", ratings)))
        
        x, m, a, s = values
        res = "in"
        while True:
            if res == "A":
                results += sum(values)
                break

            if res == "R":
                break
            
            _locals = {"res": res, "x": x, "m": m, "a": a, "s": s}
            try:
                exec(workflows[res], None, _locals)
            except Exception as err:
                print(values, res)
                raise err
            res = _locals["res"]

    return results


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")