import pytest
from src.keyboard import Keyboard


def test_keyboard_init():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.name == "Dark Project KD87A"
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == "EN"


def test_keyboard_str_repr():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert repr(kb) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    assert kb.language == "EN"

    kb.change_lang()
    assert kb.language == "RU"

    kb.change_lang()
    assert kb.language == "EN"


def test_language_no_setter():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    with pytest.raises(AttributeError):
        kb.language = "CH"
