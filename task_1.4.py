"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции"""
number = int(input("Введите целое положительное число: "))
n = number
max_digit = n % 10
while n:
    a = n % 10
    if a > max_digit:
        max_digit = a
        if max_digit == 9:
            break
    n = n // 10
print('Наибольшая цифра в числе', number, "равна", max_digit)
