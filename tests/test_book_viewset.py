from datetime import date
import pytest
from django.contrib.auth.models import User
from pytest_drf import (
    ViewSetTest,
    Returns200,
    UsesGetMethod,
    UsesDetailEndpoint,
    UsesListEndpoint,
    AsUser,
)
from pytest_lambda import lambda_fixture
from pytest_drf.util import url_for
from rest_framework.test import APIClient

from catalog.models import Book, User

user = lambda_fixture(
    lambda: User.objects.create(
        name="John",
        surname="Doe",
        email="john@doe.com",
    )
)

client = APIClient()


@pytest.mark.django_db
class TestBookViewSet(ViewSetTest, AsUser("user")):
    list_url = lambda_fixture(lambda: url_for("books-list"))
    detail_url = lambda_fixture(lambda book: url_for("books-detail", book.id))

    class TestList(
        UsesGetMethod,
        UsesListEndpoint,
        Returns200,
    ):
        book = lambda_fixture(
            lambda: [
                Book.objects.create(
                    title=i["title"],
                    description=i["descr"],
                    author=i["author"],
                    publish_date=i["pub_date"],
                )
                for i in [
                    {
                        "title": "Title #1",
                        "descr": "Lorem ipsum",
                        "author": "John Doe",
                        "pub_date": date.today(),
                    },
                    {
                        "title": "Title #2",
                        "descr": "Lorem ipsum",
                        "author": "John Doe",
                        "pub_date": date.today(),
                    },
                    {
                        "title": "Title #3",
                        "descr": "Lorem ipsum",
                        "author": "John Doe",
                        "pub_date": date.today(),
                    },
                ]
            ],
            autouse=True,
        )

    class TestRetrieve(
        UsesGetMethod,
        UsesDetailEndpoint,
        Returns200,
    ):
        book = lambda_fixture(
            lambda: Book.objects.create(
                title="Title #1",
                description="Lorem ipsum",
                author="John Doe",
                publish_date=date.today(),
            )
        )
