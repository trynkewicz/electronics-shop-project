import csv
import os

class InstantiateCSVError(Exception):
    pass

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только объекты Item или Phone.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            name = name[:10]
        self.__name = name


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename: str = 'items.csv'):
        """
        Создает объекты Item на основе данных файла CSV.
        """
        cls.all.clear()         # чтобы не накапливались объекты
        dir_path = os.path.dirname(__file__)  # папка src/
        full_path = os.path.join(dir_path, filename)

        if not os.path.exists(full_path):
            raise FileNotFoundError("Отсутствует файл item.csv")
        try:
            with open(full_path, encoding="cp1251") as f:
                reader = csv.DictReader(f)

                # Проверяем наличие нужных колонок
                if reader.fieldnames != ["name", "price", "quantity"]:
                    raise InstantiateCSVError("Файл item.csv поврежден")

                for row in reader:
                    if not (row.get("name") and row.get("price") and row.get("quantity")):
                        raise InstantiateCSVError("Файл item.csv поврежден")

                    cls(
                        row["name"],
                        cls.string_to_number(row["price"]),
                        cls.string_to_number(row["quantity"]),
                    )

        except UnicodeDecodeError:
            # Если файл имеет неверную кодировку — считаем его поврежденным
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(s: str) -> int:
        """
        Преобразует строку в число.
        '5' → 5
        '5.0' → 5
        '5.5' → 5
        """
        return int(float(s))
