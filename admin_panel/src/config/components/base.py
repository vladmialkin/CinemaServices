from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = BASE_DIR.parent.parent.parent


class Settings(BaseSettings):
    DEBUG: bool = False
    model_config = SettingsConfigDict(
        env_file=ENV_DIR.joinpath(".env"), case_sensitive=False, extra="allow"
    )
