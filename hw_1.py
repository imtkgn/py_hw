print("Задание 1 \n")
var_int = 1
var_float = 2.0
var_str = "Привет, Мир!"
var_bool = True

print("Переменная var_int = ", var_int, " (", type(var_int), ")")
print("Переменная var_float = ", var_float, " (", type(var_float), ")")
print("Переменная var_str = ", var_str, " (", type(var_str), ")")
print("Переменная var_bool = ", var_bool, " (", type(var_bool), ")")

user_name = input("Введите свое имя: ")
user_age = input("А сколько тебе лет: ")
print("Рад знакомству, ", user_name, "! ", user_age, " - это прекрасный возраст!)")

print("\nЗадание 2 \n")
user_second = int(input("Введи время в секундах, а я выведу время в формате чч:мм:сс : "))
hour = user_second // 3600
minute = (user_second - hour * 3600) // 60
second = (user_second - hour * 3600 - minute * 60)
print("Итого: %02d:%02d:%02d" %  (hour, minute, second))

print("\nЗадание 3 \n")
user_number = input("Введите любое число: ")
print("Сумма по формуле n + nn + nnn = ", (int(user_number) + int(user_number + user_number) + int(user_number + user_number + user_number)))

print("\nЗадание 4 \n")
user_pos_number = int(input("Введите положительное число, а я найду самую большую цифру: "))
max_num = 0
temp_num = 0

if (user_pos_number >= 0 and user_pos_number <= 9):
    max_num = user_pos_number
    print("А че тут думать: ", user_pos_number, " ;)")
elif user_pos_number > 9:
    while user_pos_number >= 10:
        temp_num = user_pos_number % 10
        user_pos_number = user_pos_number // 10
        if temp_num >= max_num:
            max_num = temp_num
        if (user_pos_number <= 9 and user_pos_number > max_num):
            max_num = user_pos_number
    print("Самая большая цифра в числе: ", max_num)
else:
    print("Походу Вы ввели не то, что нужно :)")

print("\nЗадание 5 \n")
amount_revenue_company = int(input("Выручка компании: "))
amount_costs_company = int(input("Издержки компании: "))
profit = amount_revenue_company - amount_costs_company

if profit > 0:
    profit_revenue = profit / amount_revenue_company
    count_workers = int(input("Численность сотрудников в компании: "))
    print("Компания в плюсе. Рентабельность выручки: ", profit_revenue, ". Прибыль в расчете на 1 сотрудника: ", (profit / count_workers))
elif profit == 0:
    print("Компания работает в ноль.")
elif profit < 0:
    print("Компания работает в убыток.")
else:
    print("Вы ввели некорректные данные.")

print("\nЗадание 6 \n")
dist_first_day = int(input("Сколько км пробежал в 1-ый день: "))
dist_finish = int(input("Цель в км: "))
total_days = 1
i = dist_first_day

print("Результат:\n1-й день: ", dist_first_day)

if dist_first_day > 0:
    while i < dist_finish:
        i = i * 1.1
        total_days = total_days + 1
        print(total_days, "-й день: ", i)
    print("Ответ: на ", total_days, "-й день спортсмен достиг результата - не менее ", dist_finish, " км.")