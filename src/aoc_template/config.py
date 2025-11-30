from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    aoc_session: str = ""

    model_config = SettingsConfigDict(env_file=".env")

    @computed_field
    @property
    def project_root(self) -> Path:
        return Path(__file__).resolve().parent.parent.parent


settings = Settings()  # type: ignore
