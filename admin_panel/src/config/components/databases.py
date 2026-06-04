from .base import Settings
from pydantic import SecretStr


class PostgreSettings(Settings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_HOST: str
    POSTGRES_PORT: int


postgres_settings = PostgreSettings()
