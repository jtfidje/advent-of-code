import subprocess
import sys
import time
from pathlib import Path

from loguru import logger

from aoc_template import utils
from aoc_template.config import settings

year, day = utils.parse_arguments()

try:
    # Wait until 06:00:00 Europe/Oslo time
    utils.block_execution(int(year), int(day))
except KeyboardInterrupt:
    logger.info("Exiting... ")
    sys.exit(0)

# Setup URLs and Paths
aoc_base_url = f"https://adventofcode.com/{year}/day/{int(day)}"
project_path = Path(settings.project_root, year, "python", f"day-{day}")

if not project_path.exists():
    logger.info(f"Creating project at {project_path}")
    project_path.mkdir(parents=True)

    # Copy template files
    logger.info("Copying template files")
    subprocess.run(f"cp -r templates/. {project_path}/.", shell=True)

    # Fetch puzzle input and title
    logger.info("Fetching puzzle input and title")
    with utils.get_aoc_session() as session:
        puzzle_input = utils.fetch_puzzle_input(aoc_base_url, session)
        time.sleep(0.3)  # Be nice to the server?
        puzzle_title = utils.fetch_puzzle_title(aoc_base_url, session)

    # Write puzzle input to file
    logger.info("Writing puzzle input to file")
    with open(project_path / "data" / "input.txt", "w") as f:
        f.write(puzzle_input[:-1])  # Remove trailing newline

    # Replace placeholder vars in README.md
    logger.info("Replacing placeholder vars in README.md")
    with open(project_path / "README.rst", "r+") as f:
        readme = f.read().format(
            title=puzzle_title,
            year=year,
            day=day,
        )
        f.seek(0)
        f.write(readme)

    # Install dependencies and the project in the virtualenv
    logger.info("Installing dependencies and the project in the virtualenv")
    subprocess.run(["uv", "sync", "--directory", project_path])

    # Start VSCode
    logger.info("Starting VSCode")
    utils.start_vscode(project_path)

# Start watcher
logger.info("Starting watcher!")
try:
    utils.start_watcher(project_path)
except KeyboardInterrupt:
    logger.info("Exiting...")
    sys.exit(0)
