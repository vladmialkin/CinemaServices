from .settings import *  # noqa
from .components import test_postgres_settings

ENVIRONMENT = "test"
DEBUG = False

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": test_postgres_settings.POSTGRES_DB,
        "USER": test_postgres_settings.POSTGRES_USER,
        "PASSWORD": test_postgres_settings.POSTGRES_PASSWORD.get_secret_value(),
        "HOST": test_postgres_settings.POSTGRES_HOST,
        "PORT": test_postgres_settings.POSTGRES_PORT,
        "OPTIONS": {
            'options': '-c search_path=public,content',
            "sslmode": "disable",
        },
    }
}