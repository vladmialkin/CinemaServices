import pytest
from django.contrib.auth import get_user_model
from django.test import Client

from config.components import superuser_settings


@pytest.fixture
def superuser(db):
    User = get_user_model()
    username = superuser_settings.DJANGO_SUPERUSER_USERNAME

    user, _ = User.objects.get_or_create(
        username=username,
        defaults={
            "email": superuser_settings.DJANGO_SUPERUSER_EMAIL,
            "is_staff": True,
            "is_superuser": True,
        },
    )

    user.set_password(superuser_settings.DJANGO_SUPERUSER_PASSWORD.get_secret_value())
    user.is_staff = True
    user.is_superuser = True
    user.save(update_fields=["password", "is_staff", "is_superuser"])

    return user


@pytest.fixture
def admin_client(superuser):
    client = Client()
    client.force_login(superuser)
    return client

