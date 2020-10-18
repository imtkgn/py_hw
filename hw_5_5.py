"""
    5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

try:
    with open("hw_5_5_file_randnum.txt", 'w') as f_obj:
        f_obj.write(' '.join([str(randint(0, 100)) for el in range(3)]))
    with open("hw_5_5_file_randnum.txt") as f_obj:
        content = f_obj.readline()
        sum_num = sum(list(map(int, [el for el in content.split(" ") if el.isnumeric()])))
        print(f"Строка: {content}\nСумма чисел в строке: {sum_num}")
except IOError as err:
    print(f"Ошибка: {err}")
