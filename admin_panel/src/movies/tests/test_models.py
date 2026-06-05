import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction

from movies.models import (
    FilmWork,
    Genre,
    GenreFilmWork,
    Person,
    PersonFilmWork,
    RolesChoice,
)

pytestmark = pytest.mark.django_db


def test_genre_film_work_unique_constraint():
    genre = Genre.objects.create(name="Action")
    film = FilmWork.objects.create(title="Matrix")

    GenreFilmWork.objects.create(genre=genre, film_work=film)

    with pytest.raises(IntegrityError):
        GenreFilmWork.objects.create(genre=genre, film_work=film)


def test_person_film_work_unique_constraint_by_role():
    person = Person.objects.create(full_name="Keanu Reeves")
    film = FilmWork.objects.create(title="Matrix")

    PersonFilmWork.objects.create(
        person=person,
        film_work=film,
        role=RolesChoice.ACTOR,
    )

    with transaction.atomic():
        with pytest.raises(IntegrityError):
            PersonFilmWork.objects.create(
                person=person,
                film_work=film,
                role=RolesChoice.ACTOR,
            )

    PersonFilmWork.objects.create(
        person=person,
        film_work=film,
        role=RolesChoice.PRODUCER,
    )


@pytest.mark.parametrize(
    "rating, should_raise",
    [
        (-1, True),
        (0, False),
        (50, False),
        (100, False),
        (101, True),
    ]
)
def test_film_work_rating_validators(rating, should_raise):
    film = FilmWork.objects.create(title="Marix", rating=rating)

    if should_raise:
        with pytest.raises(ValidationError):
            film.full_clean()
    else:
        film.full_clean()
