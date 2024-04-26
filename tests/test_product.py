def test_init(prod_1):
    assert prod_1.name == 'Samsung Galaxy C23 Ultra'
    assert prod_1.description == '256GB, Серый цвет, 200MP камера'
    assert prod_1.price == 180000.0
    assert prod_1.quantity == 5