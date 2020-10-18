"""
    4. Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
    При этом английские числительные должны заменяться на русские.
    Новый блок строк должен записываться в новый текстовый файл.
"""

def create_new_file(text_ins):
    try:
        with open("new_file_numbers.txt", 'w') as f_obj:
            f_obj.write(text_ins)
            print(f"В файл {f_obj.name} добавлен текст:\n{text_ins}")
    except IOError as err:
        print(f"Ошибка: {err}")
try:
    with open("hw_5_4_file.txt") as f_obj:
        rus_numbers = ["Ноль", "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять"]
        temp_list, text_ins = [], ""
        for line in f_obj:
            try:
                temp_list = line.split(" ")
                temp_list[0] = rus_numbers[int(''.join([el for el in line if el.isnumeric()]))]
                text_ins += ' '.join(temp_list)
            except Exception as err:
                text_ins += line
                print(f"Ошибка: {err}\nЗаписали в файл что было в строке: \"{line}\"\n")
        create_new_file(text_ins)
except IOError as err:
    print(f"Ошибка: {err}")