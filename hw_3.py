print("Задание 1")
def division_numbers(num_1, num_2):
    try:
        return float(num_1) / float(num_2)
    except Exception as err:
        return f"Ошибка: {err}"

print("Результат деления: ", division_numbers(input("1-ое число: "), input("2-ое число: ")))

print("\nЗадание 2")
def user_data(name, surname, year_birth, city, email, phone_num):
    """ Функция принимает введенные пользователем данные и возвращает их одной строкой.
        Также предусмотрел вывод undefined, если в переменной пусто.
    """
    def check_emp_var(var_value):
        if var_value == '':
            return '<undefined>'
        else:
            return var_value

    return f"{check_emp_var(name)} {check_emp_var(surname)}, {check_emp_var(year_birth)}, {check_emp_var(city)}, {check_emp_var(email)}, {check_emp_var(phone_num)}"

print(user_data(name=input("Name: "),
                surname=input("Surname: "),
                year_birth=input("Year of birth: "),
                city=input("City of residence: "),
                email=input("Email: "),
                phone_num=input("Phone number: ")))

print("\nЗадание 3")
def my_func(arg_1, arg_2, arg_3):
    """ В этой задаче в случае ошибки решил отдавать none.
    """
    try:
        list_num = [float(arg_1), float(arg_2), float(arg_3)]
        return sum(list_num) - min(list_num)
    except Exception:
        return

print(my_func(40, -20.5, 60))

print("\nЗадание 4")
def my_func(x, y):
    i, res_cycle = 1, 1
    while i <= abs(y):
        res_cycle *= (1 / x)
        i += 1
    return x ** -abs(y), res_cycle

try:
    easy, hard = my_func(float(input("Число x: ")), int(input("Степень -y: ")))
    print(f"Результат со **: {easy}\nРезультат с циклом: {hard}")
except Exception as err:
    print(f"Ошибка: {err}")

print("\nЗадание 5")

def sum_numbers():
    sum_num = 0
    exit = ""
    while exit != "q":
        list_num = input("Введите числа через пробел (символ Q - завершение): ").split()
        for el in list_num:
            if el.lower() == "q":
                exit = "q"
                break
            else:
                try:
                    sum_num += float(el)
                except Exception as err:
                    print(f"Ошибка: {err}")
                    break
        list_num.clear()
        print(f"Сумма введенных чисел равна: {sum_num}")

sum_numbers()

print("\nЗадание 6")
""" В чем была сложность задания я так и не понял.
    Есть простой метод .title(), который все умеет ).
"""
def int_func(text):
    return text.title()

print(int_func("text text text"))