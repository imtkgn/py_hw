"""
    1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
    Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
    третьего (зеленый) — на ваше усмотрение.
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep
from itertools import cycle

class TrafficLight:
    _color = {"Красный": 7, "Желтый": 2, "Зеленый": 4}

    def running(self, repeat: int):
        i = 1
        for el in cycle(TrafficLight._color.items()):
            if i <= repeat:
                print(f" {el[0]} ", end='')
                for el in range(el[1]):
                    print(".", end='')
                    sleep(1)
                print('')
                i += 1
            else:
                break

my_traffic_light = TrafficLight()
my_traffic_light.running(10)
