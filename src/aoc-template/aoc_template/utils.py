import argparse
import os
import re
import subprocess
import sys
import time
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Generator
from zoneinfo import ZoneInfo

from loguru import logger
from requests import Session
from rich import print

from aoc_template.config import settings


def block_execution(year: int, day: int):
    """Block execution until the time has passed a target time

    Target: {year}-12-{day}T06:00:00 Europe/Oslo
    """

    def puzzle_released(current: datetime, target: datetime) -> bool:
        return current >= target

    target_time = datetime(year, 12, day, 6, 0, 0, tzinfo=ZoneInfo("Europe/Oslo"))
    _now = datetime.now(tz=ZoneInfo("Europe/Oslo"))

    # NOTE: The early check here is to avoid the "waiting" message and the empty
    #       cleanup-printif the puzzle has already been released.
    if puzzle_released(_now, target_time):
        return

    msg_template = (
        f"  Waiting for puzzle to be released @ "
        f"{target_time.strftime('%d.%b %H:%M:%S')} ... "
    )
    while not puzzle_released(_now, target_time):
        print(
            f"[bold][grey74]{msg_template}[/grey74][grey46]"
            f"{_now.strftime('%d.%b %H:%M:%S')}[/grey46][/bold]",
            end="\r",
        )
        time.sleep(0.5)
        _now = datetime.now(tz=ZoneInfo("Europe/Oslo"))

    print()


def parse_arguments() -> tuple[str, str]:
    """Parse input arguments to get puzzle year and day

    Defaults to today's year and day

    Returns:
        tuple[str, str]: Returns the year and day to use
    """
    _year, _today = datetime.now().strftime("%Y %d").split()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "year", type=str, help="AoC year (i.e.: 2024)", nargs="?", default=_year
    )
    parser.add_argument(
        "day", type=str, help="AoC Day as string (i.e.: 02)", nargs="?", default=_today
    )
    args = parser.parse_args()

    return args.year, args.day


@contextmanager
def get_aoc_session() -> Generator[Session, None, None]:
    """Returns a requests.Session with the AoC session cookie set

    Returns:
        Session: The requests.Session with the AoC session cookie set
    """
    session = Session()
    session.cookies.set("session", settings.aoc_session)

    try:
        yield session
    finally:
        session.close()


def fetch_puzzle_input(puzzle_url: str, session: Session) -> str:
    """Fetches the puzzle input from the AoC website

    Args:
        puzzle_url (str): Puzzle URL to fetch the input for
        session (Session): The requests.Session to use for the request

    Returns:
        str: The puzzle input as a string
    """
    try:
        response = session.get(f"{puzzle_url}/input")
        response.raise_for_status()
    except Exception as err:
        logger.error(f"Failed to fetch puzzle input: {err}")
        sys.exit(1)

    return response.text


def fetch_puzzle_title(puzzle_url: str, session: Session) -> str:
    """Fetches the puzzle title from the AoC website

    Args:
        puzzle_url (str): Puzzle URL to fetch the title for
        session (Session): The requests.Session to use for the request

    Returns:
        str: The puzzle title as a string
    """
    try:
        response = session.get(f"{puzzle_url}")
        response.raise_for_status()
    except Exception as err:
        logger.error(f"Failed to fetch puzzle title: {err}")
        sys.exit(1)

    res = re.search(r"(--- Day \d+: .* ---)", response.text)

    if res is None:
        logger.error("Failed to parse puzzle title")
        sys.exit(1)

    return res[1]


def start_vscode(project_path: Path):
    """Starts VSCode in the project path and open relevant files

    Args:
        project_path (str): The path to the project to open
    """
    try:
        subprocess.run(
            (
                f"code --reuse-window "
                f"{project_path} "
                f"{project_path}/data/example_1.txt "
                f"{project_path}/data/example_2.txt "
                f"{project_path}/tests/test_solver.py "
                f"{project_path}/solver/part_1.py "
                f"{project_path}/solver/part_2.py "
                f"{project_path}/solver/utils.py "
                f"{project_path}/data/input.txt"
            ),
            shell=True,
        )
    except Exception as err:
        logger.error(f"Failed to start VSCode: {err}")
        sys.exit(1)


def start_watcher(project_path: Path):
    """Starts an inotifywait-watcher that performs the following on change:

      - clear the screen
      - run all tests
      - run the solvers

    Args:
        project_path (str): The path to the project to watch
    """
    os.chdir(project_path)
    subprocess.run(
        (
            "PYTHONDONOTWRITEBYTECODE=1 "
            f"VIRTUAL_ENV={project_path}/.venv "
            "bash -c '"
            f"while inotifywait -q -re modify {project_path} ; "
            "do clear && "
            "uv run pytest tests/ -p no:cacheprovider && "
            "uv run python solver/part_1.py && "
            "uv run python solver/part_2.py ; "
            "done'"
        ),
        shell=True,
    )
