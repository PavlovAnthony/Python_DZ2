# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math
def get_input():
    while True:
        try:
            n= int(input('введите целое число : '))
            return n
        except ValueError:
            print("Ошибочный ввод.")

n = get_input()
lst = [(lambda i: math.factorial(i))(i) for i in range(1, n+1)]
print (lst)
