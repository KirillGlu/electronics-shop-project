import csv
import math

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

    # def __repr__(self):
    #     return f"{self.name} {self.price} {self.quantity}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, product):
        if len(product) > 10:
            self.__name = product[0:10]
        else:
            self.__name = product


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        Item.all = []
        with open('../homework-2/items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Item(row["name"], row["price"], row["quantity"])

    @staticmethod
    def string_to_number(number):
        if "." in number:
            return math.trunc(float(number))
        else:
            return int(number)


