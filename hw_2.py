print("Задание 1")

my_list = [1, 1.0, "str", True, [1, 45, 'bla bla'], (1, 'кортеж', 3), {'a', 'b', 'c'}, {'key_1': 1, 'key_2': 2, 'key_3': 3}, None, b'hello']

for i in my_list:
    print(type(i))

print("\nЗадание 2")
user_list = list(input("Введи любой текст:  "))

result = list()
temp_list = list()

for el in user_list:
    temp_list.append(el)
    if len(temp_list) == 2:
        temp_list.reverse()
        result.extend(temp_list)
        temp_list.clear()

result.extend(temp_list)
print("Результат:  ", ''.join(result))

print("\nЗадание 3")
month_num = input("Введи число месяца:  ")
list_data = [['Зима', '12', '1', '2'], ['Весна', '3', '4', '5'], ['Лето', '6', '7', '8'], ['Осень', '9', '10', '11']]
temp_list = list()
dist_data = {}

for el in list_data:
    temp_list.extend(el)
    try:
        if temp_list.index(month_num) > 0:
            print(f'Выборка из списка: {temp_list[0]}')
            break
    except Exception:
        temp_list.clear()

dist_data = {'12': 'Зима', '1': 'Зима', '2': 'Зима',
             '3': 'Весна', '4': 'Весна', '5': 'Весна',
             '6': 'Лето', '7': 'Лето', '8': 'Лето',
             '9': 'Осень', '10': 'Осень', '11': 'Осень'}
print(f'Выборка из словаря: {dist_data.get(month_num)}')

print("\nЗадание 4")
user_text = input("Напиши предложение или нескольких слов:  ")
words_list = user_text.split()

for i, el in enumerate(words_list):
    if len(el) > 10:
        el = el[:10:]
    print(i, el)

print("\nЗадание 5")
my_list = [9, 7, 4, 8, 2, 0, 8, 5]
my_list.sort(reverse = True)
print(f'Отсортированный лист для работы: {my_list}')
exit_while = 0

print("Для выхода из цикла введи число: -1\n")

while exit_while != -1:
    try:
        user_rating = int(input("Введи новое значение рейтинга:  "))
        exit_while = user_rating
        my_list.reverse()

        try:
            my_list.insert(my_list.index(user_rating), user_rating)
        except Exception:
            for i, el in enumerate(my_list):  # 4 5 6 7 9
                if user_rating < el:
                    my_list.insert(i, user_rating)
                    break
                elif user_rating > my_list[-1]:
                    my_list.append(user_rating)
                    break
        my_list.reverse()
        print(my_list)
    except Exception:
        print("Упс, ошибочка вышла. Понимаю только целые числа )")

print("\nЗадание 6")
products = []
i = 0
var_exit = ""

while var_exit != "exit":
    i += 1
    name = input("\nНазвание: ")
    while True:
        try:
            price = float(input("Цена: "))
            break
        except Exception:
            print("Ошибка! Только число!")

    while True:
        try:
            cnt = int(input("Количество: "))
            break
        except Exception:
            print("Ошибка! Только целое число!")

    unit = input("Единица измерения: ")

    dist_temp = {"Название": name, "Цена": price, "Кол-во": cnt, "Единица": unit}
    products.append((i, dist_temp))

    print(f'\nТовар под №{i} добавлен в список.')
    var_exit = input("Нажмите Enter для продолжения или напишите exit для завершения:  ")

print("\n*** Готовая структура ***")
for el in products:
    print(el)

print("\n*** Аналитика о товарах ***")
key_name = []
key_price = []
key_cnt = []
key_unit = []

for el_tpl in products:
    key_name.append(el_tpl[1].get("Название"))
    key_price.append(el_tpl[1].get("Цена"))
    key_cnt.append(el_tpl[1].get("Кол-во"))
    key_unit.append(el_tpl[1].get("Единица"))

tuple_analytics = {"Название": key_name, "Цена": key_price, "Кол-во": key_cnt, "Единица": key_unit}

print(tuple_analytics)