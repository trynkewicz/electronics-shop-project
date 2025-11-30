"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_create_item():
    # создаём экземпляр
    item = Item("Смартфон", 10000, 20)

    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20
    assert item in Item.all  # объект добавлен в список всех


def test_calculate_total_price():
    item = Item("Ноутбук", 20000, 5)
    assert item.calculate_total_price() == 20000 * 5


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    # задаём скидку
    Item.pay_rate = 0.8

    # применяем скидку только к item1
    item1.apply_discount()

    assert item1.price == 10000 * 0.8
    assert item2.price == 20000  # цена второго товара не изменяется

def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5

def test_name_setter():
    item = Item("Телефон", 10000, 5)
    item.name = "Смартфон"
    assert item.name == "Смартфон"

    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"  # первые 10 символов