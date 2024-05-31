# -*- coding: utf-8 -*-

file_name = 'homework7_1.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:  # читает файл построчно и автоматически закрывает
        print(line)
print(file.closed)

# Oператор with автоматически закроет файл и не надо всегда в конце выполнения задачи в обязательном порядке
# использовать команду file.close() как при работе в режиме - file = open()