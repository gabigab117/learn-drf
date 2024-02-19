import pytest
from django.test import Client
from django.urls import reverse

from shop.models import Category
from .utils import format_datetime

client: Client = Client()


def test_category_list(active_category, inactive_category):
    response = client.get(reverse("category-list"))
    assert response.status_code == 200
    expected = {'count': 1, 'next': None, 'previous': None, 'results': [
        {'id': 1, 'name': 'Fruits', 'date_created': '2024-02-19T20:52:33.337187Z',
         'date_updated': '2024-02-19T20:52:33.337207Z', 'products': []}]}
    del expected["results"][0]["date_created"], expected["results"][0]["date_updated"]
    del response.json()["results"][0]["date_created"], response.json()["results"][0]["date_updated"]
    assert response.json() == expected


@pytest.mark.django_db
def test_create():
    assert not Category.objects.exists()
    response = client.post(reverse("category-list"))
    assert response.status_code == 405
    assert not Category.objects.exists()
