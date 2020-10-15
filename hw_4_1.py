from sys import argv

module_name, work_hour, wage_rate, bonus = argv

try:
    print(float(work_hour) * float(wage_rate) + float(bonus))
except Exception as err:
    print({err})

