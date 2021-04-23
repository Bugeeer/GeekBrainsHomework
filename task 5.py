"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationety:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationety):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка ручкой")


class Pencil(Stationety):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка карандашом")


class Handle(Stationety):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Отрисовка маркером")


stationery_1 = Stationety("Канцелярские принадлежности")
pen_1 = Pen('Синяя ручка')
pencil_1 = Pencil('Красный карандаш')
handle_1 = Handle("Черный маркер")

stationery_1.draw()
pen_1.draw()
pencil_1.draw()
handle_1.draw()
