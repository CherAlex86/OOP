from src.category import Category


def test_init(category_products):
    assert category_products.name == 'Смартфоны'
    assert category_products.description == 'Удобные продвинутые'
    assert category_products.products[0].name == 'Samsung Galaxy C23 Ultra'
    assert Category.total_categories == 1
    assert Category.total_products == 1