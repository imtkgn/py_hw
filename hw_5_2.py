"""
    2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
    выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("hw_5_2_file.txt") as f_obj:
    lines_count, words_count_all, words_cnt_line = 0, 0, 0
    for line in f_obj:
        lines_count += 1
        words_cnt_line = len(line.split(" ")) - line.count('\n')
        words_count_all += words_cnt_line
        print(f"Строка {lines_count}: {words_cnt_line} слов -> {line.split(' ')}")
    print(f"ИТОГО: строк - {lines_count}, слов в строках - {words_count_all}")