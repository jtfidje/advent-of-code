from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def _parse_reports(data: list[str]) -> list[list[int]]:
    return [list(map(int, line.split())) for line in data]


def _check_diff(a: int, b: int) -> bool:
    return 1 <= abs(a - b) <= 3


def _check_report(report: list[int]) -> bool:
    for direction in ("inc", "dec"):
        for a, b in utils.sliding_window(array=report, window_size=2, step=1):
            _check_dir = a > b if direction == "inc" else a < b

            if not _check_dir or not _check_diff(a, b):
                break
        else:
            return True

    return False


def solve_1(path: Path):
    data = utils.read_lines(path)
    reports = _parse_reports(data)

    return sum(_check_report(report) for report in reports)


def solve_2(path: Path):
    data = utils.read_lines(path)
    reports = _parse_reports(data)

    safe_count = 0
    for report in reports:
        if _check_report(report):
            safe_count += 1
            continue

        for i in range(len(report)):
            dampened_report = report[:]
            dampened_report.pop(i)

            if _check_report(dampened_report):
                safe_count += 1
                break

    return safe_count


if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
