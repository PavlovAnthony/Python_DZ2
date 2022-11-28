# Реализуйте алгоритм перемешивания списка.

import random
def get_input():
    while True:
        try:
            n = int(input('введите целое число : '))
            return n
        except ValueError:
            print("Ошибочный ввод.")
n = get_input()
lst = list(range(0, n+1))
print(f'исходный список: {lst}')
random.shuffle(lst)
print(f'Список после перемешивания{lst}')