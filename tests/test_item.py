"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_product():
    return Item("ТВ", 15000, 2)


def test_calculate_total_price(test_product):
    assert test_product.calculate_total_price() == 30000


def test_apply_discount(test_product):
    Item.pay_rate = 0.8
    test_product.apply_discount()
    assert test_product.price == 12000


def test_name(test_product):
    test_product.name = 'Смартфон'
    assert test_product.name == 'Смартфон'
    test_product.name = 'СуперСмартфон'
    assert test_product.name == 'СуперСмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('34.2344234') == 34
    assert Item.string_to_number('14.0') == 14
    assert Item.string_to_number('5') == 5


def test___repr__(test_product):
    assert repr(test_product) == "Item('ТВ', 15000, 2)"
    product1 = Item('Планшет', 20990, 1)
    assert repr(product1) == "Item('Планшет', 20990, 1)"


def test___str__(test_product):
    assert str(test_product) == 'ТВ'
    product1 = Item('Планшет', 20990, 1)
    assert str(product1) == 'Планшет'


def test__str__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert str(phone1) == 'iPhone 14'


def test__add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0



