"""
    4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
    который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
    Выполните вызов методов и также покажите результат.

"""

from time import sleep
from random import randint

class Car:

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала.")
        sleep(3)

    def stop(self):
        sleep(3)
        print("Машина остановилась.")

    def tern(self, direction: str):
        print(f"Машина повернула {direction}.")
        sleep(1)

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}.")
        sleep(2)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Текущая скорость: {self.speed}. Превышение на {self.speed - 60} км/ч!")
            sleep(2)
        else:
            print(f"Текущая скорость: {self.speed}.")
            sleep(3)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Текущая скорость: {self.speed}. Превышение на {self.speed - 40} км/ч!")
            sleep(2)
        else:
            print(f"Текущая скорость: {self.speed}.")
            sleep(2)

class PoliceCar(Car):
    pass

town_car = TownCar(70, "red", "Toyota", False)
sport_car = SportCar(130, "red", "Ferrari", False)
work_car = WorkCar(50, "grey", "UAZ", False)
police_car = PoliceCar(170, "black", "Ford Police", True)

cars_list = [town_car, sport_car, work_car, police_car]
rand_num = randint(0, 3)

print(f"{cars_list[rand_num].name} {cars_list[rand_num].color}.")
cars_list[rand_num].go()
cars_list[rand_num].show_speed()
cars_list[rand_num].tern("Направо" if rand_num % 2 == 0 else "Налево")
cars_list[rand_num].stop()