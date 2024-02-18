import pytest
from shop.models import Category, Product


@pytest.fixture()
def active_category(db):
    return Category.objects.create(name="Fruits", active=True)


@pytest.fixture()
def active_category_2(db):
    return Category.objects.create(name="Autre", active=True)


@pytest.fixture()
def inactive_category(db):
    return Category.objects.create(name="Légumes", active=False)


@pytest.fixture()
def active_product(db, active_category):
    return Product.objects.create(name="Banane", active=True, category=active_category)


@pytest.fixture()
def active_product_2(db, active_category_2):
    return Product.objects.create(name="Autre produit", active=True, category=active_category_2)


@pytest.fixture()
def inactive_product(db, active_category):
    return Product.objects.create(name="Sel", active=False, category=active_category)
