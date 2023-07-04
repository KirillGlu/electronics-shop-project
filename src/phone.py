from src.item import Item


class Phone(Item):
    """
    Класс для представления телефонов в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
                Создание экземпляра класса Phone.

                :param name: Название товара.
                :param price: Цена за единицу товара.
                :param quantity: Количество товара в магазине.
                :param number_of_sim: Количество поддерживаемых сим-карт
                """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f"{self.name}"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Позволяет заменить количество сим карт, но количество не может быть менее 0"""
        if value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = value
