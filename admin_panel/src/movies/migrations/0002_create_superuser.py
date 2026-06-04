import os

from django.db import migrations


def create_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model
    from django.contrib.auth.hashers import make_password

    User = get_user_model()

    username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

    if not password:
        return

    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            "email": email,
            "is_staff": True,
            "is_superuser": True,
            "is_active": True,
            "password": make_password(password),
        },
    )

    # Если пользователь уже существует — ничего не делаем (идемпотентно).
    # Если хотите обновлять пароль при наличии env — можно добавить:
    # if not created:
    #     user.password = make_password(password)
    #     user.is_staff = True
    #     user.is_superuser = True
    #     user.is_active = True
    #     user.email = email
    #     user.save(update_fields=["password", "is_staff", "is_superuser", "is_active", "email"])


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(create_superuser, reverse_code=noop_reverse),
    ]