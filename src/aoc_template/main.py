import subprocess
import sys
import time
from pathlib import Path

from loguru import logger

from aoc_template import utils
from aoc_template.config import settings

try:
    year, day = utils.parse_arguments()
except ValueError:
    sys.exit(1)

try:
    # Wait until 06:00:00 Europe/Oslo time
    utils.block_execution(int(year), int(day))
except KeyboardInterrupt:
    logger.info("Exiting... ")
    sys.exit(0)

# Setup URLs and Paths
aoc_base_url = f"https://adventofcode.com/{year}/day/{int(day)}"
project_path = Path(settings.project_root, "puzzles", f"aoc-{year}-{day}")
dest_src_path = Path(project_path, "src", f"aoc_{year}_{day}")

if not project_path.exists():
    logger.info(f"Creating puzzle workspace at {project_path}")
    subprocess.run(f"uv init --no-readme --lib {project_path}", shell=True)

    # Remove auto-generated files that we don't need or want
    subprocess.run(f"rm {dest_src_path}/py.typed", shell=True)

    # Copy template files
    logger.info("Copying template files")
    template_path = Path(settings.project_root, "src/aoc_template/templates")

    # Copy Python files
    subprocess.run(
        f"cp {template_path}/*.py {dest_src_path}/.",
        shell=True,
    )

    # Copy README
    subprocess.run(f"cp {template_path}/README.rst {project_path}/.", shell=True)

    # Inject package name into absolute import placeholder
    for py_file in dest_src_path.glob("*.py"):
        with open(py_file, "r+") as f:
            data = f.read()
            f.seek(0)
            f.write(data.replace("__PKG__", f"aoc_{year}_{day}"))

    # Run linter to fix import ordering
    subprocess.run(f"uv run ruff check {dest_src_path} --select I --fix", shell=True)

    # Fetch puzzle input and title
    logger.info("Fetching puzzle input and title")
    with utils.get_aoc_session() as session:
        puzzle_input = utils.fetch_puzzle_input(aoc_base_url, session)
        time.sleep(0.3)  # Be nice to the server?
        puzzle_title = utils.fetch_puzzle_title(aoc_base_url, session)

    # Write puzzle input to file
    logger.info("Writing puzzle input to file")
    data_path = project_path / "data"
    data_path.mkdir(exist_ok=True)
    with open(data_path / "input.txt", "w") as f:
        f.write(puzzle_input)

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

    # Start VSCode
    logger.info("Starting VSCode")
    utils.start_vscode(project_path)

# Start watcher
logger.info("Starting watcher!")
try:
    utils.start_watcher(dest_src_path)
except KeyboardInterrupt:
    logger.info("Exiting...")
    sys.exit(0)
