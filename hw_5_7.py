"""
    7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
    название, форма собственности, выручка, издержки.
    Пример строки файла: firm_1 ООО 10000 5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
    Если фирма получила убытки, в расчет средней прибыли ее не включать.
    Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
    Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
    Итоговый список сохранить в виде json-объекта в соответствующий файл.
    Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

    Подсказка: использовать менеджеры контекста.
"""

import json

try:
    with open("hw_5_7_file.txt") as f_obj:
        temp_list = [(line.replace('\n', '')).split(" ") for line in f_obj]
        comp_list, average_profit = [], []
        for i, comp in enumerate(temp_list):
            temp_list[i][2], temp_list[i][3] = int(temp_list[i][2]), int(temp_list[i][3])
            temp_list[i].append(temp_list[i][2] - temp_list[i][3])
        average_profit = [el[4] for el in temp_list if el[4] > 0]
        comp_list.append(dict([[el[0], el[4]] for el in temp_list]))
        comp_list.append({"average_profit": sum(average_profit) / len(average_profit)})
        print(comp_list)
    with open("company_list.json", "w") as json_obj:
        json.dump(comp_list, json_obj)
except IOError as err:
    print(f"Ошибка: {err}")