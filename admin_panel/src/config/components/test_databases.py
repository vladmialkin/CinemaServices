from pydantic_settings import SettingsConfigDict

from .base import ENV_DIR
from .databases import PostgreSettings


class TestPostgreSettings(PostgreSettings):
    __test__ = False
    model_config = SettingsConfigDict(
        env_file=ENV_DIR.joinpath(".env.test"),
        case_sensitive=False,
        extra="allow",
    )


test_postgres_settings = TestPostgreSettings()
