"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Автомобиль начинает движение')

    def stop(self):
        print('Автомобиль останавливается')

    def turn(self, direction):
        print(f"Автомобиль поворачивает {direction}")

    def show_speed(self):
        print(f'Скорость {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        speed_limit = 60
        if self.speed <= speed_limit:
            print(f'Скорость {self.speed}')
        else:
            print(f'Скорость {self.speed}. Притормозите, скоростной лимит {speed_limit} км/час.')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        speed_limit = 40
        if self.speed <= speed_limit:
            print(f'Скорость {self.speed}')
        else:
            print(f'Скорость {self.speed}. Притормозите, скоростной лимит {speed_limit} км/час.')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car_1 = TownCar(95, 'красного', 'Бабуля на Renault Logan', False)
town_car_2 = TownCar(55, 'черного', 'Таксист Андрей на Hyundai Solaris', False)
sport_car_1 = SportCar(210, 'зеленого', "Евгений на Porshe 911", False)
work_car_1 = WorkCar(100, 'коричневого', "Абдул на KAMAZ", False)
work_car_2 = WorkCar(25, 'серого', "Сергей на Chevrolet Niva", False)
police_car = PoliceCar(100, 'синего', 'Полицейский на Lada Granta', True)


def drive(car=town_car_1):

    print(f'Это {car.name} {car.color} цвета.')
    car.go()
    car.show_speed()
    car.turn('направо')
    car.show_speed()
    print(f'Полиция пытается остановить {car.name}.')
    if car.is_police:
        print(f'Это полицейская машина, преследование прекращается')
    else:
        car.stop()


print('\n**************************************************************************\n')
drive(town_car_1)
print('\n**************************************************************************\n')
drive(town_car_2)
print('\n**************************************************************************\n')
drive(sport_car_1)
print('\n**************************************************************************\n')
drive(work_car_1)
print('\n**************************************************************************\n')
drive(work_car_2)
print('\n**************************************************************************\n')
drive(police_car)
