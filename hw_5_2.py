"""
    2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
    выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("hw_5_2_file.txt") as f_obj:
    lines_count, words_count = 0, 0
    for line in f_obj:
        lines_count += 1
        words_count += line.count(" ")
        print(f"Строка {lines_count}: {line.count(' ')} слов")
    print(f"ИТОГО: строк - {lines_count}, слов в строках - {words_count}")