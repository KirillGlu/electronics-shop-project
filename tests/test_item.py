"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

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
