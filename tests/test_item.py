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