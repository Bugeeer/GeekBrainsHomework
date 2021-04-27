"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
классы для основных классов проекта и проверить работу декоратора @property.
"""
import abc


class Cloths(abc.ABC):

    @abc.abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Cloths):
    def __init__(self, v):
        self.V = v

    def size_height(self):
        return self.V

    def fabric_consumption(self):
        return self.V / 6.5 + 0.5


class Suit(Cloths):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if 0.75 < height < 2.5:
            self.__height = height
        elif 250 > height > 75:
            self.__height = height / 100
        else:
            print("Некорректная высота, введите данные в сантиметрах или метрах")

    def fabric_consumption(self):
        return self.height * 2 + 0.3


green_coat = Coat(48)
white_suit = Suit(175)

print(green_coat.fabric_consumption())
print(white_suit.fabric_consumption())
