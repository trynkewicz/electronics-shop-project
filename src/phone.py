from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)

        if not isinstance(number_of_sim, int) or number_of_sim < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

        self.number_of_sim = number_of_sim

    def __repr__(self):
        super().__repr__()
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        else:
            return "Складывать можно только объекты Item или Phone."



