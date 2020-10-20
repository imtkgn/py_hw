"""
    6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
    практических и лабораторных занятий по этому предмету и их количество.
    Важно, чтобы для каждого предмета не обязательно были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
    Примеры строк файла:
    Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —

    Пример словаря:
    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
try:
    with open("hw_5_6_file.txt") as f_obj:
        my_list = list()
        for line in f_obj:
            subject = line[:line.index(":")]
            hours, num = [], ""
            for i, el in enumerate(line):
                if el.isnumeric() and line[i+1].isnumeric():
                    num += el
                elif el.isnumeric() and line[i+1].isnumeric() == False:
                    num += el
                    hours.append(int(num))
                    num = ""
            my_list.append([subject, sum(hours)])
        print(dict(my_list))
except IOError as err:
    print(f"Ошибка: {err}")


