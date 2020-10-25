"""
    2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
    К типам одежды в этом проекте относятся пальто и костюм.
    У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
    Это могут быть обычные числа: V и H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
    Проверить работу этих методов на реальных данных.
    Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
    реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod

class Clothes(ABC):
    __sum_tissue_consumption = 0.0
    __secret_key = 'qwerty'

    def __init__(self, name: str, param: float):
        self.name = name
        self.param = param

    @abstractmethod
    def calc_tissue_consumption(self):
        pass

    @staticmethod
    def func_add_tissue_consumption(add_value: float, secret_key: str):
        if secret_key == Clothes.__secret_key:
            Clothes.__sum_tissue_consumption += add_value
        else:
            print("\nОблом! Неверный ключик ;)")

    @staticmethod
    def info_sum_tissue_consumption():
        return Clothes.__sum_tissue_consumption

class Coat(Clothes):
    def __init__(self, *args):
        super().__init__(*args)
        Clothes.func_add_tissue_consumption(self.calc_tissue_consumption, 'qwerty')

    @property
    def calc_tissue_consumption(self):
        return round(self.param / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Пальто "{self.name}", размер {self.param}. Расход ткани: {self.calc_tissue_consumption} ед.'

class Suit(Clothes):
    def __init__(self, *args):
        super().__init__(*args)
        Clothes.func_add_tissue_consumption(self.calc_tissue_consumption, 'qwerty')

    @property
    def calc_tissue_consumption(self):
        return round(2 * self.param + 0.3, 2)

    def __str__(self):
        return f'Костюм "{self.name}", рост {self.param}. Расход ткани: {self.calc_tissue_consumption} ед.'

my_coat = Coat("Сибиряк (муж.)", 40)
print(my_coat)
my_coat_2 = Coat("Снежная королева (жен.)", 30)
print(my_coat_2)

my_suit = Suit("Президент (муж.)", 1.7)
print(my_suit)
my_suit_2 = Suit("Школьник (муж.)", 1.4)
print(my_suit_2)

Clothes.func_add_tissue_consumption(50, 'password')
print(f"\nСуммарный расход ткани на производство одежды: {Clothes.info_sum_tissue_consumption()} ед.")

