from src.item import Item


class Mixin:

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        return self


class Keyboard(Item, Mixin):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if value != "RU" and value != "EN":
            raise AttributeError(f"property 'language' of 'KeyBoard' object has no setter")
        self.__language = value

