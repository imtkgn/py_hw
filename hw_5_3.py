"""
    3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
    Выполнить подсчет средней величины дохода сотрудников.
"""
try:
    with open("hw_5_3_file.txt") as f_obj:
        sum_salaries, cnt_workers, low_salary = 0, 0, []
        for line in f_obj:
            worker = ''.join([el for el in line[:line.index("руб")] if el.isalpha()])
            cnt_workers += 1
            salary = float(''.join([el for el in line if el.isnumeric()]))
            sum_salaries += salary
            if salary < 20000:
                low_salary.append(worker)
        print(f"Фамилии сотрудников с окладом ниже 20000 руб: {', '.join(low_salary)}")
        print(f'Средняя величина дохода сотрудника: {round(sum_salaries / cnt_workers, 2)} руб.')
except IOError as err:
    print(f"Ошибка: {err}")