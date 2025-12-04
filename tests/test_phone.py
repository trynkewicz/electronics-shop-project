import pytest
from src.phone import Phone
from src.item import Item


def test_phone_init():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_phone_str_repr():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone) == "iPhone 14"
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add_phone_phone():
    p1 = Phone("A", 1000, 5, 2)
    p2 = Phone("B", 800, 3, 1)
    assert p1 + p2 == 8


def test_add_phone_item():
    p = Phone("A", 1000, 5, 2)
    i = Item("B", 500, 10)

    assert p + i == 15
    assert i + p == 15  # проверка __radd__

