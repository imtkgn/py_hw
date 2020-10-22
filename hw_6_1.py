"""
    1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
    Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
    третьего (зеленый) — на ваше усмотрение.
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.

    Задачу можно усложнить, реализовав проверку порядка режимов,
    и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep

class TrafficLight:
    __color = {"Красный": 7, "Желтый": 2, "Зеленый": 4}

    def running(self):
        i = 1
        for el in TrafficLight.__color.items():
            print(f"{el[0]} ", end='')
            for el in range(el[1]):
                print(".", end='')
                sleep(1)
            print('')
            i += 1

my_traffic_light = TrafficLight()
my_traffic_light.running()
