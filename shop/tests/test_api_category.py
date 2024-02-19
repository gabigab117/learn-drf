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
        {'id': active_category.id, 'name': active_category.name,
         'date_created': format_datetime(active_category.date_created),
         'date_updated': format_datetime(active_category.date_updated)}]}
    assert response.json() == expected


@pytest.mark.django_db
def test_create():
    assert not Category.objects.exists()
    response = client.post(reverse("category-list"))
    assert response.status_code == 405
    assert not Category.objects.exists()


def test_detail(active_category):
    response = client.get(reverse("category-detail", kwargs={"pk": active_category.id}))
    assert response.status_code == 200
    expected = {"id": active_category.id, "name": active_category.name,
                "date_created": format_datetime(active_category.date_created),
                "date_updated": format_datetime(active_category.date_updated),
                "products": list(active_category.products.filter(active=True))}
    assert response.json() == expected
