from .base import Settings
from pydantic import SecretStr


class PostgreSettings(Settings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: SecretStr


postgres_settings = PostgreSettings()