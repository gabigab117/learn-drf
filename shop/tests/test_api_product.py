import pytest
from pytest_django.asserts import assertContains, assertNotContains
from django.test import Client
from django.urls import reverse

from shop.models import Product
from .utils import format_datetime

client: Client = Client()


def test_product_list(active_product, inactive_product):
    response = client.get(reverse("product-list"))
    assert response.status_code == 200
    expected = {'count': 1, 'next': None, 'previous': None, 'results': [
        {'id': 1, 'date_created': '2024-02-19T20:54:33.762681Z', 'date_updated': '2024-02-19T20:54:33.762695Z',
         'name': 'Banane', 'category': 1}]}
    del expected["results"][0]["date_created"], expected["results"][0]["date_updated"]
    del response.json()["results"][0]["date_created"], response.json()["results"][0]["date_updated"]
    assert response.json() == expected


@pytest.mark.django_db
def test_create(active_category):
    assert not Product.objects.exists()
    response = client.post(reverse("product-list"), data={"name": "Courgette",
                                                          "category": active_category.id})
    assert response.status_code == 405


@pytest.mark.django_db
def test_delete(active_product):
    response = client.delete(reverse("product-detail", kwargs={"pk": active_product.id}))
    assert response.status_code == 405


def test_filter(active_product, active_product_2):
    response = client.get(f"{reverse("product-list")}?category_id=1")
    category_1_products_names = [product.name for product in Product.objects.filter(active=True, category=1)]
    category_2_products_names = [product.name for product in Product.objects.filter(active=True, category=2)]

    assertContains(response, category_1_products_names[0])
    assertNotContains(response, category_2_products_names[0])
