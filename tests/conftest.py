import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_products(prod_1):
    return Category('Смартфоны', 'Удобные продвинутые', [prod_1])


@pytest.fixture
def prod_1():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
