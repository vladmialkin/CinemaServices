from .base import Settings
from pydantic import SecretStr, EmailStr


class SuperUserSettings(Settings):
    DJANGO_SUPERUSER_USERNAME: str
    DJANGO_SUPERUSER_EMAIL: EmailStr
    DJANGO_SUPERUSER_PASSWORD: SecretStr


superuser_settings = SuperUserSettings()
