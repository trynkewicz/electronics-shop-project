from src.item import Item

class LanguageMixin:
    """
    Миксин для хранения и переключения языка клавиатуры.
    """

    _supported_langs = ("EN", "RU")

    @property
    def language(self):
        return self._language

    def change_lang(self):
        """
        Меняет язык с EN -> RU -> EN.
        """
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self


class Keyboard(LanguageMixin, Item):
    """
    Клавиатура — товар с возможностью переключения языка.
    """

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = "EN"  # язык по умолчанию

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity})"

