"""
    Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
    который должен принимать данные (список списков) для формирования матрицы.
    Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
    класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
    Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
    складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix_list: list):
        self.matrix_list = matrix_list

    def __str__(self):
        str_mtx = ""
        for list_el in self.matrix_list:
            str_mtx += f'| {"   ".join([str(el) for el in list_el])} |\n'
        return str_mtx

    def __add__(self, other):
        list_sum_mtx = []
        for list_i, list_j in zip(self.matrix_list, other.matrix_list):
            list_sum_mtx.append([(el_i + el_j) for el_i, el_j in zip(list_i, list_j)])
        return Matrix(list_sum_mtx)


my_obj_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_obj_1)

my_obj_2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(my_obj_2)

my_obj_3 = (my_obj_1 + my_obj_2)
print(my_obj_3)