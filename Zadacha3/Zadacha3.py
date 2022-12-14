# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]
def get_input():
    while True:
        try:
            n = int(input('введите целое число : '))
            return n
        except ValueError:
            print("Ошибочный ввод.")


n = get_input()
lst = [(lambda i: (1+1/i)**i)(i) for i in range(1, n+1)]
print(lst)
res = sum(lst)
print(f'сумма элементов последовательности {res}')
