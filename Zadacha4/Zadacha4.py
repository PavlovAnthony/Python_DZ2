# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2 Позиции: 0,1 -> 2
import os


def get_input():
    while True:
        try:
            n = int(input('введите целое число : '))
            return n
        except ValueError:
            print("Ошибочный ввод.")


n = get_input()
lst = list(range(-n, n+1))

with open('file.txt') as f:
    lines = [int(line.rstrip('\n')) for line in f]
flag=True
res = 1
for i in range(0, len(lines)):
    if lines[i] > len(lst):
        flag = False
        break
    res = res*lst[lines[i]]

print(lst)
print(lines)
if flag ==False:
    print('значение индекса выходит за пределы списка')
else:
    print(f'произведение элементов = {res}')
