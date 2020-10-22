"""
    3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
    name, surname, position (должность), income (доход).
    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
    оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
    В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
    проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


new_worker = Position("Ivan", "Ivanov", "manager", 100000, 50000)
new_worker_2 = Position("Petr", "Petrov", "director", 250000, 150000)

print(f"{new_worker.get_full_name()}, {new_worker.get_total_income()}")
print(f"{new_worker_2.get_full_name()}, {new_worker_2.get_total_income()}")

