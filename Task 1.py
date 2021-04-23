"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        self.__color = 'red'
        print(self.__color, end='')
        for i in range(7):
            time.sleep(1)
            print('.', end='')
        print('')
        self.__color = 'yellow'
        print(self.__color, end='')
        for i in range(2):
            time.sleep(1)
            print('.', end='')
        print('')
        self.__color = 'green'
        print(self.__color, end='')
        for i in range(12):
            time.sleep(1)
            print('.', end='')
        print('\n')
        self.__color = ''


traffic_light_1 = TrafficLight('')
traffic_light_1.running()
