from pathlib import Path

DATA_PATH = Path(__file__).parent.parent.parent.resolve() / "data"

__all__ = ["DATA_PATH"]
