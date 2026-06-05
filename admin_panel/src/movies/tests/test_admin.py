import pytest
from django.urls import reverse

from movies.models import FilmWork

pytestmark = pytest.mark.django_db


def test_admin_film_work_changelist_opens(admin_client):
    url = reverse("admin:movies_filmwork_changelist")
    response = admin_client.get(url)
    assert response.status_code == 200


def test_admin_film_work_changeform_opens(admin_client):
    film = FilmWork.objects.create(title="Matrix")
    url = reverse("admin:movies_filmwork_change", args=[film.pk])
    response = admin_client.get(url)
    assert response.status_code == 200


def test_admin_film_work_addform_opens(admin_client):
    url = reverse("admin:movies_filmwork_add")
    response = admin_client.get(url)
    assert response.status_code == 200
